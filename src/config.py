"""
config.py

Central configuration file for the Olist E-Commerce Business Intelligence Project.

This module defines project paths and commonly used configuration values.
"""

from pathlib import Path

# =============================================================================
# Project Root
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# =============================================================================
# Data Directories
# =============================================================================

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

INTERIM_DATA_DIR = DATA_DIR / "interim"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

# =============================================================================
# Reports
# =============================================================================

REPORTS_DIR = PROJECT_ROOT / "reports"

FIGURES_DIR = REPORTS_DIR / "figures"

TABLES_DIR = REPORTS_DIR / "cleaned_table"

DASHBOARD_DIR = REPORTS_DIR / "dashboard"

# =============================================================================
# Assets
# =============================================================================

ASSETS_DIR = PROJECT_ROOT / "assets"

SCREENSHOTS_DIR = ASSETS_DIR / "screenshots"

ASSET_FIGURES_DIR = ASSETS_DIR / "figures"

# =============================================================================
# Random State
# =============================================================================

RANDOM_STATE = 42

# =============================================================================
# Machine Learning
# =============================================================================

TEST_SIZE = 0.20

N_ESTIMATORS = 100

# =============================================================================
# Dashboard
# =============================================================================

PAGE_TITLE = "Olist Business Intelligence Dashboard"

PAGE_ICON = "📊"

LAYOUT = "wide"