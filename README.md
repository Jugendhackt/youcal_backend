# Youcal - Youtube Comment Analyzer (Backend)
Youcal (kurz für YouTube Comment Analyzer) ist ein Tool zur Auswertung von YouTube-Kommentaren. Es soll helfen einen Meinungstrend aus YouTube-Kommentaren zu generieren.
## Installation
### 1. Klonen des Git-Repositories
```
git clone https://github.com/Jugendhackt/youcal_backend.git
```
### 2. Aufsetzen der Virtual Environment (venv)
```
python3 -m venv venv
```
### 3. Aktivieren der venv (je nach Betriebssystem und Shell verschieden). Auf Linux mit Bash:
```
source venv/bin/activate
```
### 4. Installieren der Requirements
```
pip3 install -r requirements.txt
```
Hierbei können Probleme bei Windows bei der Installation von PyTorch auftreten. Um PyTorch auf Windows zu installieren kannst Du einen Blick auf die offizielle PyTorch-Website werfen: (https://pytorch.org/get-started/locally/)
## Setzen der Environment-Variables
Einvironment-Variablen werden dafür genutzt, das private Daten wie z.B. Passwörter nicht im Klartext im Code stehen müssen. Um sie zu nutzen muss eine Datei erstellt werden, welche ```.env``` heißt. In dieser Datei wird in der ersten Zeile der API-Key festgelegt, den man sich von der Google-Developer-Console besorgen kann. (Mehr Infos: https://developers.google.com/youtube/v3?hl=de)<br>
Die Zeile für die Datei lautet wie folgt:
```
API_KEY = <YOUR_API_KEY>
```

## Starten des Servers
```
uvicorn main:app --reload
```
## Ergebnis
Bei beachten dieser Schritte sollte das aufsetzen kein Problem mehr sein. Der Server sollte normalerweise unter http://127.0.0.1:8000 verfügbar sein.