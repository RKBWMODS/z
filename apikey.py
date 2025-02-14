import random
import string
import time
import socket
from rich.console import Console
from rich.panel import Panel

console = Console()

def buatverifcode():
    return ''.join(random.choices(string.digits, k=6))

def buatApikey():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=32))

def register_user():
    console.print(Panel("[bold green]API KEY TO DDOS BY DIZ FLYZE[/bold green]", expand=True))

    email = console.input(f"[bold cyan]EMAIL : ")
    password = console.input(f"[bold cyan]PASSWORD : ")

    verification_code = buatverifcode()
    verification_file_path = "/sdcard/Download/apikeycode.txt"

    try:
        with open(verification_file_path, "w") as f:
            f.write(verification_code)
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
        return
    
    console.print("[bold yellow]Code verifikasi di kirim ke /sdcard/download[/bold yellow]")
    user_code = input("CODE : ")

    if user_code == verification_code:
        api_key = buatApikey()
        expiration_date = time.strftime("%Y-%m-%d", time.gmtime(time.time() + 60*60*24*30))
        creation_date = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        
        panel_content = f"""
[bold cyan]YOUR APIKEY:[/bold cyan] {api_key}
[bold cyan]YOUR RUN SC:[/bold cyan] DIZ FLYZE
[bold cyan]KADALUARSA:[/bold cyan] {expiration_date}
[bold cyan]DI BUAT PADA:[/bold cyan] {creation_date}
"""
        console.print(Panel(panel_content, style="bold green", expand=True))
        
        save_api_key(api_key, email, expiration_date, creation_date)
    else:
        console.print("[bold red]CODE SALAH MOHON MASUKAN DENGAN BENAR[/bold red]")

def save_api_key(api_key, email, expiration_date, creation_date):
    with open("/sdcard/Download/apikeys.json", "a") as file:
        file.write(f"{api_key} | {email} | {expiration_date} | {creation_date}\n")

if __name__ == "__main__":
    register_user()
