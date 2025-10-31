from typing import Dict

# Simple mock worker for hackathon

def market_insight(disease: str) -> Dict:
    """Return simple market metrics with numeric unmet-need score (0-100)."""
    mock_map = {
        "Alzheimer": {"tam_usd_b": 7.8, "growth_cagr": 5.0, "unmet_need_score": 85, "unmet_need_label": "high"},
        "Breast Cancer": {"tam_usd_b": 20.0, "growth_cagr": 4.2, "unmet_need_score": 60, "unmet_need_label": "medium"},
    }
    default = {"tam_usd_b": 3.0, "growth_cagr": 3.0, "unmet_need_score": 55, "unmet_need_label": "medium"}
    return mock_map.get(disease, default)
