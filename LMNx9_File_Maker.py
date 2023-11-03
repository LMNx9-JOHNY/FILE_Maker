#____________________________#
#|    !/usr/bin/python3
#|   DARK-TEAM-LMNx9
#|  Author - LIMON HOSSAIN
#|   GitHub - LMNx9-JOHNY
#|    Facebook - LJ.LMNx9
#_____________________________#
import os,re,random,uuid,subprocess,sys
import requests 
from os import system
import time, json, string
os.system('rm -rf .a.txt')
#------(modules_install)------
try:
	import mechanize
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
except:
	os.system('pip install mechanize')
 

def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def back():
    main_menu()
#def linex():
	#print('----------------------------------------------')
def linex():
	print('\033[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def contact():
	os.system('xdg-open https://www.facebook.com/LJ.LMNx9')
	back()
G = "\u001b[32m"
B = "\u001b[36m"
W = "\033[1;37m"
pemisah = '|'
q="968"
qq="8280"
qqq="52729"
qqqq="420"
client_id = f"{qqqq}038{q}89{qq}485649{qqq}208"
sim_hini = str(random.randint(2e4,4e4))
trace_id = str(uuid.uuid4())
 
try:
	android = subprocess.check_output('getprop ro.product.brand', shell=True).decode('utf-8').replace('\n', '').upper()
	model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '').upper()
	carrier = '' + subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')[1].replace('\n', '').upper()
except:
	android = random.choice(['TECNO', "INFINIX", "SAMSUNG"])
	model = random.choice(['LD2', "SM-J009", "SM-J505", "HOT12", "NOTE-11", "A5-PRO"])
	carrier = '' + random.choice(['02', 'Oramge', 'EE', "At&", "MTN", "Cricket"])

