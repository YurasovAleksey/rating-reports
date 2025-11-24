install:
	uv sync

build:
	uv build

run:
	python src/main.py --files data/products1.csv --report average-rating

lint:
	uv run ruff check src

lint-fix:
	uv run ruff check --fix src

lint-format:
	uv run ruff format src

test:
	uv run pytest