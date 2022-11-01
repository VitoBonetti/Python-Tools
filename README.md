# Wordlist_Generator
Creates a wordlist from a text file. Ability to choose min and max size of words to include in wordlist and the ability to set only words written in lower case.

Usage:

```
python3 wordlist_gen.py -s <file_path> [--min] [--max] [-l] [-o]
python3 wordlist_gen.py -s example.txt
python3 wordlist_gen.py -s example.txt 8 12 T output.txt
```

# MAC_Changer
Change the mac address of a select interface.

Usage:
```
python3 mac_change.py -i <interface> -m <mac_address>
python3 mac_change.py -i wlan0 -m 00:11:22:33:44:55
```

