
# Developing BY Emir Güner github: github.com/heqmat
# Modules
import time
import requests
import urllib3
import os
import sys
import urllib.request
from datetime import datetime
import signal
import threading


# Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    PURPLE = '\033[90m'
    CYAN = '\033[0;36;47m'
    RED   = "\033[1;31m"  
    CYAN  = '\033[1;36m'
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD    = "\033[;1m"
    REVERSE = "\033[;7m"

# Tool Version
version = 0.1

time1 = datetime.now().strftime('%H:%M:%S')

# parameters
def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', type=str, required=True, help='Target Web Domain.(Example: google.com,facebook.com,twitter.com,udemy.com)')
    parser.add_argument('-o', '--output', type=str, required=False, help='Save output as file.')
    return parser.parse_args()




#Check internet connection
def connecct(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

if connecct():                
    print("") # have internet connection.
else:
    print(bcolors.OKGREEN + f"""
     ▄▄▄▄▄   ▄   ███   █▄▄▄▄ ▄███▄   ██   █  █▀ ▄███▄   █▄▄▄▄ 
      █     ▀▄  █  █  █  █  ▄▀ █▀   ▀  █ █  █▄█   █▀   ▀  █  ▄▀ 
    ▄  ▀▀▀▀▄ █   █ █ ▀ ▄ █▀▀▌  ██▄▄    █▄▄█ █▀▄   ██▄▄    █▀▀▌  
     ▀▄▄▄▄▀  █   █ █  ▄▀ █  █  █▄   ▄▀ █  █ █  █  █▄   ▄▀ █  █  
             █▄ ▄█ ███     █   ▀███▀      █   █   ▀███▀     █   
              ▀▀▀         ▀              █   ▀             ▀    
                                        ▀                       
             Subdomain Scanner  - By: @heqmat - Emir Güner                     
                        Version: {version} 
    ============================================================
    Usage of Subreaker for attacking targets without prior mutual consent is illegal. 
    It is the end user's responsibility to obey all applicable local, state and federal laws. 
    Developers assume no liability and are not responsible for any misuse or damage caused by this program.
	
    """ + bcolors.ENDC)	
    print("[" + bcolors.FAIL + "ERROR" + bcolors.ENDC + "] " + "You do not have an internet connection or not enough.") # dont have internet connection
    print("[" + bcolors.FAIL + "ERROR" + bcolors.ENDC + "] " + "You do not have an internet connection or not enough.") # dont have internet connection
    print("[" + bcolors.FAIL + "ERROR" + bcolors.ENDC + "] " + "You do not have an internet connection or not enough.") # dont have internet connection
    print("Press CTRL + C to exit")
    time.sleep(3600)		
# Banner - Welcome page
def banner():
    global version
    print(bcolors.OKGREEN + f"""
     ▄▄▄▄▄   ▄   ███   █▄▄▄▄ ▄███▄   ██   █  █▀ ▄███▄   █▄▄▄▄ 
      █     ▀▄  █  █  █  █  ▄▀ █▀   ▀  █ █  █▄█   █▀   ▀  █  ▄▀ 
    ▄  ▀▀▀▀▄ █   █ █ ▀ ▄ █▀▀▌  ██▄▄    █▄▄█ █▀▄   ██▄▄    █▀▀▌  
     ▀▄▄▄▄▀  █   █ █  ▄▀ █  █  █▄   ▄▀ █  █ █  █  █▄   ▄▀ █  █  
             █▄ ▄█ ███     █   ▀███▀      █   █   ▀███▀     █   
              ▀▀▀         ▀              █   ▀             ▀    
                                        ▀                       
             Subdomain Scanner  - By: @heqmat - Emir Güner                     
                        Version: {version} 
    ============================================================
    Usage of Subreaker for attacking targets without prior mutual consent is illegal. 
    It is the end user's responsibility to obey all applicable local, state and federal laws. 
    Developers assume no liability and are not responsible for any misuse or damage caused by this program.
	
    """ + bcolors.ENDC)
    print(bcolors.PURPLE + "This process may take a few minutes" + bcolors.ENDC)	
    time.sleep(1)




def parse_url(url):
    try:
        host = urllib3.util.url.parse_url(url).host
    except Exception as e:
        print(bcolors.OKGREEN + f"""
         ▄▄▄▄▄   ▄   ███   █▄▄▄▄ ▄███▄   ██   █  █▀ ▄███▄   █▄▄▄▄ 
          █     ▀▄  █  █  █  █  ▄▀ █▀   ▀  █ █  █▄█   █▀   ▀  █  ▄▀ 
        ▄  ▀▀▀▀▄ █   █ █ ▀ ▄ █▀▀▌  ██▄▄    █▄▄█ █▀▄   ██▄▄    █▀▀▌  
         ▀▄▄▄▄▀  █   █ █  ▄▀ █  █  █▄   ▄▀ █  █ █  █  █▄   ▄▀ █  █  
                 █▄ ▄█ ███     █   ▀███▀      █   █   ▀███▀     █   
                  ▀▀▀         ▀              █   ▀             ▀    
                                            ▀                       
                 Subdomain Scanner  - By: @heqmat - Emir Güner                     
                            Version: {version} 
        ============================================================
        Usage of Forgery Tool for attacking targets without prior mutual consent is illegal. 
        It is the end user's responsibility to obey all applicable local, state and federal laws. 
        Developers assume no liability and are not responsible for any misuse or damage caused by this program.
                        
        """ + bcolors.ENDC)
        print("[" + bcolors.FAIL + "ERROR" + bcolors.ENDC + "]" + " Invalid domain address please try again.")
        sys.exit(1)
    return host

def write_subs_to_file(subdomain, output_file):
    with open(output_file, 'a') as fp:
        fp.write(subdomain + '\n')
        fp.close()


def main():
    banner()
    subdomains = []

    args = parse_args()
    target = parse_url(args.domain)
    output = args.output

    req = requests.get(f'https://crt.sh/?q=%.{target}&output=json')

    if req.status_code != 200:

        print("[" + bcolors.FAIL + "ERROR" + bcolors.ENDC + "] " + "System not working try again please (Code: code != 200 )")
        sys.exit(1)

    for (key,value) in enumerate(req.json()):
        subdomains.append(value['name_value'])

    print("[" + bcolors.OKBLUE + "INFO" + bcolors.ENDC + "] " + f"Subreaker's Target: {target} ")


    subs = sorted(set(subdomains))

    for s in subs:
        print("[" + bcolors.OKGREEN + "SUBDOMAIN" + bcolors.ENDC + f"] {s} " + bcolors.OKBLUE + "Subdomain was found." + bcolors.ENDC)
        if output is not None:
            write_subs_to_file(s, output)

    print("[" + bcolors.PURPLE + "FINISH" + bcolors.ENDC + "] " + "Process is complete, all subdomains have been found.")
    print(bcolors.PURPLE + f"The program was stopped at {time1}, if this is a error or not normal please let me know" + bcolors.ENDC)
    
	
if __name__=='__main__':
    main()









