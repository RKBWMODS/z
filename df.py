import sys
import json
import time
import requests

# Fungsi untuk memverifikasi API Key
def verify_api_key(api_key):
    with open("apikeys.json", "r") as file:
        data = file.readlines()
        for line in data:
            if api_key in line:
                return True
    return False

# Fungsi untuk memulai serangan DDoS (menggunakan API Key)
def start_ddos_attack(target_url, api_key):
    if not verify_api_key(api_key):
        print("API Key tidak valid!")
        sys.exit(1)

    print(f"Memulai serangan DDoS ke {target_url} dengan API Key {api_key}")
    # Lakukan serangan DDoS
    response = requests.get(target_url)
    print(f"Status code: {response.status_code}")

if __name__ == "__main__":
    api_key = input("Masukkan API Key Anda: ")
    target_url = input("Masukkan target URL untuk DDoS: ")

    # Memulai serangan DDoS
    start_ddos_attack(target_url, api_key)
