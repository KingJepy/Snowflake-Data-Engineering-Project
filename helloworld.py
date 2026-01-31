import requests
from bs4 import BeautifulSoup

BASE = "https://www.mtgtop8.com"

def get_last_20_event_links():
    url = f"{BASE}/format?f=ST"
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")
    
    # Find the div that contains "LAST 20 EVENTS" in its text
    last_20_div = None
    for div in soup.find_all("div", class_="w_title"):
        if "LAST 20 EVENTS" in div.get_text(strip=True):
            last_20_div = div
            break
    
    if not last_20_div:
        return []

    # The table we want is the next <table> after this div
    table = last_20_div.find_next("table")
    
    # Extract all event links from that table
    event_links = []
    for a in table.find_all("a", href=True):
        if "event?e=" in a["href"]:
            event_links.append(BASE + "/" + a["href"])
    
    return event_links

# Test it
events = get_last_20_event_links()
print(f"Found {len(events)} events:")
for e in events:
    print(e)