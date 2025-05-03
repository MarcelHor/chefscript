/* --------------------------------------------------------------------------------------------
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License. See License.txt in the project root for license information.
 * ------------------------------------------------------------------------------------------ */
import {
	createConnection,
	TextDocuments,
	Diagnostic,
	DiagnosticSeverity,
	ProposedFeatures,
	InitializeParams,
	DidChangeConfigurationNotification,
	CompletionItem,
	CompletionItemKind,
	TextDocumentPositionParams,
	TextDocumentSyncKind,
	InitializeResult,
	DocumentDiagnosticReportKind,
	type DocumentDiagnosticReport
} from 'vscode-languageserver/node';

import {
	TextDocument,
	Position,
} from 'vscode-languageserver-textdocument';
import { MarkupKind } from 'vscode-languageserver-types';

// Create a connection for the server, using Node's IPC as a transport.
// Also include all preview / proposed LSP features.
const connection = createConnection(ProposedFeatures.all);

// Create a simple text document manager.
const documents = new TextDocuments(TextDocument);

let hasConfigurationCapability = false;
let hasWorkspaceFolderCapability = false;
let hasDiagnosticRelatedInformationCapability = false;

connection.onInitialize((params: InitializeParams) => {
	const capabilities = params.capabilities;

	// Does the client support the `workspace/configuration` request?
	// If not, we fall back using global settings.
	hasConfigurationCapability = !!(
		capabilities.workspace && !!capabilities.workspace.configuration
	);
	hasWorkspaceFolderCapability = !!(
		capabilities.workspace && !!capabilities.workspace.workspaceFolders
	);
	hasDiagnosticRelatedInformationCapability = !!(
		capabilities.textDocument &&
		capabilities.textDocument.publishDiagnostics &&
		capabilities.textDocument.publishDiagnostics.relatedInformation
	);

	const result: InitializeResult = {
		capabilities: {
			textDocumentSync: TextDocumentSyncKind.Incremental,
			hoverProvider: true,
			completionProvider: {
				resolveProvider: true,
				triggerCharacters: ['.', '(', '[', '{', ' ', '\n']
			},
			diagnosticProvider: {
				interFileDependencies: false,
				workspaceDiagnostics: false
			}
		}
	};	
	if (hasWorkspaceFolderCapability) {
		result.capabilities.workspace = {
			workspaceFolders: {
				supported: true
			}
		};
	}
	return result;
});

connection.onInitialized(() => {
	if (hasConfigurationCapability) {
		// Register for all configuration changes.
		connection.client.register(DidChangeConfigurationNotification.type, undefined);
	}
	if (hasWorkspaceFolderCapability) {
		connection.workspace.onDidChangeWorkspaceFolders(_event => {
			connection.console.log('Workspace folder change event received.');
		});
	}
});

// The example settings
interface ExampleSettings {
	maxNumberOfProblems: number;
}

// The global settings, used when the `workspace/configuration` request is not supported by the client.
// Please note that this is not the case when using this server with the client provided in this example
// but could happen with other clients.
const defaultSettings: ExampleSettings = { maxNumberOfProblems: 1000 };
let globalSettings: ExampleSettings = defaultSettings;

// Cache the settings of all open documents
const documentSettings = new Map<string, Thenable<ExampleSettings>>();

connection.onDidChangeConfiguration(change => {
	if (hasConfigurationCapability) {
		// Reset all cached document settings
		documentSettings.clear();
	} else {
		globalSettings = (
			(change.settings.languageServerExample || defaultSettings)
		);
	}
	// Refresh the diagnostics since the `maxNumberOfProblems` could have changed.
	// We could optimize things here and re-fetch the setting first can compare it
	// to the existing setting, but this is out of scope for this example.
	connection.languages.diagnostics.refresh();
});

function getDocumentSettings(resource: string): Thenable<ExampleSettings> {
	if (!hasConfigurationCapability) {
		return Promise.resolve(globalSettings);
	}
	let result = documentSettings.get(resource);
	if (!result) {
		result = connection.workspace.getConfiguration({
			scopeUri: resource,
			section: 'languageServerExample'
		});
		documentSettings.set(resource, result);
	}
	return result;
}

// Only keep settings for open documents
documents.onDidClose(e => {
	documentSettings.delete(e.document.uri);
});


connection.languages.diagnostics.on(async (params) => {
	const document = documents.get(params.textDocument.uri);
	if (document !== undefined) {
		const diagnostics = validateDocument(document);
		connection.sendDiagnostics({ uri: document.uri, diagnostics });
		return {
			kind: DocumentDiagnosticReportKind.Full,
			items: diagnostics
		};
	} else {
		// We don't know the document. We can either try to read it from disk
		// or we don't report problems for it.
		return {
			kind: DocumentDiagnosticReportKind.Full,
			items: []
		} satisfies DocumentDiagnosticReport;
	}
});

// The content of a text document has changed. This event is emitted
// when the text document first opened or when its content has changed.
documents.onDidChangeContent(change => {
	const diagnostics = validateDocument(change.document);
	connection.sendDiagnostics({ uri: change.document.uri, diagnostics });
});

