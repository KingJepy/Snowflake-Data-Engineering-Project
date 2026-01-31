import requests
from bs4 import BeautifulSoup

BASE = "https://www.mtgtop8.com"

def get_event_links():
    url = f"{BASE}/format?f=ST"
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")

    print(soup.prettify())

    event_links = set()
    for a in soup.select("a[href*='event?e=']"):
        event_links.add(BASE + "/" + a["href"])

    return list(event_links)

events = get_event_links()
print(f"Found {len(events)} events")

for event in events:
    print(event)

