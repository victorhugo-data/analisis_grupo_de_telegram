"""Rutas del proyecto (estructura Cookiecutter Data Science)."""

from pathlib import Path

PROJ_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

CHAT_EXPORT_DIR = RAW_DATA_DIR / "ChatExport_2026-09-26"

NOTEBOOKS_DIR = PROJ_ROOT / "notebooks"
REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
