from pathlib import Path

PROJECT_ROOT_DIR = Path(__file__).resolve().parent.parent.parent

APP_ROOT_DIR = PROJECT_ROOT_DIR / "src"
APP_DESCRIPTION_PATH = APP_ROOT_DIR / "description.md"

TESTS_DIR = PROJECT_ROOT_DIR / "tests"
