import requests
from bs4 import BeautifulSoup

BASE = "https://www.mtgtop8.com"

def get_last_20_event_links():
    url = f"{BASE}/format?f=ST"
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")
    
    # Find the div that says "LAST 20 EVENTS"
    last_20_div = soup.find("div", string="LAST 20 EVENTS")
    if not last_20_div:
        return []

    # The table we want is the next <table> after this div
    table = last_20_div.find_next("table")
    
    # Get all event links in that table
    event_links = []
    for a in table.find_all("a", href=True):
        href = a['href']
        if "event?e=" in href:
            event_links.append(BASE + "/" + href)

    return event_links

events = get_last_20_event_links()
print(f"Found {len(events)} events:")
for e in events:
    print(e)
