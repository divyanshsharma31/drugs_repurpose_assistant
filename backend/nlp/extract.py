from typing import Dict, List
import re

COMMON_DISEASE_TERMS = [
    "cancer", "carcinoma", "tumor", "tumour", "neoplasm", "diabetes", "obesity",
    "alzheimer", "parkinson", "asthma", "copd", "hypertension", "depression",
    "anxiety", "schizophrenia", "arthritis", "psoriasis", "hepatitis", "covid",
    "influenza", "migraine", "epilepsy", "stroke", "heart failure", "coronary",
    "ibd", "crohn", "colitis", "lupus", "fibrosis", "tuberculosis"
]


def extract_diseases(abstracts: List[dict], trials: List[dict]) -> Dict[str, List[dict]]:
    evidence_map: Dict[str, List[dict]] = {}

    # From trials conditions
    for t in trials:
        for cond in t.get("conditions", []):
            disease = cond.strip()
            if not disease:
                continue
            evidence_map.setdefault(disease, []).append({
                "type": "trial",
                "title": t.get("title", ""),
                "source_id": t.get("source_id", ""),
                "phase": t.get("phase", ""),
                "status": t.get("status", "")
            })

    # From abstracts text
    for a in abstracts:
        text = f"{a.get('title','')}\n{a.get('abstract','')}".lower()
        for term in COMMON_DISEASE_TERMS:
            if re.search(r"\\b" + re.escape(term) + r"\\b", text):
                key = term.title()
                evidence_map.setdefault(key, []).append({
                    "type": "literature",
                    "title": a.get("title", ""),
                    "source_id": a.get("source_id", ""),
                })

    return evidence_map


COMMON_DRUG_SUFFIXES = [
    "mab",  # monoclonal antibodies
    "nib",  # kinase inhibitors
    "pril", "sartan", # anti-hypertensives
    "statin", # lipid lowering
    "caine", # anesthetics
    "zolam", "zepam", # benzos
    "oxetine", "triptyline", # antidepressants
]


def extract_drugs(abstracts: List[dict], trials: List[dict]) -> Dict[str, List[dict]]:
    evidence_map: Dict[str, List[dict]] = {}

    # 1) Prefer clinical trial interventions (high precision)
    for t in trials:
        for name in t.get("interventions", []):
            drug = name.strip()
            if not drug:
                continue
            evidence_map.setdefault(drug, []).append({
                "type": "trial",
                "title": t.get("title", ""),
                "source_id": t.get("source_id", ""),
                "phase": t.get("phase", ""),
                "status": t.get("status", "")
            })

    if evidence_map:
        return evidence_map

    # 2) Fallback to lightweight literature heuristic with strict filters
    MONTHS = {
        "january","february","march","april","may","june","july","august","september","october","november","december"
    }

    for a in abstracts:
        text = f"{a.get('title','')}\n{a.get('abstract','')}".lower()
        tokens = re.findall(r"[a-z][a-z\-]{4,}", text)
        for tok in set(tokens):
            if tok in MONTHS:
                continue
            if any(tok.endswith(suf) for suf in COMMON_DRUG_SUFFIXES):
                key = tok.title()
                evidence_map.setdefault(key, []).append({
                    "type": "literature",
                    "title": a.get("title", ""),
                    "source_id": a.get("source_id", ""),
                })

    return evidence_map
