from typing import Dict

# Mock patent validation worker

def patent_risk(drug: str, disease: str) -> Dict:
    """Return numeric patent risk score (0-100, higher=worse)."""
    # Simple heuristic/mock: shorter, off-patent generics => lower score
    base = 40 if len(drug) <= 9 else 60
    score = max(0, min(100, base))
    label = "low" if score < 35 else ("medium" if score < 70 else "high")
    return {"risk_score": score, "risk_label": label, "notes": "Preliminary search suggests manageable freedom-to-operate."}
