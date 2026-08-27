# HCQ Demo — 5-Minute Quickstart (Sales)

**Ziel:** Zeigen, dass HCQ **Export-Dateien** aus typischen Automotive-Werkzeugen
einliest und synchronisiert — kuratierte CSV-Dateien in `data/demo/` simulieren
DOORS-, SAP- und PLM-Exporte mit realistischen Feldnamen und IDs.

**Datenherkunft (vollständig):** [`docs/DATENHERKUNFT.md`](../DATENHERKUNFT.md) — Demo-Seed vs. Produktion, Speicherschichten, OSCAL/OPA.

## Voraussetzungen

- Python 3.11+, Repo geklont
- `pip install -e ".[dev]"` im Projektroot

## 1. Simulation starten (2 Min.)

```powershell
cd C:\Users\Kai\Documents\HCQ
$env:ENVIRONMENT = "simulation"
$env:INITIAL_ADMIN_MUST_CHANGE_PASSWORD = "false"
hcq-seed --profile demo --force
uvicorn hcq.api.app:create_app --factory --host 127.0.0.1 --port 8000
```

`hcq-seed --profile demo` laedt die CSV-Exporte aus `data/demo/` (oder
`DEMO_DATA_DIR`) und synchronisiert DOORS/SAP/PLM in HCQ.

In einem zweiten Terminal (Frontend):

```powershell
cd frontend
npm install
npm run dev
```

Login: `admin` / `hcq-admin-change-me` (nur Simulation).

**Branchenwahl (SWREQ-229):** Auf der Login-Seite **Automotive** oder **Robotik** wählen,
dann **Demo starten**. Nach dem Login bleibt der Umschalter in der **Kopfzeile** — unter
**Compliance** sieht man die passende Norm-Matrix.

**Schnellweg in der UI:** Nach dem Login erscheint in der Kopfzeile (neben DE|EN)
der Button **„Simulation“**. Ein Klick synchronisiert die Demo-Exporte per
`POST /integrations/sync-all` und oeffnet die Integrations-Uebersicht.

## 2. APIs live zeigen (1 Min.)

OpenAPI: http://127.0.0.1:8000/docs

| Endpoint | Was es beweist |
|----------|----------------|
| `GET /integrations/doors/requirements` | 12× `DOORS-REQ-xxx` aus `doors_requirements_export.csv` |
| `GET /integrations/sap/changes` | `SAP-CHG-001` … aus `sap_change_masters.csv` |
| `GET /integrations/plm/parts` | `PLM-PART-001` … `PLM-PART-005` aus `plm_parts.csv` (5 Bauteile, Zeichnungslink) |
| `GET /integrations/plm/parts/{id}` | Einzelteil inkl. `drawing_url` / `drawing_container` |
| `GET /demo/drawings/{filename}` | Demo-Zeichnung aus `data/demo/drawings/` |
| `GET /integrations/status` | Quelldateien, letzter Import, Export-Vorschau |
| `POST /integrations/sync-all` | `source_file`, `records_read`, `synced_at` |
| `GET /traceability/by-material/{nr}` | Material → APQP/PPAP-Kette (5 Demo-Materialnummern) |

## 3. UI-Demo (2 Min.)

**Sales-Script (DE):** *„Hier sehen Sie den DOORS-Export, den wir gerade
eingespielt haben — `doors_requirements_export.csv` mit 12 Anforderungen,
ASIL-Verknuepfung und Zeitstempel. SAP- und PLM-Exporte laufen parallel.“*

1. **Integrationen (Sim)** — Quelldateien, „Synchronisieren“, Export-Vorschau (3 Zeilen)
2. **Anforderungen** — Detail oeffnen: Badge `DOORS-REQ-001` (nach Demo-Seed)
3. **Architektur** — PLM-verknuepfte Komponenten (`PLM-PART-xxx`); Detail: Bauteilname, **Zeichnung oeffnen**
4. **Change & Config** — SAP-Sync Change Requests (`SAP-CHG-xxx`)
5. **Traceability → Material / APQP** — `100000001` oder `MAT-001` (Steuergerät); siehe [`DEMO-PARTS.md`](DEMO-PARTS.md) fuer alle 5 Demo-Bauteile
6. **QA Dashboard / Audit Cockpit** — Querverknuepfte Traceability

## Manuelle Re-Sync (optional)

```bash
curl -X POST http://127.0.0.1:8000/integrations/sync-all -H "Authorization: Bearer <token>"
```

## Ehrliche Abgrenzung

Die CSV-Dateien in `data/demo/` sind **kuratierte Demo-Exporte**, keine echten
Kundendaten aus SAP, DOORS oder PLM. Sie dienen dem Nachweis der HCQ-
Integrationsarchitektur (ADR-0031, ADR-0008). Echte Connectoren bleiben Roadmap.
