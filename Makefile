.DEFAULT_GOAL := all
sources = dags plugins

.PHONY: format
format:
	poetry run ruff check --fix $(sources)
	poetry run ruff format $(sources)

.PHONY: lint
lint:
	poetry run ruff check $(sources)
	poetry run ruff format --check $(sources)

.PHONY: all
all: format lint test
