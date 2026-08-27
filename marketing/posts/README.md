# LinkedIn Posts — Ablage & Clipboard-Helfer

## Posts

Fertige Texte: `YYYY-MM-DD_post-0X.md` (Abschnitt **Fertig zum Posten**).

## Nächsten Post in die Zwischenablage

```powershell
cd "D:\Marketing Manager"
python copy_post.py
```

Dann auf LinkedIn einfügen (Strg+V).

Als erledigt markieren:

```powershell
python copy_post.py --done
```

Queue anzeigen:

```powershell
python copy_post.py --list
```

Bestimmte Datei:

```powershell
python copy_post.py --file 2026-09-01_post-01.md
```
