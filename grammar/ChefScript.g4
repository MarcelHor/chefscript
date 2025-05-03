grammar ChefScript;

// ===== Lexer =====
INGREDIENT: 'ingredient';
DISH: 'dish';
TASTE: 'taste';
TASTE_MORE: 'taste more';
ELSE: 'else';
RECIPE: 'recipe';
SERVE: 'serve';
STIR: 'stir';
TRUE: 'true';
FALSE: 'false';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: '-'? [0-9]+ ('.' [0-9]+)?;
STRING: '"' (~["\r\n])* '"';

WS: [ \t\r\n]+ -> skip;

// ===== Parser =====
program: statement* EOF;

statement:
	ingredientDeclaration
	| dishStatement
	| assignmentStatement
	| tasteStatement
	| functionDeclaration
	| functionCallStatement
	| stirStatement
	| serveStatement;

ingredientDeclaration: INGREDIENT ID '=' expression ';';

dishStatement: DISH '(' expression ')' ';';

assignmentStatement: ID '=' expression ';';

tasteStatement:
	TASTE '(' expression ')' block (tasteMoreBlock)* (ELSE block)?;

tasteMoreBlock: TASTE_MORE '(' expression ')' block;

functionDeclaration: RECIPE ID '(' paramList? ')' block;

functionCallStatement: functionCall ';';

functionCall: ID '(' argumentList? ')';

paramList: param (',' param)*;

param: INGREDIENT ID;

argumentList: expression (',' expression)*;

stirStatement:
	STIR '(' ingredientDeclaration expression ';' assignmentStatement ')' block;

serveStatement: SERVE expression ';';

block: '{' statement* '}';

expression:
	expression '*' expression							# multiplyExpr
	| expression '/' expression							# divideExpr
	| expression '+' expression							# addExpr
	| expression '-' expression							# subtractExpr
	| expression '>' expression							# greaterExpr
	| expression '<' expression							# lessExpr
	| expression '>=' expression						# greaterEqualExpr
	| expression '<=' expression						# lessEqualExpr
	| expression 'same' expression						# sameExpr
	| expression 'notSame' expression					# notSameExpr
	| expression 'mix' expression						# andExpr
	| expression 'either' expression					# orExpr
	| 'ew' expression									# notExpr
	| '(' expression ')'								# parensExpr
	| NUMBER											# numberExpr
	| STRING											# stringExpr
	| TRUE												# trueExpr
	| FALSE												# falseExpr
	| functionCall										# functionCallExpr
	| ID												# variableExpr;