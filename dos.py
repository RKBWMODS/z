import threading
import time
import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from DDos import checkUrl, DDos

console = Console()

def clear_console():
    os.system('clear')  # Untuk Linux/Mac
    # os.system('cls')  # Untuk Windows

def draw_ring_with_text():
    clear_console()

    ring = """
█████████████████
██                   ██
██                       ██
██                           ██
██                               ██

██████╗  ██╗ ███████╗  █████╗   █████╗   █████╗
██╔══██╗ ██║ ╚══███╔╝ ██╔══██╗ ██╔══██╗ ██╔══██╗
██║  ██║ ██║   ███╔╝  ╚██████║ ╚██████║ ╚██████║
██║  ██║ ██║  ███╔╝    ╚═══██║  ╚═══██║  ╚═══██║
██████╔╝ ██║ ███████╗  █████╔╝  █████╔╝  █████╔╝
╚═════╝  ╚═╝ ╚══════╝  ╚════╝   ╚════╝   ╚════╝

██                               ██
██                           ██
██                       ██
██                   ██
█████████████████
"""
    # Menampilkan Ring dengan Teks
    console.print(Text(ring, style="bold cyan"), justify="center")
    time.sleep(1)  # Delay untuk memberikan efek visual
    console.print("\n")

def display_intro_message():
    
    os.system("xdg-open https://youtube.com/@dizflyze999")

def display_header():
    
    console.print(Panel("[bold cyan]───────────────| THE KING DDOS ATTACK SCRIPT |───────────────[/bold cyan]", style="bold green", width=console.width))
    console.print(Panel("[bold cyan]PEMBUAT : DIZ FLYZE\nYOUTUBE : DIZFLYZE999\nVERSION : v999 KING[/bold cyan]", style="bold yellow", width=console.width))

def display_input_prompt():
    
    console.print("[bold cyan]╭─────| ATTACK URL |")
    url = input("╰─> | ")
    
    console.print("[bold cyan]╭─────| ATTACK IP |")
    ip = input("╰─> | ")

    console.print("[bold cyan]╭─────| ATTACK PORT |")
    port = input("╰─> | ")

    if checkUrl(url):
        return url
    elif checkUrl(ip):
        return ip
    elif checkUrl(port):
        return port
    else:
        print("TIDAK MENEMUKAN URL YANG ANDA MAKSUD")
        return None

# Fungsi untuk menampilkan teks dinamis dalam panel
def display_attack_status():
    count = 1
    while True:
        panel = Panel(f"[bold red]● [bold yellow]● [bold green]● [bold green]────────────| 🥶 DIZ ATTACK : {count} 🥶 |────────────[/bold green] [bold green]● [bold yellow]● [bold red]●", style="bold yellow", width=console.width)
        console.print(panel, justify="center")
        time.sleep(5)  # Delay agar tidak terlalu cepat
        count += 1

# Fungsi untuk menjalankan serangan DDoS
def run_ddos(target):
    DDos(target)  # Ganti dengan kode serangan asli

# Program utama
def main():
    draw_ring_with_text()
    display_intro_message()
    display_header()
    
    target = None
    while target is None:
        target = display_input_prompt()

    # Menjalankan tampilan teks di thread terpisah
    status_thread = threading.Thread(target=display_attack_status)
    status_thread.daemon = True  # Agar thread ini berhenti saat program utama selesai
    status_thread.start()

    # Menjalankan serangan DDoS
    run_ddos(target)

if __name__ == "__main__":
    main()
