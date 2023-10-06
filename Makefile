.PHONY: docs

default: help

POETRY := $(shell which poetry 2> /dev/null)
VIRTUALENV=$(shell poetry env list | tr -s ' ' | cut -d ' ' -f 1)
POETRY_NOT_INSTALLED_MESSAGE := "Poetry could not be found, please run 'make install'"
PIP := $(if [-z $(shell which pip) ],pip3,pip)

help: ## Show help
	@echo "\nUsage: \e[1;36mmake [target]\e[0m\n"
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf " -\033[36m  %-20s\033[0m %s\n", $$1, $$2}'

install: ## Install required dependencies
	@if [ -z $(POETRY) ]; then \
		echo "Poetry could not be found, installing..."; \
		$(PIP) install poetry; \
	else \
		poetry install; \
	fi

	$(PIP) install pre-commit;
	pre-commit install

remove: ## Remove poetry virtualenv
	@if [ -z $(POETRY) ]; then \
  		echo $(POETRY_NOT_INSTALLED_MESSAGE); \
	else \
	     if [ -z $(VIRTUALENV) ]; then \
			echo "There is not virtualenv"; \
		 else \
		   echo "Removing virtualenv $(VIRTUALENV)"; \
		   poetry env remove $(VIRTUALENV); \
		 fi \
	fi

serve: ## Serve mkdocs in local
	@if [ -z $(POETRY) ]; then \
		echo $(POETRY_NOT_INSTALLED_MESSAGE); \
	else \
	  if [ -z $(VIRTUALENV) ]; then \
			echo "There is not virtualenv"; \
		 else \
		   echo "Removing virtualenv $(VIRTUALENV)"; \
		   poetry run mkdocs serve --strict -w src; \
		 fi \
	fi

build: ## Build mkdocs in local
	@if [ -z $(POETRY) ]; then \
  		echo $(POETRY_NOT_INSTALLED_MESSAGE); \
  	else \
	  if [ -z $(VIRTUALENV) ]; then \
			echo "There is not virtualenv"; \
		 else \
		   echo "Removing virtualenv $(VIRTUALENV)"; \
		   poetry run mkdocs build --strict; \
		 fi \
	fi

test: ## Run test
	@if [ -z $(POETRY) ]; then \
  		echo $(POETRY_NOT_INSTALLED_MESSAGE); \
  	else \
		poetry run pytest --cov=src --cov-report=term-missing --cov-fail-under=100; \
	fi
