# ======================
# Environment Variables
# ======================
export PYTHONPATH = ./src:$PYTHONPATH

# ======================
# Variables
# ======================
PORT := 32000

# ======================
# Commmands
# ======================
run:
	poetry run uvicorn src.main:create_app --port $(PORT) --factory --reload

test:
	poetry run pytest -c pyproject.toml

format:
	poetry run black --config=pyproject.toml .
	poetry run isort --sp=pyproject.toml .

check:
	poetry run mypy --config-file=pyproject.toml .
	poetry run black --config=pyproject.toml --check .
	poetry run isort --sp=pyproject.toml --check .
	poetry run flake8 --toml-config=pyproject.toml .
