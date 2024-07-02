import json
import httpx
from time import sleep

CLIENT = httpx.Client(
    headers={
        "x-ig-app-id": "936619743392459",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Accept-Language": "ja-JP,ja;q=0.9,en-US,en;q=0.8,ru;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
    }
)

def scrape(username):
    
    res = CLIENT.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}")

    if res.status_code != 200:
        print("You've sent too many requests in a short period of time.")
        print("Please try again a little while later.")
        return
    else:
        data = json.loads(res.content)
        return data["data"]["user"]
