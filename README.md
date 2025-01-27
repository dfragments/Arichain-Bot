# AriChain Automation Script 📜🤖

Welcome to the AriChain Automation Script! This script is designed to automate various tasks on the AriChain platform, such as logging in, checking in, and answering quiz questions. It supports multiple users and can optionally use proxies for each user.

![App Screenshot](https://raw.githubusercontent.com/MrTimonM/Arichain-Bot/refs/heads/main/arichain.png)

Make sure to star ⭐️ this repo for new scripts :D 



---


## Features ✨

- **Multi-User Support**: Handle multiple users with ease. Each user's details are stored in a `users.json` file.
- **Proxy Support**: Optionally use proxies for each user to mask your IP address.
- **Automated Tasks**:
  - **Login**: Authenticate users and fetch their wallet balance.
  - **Check-in**: Perform daily check-ins.
  - **Quiz**: Retrieve and answer quiz questions.
- **Logging**: Detailed logging with timestamps and color-coded messages for easy debugging.

---

## 📝 Sign Up Guide  

Follow these steps to get started with the **AriChain Wallet Testnet** and earn rewards!  

### 🔄 **AriChain Wallet Testnet Reward Confirmed**  
- 📱 **Details**: [AriChain Wallet Announcement on Twitter](https://x.com/Arichain_/status/1878031797289992374)  

### 📥 **Download the ARI Wallet**  
- **For iOS**: [Download from App Store](https://apps.apple.com/id/app/ari-wallet/id6504207160)  
- **For Android**: [Download from Google Play](https://play.google.com/store/apps/details?id=arichain.app.ari.wallet)  

### ➡️ **Steps to Sign Up**  
 1. Open the **ARI Wallet** app.  
 2. Click on the **"Testnet"** option.  
 3. Sign up and verify your email address.  
 4. Enter the referral code **`678e3530a7072`** to receive **+50 ARI** rewards! 🎉  

## Prerequisites 🛠️

Before you begin, ensure you have the following installed:

- **Python 3.10+**
- Required libraries: `requests` and `colorama`.

You can install the required libraries using pip:

```bash
pip install requests colorama
```
# Setup 🚀
- **Clone the Repository:**
```bash
git clone https://github.com/MrTimonM/Arichain-Bot
cd Arichain-Bot
```
# Prepare users.json:
Create a **users.json** file in the root directory with the following structure:
```bash
[
    {
        "name": "User1",
        "email": "user1@example.com",
        "wallet_address": "Arichain wallet address",
        "proxy": "http://user:pass@ip:port"
    },
    {
        "name": "User2",
        "email": "user2@example.com",
        "wallet_address": "Arichain wallet address"
    }
]
```
simply don't use proxy if you don't want to use proxy. 
# Run the Script:
**Execute the script using Python:**
```bash
python main.py

```
The script will prompt you to confirm before starting. Type **yes** to proceed.




# Contributing 🤝
Contributions are welcome! Please fork the repository and submit a pull request.


# License 📄
This project is licensed under the MIT License.
