import requests
import pandas as pd
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

# ⚙️ Google Sheets configuration
SCOPES = ["https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"]

# 🔑 Charger les credentials depuis le fichier JSON
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
gc = gspread.authorize(creds)

# 📄 Créer / ouvrir Google Sheets
sh = gc.create("Pronostics_Foot_Auto")
worksheet = sh.get_worksheet(0)

# 🌍 Exemple de données (test)
data = {
    "Match": ["Team A vs Team B", "Team C vs Team D"],
    "Pronostic": ["1", "Over 2.5"],
    "Date": [datetime.now().strftime("%Y-%m-%d %H:%M")] * 2
}

df = pd.DataFrame(data)

# 🔄 Mettre à jour la feuille
worksheet.update([df.columns.values.tolist()] + df.values.tolist())

print("✅ Données envoyées automatiquement vers Google Sheets")
print("📌 Lien du fichier :", sh.url)
