.PHONY: help check-env install-python python-env install remove clean serve build test lint lint-fix format typecheck spelling coverage mutations deploy

default: help

PYTHON_VERSION ?= $(shell grep '^python = ' pyproject.toml | sed 's/[^0-9.]*//g')
POETRY := $(shell which poetry 2> /dev/null)
UV := $(shell command -v uv 2> /dev/null)
VIRTUALENV=$(shell poetry env info --path 2>/dev/null)
POETRY_NOT_INSTALLED_MESSAGE := "Poetry could not be found, please run 'make install'"
PIP := $(if [-z $(shell which pip) ],pip3,pip)


help: ## Show help
	@echo "\nUsage:\e[1;36m make [target]\e[0m\n"
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk -v python_version="$(PYTHON_VERSION)" 'BEGIN {FS = ":.*?## "}; {gsub(/PYTHON_VERSION/, python_version, $$2); printf " -\033[36m  %-20s\033[0m %s\n", $$1, $$2}'

check-env: ## Check if Poetry and virtualenv are installed
	@if [ -z "$(POETRY)" ]; then \
		@echo $(POETRY_NOT_INSTALLED_MESSAGE); \
		exit 1; \
	fi
	@if [ -z "$(VIRTUALENV)" ]; then \
		echo "There is not virtualenv."; \
		exit 1; \
	fi

install-python: ## Install Python PYTHON_VERSION
	@if [ -z "$(UV)" ]; then \
		echo "uv could not be found; install uv before running this target."; \
		exit 1; \
	fi
	@echo "Installing Python $(PYTHON_VERSION) with uv."
	@$(UV) python install "$(PYTHON_VERSION)"

python-env: install-python ## Point Poetry at Python PYTHON_VERSION
	@if [ -z "$(POETRY)" ]; then \
		echo $(POETRY_NOT_INSTALLED_MESSAGE); \
		exit 1; \
	fi
	@echo "Ensuring Poetry uses Python $(PYTHON_VERSION)."
	@$(POETRY) env use "$(PYTHON_VERSION)"

install: python-env ## Install required dependencies
	@if [ -z $(POETRY) ]; then \
  		@echo "Poetry could not be found, installing..."; \
		$(PIP) install poetry; \
	else \
		poetry install; \
	fi

	$(PIP) install pre-commit;
	pre-commit install

remove: check-env ## Remove poetry virtualenv
	@echo "Removing virtualenv $(VIRTUALENV)."
	@rm -rf -- "$(VIRTUALENV)"

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

typecheck: check-env ## Run pyrefly type checking
	@echo "Running pyrefly type checking."
	@poetry run pyrefly check

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
