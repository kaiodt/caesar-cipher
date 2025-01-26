.PHONY: all install format lint test sec

all: install format lint test

install:
	@poetry install

format:
	@poetry run blue .

lint:
	@poetry run ruff check --fix .
	@poetry run ruff check .

test:
	@poetry run pytest -v

sec:
	@poetry run safety scan