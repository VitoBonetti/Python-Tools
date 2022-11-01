
import subprocess
import argparse
from colorama import Fore
import re

# setting up text style
ITALIC = "\x1B[3m"
NORMAL = "\x1B[0m"
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
BLUE = Fore.BLUE
BLUE_LIGHT = Fore.LIGHTBLUE_EX
RESET = Fore.RESET

def get_flags():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", type=str, help="help", dest="interface", required=True)
    parser.add_argument("-m", "--mac", dest="new_mac", help="help", type=str, required=True)
    flags = parser.parse_args()
    if not flags.interface:
        parser.error(f"{YELLOW}[-] Please specify an interface using the flag -i or --interface, "
                     f"use -h or --help for more info")
    elif not flags.new_mac:
        parser.error(f"{YELLOW}[-] Please specify an new MAC address using the flag -m or --mac, "
                     f"use -h or --help for more info")
    return flags

def mac_changer(interface, new_mac):
    print(f"[*] Changing the MAC address fot the interface {interface} into {new_mac}...")
    subprocess.call(["ifconfig", interface, "down"], shell=True)
    subprocess.call(["ifconfig", interface, "hw" "either", new_mac], shell=True)
    subprocess.call(["ifconfig", interface, "up"], shell=True)

def get_current_mac(interface):
    ifconfig_check = subprocess.check_output(["ifconfig", interface])
    mac_from_ifconfig_check = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_check))
    if mac_from_ifconfig_check:
        return mac_from_ifconfig_check.group(0)
    else:
        print(f"{YELLOW}[-] Sorry could not read the MAC Address for interface{RESET}{BLUE}{interface}{RESET}")

flags = get_flags()
current_mac = get_current_mac(flags.interface)
if current_mac is None:
    print(f"{YELLOW}[-] No MAC Address.")
else:
    print(f"[*] Current MAC Address is {BLUE}{current_mac}{RESET}")
mac_changer(flags.interface, flags.new_mac)
current_mac = get_current_mac(flags.interface)
if current_mac == flags.new_mac:
    print(f"[+] MAC Address Successfully changed to {BLUE}{flags.new_mac}{RESET}")
else:
    print(f"{YELLOW}[-] We Could not change the MAC address. Please try again!{RESET}")

