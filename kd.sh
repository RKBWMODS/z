#!/bin/bash

clear
echo "========================================"
echo "          SQL Injection Scanner        "
echo "========================================"
echo ""
read -p "MASUKKAN LINK WEB: " target

echo "[*] Memulai scanning SQL Injection..."
sleep 2

sqlmap -u "$target" --dbs --batch

echo "[*] Scanning selesai."
