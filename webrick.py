import argparse
import requests
from colorama import Fore,Back

def webrick_logo():
    print(Fore.RED+"""

		███████▀▀▀░░░░░░░▀▀▀███████
		████▀░░░░░░░░░░░░░░░░░▀████
		███│░░░░░░░░░░░░░░░░░░░│███
		██▌│░░░░░░░░░░░░░░░░░░░│▐██
		██░└┐░░░░░░░░░░░░░░░░░┌┘░██
		██░░└┐░░░░░░░░░░░░░░░┌┘░░██
		██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
		██▌░│██████▌░░░▐██████│░▐██
		███░│▐███▀▀░░▄░░▀▀███▌│░███
		██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
		██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
		████▄─┘██▌░░░░░░░▐██└─▄████
		█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
		████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
		█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
		███████▄░░░░░░░░░░░▄███████
		██████████▄▄▄▄▄▄▄██████████
				                                			        								
  This tool only for education purpose
  Developer of this tool is not responsile . If any one harm 
  _____________________________________________________________________________________________________________________________________________________________________
    """)

webrick_logo()

def main(url_file_path):
    with open(url_file_path, 'r') as file:
        for line in file:
            url = line.strip()
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(Fore.BLUE+f"[+]{url}	--------->{response.status_code}")
                else:
                    print(Fore.YELLOW+f"[+]{url}	--------->{response.status_code}")
            except requests.exceptions.RequestException as e:
                print(Fore.RED+f"An error occurred while accessing {url}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send HTTP requests to URLs from a file')
    parser.add_argument('url_file', help='Path to the file containing URLs')

    args = parser.parse_args()
    main(args.url_file)
