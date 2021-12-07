#!/usr/bin/env python
# -*- coding:utf-8 -*- 

# Tool created by justgr0w(David León) - TI & SEC

# Pyfuzzer testing is an automated software testing technique that involves providing invalid, unexpected, or random data as input to a computer program.

import argparse
import requests
import os
import re
import time
import sys
from modules.colors import colors as c
from urllib.parse import urlparse

wordlists ={"dict":"db/discover_file_paths/predictable/dicc.txt",
		"wp":"db/discover_file_paths/predictable/CMS/wordpress.txt",
		"dp":"db/discover_file_paths/predictable/CMS/drupal_plugins.txt",
		"jm":"db/discover_file_paths/predictable/CMS/joomla_plugins.txt",
		"php":"db/discover_file_paths/predictable/php/PHP.txt"
}

def banner():
    print(c.RED)
    os.system("figlet PyFuzzer")
    print(c.RESET)

def main():
    
    pars = argparse.ArgumentParser(description="PyFuzzer, discover hidden files or directories")
    
    pars.add_argument("-u", "--url"
    , metavar="Target URL"
    , dest='url'
    , action="store"
    , type=str
    , help='Here goes the URL of the objective'
    , default=None)
    
    pars.add_argument("-c"
    , metavar="CMS"
    , dest='cms'
    , action="store"
    , type=str
    , help='scan CMS that are by default'
    , default=False)
    
    pars.add_argument('-w'
    , metavar="WordList"
    , dest="wordlist"
    , action="store"
    , type=str
    , help="Custom wordlist"
    , default=None)

    pars.add_argument("-f","--filter"
    , metavar="Filter"
    , dest="filter"
    , action="store"
    , type=str
    , choices=["hc", "sc"]
    , help="Filter the output, hc: Hide code; sc: Show code only"
    , default=None)

    pars.add_argument("-v", "--values"
    , dest="val"
    , metavar="Values"
    , type=int
    , nargs="*"
    , help="Values for the --filter parameter"
    , default=None)
    
    args = pars.parse_args()
    
    if args.url:
        verify_url = urlparse(args.url)
        
        if verify_url[0] not in ['http', 'https']:
            banner()
            print (c.RED+"[!] Please checkout your URL http:// or https://"+c.RESET)
            sys.exit(0)

    if not args.url:
        banner()
        print(f"{c.RED}[!] Enter the URL objetive --url=\"{c.YELLOW}Target{c.RESET}{c.RED}\"{c.RESET}")
        print(c.GREEN+"Usage: python PyFuzzer.py -h"+c.RESET)
        sys.exit(0)
    
    if args.cms:
        banner()
        if args.cms not in ["wp","dp","jm", "php"]:
            print (c.RED+"[!] Please chose the cms name {dict, wp, dp...}"+c.RESET)
            sys.exit(0)
	
    if args.wordlist:
        if not os.path.isfile(str(args.wordlist)):
            banner()
            print (c.RED+"[!] Please checkout your Custom wordlist path"+c.RESET)
            print(f"Example: python Pyfuzzer.py --url={c.YELLOW}Target{c.RESET} -w {c.GREEN}C:/dictionaries/rockyou.txt{c.RESET}")
            sys.exit(0)

    if args.filter:
        if not args.val:
            banner()
            print(f"{c.RED}Error, the parameter -f needs the parameter -v{c.RESET}\nExample: {c.YELLOW}./Pyfuzzer.py -u [TARGET] --filter=hc -v 404 505")
            sys.exit(1)

    if not args.filter:
        if args.val:
            banner()
            print(f"{c.RED}Error, the parameter -v needs the parameter --filter{c.RESET}\nExample: {c.YELLOW}./Pyfuzzer.py -u [TARGET] --filter=hc -v 404 505")
            sys.exit(1)

    init_Fuzz(args.url,args.cms,args.wordlist, args.filter, args.val)

def startinit_Fuzz(url):
    print("".center(50, "-"))
    print(c.RED+"PyFuzzer 0.1 by justgr0w".center(50, " ")+c.RESET)
    print("".center(50, "-"))
    print(f"{c.YELLOW}  Target: {url}  {c.RESET}".center(35, "_"))
    print("".center(50, "*"))
    print("    Response        Time                Payload")
    print("".center(50, "*"))

def color_code(code, paths):
    if code == 200:
        print("[+] C={GREEN}{code}{RESET}            {time}             \"{paths}\"".format(time=time.strftime("%H:%M:%S"),code=code,paths=paths, GREEN=c.GREEN, RESET=c.RESET))      
           
    elif code == 301:
        print("[+] C={BLUE}{code}{RESET}            {time}             \"{paths}\"".format(time=time.strftime("%H:%M:%S"),code=code,paths=paths, BLUE=c.BLUE, RESET=c.RESET))
    
    elif code == 404:
        print("[+] C={RED}{code}{RESET}            {time}             \"{paths}\"".format(time=time.strftime("%H:%M:%S"),code=code,paths=paths, RED=c.RED, RESET=c.RESET))
            
    else:
        print("[+] {RESET}C={code}{RESET}            \"{time}\"        \"{paths}\"".format(time=time.strftime("%H:%M:%S"),code=code,paths=paths, RESET=c.RESET))

def Fuzz1(code, paths):
    color_code(code, paths)

def Fuzz2(code, paths, val):
    # Hide Code
    if code not in val:
        color_code(code, paths)

def Fuzz3(code, paths, val):
    # Show Code
    if code in val:
        color_code(code, paths)

def init_Fuzz(url, cms_type, custom_wordlist, filter, val):
    
    if cms_type:
        words = [w.strip() for w in open(wordlists[cms_type], "rb").readlines()] #parse wordlist
    
    elif custom_wordlist:
        words = [w.strip() for w in open(str(custom_wordlist), "rb").readlines()]
    
    else:
        words = [w.strip() for w in open(wordlists["dict"], "rb").readlines()] #parse wordlist
    
    try:
        filter = str(filter)
        startinit_Fuzz(url)
        for paths in words:
            paths2 = paths
            paths2 = paths2.decode("UTF-8")
            paths = paths.decode("UTF-8")
            
            if "/" not in paths[0]:
                paths = "/"+paths

            if "/" not in paths[-1:]:
                paths = paths+"/"
            
            fullPath = url+paths
            r = requests.get(fullPath)
            code = int(r.status_code)
            
            if filter.upper() == "HC":
                # Hide Code
                Fuzz2(code, paths2, val)

            elif filter.upper() == "SC":
                # Show Code
                Fuzz3(code, paths2, val)

            else:
                Fuzz1(code, paths2)
            
    except Exception as e:
        print(f"Hubo un error, {e}")
        sys.exit(1)
  
if __name__ == "__main__":
    try:
        main() 
    except KeyboardInterrupt as e:
        print("\n[!]...")
        sys.exit(0)