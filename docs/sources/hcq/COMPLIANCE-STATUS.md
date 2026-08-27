# Compliance-Status — Master-Übersicht

**Stand:** 2026-07-07 · **Prozess:** SUP.1, MAN.6 · **Baseline:** 0.1.0 ·
**Bezug:** [`ADR-0024`](../architecture/adr/ADR-0024-compliance-norm-matrix.md),
[`HCQ-SELF-AUDIT-PACKAGE.md`](../quality/HCQ-SELF-AUDIT-PACKAGE.md)

> **Disclaimer (verbindlich):** Dieses Dokument ist eine **interne Selbstbewertung**
> auf Basis von Repo-Nachweisen (Dokumentation, Code, Tests). Es begründet **keinen**
> Anspruch auf externe Zertifizierung oder formelles Assessment durch akkreditierte
> Stellen (ASPICE, IATF 16949, ISO 26262, ISO/IEC 42001, EU AI Act, ISO/SAE 21434).
> Bewusst offene Punkte sind als Roadmap ausgewiesen — nicht verschwiegen.

---

## 1. Reifegrad-Matrix (Master)

| Norm / Standard | Reife % | Status | Nachweis (Evidenz im Repo) |
|-----------------|--------:|--------|----------------------------|
| **ASPICE v4.0** (SWE + SYS) | ~78 % | **Partial** | [`compliance-norm-matrix.md`](../quality/compliance-norm-matrix.md) §2, [`process/`](../process/) (SYS/SWE), [`standard-process.md`](../process/standard-process.md), `src/hcq/compliance_matrix/`, API `GET /compliance/standards/aspice_v40` |
| **ISO 26262:2018** | ~62 % | **Partial** | [`compliance-norm-matrix.md`](../quality/compliance-norm-matrix.md) §3, `src/hcq/risk_engine/` (HARA/ASIL), [`ADR-0009`](../architecture/adr/ADR-0009-dfmea-risk-engine.md), `tests/test_risk_engine.py` |
| **ISO/IEC 42001:2023** | ~68 % | **Partial** | [`ai-governance/`](../ai-governance/), [`ai-requirements.md`](../requirements/ai-requirements.md), `src/hcq/ai_governance/`, [`ADR-0029`](../architecture/adr/ADR-0029-ai-governance-operational.md), `tests/test_ai_governance.py` |
| **EU AI Act** (VO 2024/1689) | ~60 % | **Partial** | [`ai-requirements.md`](../requirements/ai-requirements.md) (AIREQ-*), [`ai-governance/`](../ai-governance/), [`data-isolation-security-note.md`](../quality/data-isolation-security-note.md) — **keine** abgeschlossene Rechtsklassifizierung |
| **IATF 16949:2016** | ~72 % | **Partial** | [`iatf16949-documentation-map.md`](../quality/iatf16949-documentation-map.md), `src/hcq/iatf16949/`, [`ADR-0013`](../architecture/adr/ADR-0013-iatf16949-compliance.md), `tests/test_iatf16949.py`, API `GET /iatf/audit-readiness` |
| **ISO/SAE 21434** (Cybersecurity) | ~5 % | **Roadmap** | Nur strategischer Bezug in Projektgrundsätzen; **kein** dediziertes TARA-/CSMS-Mapping, kein Modul in `compliance_matrix` — siehe [`zero-trust-compliance-matrix.md`](../security/zero-trust-compliance-matrix.md) (Security, nicht 21434-äquivalent) |
| **ISO 10218 / ISO/TS 15066 / ISO 13849 / IEC 62443** (Robotik) | ~18 % | **Partial/Roadmap** | [`compliance-norm-matrix.md`](../quality/compliance-norm-matrix.md) §6 (19 kuratierte Klauseln: 12 partial / 7 roadmap / 0 fulfilled), `src/hcq/compliance_matrix/` Domain `robotics`, 4 Diagnose-Profile (`iso_10218_cl2`, `iso_ts_15066`, `iso_13849`, `iec_62443` + `robotics_base`, `SWREQ-242/QT-242`), `GET /compliance/overview?domain=robotics`, Login-Voreinstellung (`SWREQ-229/230`); kein Robotik-Zertifikat |

**Status-Legende:**

| Status | Bedeutung |
|--------|-----------|
| **Complete** | Kuratierter Normausschnitt mit durchgängigem Nachweis (Doku + Code + Test); selten bei HCQ wegen bewusst offener Roadmap-Punkte |
| **Partial** | Kernartefakte und operative Module vorhanden; Lücken transparent dokumentiert |
| **Scaffold** | Struktur/Platzhalter angelegt, fachliche Umsetzung unvollständig |
| **Roadmap** | Bewusst nicht umgesetzt; nur Planungs-/Scope-Bezug |

