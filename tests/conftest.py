"""Pytest fixtures."""

from __future__ import annotations

from pathlib import Path

import pytest
from dotenv import load_dotenv

# Load monorepo .env for local integration runs (never log keys).
_monorepo_env = Path(__file__).resolve().parents[3] / ".env"
if _monorepo_env.is_file():
    load_dotenv(_monorepo_env)

_package_env = Path(__file__).resolve().parents[1] / ".env"
if _package_env.is_file():
    load_dotenv(_package_env)


@pytest.fixture
def mock_manifest() -> dict:
    return {
        "tool_id": "ddct-clarity",
        "title": "ΔΔCt Clarity",
        "execution_mode": "sync",
        "examples": [
            {
                "name": "il6_livak_example",
                "input": {
                    "rows": [
                        {"gene": "GAPDH", "group": "Control", "ct": 20.5, "well": "A1"},
                        {"gene": "GAPDH", "group": "Control", "ct": 20.6, "well": "A2"},
                        {"gene": "GAPDH", "group": "Control", "ct": 20.4, "well": "A3"},
                        {"gene": "IL6", "group": "Control", "ct": 30.0, "well": "B1"},
                        {"gene": "IL6", "group": "Control", "ct": 30.2, "well": "B2"},
                        {"gene": "IL6", "group": "Control", "ct": 29.8, "well": "B3"},
                        {
                            "gene": "GAPDH",
                            "group": "Treatment",
                            "ct": 20.7,
                            "well": "C1",
                        },
                        {
                            "gene": "GAPDH",
                            "group": "Treatment",
                            "ct": 20.5,
                            "well": "C2",
                        },
                        {
                            "gene": "GAPDH",
                            "group": "Treatment",
                            "ct": 20.6,
                            "well": "C3",
                        },
                        {"gene": "IL6", "group": "Treatment", "ct": 28.0, "well": "D1"},
                        {"gene": "IL6", "group": "Treatment", "ct": 28.2, "well": "D2"},
                        {"gene": "IL6", "group": "Treatment", "ct": 27.8, "well": "D3"},
                    ],
                    "reference_genes": ["GAPDH"],
                    "calibrator_group": "Control",
                    "replicate_type": "technical",
                },
                "output": {"has_blocking_errors": False, "method": "livak"},
            },
        ],
    }


@pytest.fixture
def mock_run_response() -> dict:
    return {
        "run_id": "run_ddct_test123",
        "status": "completed",
        "result": {
            "method": "livak",
            "formula": "2^(-ddCt)",
            "gene_results": [],
            "has_blocking_errors": False,
        },
        "error": None,
        "result_url": "https://tools.pepkio.com/api/tools/v1/runs/run_ddct_test123",
        "permalink": "https://tools.pepkio.com/r/run_ddct_test123",
    }
