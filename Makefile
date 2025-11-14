install:
	uv sync

build:
	uv build

run:
	python src/main.py --files data/products1.csv --report average-rating

lint:
	uv run ruff check src