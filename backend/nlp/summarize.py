from typing import List, Dict

def summarize_evidence(drug: str, disease: str, evidence: List[Dict]) -> str:
    trials = [e for e in evidence if e.get("type") == "trial"]
    lits = [e for e in evidence if e.get("type") == "literature"]
    parts = []
    if trials:
        phases = list({t.get("phase", "") for t in trials if t.get("phase")})
        status_counts = {}
        for t in trials:
            s = t.get("status", "")
            if s:
                status_counts[s] = status_counts.get(s, 0) + 1
        sc = ", ".join(f"{k}:{v}" for k, v in status_counts.items()) if status_counts else "trials found"
        parts.append(f"ClinicalTrials.gov shows {len(trials)} trial(s) for {drug} in {disease} (phases: {', '.join(phases) or 'N/A'}, {sc}).")
    if lits:
        parts.append(f"Literature mentions support potential activity of {drug} in {disease} ({len(lits)} publication snippets).")
    if not parts:
        return f"Preliminary signals for {drug} in {disease}. Further investigation required."
    return " ".join(parts)
