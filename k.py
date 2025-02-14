#!/usr/bin/env python3
import requests

API_KEY = "SmqiwkKOQfj02BmmIaTSMb3DXWxOTcOK"
TOKEN = "GBQSimfvjGpVnfuq"

TRACK_LINK = f"https://dizflyzeapikey.vercel.app/api/track?apikey={API_KEY}&token={TOKEN}"
print("Link :", TRACK_LINK)

response = requests.get(TRACK_LINK)
print(response.text)
