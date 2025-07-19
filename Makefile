#----------------------------------------------
# Environment Variables
#----------------------------------------------
export PYTHONPATH = ./src:$PYTHONPATH

#----------------------------------------------
# Variables
#----------------------------------------------
PORT := 55000

#----------------------------------------------
# Commands
#----------------------------------------------
run:
	uv run uvicorn src.main:create_app --port $(PORT) --factory --reload

test:
	uv run pytest -c pyproject.toml

format:
	uv run ruff check --fix --config=pyproject.toml .
	uv run ruff format --config=pyproject.toml .

check:
	uv run ruff check --config=pyproject.toml .
	uv run mypy --config-file=pyproject.toml .
