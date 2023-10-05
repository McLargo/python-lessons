.PHONY: docs

default: help

POETRY := $(shell which poetry 2> /dev/null)
VIRTUALENV=$(shell poetry env list | tr -s ' ' | cut -d ' ' -f 1)

help: ## Show help
	@echo "\nUsage: \e[1;36mmake [target]\e[0m\n"
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf " -\033[36m  %-20s\033[0m %s\n", $$1, $$2}'

install: ## Install required dependencies
	@if [ -z $(POETRY) ]; then \
		echo "Poetry could not be found, installing..."; \
		pip install poetry;\
	else \
		poetry install;\
	fi
	pip install pre-commit
	pre-commit install

remove: ## Remove poetry virtualenv
	@echo "Removing virtualenv $(VIRTUALENV)"
	poetry env remove $(VIRTUALENV)

serve: ## Serve mkdocs in local
	poetry run mkdocs serve --strict -w src

build: ## Build mkdocs in local
	poetry run mkdocs build --strict

test: ## Run test
	poetry run pytest --cov=src --cov-report=term-missing --cov-fail-under=100
