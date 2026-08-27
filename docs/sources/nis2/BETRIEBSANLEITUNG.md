# Betriebsanleitung — NIS2 Gap-Analyse-App

**Zielgruppe:** QM, IT, CISO, Geschäftsleitung (Betrieb vor Ort)  
**Stand:** 20. August 2026  
**Produkt:** NIS2 Readiness- & Gap-App (nicht das BSI-Portal)

> Dieses Dokument erklärt **was die App im Alltag bewirkt** und **wie Sie die Module bedienen**.  
> Technisches Änderungsprotokoll: [CHANGELOG-2026-08-20.md](./CHANGELOG-2026-08-20.md) · [CHANGELOG-2026-07-28.md](./CHANGELOG-2026-07-28.md)  
> Compliance-Hintergrund: [COMPLIANCE-HANDBUCH.md](./COMPLIANCE-HANDBUCH.md)  
> Datenherkunft: [DATENHERKUNFT.md](./DATENHERKUNFT.md)  
> § 38 Status Quo: [legal/BSIG-Paragraf-38-Status-Quo.txt](./legal/BSIG-Paragraf-38-Status-Quo.txt)

---

## 1. Schnellübersicht: Was bewirken die aktuellen Änderungen?

| Änderung | Was Sie davon haben | Was Sie tun müssen |
|----------|---------------------|--------------------|
| **Brand Navy/Teal/Amber** | Einheitliches Erscheinungsbild (Login, Header, CTAs) | Keine Aktion — UI |
| **OSCAL/OPA (Architektur)** | Zielbild: maschinenlesbare Evidence + Policy-as-Code dokumentiert | Kennen; Runtime folgt — siehe Handbuch §2.1 |
| **Trennung Incident ↔ Governance** | Schulungszertifikate landen **nicht** mehr in 24h-/72h-Behördenentwürfen. Krisenmeldung = nur Vorfall; Governance = Sorgfaltsnachweis. | Zertifikate nur unter Governance pflegen. |
| **Governance-Evidenzreport** | Nachweis „Leitung war geschult“ für Prüfung/Haftung (§ 38 BSIG), inkl. Hash-Chain und optional Server-Siegel. | Nach Schulung Zertifikat hochladen, digital bestätigen, PDF bei Bedarf exportieren. |
| **Leitungs-Review** | Billigung & Überwachung dokumentiert (B-02 / E-03). | Periodisch Review erfassen und bestätigen. |
| **Notfall-Übungen** | BCP/DR/Krise mit Protokoll → Sync C-05–C-07. | Übung erfassen, **Protokoll hochladen**, bestätigen. |
| **Sorgfaltspaket ZIP v2** | Vollarchiv für Prüfung: JSON + Dateien + Freezes + Manifest. | Nach wichtigen Bestätigungen ZIP speichern. |
| **Gesetzestext § 38** | Wortlaut + Veröffentlichungsdatum + was wir abdecken. | Button unter Governance; bei neuem Gesetz: Update durch uns. |
| **Unveränderlichkeit** | Bestätigte Nachweise können nicht still überschrieben werden. | Vor Bestätigung Inhalte/Dateien prüfen. |
| **3-Jahres-Countdown + Alarm** | Automatische Wiedervorlage; ab 30 Tagen Alarm an HCQ. | Bei Alarm neue Schulung planen; Zertifikat ersetzen. |
| **Tages-Freeze (3 Tage)** | Letzter guter Melde-Stand lokal verfügbar. | App idealerweise **täglich einmal öffnen**; Freeze auf USB. |
| **Digital Twin (HCQ)** | Ein Asset mit Funktion + Bauteil + Lieferant. | Gap → Twin-Karte pflegen. |
| **1-Monats-Abschluss (D-04)** | Bleibt **Aufgabe QM/IT vor Ort** — kein App-Modul. | Abschlussbericht im BSI-Portal / IR-Prozess führen. |
| **Datenherkunft** | Nachvollziehbar, woher Status/Twins/Nachweise stammen | Siehe [DATENHERKUNFT.md](./DATENHERKUNFT.md) |

---

## 1a. Datenherkunft (Kurz)

| Frage | Antwort |
|-------|---------|
| Wer setzt „erfüllt“? | Immer der Mensch in der Gap-UI (mit Evidenz) |
| Was liefert HCQ-K? | Vorschläge per Snapshot/API — Übernehmen/Ignorieren |
| Wo liegen Kundendaten? | Primär lokal (localStorage / IndexedDB), Air-Gap-fähig |

