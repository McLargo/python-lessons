.PHONY: help check-env python-env install remove clean serve build test lint lint-fix format spelling coverage mutations deploy

default: help

PYTHON_VERSION ?= 3.14.7
POETRY := $(shell which poetry 2> /dev/null)
UV := $(shell which uv 2> /dev/null)
VIRTUALENV=$(shell poetry env list | tr -s ' ' | cut -d ' ' -f 1)
POETRY_NOT_INSTALLED_MESSAGE := "Poetry could not be found, please run 'make install'"
PIP := $(if [-z $(shell which pip) ],pip3,pip)


help: ## Show help
	@echo "\nUsage:\e[1;36m make [target]\e[0m\n"
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf " -\033[36m  %-20s\033[0m %s\n", $$1, $$2}'

check-env: ## Check if Poetry and virtualenv are installed
	@if [ -z "$(POETRY)" ]; then \
		echo $(POETRY_NOT_INSTALLED_MESSAGE); \
		exit 1; \
	fi
	@if [ -z "$(VIRTUALENV)" ]; then \
		echo "There is not virtualenv."; \
		exit 1; \
	fi

python-env: ## Point Poetry at Python $(PYTHON_VERSION), installing it via uv if needed
	@if [ -z "$(POETRY)" ]; then \
		echo $(POETRY_NOT_INSTALLED_MESSAGE); \
		exit 1; \
	fi
	@echo "Ensuring Poetry uses Python $(PYTHON_VERSION)."
	@if [ -n "$(UV)" ]; then \
		uv python install $(PYTHON_VERSION) >/dev/null; \
		PY_BIN=$$(uv python find $(PYTHON_VERSION)); \
	elif command -v python$(basename $(PYTHON_VERSION)) >/dev/null 2>&1; then \
		PY_BIN=$$(command -v python$(basename $(PYTHON_VERSION))); \
	else \
		echo "Python $(PYTHON_VERSION) not found and 'uv' is not installed."; \
		echo "Install uv (https://docs.astral.sh/uv/) or install python$(basename $(PYTHON_VERSION)) manually."; \
		exit 1; \
	fi; \
	echo "Using $$PY_BIN"; \
	poetry env use "$$PY_BIN"

install: python-env ## Install required dependencies
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
	@poetry run mkdocs serve --strict --livereload

build: check-env ## Build mkdocs in local
	@echo "Building mkdocs in local."
	@poetry run mkdocs build --strict

test: check-env clean ## Run test
	@echo "Running test."
	@poetry run python -m pytest --cov=src --cov-report=term-missing --cov-fail-under=100

lint: check-env ## Run ruff linting checks
	@echo "Running ruff linting checks (including docstrings)."
	@poetry run ruff check .

lint-fix: check-env ## Run ruff linting checks and fix issues
	@echo "Running ruff linting checks and fixing issues (including docstrings)."
	@poetry run ruff check --fix .

format: check-env ## Format code with ruff
	@echo "Formatting code with ruff."
	@poetry run ruff format .

spelling: check-env ## Check spelling in source and docs
	@echo "Checking spelling in Python and Markdown files."
	@poetry run codespell src/ docs/ README.md CONTRIBUTING.md

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
