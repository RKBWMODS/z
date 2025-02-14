import requests

def get_number():
    url = "https://sms-activate.org/api/getNumbers"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("===> NOKOS BY DIZ FLYZE <===")
        print("CODE :", data["country_code"])
        print("NUMBER :", data["number"])
        print("AKTIF : WHATSAPP")
        print("===> NOKOS BY DIZ FLYZE <===")
        return data["id"]
    else:
        print("Gagal mendapatkan nomor")

def get_sms(id):
    url = f"https://sms-activate.org/api/getSms?id={id}"
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "sms" in data:
                print("SMS CODE:", data["sms"])
                break

nomor_id = get_number()
if nomor_id:
    get_sms(nomor_id)
