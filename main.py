import json
import time
import requests
from colorama import Fore, Style, init
from datetime import datetime

init(autoreset=True)

with open('users.json', 'r') as file:
    users = json.load(file)

headers = {
    "accept": "application/json",
    "accept-encoding": "gzip",
    "content-type": "application/x-www-form-urlencoded; charset=utf-8",
    "host": "arichain.io",
    "user-agent": "Dart/3.3 (dart:io)"
}

def print_timestamped(message, color=Fore.WHITE):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{Fore.LIGHTBLACK_EX}[{timestamp}]{Style.RESET_ALL} {color}{message}")

def fetch_proxy_info(proxy):
    try:
        response = requests.get("https://ipinfo.io", proxies={"http": proxy, "https": proxy})
        if response.status_code == 200:
            data = response.json()
            ip = data.get("ip", "Unknown")
            city = data.get("city", "Unknown")
            country = data.get("country", "Unknown")
            return ip, city, country
        else:
            return None, None, None
    except Exception as e:
        print_timestamped(f"Failed to fetch proxy info: {e}", Fore.RED)
        return None, None, None

def first_request(email, proxy=None):
    url = "https://arichain.io/api/wallet/get_list_mobile"
    data = {
        "blockchain": "testnet",
        "email": email,
        "lang": "en",
        "device": "app",
        "is_mobile": "Y"
    }
    try:
        response = requests.post(url, headers=headers, data=data, proxies={"http": proxy, "https": proxy} if proxy else None)
        if response.status_code == 200:
            response_data = response.json()
            if response_data.get("status") == "success":
                print_timestamped("Login Success", Fore.GREEN)
                balance = response_data["result"][0]["balance"]
                print_timestamped(f"Balance: {balance}", Fore.CYAN)
                return True
            else:
                print_timestamped("Login Failed", Fore.RED)
        else:
            print_timestamped(f"Request failed with status code: {response.status_code}", Fore.RED)
    except Exception as e:
        print_timestamped(f"Request failed: {e}", Fore.RED)
    return False

def second_request(address, proxy=None):
    url = "https://arichain.io/api/event/get_checkin"
    data = {
        "blockchain": "testnet",
        "address": address,
        "lang": "en",
        "device": "app",
        "is_mobile": "Y"
    }
    try:
        response = requests.post(url, headers=headers, data=data, proxies={"http": proxy, "https": proxy} if proxy else None)
        if response.status_code == 200:
            response_data = response.json()
            if response_data.get("status") == "success":
                print_timestamped("Check-in data retrieved successfully", Fore.GREEN)
            else:
                print_timestamped("Failed to retrieve check-in data", Fore.RED)
        else:
            print_timestamped(f"Request failed with status code: {response.status_code}", Fore.RED)
    except Exception as e:
        print_timestamped(f"Request failed: {e}", Fore.RED)

def checkin_request(address, proxy=None):
    url = "https://arichain.io/api/event/checkin"
    data = {
        "blockchain": "testnet",
        "address": address,
        "lang": "en",
        "device": "app",
        "is_mobile": "Y"
    }
    try:
        response = requests.post(url, headers=headers, data=data, proxies={"http": proxy, "https": proxy} if proxy else None)
        if response.status_code == 200:
            response_data = response.json()
            if "Already Checked in" in response.text:
                print_timestamped("You already checked in Today", Fore.YELLOW)
            else:
                print_timestamped("Check-in Successful", Fore.GREEN)
        else:
            print_timestamped(f"idk bruh what happened: {response.status_code}", Fore.RED)
    except Exception as e:
        print_timestamped(f"Request failed: {e}", Fore.RED)

def third_request(address, proxy=None):
    url = "https://arichain.io/api/event/quiz_q"
    data = {
        "blockchain": "testnet",
        "address": address,
        "lang": "en",
        "device": "app",
        "is_mobile": "Y"
    }
    try:
        response = requests.post(url, headers=headers, data=data, proxies={"http": proxy, "https": proxy} if proxy else None)
        if response.status_code == 200:
            response_data = response.json()
            if response_data.get("status") == "success":
                quiz_idx = response_data["result"]["quiz_idx"]
                q_idx = response_data["result"]["quiz_q"][0]["q_idx"]
                print_timestamped(f"Quiz ID: {quiz_idx}, Question ID: {q_idx}", Fore.BLUE)
                return quiz_idx, q_idx
            else:
                print_timestamped("Failed to retrieve quiz question", Fore.RED)
        else:
            print_timestamped(f"Request failed with status code: {response.status_code}", Fore.RED)
    except Exception as e:
        print_timestamped(f"Request failed: {e}", Fore.RED)
    return None, None

def fourth_request(address, quiz_idx, answer_idx, proxy=None):
    url = "https://arichain.io/api/event/quiz_a"
    data = {
        "blockchain": "testnet",
        "address": address,
        "quiz_idx": quiz_idx,
        "answer_idx": answer_idx,
        "lang": "en",
        "device": "app",
        "is_mobile": "Y"
    }
    try:
        response = requests.post(url, headers=headers, data=data, proxies={"http": proxy, "https": proxy} if proxy else None)
        if "Already taken quiz" in response.text:
            print_timestamped("You already answered Quiz Today", Fore.YELLOW)
        else:
            print_timestamped("Quiz Answered Successfully", Fore.GREEN)
    except Exception as e:
        print_timestamped(f"Request failed: {e}", Fore.RED)

ascii_art = r"""
    _         _    ____ _           _       
   / \   _ __(_)  / ___| |__   __ _(_)_ __  
  / _ \ | '__| | | |   | '_ \ / _` | | '_ \ 
 / ___ \| |  | | | |___| | | | (_| | | | | |
/_/   \_\_|  |_|  \____|_| |_|\__,_|_|_| |_|
"""

print(ascii_art)
print(f"{Fore.GREEN}GitHub Profile: https://github.com/MrTimonM{Style.RESET_ALL}")

print(f"Accounts loaded: {len(users)}")
confirmation = input("Do you want to start the script? (yes/no): ").strip().lower()
if confirmation != "yes":
    exit()

for user in users:
    print_timestamped(f"Processing user: {user['name']}", Fore.YELLOW)
    
    proxy = user.get("proxy")
    if proxy:
        ip, city, country = fetch_proxy_info(proxy)
        if ip and city and country:
            print_timestamped(f"Proxy connected - IP: {ip}, City: {city}, Country: {country}", Fore.GREEN)
        else:
            print_timestamped("Failed to fetch proxy info", Fore.RED)
    else:
        print_timestamped("No proxy provided", Fore.LIGHTBLACK_EX)
    
    if first_request(user['email'], proxy):
        time.sleep(3)
        print_timestamped("Sleeping for 3 seconds...", Fore.LIGHTBLACK_EX)
        second_request(user['wallet_address'], proxy)
        time.sleep(2)
        print_timestamped("Sleeping for 2 seconds...", Fore.LIGHTBLACK_EX)
        checkin_request(user['wallet_address'], proxy)
        time.sleep(5)
        print_timestamped("Sleeping for 5 seconds...", Fore.LIGHTBLACK_EX)
        quiz_idx, q_idx = third_request(user['wallet_address'], proxy)
        if quiz_idx and q_idx:
            fourth_request(user['wallet_address'], quiz_idx, q_idx, proxy)
    print("\n")
