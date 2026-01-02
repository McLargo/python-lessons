.PHONY: docs

default: help

POETRY := $(shell which poetry 2> /dev/null)
VIRTUALENV=$(shell poetry env list | tr -s ' ' | cut -d ' ' -f 1)
POETRY_NOT_INSTALLED_MESSAGE := "Poetry could not be found, please run 'make install'"
PIP := $(if [-z $(shell which pip) ],pip3,pip)


help: ## Show help
	@echo "\nUsage:\e[1;36m make [target]\e[0m\n"
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf " -\033[36m  %-20s\033[0m %s\n", $$1, $$2}'

check-env:
	@if [ -z "$(POETRY)" ]; then \
		echo $(POETRY_NOT_INSTALLED_MESSAGE); \
		exit 1; \
	fi
	@if [ -z "$(VIRTUALENV)" ]; then \
		echo "There is not virtualenv."; \
		exit 1; \
	fi

install: ## Install required dependencies
	@if [ -z $(POETRY) ]; then \
  		echo "Poetry could not be found, installing..."; \
		$(PIP) install poetry; \
	else \
		poetry install; \
	fi

	$(PIP) install pre-commit;
	pre-commit install

remove: check-env ## Remove poetry virtualenv
	@echo "Removing virtualenv $(VIRTUALENV)."
	@poetry env remove $(VIRTUALENV)

clean: ## Clean Python cache files and directories
	@echo "Cleaning Python cache files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
	@find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	@rm -rf mutants/ .mutmut-cache 2>/dev/null || true
	@echo "Cache files cleaned."

serve: check-env ## Serve mkdocs in local
	@echo "Starting mkdocs server to access documentation."
	@poetry run mkdocs serve --strict -w src

build: check-env ## Build mkdocs in local
	@echo "Building mkdocs in local."
	@poetry run mkdocs build --strict

test: check-env clean ## Run test
	@echo "Running test."
	@poetry run python -m pytest --cov=src --cov-report=term-missing --cov-fail-under=100

coverage: check-env ## Run coverage, generate report in html and open in browser
	@echo "Running coverage report in html."
	@poetry run python -m pytest --cov=src --cov-report=html
	@echo "Opening htmlcov/index.html report in browser."
	@browse htmlcov/index.html >/dev/null 2>&1

mutations: check-env clean ## Run mutation testing with mutmut
	@echo "Running mutational tests."
	@poetry run mutmut run

deploy: check-env  # Triggers a manual deployment of python lessons to gh-pages
	@echo "Deploying python-lessons to gh-pages."
	@poetry run mkdocs gh-deploy --force
