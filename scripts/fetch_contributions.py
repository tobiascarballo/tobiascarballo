import os
import json
import requests
from bs4 import BeautifulSoup

# Tu usuario de GitHub
USERNAME = "tobiascarballo"

def fetch_contributions():
    url = f"https://github.com/users/{USERNAME}/contributions"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    print(f"Obteniendo contribuciones para @{USERNAME}...")
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error al obtener datos: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    days = soup.find_all("td", class_="ContributionCalendar-day")
    
    calendar_data = []
    total_contribs = 0

    for day in days:
        date = day.get("data-date")
        level = day.get("data-level", "0")
        if date:
            # Obtener conteo de contribuciones del tool-tip o texto
            calendar_data.append({
                "date": date,
                "level": int(level)
            })

    # Extraer total anual si está disponible en el texto
    h2 = soup.find("h2", class_="f4 text-normal mb-2")
    if h2:
        text = h2.get_text(strip=True)
        total_str = "".join(filter(str.isdigit, text))
        if total_str:
            total_contribs = int(total_str)

    output = {
        "username": USERNAME,
        "total_contributions": total_contribs,
        "days": calendar_data
    }

    os.makedirs("data", exist_ok=True)
    with open("data/contributions.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"Listo! Guardado en data/contributions.json ({len(calendar_data)} dias obtenidos)")

if __name__ == "__main__":
    fetch_contributions()