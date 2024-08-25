import requests
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

def is_proxy_working(proxy):
    try:
        response = requests.get('http://httpbin.org/ip', proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            return True
    except requests.RequestException:
        return False
    return False

def check_proxies_from_file(filename):
    try:
        with open(filename, 'r') as file:
            proxies = file.readlines()
        for proxy in proxies:
            proxy = proxy.strip()
            if is_proxy_working(proxy):
                print(Fore.GREEN + f"{proxy} berfungsi")
            else:
                print(Fore.RED + f"{proxy} tidak berfungsi")
    except FileNotFoundError:
        print(f"File {filename} not found.")

# Form input
filename = input("Masukkan nama file proxy yang ingin diperiksa: ")
check_proxies_from_file(filename)