#/-----logo-----/
#      \033[1;30m    ➤ Black
#      \033[1;31m    ➤ Red
#      \033[1;32m    ➤ Green
#      \033[1;33m    ➤ Yellow
#      \033[1;34m    ➤ Blue
#      \033[1;35m    ➤ Purple (pink)
#      \033[1;36m    ➤ Cyan (sky)
#      \033[1;37m    ➤ White
linex()
print(' \033[1;31m⌠\033[1;32m+\033[1;31m⌡ \033[1;32m𝗙𝗜𝗥𝗦𝗧 \033[1;31m➤ \033[1;36m𝗝𝗢𝗜𝗡 𝗠𝗬 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗚𝗥𝗢𝗨𝗣')
linex()
print(' \033[1;31m⌠\033[1;32m+\033[1;31m⌡ \033[1;33m𝗦𝗘𝗔𝗥𝗖𝗛𝗜𝗡𝗚 𝗟𝗜𝗡𝗞...')
linex()
time.sleep(5)
os.system('xdg-open https://t.me/+YTU768eCwN1mYzdl')
print(' \033[1;31m⌠\033[1;32m+\033[1;31m⌡ \033[1;35m𝗪𝗵𝗮𝘁𝘀 𝗬𝗼𝘂𝗿 𝗡𝗮𝗺𝗲 ?')
linex()
sh = input(" \033[1;31m⌠\033[1;32m+\033[1;31m⌡ \033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗬𝗢𝗨𝗥 𝗡𝗔𝗠𝗘 \033[1;31m➤\033[1;32m ")
logo = f"""
\033[1;31m┏\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;31m┓
\033[1;37m┃ \033[1;33m┏\033[1;33m━┓\033[1;31m➤     ▄▄▄▄▄▄▄ ▄▄ ▄▄     ▄▄▄▄▄▄▄           \033[1;37m   ┃
\033[1;37m┃ \033[1;33m┃\033[1;32m𝗗\033[1;33m┃\033[1;31m➤     ███████           ███████  \033[1;36m𝗙𝗜𝗟𝗘 𝗠𝗔𝗞𝗘𝗥  \033[1;37m┃
\033[1;37m┃ \033[1;33m┃\033[1;32m𝗔\033[1;33m┃\033[1;31m➤     ██      ██ ██     ██                 \033[1;37m  ┃
\033[1;37m┃ \033[1;33m┃\033[1;32m𝗥\033[1;33m┃\033[1;31m➤     ████    ██ ██     ████               \033[1;37m  ┃
\033[1;37m┃ \033[1;33m┃\033[1;32m𝗞\033[1;33m┃\033[1;31m➤     ██      ██ ██     ██                  \033[1;37m ┃
\033[1;37m┃ \033[1;33m┃\033[1;31m©\033[1;33m┃\033[1;31m➤     ██  █▄▄▄██ ██▄▄▄█ ██▄▄▄▄█  \033[1;36m𝘃 𝟭.𝟬.𝟭   \033[1;37m  ┃
\033[1;37m┃ \033[1;33m┗\033[1;33m━┛\033[1;31m➤                                            \033[1;31m┛
\033[1;37m┃          \033[1;32m𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 \033[1;31m➤ \033[1;36m{sh} 
\033[1;37m┃ \033[1;33m┏━\033[1;33m┓\033[1;31m➤ \033[1;32m┏\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;32m┓\033[1;31m ┓
\033[1;37m┃ \033[1;33m┃\033[1;32m𝗟\033[1;33m┃\033[1;31m➤ \033[1;33m┃  \033[1;31m⌠\033[1;32m+\033[1;31m⌡  \033[1;32m𝐀𝐮𝐭𝐡𝐨𝐫     \033[1;31m ➤   \033[1;32m𝐋𝐈𝐌𝐎𝐍 𝐇𝐎𝐒𝐒𝐀𝐈𝐍    \033[1;33m┃\033[1;37m ┃
\033[1;37m┃ \033[1;33m┃\033[1;32m𝗠\033[1;33m┃\033[1;31m➤ \033[1;33m┃ \033[1;31m ⌠\033[1;32m+\033[1;31m⌡ \033[1;37m 𝐆𝐢𝐭𝐇𝐮𝐛     \033[1;31m ➤ \033[1;37m  𝐋𝐌𝐍𝐱𝟗-𝐉𝐎𝐇𝐍𝐘     \033[1;33m ┃\033[1;37m ┃
\033[1;37m┃ \033[1;33m┃\033[1;32m𝗡\033[1;33m┃\033[1;31m➤\033[1;33m ┃  \033[1;31m⌠\033[1;32m+\033[1;31m⌡ \033[1;35m 𝐘𝐨𝐮𝐓𝐮𝐛𝐞     \033[1;31m➤  \033[1;35m 𝐋𝐌𝐍𝐱𝟗          \033[1;33m  ┃ \033[1;37m┃
\033[1;37m┃ \033[1;33m┃\033[1;32m𝘅\033[1;33m┃\033[1;31m➤ \033[1;33m┃ \033[1;31m ⌠\033[1;32m+\033[1;31m⌡  \033[1;36m𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦    \033[1;31m➤  \033[1;36m 𝐃𝐀𝐑𝐊_𝐋𝐌𝐍𝐱𝟗    \033[1;33m   ┃\033[1;37m ┃
\033[1;37m┃ \033[1;33m┃\033[1;32m𝟗\033[1;33m┃\033[1;31m➤\033[1;33m ┃ \033[1;31m ⌠\033[1;32m+\033[1;31m⌡  \033[1;33m𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤   \033[1;31m ➤ \033[1;33m  𝐋𝐣.𝐋𝐌𝐍𝐱𝟗       \033[1;33m  ┃\033[1;37m ┃
\033[1;37m┃ \033[1;33m┗\033[1;33m━┛\033[1;31m➤\033[1;32m ┗\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;32m┛ \033[1;37m┃
\033[1;31m┗\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;31m┛
"""
 
