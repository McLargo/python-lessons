.PHONY: docs

default: help

all: build serve  ## Executes build and serve together

help: ## Show help
	@echo "\nUsage: \e[1;36mmake [target]\e[0m\n"
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf " -\033[36m  %-20s\033[0m %s\n", $$1, $$2}'


install: ## Install required dependencies
	poetry install

serve: ## Serve mkdocs in local
	poetry run mkdocs serve --strict -w beginner -w intermediate

build: ## Build mkdocs in local
	poetry run mkdocs build --strict

test: ## Run test
	poetry run pytest --cov=src --cov-report=term-missing --cov-fail-under=100
