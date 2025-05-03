ANTLR=antlr
GRAMMAR=grammar/ChefScript.g4
OUT_DIR=src
FILE?=input/calculator.chef
VENV_DIR=.venv
PYTHON=$(VENV_DIR)/bin/python

all: run

generate:
	$(ANTLR) -Dlanguage=Python3 -visitor -o $(OUT_DIR) $(GRAMMAR)
	mv $(OUT_DIR)/grammar/* $(OUT_DIR)/
	rm -rf $(OUT_DIR)/grammar

install: $(PYTHON)

$(PYTHON):
	python3 -m venv $(VENV_DIR)
	$(PIP) install -r requirements.txt

run: install
	$(PYTHON) src/main.py ${FILE}