class login():
	def __init__(self):
		ids=[]
	def lo_epa(self):
		system('clear')
		print(logo)
		em = input(' PUT ID/EMAIL : ')
		ps = input(' PUT PASSWORD : ')
		e="5990"
		ee="655"
		eee="59"
		tok1 = f"2377{e}9{eee}1{ee}"
		ei="0f140aabedfb65"
		ei2="a2263b1"
		tok2 = f"25257C{ei}ac27a739ed1{ei2}"
		us = f'Mozilla/5.0 (Linux; Android {str(random.randint(4,11))}.0; Nexus 5 Build/MRA{str(random.randint(30,60))}N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edg/111.0.{str(random.randint(1600,1661))}.41'
		br.addheaders = [('User-Agent', us)]
		li = "b-ap"
		lo = "od/auth.l"
		op="3f555f98"
		op2 = "d7aa0c"
		op3="58f522efm"
		sig=f"{op}fb61fc{op2}44f{op3}"
		p = br.open(
			'https://'+li+'i.facebook.com/meth'+lo+'ogin?access_token='+tok1+'%'+tok2+'&format=json&sdk_version=1&email=' + em + '&locale=en_US&password=' + ps + '&sdk=ios&generate_session_cookies=1&sig='+sig+'')
		po = json.load(p)
		if 'access_token' in po:
			toke=po['access_token']
			linex()
			animation(f' [{B}•{W}] 𝗟𝗢𝗚𝗜𝗡 𝗗𝗢𝗡𝗘 ! 𝗥𝗨𝗡 𝗔𝗚𝗔𝗜𝗡')
			open('.token.txt','w').write(toke)
			exit()
		else:
			if 'www.facebook.com' in po['error_msg']:
				print('\033[1;33m ACCOUNT IS IN CHECKPOINT\033[0m')
				exit(em+'|'+ps)
			else:
				linex()
				exit('\033[1;31m WORNG ID/EMAIL OR PASSWORD\033[0m')
	def login_epa2(self):
		system('clear');
		print(logo)
		cooke = input(' cookie : ')
		cookie = {'Cookie': cooke}
		xyz = requests.session()
		data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}
		req = xyz.post('https://graph.facebook.com/v16.0/device/login/', data=data).json()
		cd = req['code']
		ucd = req['user_code']
		url = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038' % (
			cd)
		req = bs(xyz.get('https://mbasic.facebook.com/device', cookies=cookie).content, 'html.parser')
		raq = req.find('form', {'method': 'post'})
		dat = {'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(raq)).group(1),
			   'fb_dtsg': re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(req)).group(1), 'qr': '0',
			   'user_code': ucd}
		rel = 'https://mbasic.facebook.com' + raq['action']
		pos = bs(xyz.post(rel, data=dat, cookies=cookie).content, 'html.parser')
		dat = {}
		raq = pos.find('form', {'method': 'post'})
		for x in raq('input', {'value': True}):
			try:
				if x['name'] == '__CANCEL__':
					pass
				else:
					dat.update({x['name']: x['value']})
			except Exception as e:
				pass
		rel = 'https://mbasic.facebook.com' + raq['action']
		pos = bs(xyz.post(rel, data=dat, cookies=cookie).content, 'html.parser')
		req = xyz.get(url, cookies=cookie).json()
		if 'access_token' in req:
           # linex()
			print(f' [{B}•{W}]\033[1;32m 𝗟𝗢𝗚𝗜𝗡 𝗗𝗢𝗡𝗘 !\033[1;32m 𝗥𝗨𝗡 𝗔𝗚𝗔𝗜𝗡 ')
            #linex()
			open('.token.txt', 'w').write(req['access_token'])
			exit()
		else:
			exit('\033[1;31m 𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗖𝗢𝗢𝗞𝗜𝗘𝗦 𝗢𝗥 𝗦𝗢𝗠𝗘𝗧𝗛𝗜𝗡𝗚𝗦 𝗪𝗥𝗢𝗡𝗚')
	def login_WALA(self):
		system('clear');print(logo)
		print(' [\u001b[36mA\033[1;32m] 𝗟𝗢𝗚𝗜𝗡 𝗪𝗜𝗧𝗛 𝗜𝗗 𝗣𝗔𝗦𝗦 • 𝗪𝗢𝗥𝗞𝗜𝗡𝗚 ')
		print(' [\u001b[36mB\033[1;31m] 𝗟𝗢𝗚𝗜𝗡 𝗪𝗜𝗧𝗛 𝗖𝗢𝗢𝗞𝗜𝗘𝗦 • 𝗡𝗢𝗧 𝗪𝗢𝗥𝗞𝗜𝗡𝗚 ')
		print(' [\u001b[36mC\033[1;30m] 𝗘𝗡𝗧𝗘𝗥 𝗧𝗢 𝗕𝗔𝗖𝗞 ')
		linex()
		menu = input('\033[1;32m [√] 𝗖𝗛𝗢𝗦𝗘 𝗢𝗣𝗧𝗜𝗢𝗡 ➤ ')
		if menu in ['01', '1', 'A', 'a']:
			login().lo_epa()
		if menu in ['02', '2', 'B', 'b']:
			login().login_epa2()
		if menu in ['00', '0', 'C', 'c']:
			back()
		else:
			linex()
			animation('\033[1;31m [×] 𝗖𝗛𝗢𝗦𝗘 𝗖𝗢𝗥𝗥𝗘𝗖𝗧𝗟𝗬 ➤ ')
			time.sleep(1)
			login_WALA()
 
