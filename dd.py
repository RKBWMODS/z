import random
import string
import time

# Fungsi untuk menghasilkan kode verifikasi
def generate_verification_code():
    return ''.join(random.choices(string.digits, k=6))

# Fungsi untuk membuat API Key
def generate_api_key():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=32))

# Fungsi untuk pendaftaran dan verifikasi
def register_user():
    print("[==> WELCOME <==]")
    print("* REGISTER TO LOGIN *")

    email = input("EMAIL : ")
    password = input("PASSWORD : ")

    # Menghasilkan kode verifikasi acak
    verification_code = generate_verification_code()
    
    # Simpan kode verifikasi ke file
    with open("verification_code.txt", "w") as f:
        f.write(verification_code)
    
    print("Kode verifikasi telah disimpan. Silakan buka file 'verification_code.txt' untuk melihat kode verifikasi.")
    user_code = input("CODE : ")

    # Verifikasi kode yang dimasukkan pengguna
    if user_code == verification_code:
        print("\n[==• APIKEY DDOS •==]")
        print(f"YOUR IP : {get_ip()}")  # Mengambil IP pengguna
        api_key = generate_api_key()
        expiration_date = time.strftime("%Y-%m-%d", time.gmtime(time.time() + 60*60*24*30))  # Kadaluwarsa dalam 30 hari
        creation_date = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        
        # Menampilkan informasi API Key
        print(f"YOUR APIKEY : {api_key}")
        print(f"YOUR RUN SC : DIZ FLYZE")
        print(f"KADALUARSA : {expiration_date}")
        print(f"DI BUAT PADA : {creation_date}")
        
        # Menyimpan API Key dan informasi
        save_api_key(api_key, email, expiration_date, creation_date)
    else:
        print("Kode verifikasi salah. Pendaftaran gagal.")

# Fungsi untuk menyimpan API Key ke file
def save_api_key(api_key, email, expiration_date, creation_date):
    with open("apikeys.json", "a") as file:
        file.write(f"{api_key} | {email} | {expiration_date} | {creation_date}\n")

# Fungsi untuk mendapatkan IP pengguna
def get_ip():
    import socket
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

if __name__ == "__main__":
    register_user()
