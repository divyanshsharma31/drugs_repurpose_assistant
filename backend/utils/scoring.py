from typing import List, Dict


def score_opportunity(drug: str, disease: str, evidence: List[Dict]) -> float:
    trials = [e for e in evidence if e.get("type") == "trial"]
    lits = [e for e in evidence if e.get("type") == "literature"]
    score = 0.0
    # Base on counts
    score += min(len(trials) * 0.15, 0.6)
    score += min(len(lits) * 0.05, 0.3)
    # Phase weighting
    for t in trials:
        ph = (t.get("phase") or "").lower()
        if "phase 3" in ph:
            score += 0.2
        elif "phase 2" in ph:
            score += 0.12
        elif "phase 1" in ph:
            score += 0.06
    # Cap at 1.0
    return max(0.0, min(score, 1.0))
