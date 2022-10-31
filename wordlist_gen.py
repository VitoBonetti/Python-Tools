
import os
import re
import argparse
from colorama import Fore

# setting up text style
ITALIC = "\x1B[3m"
NORMAL = "\x1B[0m"
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
BLUE = Fore.BLUE
BLUE_LIGHT = Fore.LIGHTBLUE_EX
RESET = Fore.RESET
ERROR = f"{BLUE}{ITALIC}The following arguments are required: -s or --source.{RESET}{NORMAL}"
USAGE = f"{YELLOW}\n{ITALIC}%(prog)s -s <file_path> [--min] [--max] [-l] [-o]\n%(prog)s -s example.txt\n%(prog)s -s " \
        f"example.txt 8 12 T output.txt\nFor more information: \n%(prog)s -h or %(prog)s --help.{RESET}{NORMAL}\n\n"
BANNER = """ 
  _    _               _ _ _     _              
| |  | |             | | (_)   | |             
| |  | | ___  _ __ __| | |_ ___| |_            
| |/\| |/ _ \| '__/ _` | | / __| __|           
\  /\  / (_) | | | (_| | | \__ \ |_            
 \/  \/ \___/|_|  \__,_|_|_|___/\__|           
                                               
                                               
 _____                           _             
|  __ \                         | |            
| |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |_\ \  __/ | | |  __/ | | (_| | || (_) | |   
 \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|                                                                                                                                                                                                                                                                     
"""
print(BLUE_LIGHT + BANNER + RESET + "\n")

# overwrite the error function of argparse
class ArgumentParser(argparse.ArgumentParser):
    def error(self, status=2, message=ERROR):
        return super(ArgumentParser, self).error(message)

# define the flags
parser = ArgumentParser(prog="wordlist_gen.py", usage=USAGE)
parser.add_argument("-s", "--source", type=str, required=True, help="REQUIRED - The file from which to extract the passwords for the wordlist.")
parser.add_argument('--min', "--minlength", default=6, type=int, help="The minimum length for the word to extract. Default is 6.")
parser.add_argument('--max', "--maxlength", default=24, type=int, help="The maximum length for the word to extract. Default is 24.")
parser.add_argument("-l", "--lowercase", type=bool, default=False, help="Only lowercase word. True(T) or False(F). Default is False(F).")
parser.add_argument("-o", "--output", type=str, default="wg.txt", help="Output file where to save the wordlist. Default wg.txt.")

flags = parser.parse_args()

with open(flags.source, 'r') as f:
    words_file = f.read()

regexpr = re.findall(r'\w+', words_file)
types = set(regexpr)
min_length = int(flags.min)
max_length = int(flags.max)
lowcase = flags.lowercase

if lowcase:
    words = [word for word in types if len(word) >= min_length and len(word) <= max_length and word.islower()]
else:
    words = [word for word in types if len(word) >= min_length and len(word) <= max_length]

with open(flags.output, "w") as myfile:
    for w in words:
        myfile.write(w)
        myfile.write("\n")

with open(flags.output, "r") as myfile:
    for count, line in enumerate(myfile):
        total_word = count+1

file_size = os.stat(flags.output).st_size
print(f"\n{GREEN}FINAL RESULT:{RESET}")
print(f"{BLUE_LIGHT}Name File:{RESET} {ITALIC}{flags.output}{NORMAL}")
print(f"{BLUE_LIGHT}Size File:{RESET} {ITALIC}{file_size}{NORMAL} bytes")
print(f"{BLUE_LIGHT}Words:{RESET} {ITALIC}{total_word}{NORMAL}\n")



