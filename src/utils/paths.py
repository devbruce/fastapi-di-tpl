from pathlib import Path

APP_ROOT_DIR = Path(__file__).resolve().parent.parent
APP_DESCRIPTION_PATH = APP_ROOT_DIR / "description.md"

PROJECT_ROOT_DIR = Path(__file__).resolve().parent.parent.parent
TESTS_DIR = PROJECT_ROOT_DIR / "tests"
