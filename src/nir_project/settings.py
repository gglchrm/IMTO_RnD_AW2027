# src/nir_project/settings.py
from pathlib import Path
from typing import Any, cast

import yaml
from dotenv import load_dotenv


def _find_project_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / "pyproject.toml").exists():  # было: pyprokect.toml
            return p
    raise FileNotFoundError("pyproject.toml не найден вверх по дереву")


PROJECT_ROOT = _find_project_root(Path(__file__).resolve().parent)

CONFIG_PATH = PROJECT_ROOT / "configs" / "config.yaml"
DATA_PATH = PROJECT_ROOT / "data" / "RuSafety_final.csv"
CHECKPOINT_DIR = PROJECT_ROOT / "checkpoints"
MLRUNS_DIR = PROJECT_ROOT / "mlruns"

load_dotenv(PROJECT_ROOT / ".env")

for _d in (CHECKPOINT_DIR, MLRUNS_DIR):
    _d.mkdir(exist_ok=True)


def load_config() -> dict[str, Any]:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return cast(dict[str, Any], yaml.safe_load(f))


def get_models(provider: str) -> list[str]:
    """Возвращает список моделей провайдера из configs/config.yaml.

    get_models("gigachat") -> ["GigaChat-2", "GigaChat-2-Pro", ...]
    """
    config = load_config()
    models = config.get("models", {}).get(provider, [])
    return cast(list[str], models)