**Lesart der Reife-%:** Konservative Schätzung über erfüllte vs. kuratierte Klauseln bzw.
Work Products je Standard (siehe [`compliance-norm-matrix.md`](../quality/compliance-norm-matrix.md)
und interner Score ~75/100 in [`HCQ-SELF-AUDIT-PACKAGE.md`](../quality/HCQ-SELF-AUDIT-PACKAGE.md)).
Kein Ersatz für ein formales Assessment.

---

## 2. Verknüpfte Quelldokumente

| Dokument | Zweck |
|----------|-------|
| [`HCQ-PRODUKT-COMPLIANCE-PAKET.md`](HCQ-PRODUKT-COMPLIANCE-PAKET.md) | **Master-Paket:** Dogfooding, Scope/Tailoring, Operator-Checkliste, Evidenzindex |
| [`HCQ-EVIDENZ-MATRIX.md`](HCQ-EVIDENZ-MATRIX.md) | Requirement → Artefakt → Test → Status |
| [`HCQ-CRA-SELBSTBEWERTUNG.md`](HCQ-CRA-SELBSTBEWERTUNG.md) | CRA-Readiness HCQ als Vendor-Software (ehrlich, kein Zertifikat) |
| [`documentation-gaps.md`](../quality/documentation-gaps.md) | Ehrliche Gap-Analyse: was rückverfolgbar ist, was offen bleibt |
| [`compliance-norm-matrix.md`](../quality/compliance-norm-matrix.md) | Klausel-für-Klausel-Mapping Norm → HCQ-Nachweis → Status |
| [`requirements-traceability-matrix.md`](../traceability/requirements-traceability-matrix.md) | RTM (menschenlesbar): Req → Design → Code → Test |
| [`ai-governance/`](../ai-governance/) | ISO 42001 / EU AI Act Work Products (Policy, AIIA, Risk, Dataset, Model Card, V&V, Monitoring) |

**Maschinenlesbare Live-Quelle:** `GET /compliance/overview`, `GET /compliance/export`
(`src/hcq/compliance_matrix/service.py`).

---

## 3. Top 5 offene Maßnahmen (ehrlich)

| # | Maßnahme | Priorität | Bezug |
|---|----------|-----------|-------|
| 1 | **Keine externe Zertifizierung** — ASPICE-Assessment, IATF-Audit, ISO-42001-Zertifikat durch Dritte fehlen | Hoch (OEM-Due-Diligence) | [`documentation-gaps.md`](../quality/documentation-gaps.md) §Bekannte Lücken #1, [`HCQ-SELBSTAUDIT-REPORT.md`](../quality/HCQ-SELBSTAUDIT-REPORT.md) NC-01 |
| 2 | **ISO/SAE 21434** — kein CSMS/TARA-Mapping, kein dediziertes Cybersecurity-Engineering-Modul | Hoch (Automotive-Cybersecurity) | Projektgrundsätze; Roadmap |
| 3 | **EU AI Act Risikoklassifizierung** (AIREQ-013) — dokumentierte, rechtlich geprüfte Einstufung offen | Mittel | [`ai-requirements.md`](../requirements/ai-requirements.md) |
| 4 | **Enterprise-Security** — PKI, HSM, zentraler Rate-Limit-Store, Anomalie-Scoring noch Roadmap | Mittel | [`documentation-gaps.md`](../quality/documentation-gaps.md) #6, [`ADR-0030`](../architecture/adr/ADR-0030-security-depth-increment.md) |
| 5 | **Echte Enterprise-Connectoren** (SAP OData/RFC, DOORS DXL, PLM REST) — nur Simulations-Gateways + CSV-Demo | Mittel | [`documentation-gaps.md`](../quality/documentation-gaps.md) #2, [`ADR-0031`](../architecture/adr/ADR-0031-demo-simulation-framework-sap-doors-plm.md) |

---

## 4. Nächste Schritte

| Schritt | Artefakt | Status |
|---------|----------|--------|
| **Schritt 2 (geplant)** | [`TEST-INDEX`](../test/TEST-INDEX.md) — zentraler Test-Nachweisindex (Modul → pytest → SWREQ/QT) | **Noch nicht erstellt** |
| Laufend | Compliance-Matrix bei neuen Features in `service.py` pflegen | Aktiv |
| Laufend | `traceability.yaml` ↔ `srs.md` synchron halten | Aktiv |

> **Hinweis:** `TEST-INDEX.md` ist Teil der geplanten Compliance-Dokumentationskette
> (Schritt 2). Dieses Dokument verweist darauf vorab; der Index selbst wird separat angelegt.

---

*Vertraulich – nur zur internen Verwendung. © Hampa Core Q.*
