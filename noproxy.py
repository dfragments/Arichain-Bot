import json
import time
import random
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

def first_request(email):
    url = "https://arichain.io/api/wallet/get_list_mobile"
    data = {
        "blockchain": "testnet",
        "email": email,
        "lang": "en",
        "device": "app",
        "is_mobile": "Y"
    }
    try:
        response = requests.post(url, headers=headers, data=data)
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

def second_request(address):
    url = "https://arichain.io/api/event/get_checkin"
    data = {
        "blockchain": "testnet",
        "address": address,
        "lang": "en",
        "device": "app",
        "is_mobile": "Y"
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            print_timestamped("Check-in data retrieved successfully", Fore.GREEN)
        else:
            print_timestamped("Failed to retrieve check-in data", Fore.RED)
    except Exception as e:
        print_timestamped(f"Request failed: {e}", Fore.RED)

def checkin_request(address):
    url = "https://arichain.io/api/event/checkin"
    data = {
        "blockchain": "testnet",
        "address": address,
        "lang": "en",
        "device": "app",
        "is_mobile": "Y"
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        if "Already Checked in" in response.text:
            print_timestamped("You already checked in Today", Fore.YELLOW)
        else:
            print_timestamped("Check-in Successful", Fore.GREEN)
    except Exception as e:
        print_timestamped(f"Request failed: {e}", Fore.RED)

def third_request(address):
    url = "https://arichain.io/api/event/quiz_q"
    data = {
        "blockchain": "testnet",
        "address": address,
        "lang": "en",
        "device": "app",
        "is_mobile": "Y"
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            response_data = response.json()
            if response_data.get("status") == "success":
                quiz_idx = response_data["result"]["quiz_idx"]
                q_idx = response_data["result"]["quiz_q"][0]["q_idx"]
                print_timestamped(f"Quiz ID: {quiz_idx}, Question ID: {q_idx}", Fore.BLUE)
                return quiz_idx, q_idx
            else:
                print_timestamped("Failed to retrieve quiz question", Fore.RED)
    except Exception as e:
        print_timestamped(f"Request failed: {e}", Fore.RED)
    return None, None

def fourth_request(address, quiz_idx, answer_idx):
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
        response = requests.post(url, headers=headers, data=data)
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

while True:
    for user in users:
        print_timestamped(f"Processing user: {user['name']}", Fore.YELLOW)
        
        if first_request(user['email']):
            time.sleep(3)
            print_timestamped("Sleeping for 3 seconds...", Fore.LIGHTBLACK_EX)
            second_request(user['wallet_address'])
            time.sleep(2)
            print_timestamped("Sleeping for 2 seconds...", Fore.LIGHTBLACK_EX)
            checkin_request(user['wallet_address'])
            time.sleep(5)
            print_timestamped("Sleeping for 5 seconds...", Fore.LIGHTBLACK_EX)
            quiz_idx, q_idx = third_request(user['wallet_address'])
            if quiz_idx and q_idx:
                fourth_request(user['wallet_address'], quiz_idx, q_idx)
        print("\n")
    
    sleep_duration = random.randint(25 * 3600, 26 * 3600)
    print_timestamped("All accounts processed", Fore.LIGHTBLACK_EX)
    print_timestamped(Fore.GREEN + f"Sleeping for {sleep_duration // 3600} hours..." + Style.RESET_ALL)
    time.sleep(sleep_duration)
