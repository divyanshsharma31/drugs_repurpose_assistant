from typing import Dict, List

def demo_evidence(drug: str) -> Dict[str, List[dict]]:
    d = drug.strip().lower()
    data: Dict[str, Dict[str, List[dict]]] = {
        "metformin": {
            "Breast Cancer": [
                {"type": "literature", "title": "Metformin and tumor metabolism", "source_id": "PMID:demo1"},
                {"type": "trial", "title": "Metformin in HER2- breast cancer", "phase": "Phase 2", "status": "Recruiting", "source_id": "NCT:demo1"},
            ],
            "Alzheimer's Disease": [
                {"type": "literature", "title": "AMPK activation and neuroprotection", "source_id": "PMID:demo2"},
            ],
            "Polycystic Ovary Syndrome": [
                {"type": "trial", "title": "Metformin in PCOS", "phase": "Phase 3", "status": "Completed", "source_id": "NCT:demo2"},
            ],
        },
        "aspirin": {
            "Colorectal Cancer": [
                {"type": "literature", "title": "Aspirin and colorectal cancer chemoprevention", "source_id": "PMID:demo3"},
            ],
            "Preeclampsia": [
                {"type": "trial", "title": "Low-dose aspirin for preeclampsia prevention", "phase": "Phase 3", "status": "Completed", "source_id": "NCT:demo3"},
            ],
            "COVID-19": [
                {"type": "literature", "title": "Antiplatelet therapy and COVID coagulopathy", "source_id": "PMID:demo4"},
            ],
        },
        "propranolol": {
            "Infantile Hemangioma": [
                {"type": "trial", "title": "Propranolol for hemangioma", "phase": "Phase 3", "status": "Completed", "source_id": "NCT:demo4"},
            ],
            "PTSD": [
                {"type": "literature", "title": "Beta-blockade and memory reconsolidation", "source_id": "PMID:demo5"},
            ],
        },
        "atorvastatin": {
            "Sepsis": [
                {"type": "literature", "title": "Statins and inflammation modulation in sepsis", "source_id": "PMID:demo6"},
            ],
            "Multiple Sclerosis": [
                {"type": "trial", "title": "Atorvastatin adjunct in MS", "phase": "Phase 2", "status": "Completed", "source_id": "NCT:demo5"},
            ],
        },
    }
    return data.get(d, {})


def demo_treatments(condition: str) -> Dict[str, List[dict]]:
    c = condition.strip().lower()
    data: Dict[str, Dict[str, List[dict]]] = {
        "migraine": {
            "Sumatriptan": [
                {"type": "trial", "title": "Sumatriptan in acute migraine", "phase": "Phase 3", "status": "Completed", "source_id": "NCT:demoM1"}
            ],
            "Propranolol": [
                {"type": "literature", "title": "Beta-blockers for migraine prophylaxis", "source_id": "PMID:demoM2"}
            ],
        },
        "asthma": {
            "Salbutamol": [
                {"type": "trial", "title": "Albuterol efficacy in asthma", "phase": "Phase 3", "status": "Completed", "source_id": "NCT:demoA1"}
            ],
            "Montelukast": [
                {"type": "literature", "title": "Leukotriene antagonists in asthma control", "source_id": "PMID:demoA2"}
            ],
        },
        "hypertension": {
            "Amlodipine": [
                {"type": "trial", "title": "Amlodipine monotherapy in hypertension", "phase": "Phase 3", "status": "Completed", "source_id": "NCT:demoH1"}
            ],
            "Losartan": [
                {"type": "literature", "title": "ARB therapy outcomes", "source_id": "PMID:demoH2"}
            ],
        },
        "diabetes": {
            "Metformin": [
                {"type": "trial", "title": "Metformin outcomes in T2D", "phase": "Phase 3", "status": "Completed", "source_id": "NCT:demoD1"}
            ],
            "Empagliflozin": [
                {"type": "literature", "title": "SGLT2 inhibitors and cardio-renal benefit", "source_id": "PMID:demoD2"}
            ],
        },
    }
    return data.get(c, {})


def _normalize_condition(name: str) -> str:
    n = (name or "").strip().lower()
    aliases = {
        "migrane": "migraine",
        "covid": "covid-19",
        "hbp": "hypertension",
        "bp": "hypertension",
    }
    return aliases.get(n, n)


def demo_treatments(condition: str) -> Dict[str, List[dict]]:
    c = _normalize_condition(condition)
    data: Dict[str, Dict[str, List[dict]]] = {
        "migraine": {
            "Sumatriptan": [
                {"type": "trial", "title": "Sumatriptan for acute migraine", "phase": "Phase 3", "status": "Completed", "source_id": "NCT:demo7"},
            ],
            "Propranolol": [
                {"type": "literature", "title": "Beta-blockers for migraine prophylaxis", "source_id": "PMID:demo8"},
            ],
            "Topiramate": [
                {"type": "trial", "title": "Topiramate in episodic migraine prevention", "phase": "Phase 3", "status": "Completed", "source_id": "NCT:demo9"},
            ],
        },
        "asthma": {
            "Budesonide": [
                {"type": "trial", "title": "ICS therapy in persistent asthma", "phase": "Phase 3", "status": "Completed", "source_id": "NCT:demo10"},
            ],
            "Montelukast": [
                {"type": "literature", "title": "Leukotriene receptor antagonists in asthma", "source_id": "PMID:demo11"},
            ],
        },
        "hypertension": {
            "Losartan": [
                {"type": "trial", "title": "ARB efficacy in stage 1 hypertension", "phase": "Phase 3", "status": "Completed", "source_id": "NCT:demo12"},
            ],
            "Amlodipine": [
                {"type": "literature", "title": "Calcium-channel blockers in hypertension management", "source_id": "PMID:demo13"},
            ],
        },
        "covid-19": {
            "Dexamethasone": [
                {"type": "trial", "title": "RECOVERY: Dexamethasone in hospitalized COVID-19", "phase": "Phase 3", "status": "Completed", "source_id": "NCT:demo14"},
            ],
            "Remdesivir": [
                {"type": "trial", "title": "Antiviral therapy and time-to-recovery", "phase": "Phase 3", "status": "Completed", "source_id": "NCT:demo15"},
            ],
        },
    }
    return data.get(c, {})