def main_menu():
	os.system("clear");print(logo)
    
	print(' \033[1;32m[𝗔] 𝗖𝗥𝗘𝗔𝗧 𝗦𝗜𝗠𝗣𝗟𝗘 𝗙𝗜𝗟𝗘 ')
	print('\033[1;33m [𝗕] 𝗖𝗥𝗘𝗔𝗧 𝗨𝗡𝗟𝗜𝗠𝗜𝗧𝗘𝗗 𝗙𝗜𝗟𝗘 ')
	print('\033[1;34m [𝗖] 𝗥𝗘𝗠𝗢𝗩𝗘 𝗗𝗨𝗣𝗟𝗜𝗖𝗔𝗧𝗘 𝗜𝗗𝘇 ')
	print(' \033[1;30m[𝗗] 𝗥𝗘𝗣𝗢𝗥𝗧 𝗔 𝗣𝗥𝗢𝗕𝗟𝗘𝗠 ')
	print('\033[1;31m [𝗘] 𝗟𝗢𝗚𝗢𝗨𝗧 𝗗𝗔𝗧𝗔')
	linex()
	xo = input(f' \033[1;32m[√] 𝗖𝗛𝗢𝗦𝗘 𝗢𝗣𝗧𝗜𝗢𝗡 ➤ ')
	if xo in ['01','1', 'A', 'a']:
		file_create_menu().file_simple()
	if xo in ['02','2', 'B', 'b']:
		file_create_menu().file_unlimmited()
	if xo in ['03','3', 'c', 'C']:
		remove_dub()
	if xo in ['04','4', 'D', 'd']:
		contact()
	if xo in ['00','0', 'E', 'e']:
		os.system('rm -rf .token.txt')
		linex()
		animation(f"\033[1;32m [√] 𝗟𝗢𝗚𝗢𝗨𝗧 𝗗𝗢𝗡𝗘 + \033[1;31m𝗖𝗢𝗢𝗞𝗜𝗘 𝗥𝗘𝗠𝗢𝗩𝗘𝗗 ")
		exit()
	else:
		linex()
		animation('\033[1;31m [×] 𝗖𝗛𝗢𝗦𝗘 𝗖𝗢𝗥𝗥𝗘𝗖𝗧𝗟𝗬 ➤ ')
		time.sleep(1)
		main_menu()
siid=[]
sep=[]
 
