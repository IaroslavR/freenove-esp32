SHELL := /bin/bash
# https://www.gushiciku.cn/pl/p6TH
.SHELLFLAGS := -eu -o pipefail -c
.ONESHELL:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

VERSION := 0.1.0
ROOT := $(shell pwd)
PACKAGE_PATH := ${ROOT}/src/blueprint_python
PYTHON_VERSION := $(shell cat .python-version)

.DEFAULT_GOAL := help
##@ Bootstrap
.PHONY: init-repo init-env bootstrap init

init-repo:  ## Configure git repository
	pre-commit install -t pre-commit -t commit-msg

init-env: clean  ## Initialize local environment
	poetry env use ${PYTHON_VERSION}
	cat .test.env > .env
	echo "dotenv" > .envrc

bootstrap:  ## Install/update required tools(dev tools included)
	poetry install
	git add poetry.lock

init: init-repo init-env bootstrap  ## All init steps at once

##@ Checks
.PHONY: check

check:  ## Run pre-commit against all files
	pre-commit run --all-files

mypy:  ## Run type checker
	poetry run mypy

##@ Tests
.PHONY: test

test:  ## Run tests
	PYTHONPATH=${PACKAGE_PATH} poetry run pytest --cov-config=.coveragerc --cov=src 2>&1 | tee pytest-coverage.txt

test-integration: ## Run integration tests
	PYTHONPATH=${PACKAGE_PATH} poetry run pytest --runintegration

##@ Miscellaneous
.PHONY: secrets-baseline-create secrets-baseline-audit secrets-update replace-me

secrets-baseline-create:  ## Create/update .secrets.baseline file
	poetry run detect-secrets scan --baseline .secrets.baseline

secrets-baseline-audit:  ## Check updated .secrets.baseline file
	poetry run detect-secrets audit .secrets.baseline
	git commit .secrets.baseline --no-verify -m "build(security): update secrets.baseline"

secrets-update: secrets-baseline-create secrets-baseline-audit  ## Update secrets

refresh-lock:  ## Refresh the poetry.lock file without packages updates
	poetry lock --no-update

clean:  ## Clean local environment
	rm -rf .coverage .mypy_cache .pytest_cache .venv poetry.lock

replace-me:  ## Highlight not modified parts of blueprint
	git grep -Ei 'blueprint*|replace*|${VERSION}'

##@ Helpers
.PHONY: help

help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-24s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