function validateDocument(document: TextDocument): Diagnostic[] {
	const diagnostics: Diagnostic[] = [];
	const lines = document.getText().split(/\r?\n/);

	lines.forEach((line, i) => {
		const trimmed = line.trim();

		// 1. ingredient musí mít =
		if (trimmed.startsWith("ingredient") && !trimmed.includes("=")) {
			diagnostics.push({
				severity: DiagnosticSeverity.Error,
				range: {
					start: { line: i, character: 0 },
					end: { line: i, character: line.length }
				},
				message: `Missing '=' in ingredient declaration.`,
				source: 'chefscript'
			});
		}

		// 2. Řádky kromě {} musí končit ;
		if (
			trimmed.length > 0 &&
			!trimmed.endsWith(";") &&
			!trimmed.endsWith("{") &&
			!trimmed.endsWith("}") &&
			!trimmed.startsWith("taste") &&
			!trimmed.startsWith("stir") &&
			!trimmed.startsWith("recipe") &&
			!trimmed.startsWith("//")
		) {
			diagnostics.push({
				severity: DiagnosticSeverity.Warning,
				range: {
					start: { line: i, character: 0 },
					end: { line: i, character: line.length }
				},
				message: `Possible missing semicolon.`,
				source: 'chefscript'
			});
		}

		if (trimmed.startsWith("dish") && !trimmed.includes("(")) {
			diagnostics.push({
				severity: DiagnosticSeverity.Warning,
				range: {
					start: { line: i, character: 0 },
					end: { line: i, character: line.length }
				},
				message: `Missing '(' in dish declaration.`,
				source: 'chefscript'
			});
		}
	});

	return diagnostics;
}


connection.onDidChangeWatchedFiles(_change => {
	// Monitored files have change in VSCode
	connection.console.log('We received a file change event');
});

// This handler provides the initial list of the completion items.
connection.onCompletion(
	(_textDocumentPosition: TextDocumentPositionParams): CompletionItem[] => {
		return [
			{ label: 'ingredient', kind: CompletionItemKind.Keyword, data: 1 , detail: `ChefScript keyword`, documentation: 'The ingredient keyword is used to define an ingredient in a recipe.'},
			{ label: 'dish', kind: CompletionItemKind.Keyword, data: 2 , detail: `ChefScript keyword`, documentation: 'The dish keyword is used to define a dish in a recipe.'},
			{ label: 'taste', kind: CompletionItemKind.Keyword, data: 3 , detail: `ChefScript keyword`, documentation: 'The taste keyword is used to define the taste of a dish.'},
			{ label: 'stir', kind: CompletionItemKind.Keyword, data: 4 , detail: `ChefScript keyword`, documentation: 'The stir keyword is used to stir the ingredients in a dish.'},
			{ label: 'serve', kind: CompletionItemKind.Keyword, data: 5 , detail: `ChefScript keyword`, documentation: 'The serve keyword is used to serve the dish.'},
		];
	}
);

connection.onHover((params: any) => {
	console.log("Hover params: ", params);
	const document = documents.get(params.textDocument.uri);
	if (document) {
		const range = getWordRangeAtPosition(document, params.position);
		if (range) {
			const word = document.getText(range);
			return {
				range,
				contents: [
					`**${word}** is a keyword in ChefScript.`,
					`The ${word} keyword is used to define a ${word} in a recipe.`
				]
			};
		}
	}
	return null;
});

function getWordRangeAtPosition(document: TextDocument, position: Position) {
	const line = document.getText({
		start: { line: position.line, character: 0 },
		end: { line: position.line, character: Number.MAX_VALUE }
	});

	let startChar = position.character;
	while (startChar > 0 && /\w/.test(line[startChar - 1])) {
		startChar--;
	}

	let endChar = position.character;
	while (endChar < line.length && /\w/.test(line[endChar])) {
		endChar++;
	}

	if (startChar === endChar) return null;

	return {
		start: { line: position.line, character: startChar },
		end: { line: position.line, character: endChar }
	};
}


// This handler resolves additional information for the item selected in
// the completion list.
connection.onCompletionResolve((item: CompletionItem): CompletionItem => {
	switch (item.label) {
		case 'ingredient':
			item.detail = 'Declare an ingredient';
			item.documentation = 'Example: `ingredient flour = 200;`';
			break;
		case 'dish':
			item.detail = 'Output value';
			item.documentation = 'Example: `dish(flour);`';
			break;
		case 'taste':
			item.detail = 'Declare a taste';
			item.documentation = 'Example: `taste sweet;`';
			break;
		case 'stir':
			item.detail = 'Stir the ingredients';
			item.documentation = 'Example: `stir(flour);`';
			break;
		case 'serve':
			item.detail = 'Serve the dish';
			item.documentation = 'Example: `serve(dish);`';
			break;
		default:
			item.detail = 'Unknown keyword';
			item.documentation = 'No documentation available.';
			break;
	}
	return item;
});


// Make the text document manager listen on the connection
// for open, change and close text document events
documents.listen(connection);

// Listen on the connection
connection.listen();
