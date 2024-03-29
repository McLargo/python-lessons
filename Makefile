.PHONY: docs

default: help

POETRY := $(shell which poetry 2> /dev/null)
VIRTUALENV=$(shell poetry env list | tr -s ' ' | cut -d ' ' -f 1)
POETRY_NOT_INSTALLED_MESSAGE := "Poetry could not be found, please run 'make install'"
PIP := $(if [-z $(shell which pip) ],pip3,pip)


help: ## Show help
	@echo "\nUsage:\e[1;36m make [target]\e[0m\n"
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
	    echo "There is not virtualenv."; \
	  else \
	    echo "Removing virtualenv $(VIRTUALENV)."; \
	    poetry env remove $(VIRTUALENV); \
	  fi \
	fi

serve: ## Serve mkdocs in local
	@if [ -z $(POETRY) ]; then \
		echo $(POETRY_NOT_INSTALLED_MESSAGE); \
	else \
	  if [ -z $(VIRTUALENV) ]; then \
	    echo "There is not virtualenv."; \
	  else \
	    echo "Starting mkdocs server to access documentation."; \
	  	poetry run mkdocs serve --strict -w src; \
	  fi \
	fi

build: ## Build mkdocs in local
	@if [ -z $(POETRY) ]; then \
  		echo $(POETRY_NOT_INSTALLED_MESSAGE); \
  	else \
	  if [ -z $(VIRTUALENV) ]; then \
	    echo "There is not virtualenv."; \
	  else \
	    echo "Building mkdocs in local."; \
	  	poetry run mkdocs build --strict; \
	  fi \
	fi

test: ## Run test
	@if [ -z $(POETRY) ]; then \
  		echo $(POETRY_NOT_INSTALLED_MESSAGE); \
  	else \
  	  if [ -z $(VIRTUALENV) ]; then \
	    echo "There is not virtualenv."; \
	  else \
	    echo "Running test."; \
		poetry run python -m pytest --cov=src --cov-report=term-missing --cov-fail-under=100; \
	  fi \
	fi


coverage: ## Run coverage, generate report in html and open in browser
	@if [ -z $(POETRY) ]; then \
  		echo $(POETRY_NOT_INSTALLED_MESSAGE); \
  	else \
  	  if [ -z $(VIRTUALENV) ]; then \
	    echo "There is not virtualenv."; \
	  else \
	    echo "Running coverage report in html."; \
	  	poetry run python -m pytest --cov=src --cov-report=html; \
		echo "Opening htmlcov/index.html report in browser."; \
		browse htmlcov/index.html >/dev/null 2>&1; \
	  fi \
	fi


deploy:  # Triggers a manual deployment of python lessons to gh-pages
	@if [ -z $(POETRY) ]; then \
		echo $(POETRY_NOT_INSTALLED_MESSAGE); \
	else \
		if [ -z $(VIRTUALENV) ]; then \
	    echo "There is not virtualenv."; \
	  else \
	    echo "Deploying python-lessons to gh-pages."; \
		poetry run mkdocs gh-deploy --force; \
	  fi \
	fi
