#!/usr/bin/env python3
import requests

API_KEY = "Nb2ibfdL8UlKSlXOthxZsZODvIc6mpdR"
TOKEN = "3XDrkumDH2HlhQRI"

TRACK_LINK = f"https://dizflyzeapi.vercel.app/api/track?apikey={API_KEY}&token={TOKEN}"
print("Link :", TRACK_LINK)

response = requests.get(TRACK_LINK)
print(response.text)