Ausführlich: [DATENHERKUNFT.md](./DATENHERKUNFT.md)

---

## 2. Module und Routen (Betrieb)

| Modul | Route | Wirkung im Betrieb |
|-------|-------|-------------------|
| Fragebogen | `/fragebogen` | Vorabanalyse ohne Lizenz |
| Gap Visitenkarten | `/gap/twins` … | Twin · NIS2 · CRA · ISO · Notfall · Governance |
| Zulieferer + Tages-Freeze | `/zulieferer` | Lieferkette lokal, Melde-Cache, Autarkie-Freeze |
| Governance | `/gap/governance` (auch `/governance`) | GF-Schulung, Review, § 38, ZIP, B-03 |
| Notfall | `/gap/continuity` | Übungen BCP/DR/Krise |
| 24h-Frühwarnung | `/meldung-24h` | Behörden-Frühwarnung vorbereiten (Premium) |
| 72h-Meldung | `/meldung-72h` | Detailmeldung + CEO-Freigabe (Premium) |

Demo-Zugang (falls aktiv): Zugangscode von HAMPA — Prüfung nur serverseitig (kein Code im Browser-Bundle). Impressum/Datenschutz am Demo-Login.

---

## 3. Incident-Reporting (Art. 23) — was gilt im Ernstfall

### Wirkung

Die App liefert **Entwürfe und Freigabe-Nachweise** für die Behördenmeldung.  
Sie **ersetzt nicht** das BSI-Portal (`portal.bsi.bund.de`).

### Fristen (nur Vorfall, kein Zertifikat)

1. **24 Stunden** — Frühwarnung (`/meldung-24h`)  
2. **72 Stunden** — detaillierte Meldung (`/meldung-72h`)  
3. **ca. 1 Monat** — Abschlussbericht (**QM/IT vor Ort**, nicht in der App)

### Betriebsregel

- In 24h-/72h-Entwürfen **kein** GF-Schulungszertifikat beilegen.  
- Sorgfaltsnachweise der Leitung gehören unter **Governance** und werden bei Prüfung oder Haftungsfrage vorgelegt — nicht als Beilage zum akuten Alarm.

Siehe auch: [NOTFALL-CHECKLISTE-BSI-PORTAL.md](./NOTFALL-CHECKLISTE-BSI-PORTAL.md).

---

## 4. Governance & Evidenzreport — was bewirkt das Modul?

### Wirkung

| Funktion | Betriebsnutzen |
|----------|----------------|
| Zertifikat + SHA-256 | Datei-Manipulation wird erkennbar |
| Digitale Bestätigung | Nachvollziehbar, wer wann bestätigt hat |
| Hash-Chain (Audit) | Lokale Änderungshistorie prüfbar |
| Server-Siegel (optional) | Server-Zeitstempel + HMAC, wenn API konfiguriert |
| Evidenz-PDF | Ausdruck/Archiv für Auditor, BSI-Prüfung |
| Sorgfaltspaket ZIP v2 | Vollarchiv inkl. Protokolle und Melde-Freezes |
| Leitungs-Review | Billigung/Überwachung (B-02, E-03) |
| Gesetzestext § 38 | Status-Quo-Wortlaut + Abdeckungsmatrix |
| B-03-Sync | Gap-Punkt „Schulung Leitungsorgane“ aus dem Modul |

### Bedienung (Kurz)

1. Governance-Karte öffnen → Leitungsprofil anlegen.  
2. Schulungszertifikat erfassen, Datei hochladen.  
3. Digital bestätigen (Checkbox + Name/E-Mail).  
4. Optional: Leitungs-Review erfassen (Protokoll optional) und bestätigen.  
5. **Evidenzreport (PDF)** und/oder **Sorgfaltspaket (ZIP)** speichern.  
6. Button **Gesetzestext § 38 BSIG** → Wortlaut prüfen / TXT herunterladen.  
7. Bei Ablaufalarm: neue Schulung → neues Zertifikat.

**Wichtig:** Ohne Seal-API bleibt die Chain **lokal**. Bestätigte Zertifikate/Reviews sind **unveränderlich**.

---

## 4a. Notfall-Übungen (BCP / DR / Krise)

### Wirkung

Dokumentierte Übungen mit Protokoll belegen Business Continuity / DR / Krisenmanagement und setzen die Gap-Punkte **C-05 / C-06 / C-07** nach Bestätigung.

