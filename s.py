import requests

# Masukkan API Key dari SMS-Activate
API_KEY = "40c7B97ffB05307fff15dBe5656e36f5"

def get_number(country_code):
    url = f"https://api.sms-activate.ae/stubs/handler_api.php?api_key={API_KEY}&action=getNumber&service=wa&maxPrice=0&country={country_code}"
    response = requests.get(url).text
    
    if "ACCESS_NUMBER" in response:
        parts = response.split(":")
        activation_id = parts[1]
        phone_number = parts[2]
        print("\n===> NOKOS BY DIZ FLYZE <===")
        print(f"CODE : +{country_code}")
        print(f"NUMBER : {phone_number}")
        print("AKTIF : WHATSAPP")
        print("===> NOKOS BY DIZ FLYZE <===\n")
        return activation_id, phone_number
    else:
        print("Gagal mendapatkan nomor, coba lagi.")
        return None, None

def get_sms(activation_id):
    url = f"https://api.sms-activate.ae/stubs/handler_api.php?api_key={API_KEY}&action=getStatus&id={activation_id}"
    print("Menunggu SMS dari WhatsApp...")
    
    while True:
        response = requests.get(url).text
        if "STATUS_OK" in response:
            sms_code = response.split(":")[1]
            print("\n===> NOKOS BY DIZ FLYZE <===")
            print(f"SMS CODE : {sms_code}")
            print("===> NOKOS BY DIZ FLYZE <===\n")
            break

if __name__ == "__main__":
    country_code = input("MASUKAN KODE NEGARA: ")
    activation_id, phone_number = get_number(country_code)
    
    if activation_id:
        get_sms(activation_id)