class file_create_menu():
	def file_simple(self):
		os.system('clear');print(logo)
		try:
			print(f' [•] 𝗪𝗥𝗜𝗧𝗘 𝗙𝗜𝗟𝗘 𝗡𝗔𝗠𝗘 𝗪𝗜𝗧𝗛𝗢𝗨𝗧 /sdcard ')
			nm  = input(f' \033[1;32m[•] 𝗘𝗡𝗧𝗘𝗥 𝗙𝗜𝗟𝗘 𝗡𝗔𝗠𝗘 ➤ ').replace(' ','_')
			lk = '/sdcard/'
			lok = '%s%s'%(lk,nm)
			open(lok,'w')
		except FileNotFoundError:
			print(f'\033[1;31m [×] 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗 , 𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡 !! ')
			time.sleep(2)
			back()
		except IsADirectoryError:
			time.sleep(1)
			file_create_menu().file_simple()
		if IOError:
			pass
			print(f' \033[1;33m[•] 𝗣𝗔𝗦𝗧 𝗨𝗜𝗗 𝗢𝗡𝗘 𝗕𝗬 𝗢𝗡𝗘 ')
			linex()
			while True:
				ids_all = input(f"\033[1;32m [√] 𝗘𝗡𝗧𝗘𝗥 𝗨𝗜𝗗 ➤ ")
				if ids_all == "":
					linex()
					print(f' \033[1;33m[•] 𝗙𝗜𝗟𝗘 𝗦𝗔𝗩𝗘𝗗 𝗜𝗡 ➤ {lok} ')
					input(f'\033[1;30m [•] 𝗘𝗡𝗧𝗘𝗥 𝗧𝗢 𝗕𝗔𝗖𝗞 ')
					back()
					break
				try:
					uid = ids_all.split("|")[0]
				except:
					uid = ids_all
				try:
					headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
							   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
							   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
							   "Authorization": "OAuth "+self.token+"",
							   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
							   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
							   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
							   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
							   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
							   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
							   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
							   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
					data = {
						'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
						'client_doc_id': client_id,
						'method': 'post',
						'locale': 'en_US',
						'pretty': 'false',
						'format': 'json',
						'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
						'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
						'fb_api_caller_class': 'graphservice',
						'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
						'client_trace_id': trace_id,
						'server_timestamps': 'true',
						'purpose': 'fetch'
					}
					posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
					try:
						data = posted['data']['user']['friends']['edges']
					except:
						print(f' \033[1;31m 𝗦𝗢𝗠𝗘𝗧𝗛𝗜𝗡𝗚 𝗪𝗥𝗢𝗡𝗚 𝗪𝗜𝗧𝗛 {uid}\033[0m ')
					if len(data) < 100:
						print(f'\033[1;31m [×] 𝗣𝗥𝗜𝗩𝗘𝗧 𝗙𝗥𝗜𝗘𝗡𝗗𝗟𝗜𝗦𝗧 𝗢𝗙 {uid} ')
						linex()
					else:
						for edge in data:
							node = edge['node']
							open(lok, 'a', encoding='utf-8').write(node['id'] + "|" + node['name'] + '\n')
						try:
							total_idss=len(open(lok,'r').readlines())
						except:
							total_idss='-'
						print(f' \033[1;32m[•] 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗘𝗫𝗧𝗥𝗔𝗖𝗧𝗘𝗗 {uid} [{total_idss}] \033[0m')
						linex()
				except KeyError:
					pass
				except requests.exceptions.ConnectionError:
					input(f" \033[1;31m[×] 𝗖𝗢𝗡𝗡𝗘𝗖𝗧𝗜𝗢𝗡 𝗘𝗥𝗥𝗢𝗥 - 𝗘𝗡𝗧𝗘𝗥 𝗧𝗢 𝗖𝗢𝗡𝗧𝗜𝗡𝗨𝗘")
	def __init__(self):
		try:
			os.system('.a.txt')
			os.system('.temp.txt')
			os.remove('.temp.txt')
			os.remove('.a.txt')
		except:
			pass
		self.ids = []
		self.total = []
		self.loop = 0
		try:
			self.token = open('.token.txt', 'r').read()
			uid="100061689760374"
			try:
				headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
						   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
						   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
						   "Authorization": "OAuth "+self.token+"",
						   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
						   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
						   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
						   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
						   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
						   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
						   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
						   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
				data = {
					'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
					'client_doc_id': client_id,
					'method': 'post',
					'locale': 'en_US',
					'pretty': 'false',
					'format': 'json',
					'variables': '{"profile_id":'+uid+',"suggestion_friends_paginating_first":2500}',
					'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
					'fb_api_caller_class': 'graphservice',
					'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
					'client_trace_id': trace_id,
					'server_timestamps': 'true',
					'purpose': 'fetch'
				}
				posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
				if not posted['data']['user']['friends']['edges']:
				    os.system('clear');print(logo)
				    os.system('.token.txt')
				try:
					data = posted['data']['user']['friends']['edges']
				except:
					print(f' \033[1;31m 𝗦𝗢𝗠𝗘𝗧𝗛𝗜𝗡𝗚 𝗪𝗥𝗢𝗡𝗚 𝗪𝗜𝗧𝗛 𝗧𝗛𝗜𝗦 𝗜𝗗 \033[0m ')
					os.system('.token.txt')
					exit()
			except Exception as e:
				os.system('clear');print(logo)
				print(f" [{B}×{W}] \033[1;31m𝗖𝗢𝗢𝗞𝗜𝗘𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗 !")
				print(e)
				login.login_WALA('')
		except Exception as e:
			print(e)
			login.login_WALA('')
	def file_unlimmited(self):
		os.system('clear');print(logo)
		limit = input(f" [{B}•{W}]\033[1;33m 𝗛𝗢𝗪 𝗠𝗔𝗡𝗬 𝗨𝗜𝗗 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗔𝗗𝗗𝗘𝗗 ? : ")
		try:
			print(f' [{B}•{W}] 𝗪𝗥𝗜𝗧𝗘 𝗙𝗜𝗟𝗘 𝗡𝗔𝗠𝗘 𝗪𝗜𝗧𝗛𝗢𝗨𝗧 /sdcard ')
			nm  = input(f' [{B}•{W}] \033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗙𝗜𝗟𝗘 𝗡𝗔𝗠𝗘 ➤ ').replace(' ','_')
			lk = '/sdcard/'
			lok = '%s%s'%(lk,nm)
			open(lok,'w')
		except FileNotFoundError:
			print(f' [{B}×{W}]\033[1;31m 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗 , 𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡 !! ')
			time.sleep(2)
			back()
		except IsADirectoryError:
			time.sleep(1)
			file_create_menu().file_simple()
		if IOError:
			pass
			os.system('clear');print(logo)
			try:
				file = open('.temp.txt', 'r').read().splitlines()
			except:
				file = []
			os.system('clear');print(logo)
			for i in range(int(limit)):
				uid = input(" PUT UID {} : ".format(i+1))
				try:
					headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
							   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
							   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
							   "Authorization": "OAuth " + self.token + "",
							   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
							   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
							   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
							   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
							   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
							   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
							   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
							   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
					data = {
						'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
						'client_doc_id': client_id,
						'method': 'post',
						'locale': 'en_US',
						'pretty': 'false',
						'format': 'json',
						'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
						'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
						'fb_api_caller_class': 'graphservice',
						'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
						'client_trace_id': trace_id,
						'server_timestamps': 'true',
						'purpose': 'fetch'
					}
					posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
					try:
						data = posted['data']['user']['friends']['edges']
					except:
						print(f' \033[1;31m 𝗦𝗢𝗠𝗘𝗧𝗛𝗜𝗡𝗚 𝗪𝗥𝗢𝗡𝗚 𝗪𝗜𝗧𝗛 {uid}\033[0m ')
					if len(data) < 100:
						print(f' [{B}×{W}] \033[1;31m𝗣𝗥𝗜𝗩𝗔𝗧𝗘 𝗙𝗥𝗜𝗘𝗡𝗗𝗟𝗜𝗦𝗧 𝗢𝗙 {uid} ')
					else:
						for edge in data:
							node = edge['node']
							open('.a.txt', 'a', encoding='utf-8').write(node['id'] + '\n')
							idss = len(open('.a.txt','r').readlines())
						print(f' [{B}×{W}] \033[1;32m𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗘𝗫𝗧𝗥𝗔𝗖𝗧𝗘𝗗 {uid} [{idss}]\033[0m')
				except KeyError:
					pass
				except requests.exceptions.ConnectionError:
					input(f" [{B}×{W}]\033[1;31m 𝗖𝗢𝗡𝗡𝗘𝗖𝗧𝗜𝗢𝗡 𝗘𝗥𝗥𝗢𝗥 - 𝗘𝗡𝗧𝗘𝗥 𝗧𝗢 𝗖𝗢𝗡𝗧𝗜𝗡𝗨𝗘")
			try:
				file = open('.a.txt', 'r').read().splitlines()
			except:
				file = [] 
			os.system('clear');print(logo)
			print(f' [{B}√{W}] \033[1;32m𝗧𝗢𝗧𝗔𝗟 𝗜𝗗 𝗧𝗢 𝗘𝗫𝗧𝗥𝗔𝗖𝗧 ➤ ' + str(len(file)))
			print(f' [{B}√{W}] \033[1;33m𝗙𝗜𝗟𝗘 𝗦𝗔𝗩𝗘 𝗔𝗦 ➤ {lok} ')
			print(f' [{B}√{W}] \033[1;30m𝗣𝗥𝗘𝗦𝗦 𝗖𝗧𝗥𝗟 + 𝗭 𝗧𝗢 𝗦𝗧𝗢𝗣 ')
			linex()
			for uid in file:
				try:
					headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
							   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
							   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
							   "Authorization": "OAuth " + self.token + "",
							   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
							   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
							   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
							   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
							   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
							   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
							   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
							   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
					data = {
						'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
						'client_doc_id': client_id,
						'method': 'post',
						'locale': 'en_US',
						'pretty': 'false',
						'format': 'json',
						'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
						'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
						'fb_api_caller_class': 'graphservice',
						'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
						'client_trace_id': trace_id,
						'server_timestamps': 'true',
						'purpose': 'fetch'
					}
					posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
					try:
						data = posted['data']['user']['friends']['edges']
					except:
						print(f' \033[1;31m 𝗦𝗢𝗠𝗘𝗧𝗛𝗜𝗡𝗚 𝗪𝗥𝗢𝗡𝗚 𝗪𝗜𝗧𝗛 {uid}\033[0m ')
					if len(data) < 100:
						print(f' [{B}×{W}] \033[1;31m𝗣𝗥𝗜𝗩𝗔𝗧𝗘 𝗙𝗥𝗜𝗘𝗡𝗗𝗟𝗜𝗦𝗧 𝗢𝗙 {uid} ')
					else:
						for edge in data:
							node = edge['node']
							open(lok, 'a', encoding='utf-8').write(node['id'] + "|" + node['name'] + '\n')
						if 'y' in sep:
							perfector(lok)
						try:
							total_idss=len(open(lok,'r').readlines())
						except:
							total_idss='-'
						print(f' [{B}•{W}]\033[1;32m 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗘𝗫𝗧𝗥𝗔𝗖𝗧𝗘𝗗 {uid} [{total_idss}] ')
				except KeyError:
					pass
				except requests.exceptions.ConnectionError:
					input(f" [{B}•{W}]\033[1;31m 𝗖𝗢𝗡𝗡𝗘𝗖𝗧𝗜𝗢𝗡 𝗘𝗥𝗥𝗢𝗥 - 𝗘𝗡𝗧𝗘𝗥 𝗧𝗢 𝗖𝗢𝗡𝗧𝗜𝗡𝗨𝗘")
			print(' 𝗜𝗗𝘇 𝗦𝗔𝗩𝗘𝗗 𝗜𝗡 {} path'.format(lok))
			print(' \033[1;32m𝗧𝗢𝗧𝗔𝗟 𝗜𝗗𝘇 𝗦𝗔𝗩𝗘𝗗 𝗜𝗡 𝗙𝗜𝗟𝗘 {} '.format(len(open(lok,'r').read().splitlines())))
			input(' \033[1;30m𝗘𝗡𝗧𝗘𝗥 𝗧𝗢 𝗕𝗔𝗖𝗞 ')
			exit()
 
def remove_dub():
    clear()
    print(logo)
    try:
        filename = input(f" [{B}•{W}] \033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗙𝗜𝗟𝗘 𝗡𝗔𝗠𝗘 ➤ ")
        sd = '/sdcard/'
        file_path = os.path.join(sd, filename)
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
        lines = sorted(set(lines))
        with open(file_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')
        linex()
        print(f' [{B}√{W}] \033[1;32m𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗥𝗘𝗠𝗢𝗩𝗘𝗗')
        input(f' [{B}√{W}] \033[1;30m𝗘𝗡𝗧𝗘𝗥 𝗧𝗢 𝗕𝗔𝗖𝗞 ')
        back()
    except FileNotFoundError:
        linex()
        print(f' [{B}×{W}] \033[1;31m𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗 , 𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡 ')
        time.sleep(2)
        remove_dub()
 
main_menu()
os.system('rm -rf .a.txt')
    