### Bedienung

1. Visitenkarte **Notfall** (`/gap/continuity`).  
2. Übung erfassen (Art, Datum, Scope, Teilnehmer, Ergebnis).  
3. **Protokoll-Datei** hochladen (PDF/DOCX/TXT, Pflicht vor Bestätigung).  
4. Digital bestätigen → Eintrag wird unveränderlich; Audit-Eintrag mit Datei-Hash + `content_hash`.

---

## 4b. Gesetzestext § 38 BSIG (Status Quo)

### Wirkung

Belegt, **welchen** Gesetzestext das Tool zugrunde legt (Veröffentlichungsdatum + Fundstelle) und **was** Framework/Dokumentation zu Abs. 1–3 abdecken.

### Bedienung

1. Unter Governance: **Gesetzestext § 38 BSIG** öffnen.  
2. Wortlaut und Abdeckungsmatrix lesen.  
3. Optional **Textdatei herunterladen** (gleicher Inhalt wie [docs/legal/…](./legal/BSIG-Paragraf-38-Status-Quo.txt)).

### Update-Regel

Ändert sich der amtliche Wortlaut, aktualisieren **wir** `bsigSection38.ts` + die Textdatei und setzen `tool_stand_am` neu. Keine automatische Abfrage.

---

## 5. Tages-Freeze — Autarkie bei SAP-/HCQ-Ausfall

### Wirkung

Wenn die Lieferkette (z. B. SAP) oder HCQ nicht erreichbar bzw. kompromittiert ist, können Sie mit dem **eingefrorenen Stand** weiter 24h/72h vorbereiten:

- Melde-Cache (Twins/Kontakte)  
- Zulieferer-Stammdaten  
- Twin↔Zulieferer-Links  

### Automatik

- **1× pro Kalendertag** (lokale Zeitzone), sobald ein Melde-Cache existiert.  
- Speicherung in IndexedDB, **Retention 3 Tage** (ältere Freezes werden gelöscht).  
- Nach erfolgreichem Melde-Cache-Sync wird der heutige Freeze aktualisiert.

### Was Sie im Betrieb tun

| Aktion | Wann |
|--------|------|
| App öffnen | Idealerweise täglich (sonst kein neuer Auto-Freeze) |
| „Heute herunterladen (USB)“ | Für Air-Gap / getrennten Träger |
| „Wiederherstellen“ | Nur im Ernstfall — ersetzt aktuellen Cache/Zulieferer durch den Freeze-Tag |
| Live-Sync stoppen | Nach Kompromittierung der Quelle, bis Stand geprüft ist |

UI: `/zulieferer` → Abschnitt **Tages-Freeze (Meldeautarkie)**.  
Details: [MELDEAUTARK-ZULIEFERER.md](./MELDEAUTARK-ZULIEFERER.md).

---

## 6. Digital Twin: Funktion · Bauteil · Lieferant

### Wirkung

Die Gap-Analyse ist ein **Visitenkarten-Stapel**:

| Visitenkarte | Route | Inhalt |
|--------------|-------|--------|
| Digital Twin | `/gap/twins` | Funktion · Bauteil · Lieferant |
| NIS2 | `/gap/nis2` | Art. 21 · Maßnahmen · Checkliste |
| CRA | `/gap/cra` | Produkt-Compliance · Checkliste |
| ISO 27001 | `/gap/iso27001` | ISMS · Checkliste |
| Notfall | `/gap/continuity` | BCP-/DR-/Krisenübungen (bestätigt → C-05–C-07) |
| Governance | `/gap/governance` | GF-Schulung · Leitungs-Review · Sorgfaltspaket-ZIP · Gesetzestext § 38 |
| Handbuch | `/gap/handbuch` | Compliance-Handbuch (eingebettet) |
| Whitepaper | `/gap/whitepaper` | Framework-Whitepaper (eingebettet) |

Jede Karte zeigt **nur** ihr Thema — Navigation links, Inhalt rechts.

Jeder Digital Twin hat drei Dimensionen (SSOT in HCQ-K):

| Dimension | Quelle |
|-----------|--------|
| **Funktion** | `metadata.process_function` (HCQ) · lokal als Offline-Fallback |
| **Bauteil** | `metadata.asset_type` / Version (HCQ) |
| **Lieferant** | `metadata.supplier_refs[]` (HCQ) · Stammdaten lokal unter `/zulieferer` |

