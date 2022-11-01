import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--interface", type=str, help="help", dest="interface", required=True)
parser.add_argument("-m", "--mac", dest="new_mac", help="help", type=str, required=True)

options = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print(f"[*] Changing the MAC address fot the interface {interface} into {new_mac}...")

subprocess.call(["ifconfig", interface, "down"], shell=True)
subprocess.call(["ifconfig", interface, "hw" "either", new_mac], shell=True)
subprocess.call(["ifconfig", interface, "up"], shell=True)
