import requests
from bs4 import BeautifulSoup
import json

def scrape_events():
    url = 'https://www.timeout.com/sydney/things-to-do'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        events = []

        # New selector based on latest site structure
        event_cards = soup.select('div.card-content')  # adjust this if still no result

        for card in event_cards[:10]:  # limit to 10 for demo
            title_tag = card.find('a', class_='card-title')
            if title_tag:
                title = title_tag.text.strip()
                link = title_tag['href']
                if not link.startswith('http'):
                    link = 'https://www.timeout.com' + link

                events.append({'title': title, 'link': link})

        # Save data to JSON
        with open('../events.json', 'w') as f:
            json.dump(events, f, indent=4)
        
        print("✅ Events scraped and saved to events.json")
    else:
        print(f"❌ Failed to retrieve page, status code: {response.status_code}")

if __name__ == '__main__':
    scrape_events()