### Bedienung

1. Gap-Analyse öffnen — Kartenstapel oben wählen (nur **eine** Karte sichtbar).
2. Karte **Digital Twin** tippen — kein Scrollen durch Scorecard/Checkliste.
3. Scorecard lit. **d** / **e** springt zur Twin-Karte.

---

## 7. Export & Backup (was bewirkt der JSON-Export?)

| Export | Wirkung |
|--------|---------|
| Gap-JSON | Gesamtstand der Checkliste inkl. Governance-Metadaten |
| `_governance_certificate_blobs` | Zertifikat-Dateien aus IndexedDB im Backup enthalten |
| **Sorgfaltspaket (ZIP) v2** | `liability-evidence.json` + Anhänge (Zertifikate, Übungs-/Review-Protokolle) + Melde-Freezes + SHA-256-Manifest + Integrity |
| Melde-Snapshot | Offline-Übergabe Twins + Zulieferer (`nis2-melde-snapshot-v1`) |
| Tages-Freeze Download | Tagesgenauer Autarkie-Stand für USB |

**Notfall-Übungen:** Vor Bestätigung ist ein Protokoll (PDF/DOCX/TXT) erforderlich. Bestätigte Übungen/Reviews/Zertifikate sind unveränderlich.

**Praxis:** Nach wichtigen Änderungen Gap-JSON **und** Freeze/Snapshot auf gesichertes Laufwerk legen.

---

## 8. Rollen — wer macht was?

| Rolle | Typische Aufgaben in der App |
|-------|------------------------------|
| **Geschäftsleitung** | Governance / Review / Übungen bestätigen; § 38 lesen; 72h CEO-Freigabe |
| **Qualitätsleitung** | 24h-Freigabe; Gap-Status; Sorgfaltspaket archivieren |
| **IT / Security** | HCQ-Sync, Twin-Links, Melde-Cache, Tages-Freeze, USB-Backup, Protokolle hochladen |
| **HCQ / Berater** | Ablaufalarm-Mails; Schulung nachziehen; Gesetzes-Status-Quo pflegen |

---

## 9. Grenzen (ehrlich)

- Kein Auto-Versand an das BSI.  
- Kein 1-Monats-Abschlussmodul in der App.  
- Tages-Freeze braucht, dass die App am Tag geöffnet wird (kein Server-Cron).  
- Browser-Daten allein sind kein Air-Gap — USB-Download bleibt Pflicht für kritische Stände.  
- Server-Siegel nur mit korrekt gesetzten Env-Variablen (siehe `app/.env.example`).  
- Keine Haftungsfreiheit / kein WORM-Notariat — Sorgfaltspaket dokumentiert, ersetzt keine Rechtsberatung.  
- § 38-Text ist Status Quo zum Einpflege-Datum — bei Gesetzesänderung manuelles Update.

---

## 10. Weiterführende Dokumente

| Dokument | Nutzen |
|----------|--------|
| [COMPLIANCE-HANDBUCH.md](./COMPLIANCE-HANDBUCH.md) | Regelbezug NIS2/CRA/ISO · Kap. 13 § 38 |
| [DATENHERKUNFT.md](./DATENHERKUNFT.md) | Provenienz: Gap-, Twin-, Mapping-Quellen |
| [CHANGELOG-2026-08-20.md](./CHANGELOG-2026-08-20.md) | Brand, OSCAL/OPA, Datenherkunft |
| [CHANGELOG-2026-07-28.md](./CHANGELOG-2026-07-28.md) | Technische Änderung + Testergebnis |
| [legal/BSIG-Paragraf-38-Status-Quo.txt](./legal/BSIG-Paragraf-38-Status-Quo.txt) | Gesetzestext-Beleg |
| [MELDEAUTARK-ZULIEFERER.md](./MELDEAUTARK-ZULIEFERER.md) | Guards, Snapshot-Schema, Abnahme |
| [NOTFALL-CHECKLISTE-BSI-PORTAL.md](./NOTFALL-CHECKLISTE-BSI-PORTAL.md) | Portal-Ernstfall |
| [USB-STICK-CHECKLISTE.md](./USB-STICK-CHECKLISTE.md) | Offline-Übergabe |
| [compliance/reports/TESTLAUF-2026-07-29.md](./compliance/reports/TESTLAUF-2026-07-29.md) | Gate-Testlauf 29.07.2026 |
