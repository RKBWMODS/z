#!/usr/bin/env python3
import requests

API_KEY = "JVaKxhhFb7yRqJ23c9qf2Jl5ATG1b98h"
TOKEN = "8VfU5q8mibzPFf3I"

TRACK_LINK = f"https://dizflyzeapikey.vercel.app/api/track?apikey={API_KEY}&token={TOKEN}"
print("Link :", TRACK_LINK)

response = requests.get(TRACK_LINK)
print(response.text)
