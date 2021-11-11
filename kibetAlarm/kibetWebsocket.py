import random
import string
from websocket import create_connection
import json
import mechanicalsoup
import webSocket
import time
import string
import random
import traceback
#strCase = string.ascii_lowercase+string.ascii_uppercase+string.digits

def tt():
    return str(time.time()).replace("." , "")[:13]
def wid():
    strCase = string.ascii_lowercase+string.ascii_uppercase+string.digits
    return ''.join(random.choice(strCase) for x in range(10))

sessionHeaders = {}
sessionHeaders["Connection"] = "keep-alive"
sessionHeaders["Origin"] = "https://kibet-1.com"
sessionHeaders['Accept'] = '*/*'
sessionHeaders["X-Requested-With"] = "XMLHttpRequest"
sessionHeaders["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
sessionHeaders["Referer"] = "https://kibet-1.com/"
sessionHeaders["Accept-Encoding"] = "gzip, deflate, br"
sessionHeaders["Accept-Language"] = "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
sessionHeaders["User-Agent"] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'

browser = mechanicalsoup.StatefulBrowser()

        
myInfo = b"Email=%s&Password=%s&gameUrl="%(b"xxxxjune" ,b"cxxx5835")
while 1:
    r = browser.get("https://kibet-1.com/ko/", verify=False)
    if r.status_code == 200:
        r = browser.post("https://kibet-1.com/ko/Login/Login", data=myInfo, headers=sessionHeaders, verify=False)
        if r.status_code == 200:
            b = browser.get("https://kibet-1.com/LiveCasino/GetLiveCasinoUrl", verify=False, headers=sessionHeaders)
            if b.status_code == 200:
                gameURL = b.content.decode()
                if 'https://livecasino.kibet-1.com/cgibin/UserAuthentication?' in gameURL:
                    b = browser.get(gameURL, verify=False, headers=sessionHeaders)
                    if b.status_code == 200:
                        b = browser.get('https://livecasino.kibet-1.com/mobile/' , verify=False, headers=sessionHeaders)
                        if b.status_code == 200:
                            if "EVOSESSIONID" in browser.get_cookiejar().keys():
                                break
print("EVOSESSIONID" , browser.get_cookiejar()['EVOSESSIONID'])
#b = browser.get(gameURL, verify=False, headers=sessionHeaders)

input("...")

headers = {}

headers['Host'] = 'livecasino.kibet-1.com'
headers['Connection'] = 'Upgrade'
headers['Pragma'] = 'no-cache'
headers['Cache-Control'] = 'no-cache'
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
headers['Upgrade'] = 'websocket'
headers['Origin'] = 'https://livecasino.kibet-1.com'
headers['Sec-WebSocket-Version'] = '13'
headers['Accept-Encoding'] = 'gzip, deflate, br'
headers['Accept-Language'] = 'ko,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,zh-TW;q=0.5,de;q=0.4,de-CH;q=0.3,de-AT;q=0.2,ja;q=0.1'
headers['Cookie'] = 'EVOSESSIONID=9e3a6b6c62e1a2ab53548e0eb1002fa63e6b15cdeab5dc05f225580cfebd3928df337c5a81b719ae'
headers['Sec-WebSocket-Key'] = 'abcdefrt/abc9GcnEbxk+Q==")'
headers['Sec-WebSocket-Extensions'] = 'permessage-deflate; client_max_window_bits'
ws = create_connection("wss://livecasino.kibet-1.com/public/lobby/player/socket?messageFormat=json", header=headers)

tb = time.time()

webSocket.init(ws)

try:
    print("init complete")
    for i in range(100000):
        result =  ws.recv()
        data = json.loads(result)
        if data["type"] == "lobby.rouletteNumbersUpdated":
            if data["args"]['tableId'] == "wzg6kdkad1oe7m5k":
                print("\n",str(int((time.time()-tb)/60)).zfill(3) ,  str(i).zfill(6) , data['args']['numbers']['results'][:3])
            else:
                print("x", end = ",")
        else:
            print("x", end = ",")
            
        if i%10 == 0:
            ws.send(json.dumps('{"id":"%s","type":"metrics.ping","args":{"t":%s}}'%(wid(),tt())))
        if i%30 == 0:
            print("\n")
except:
    print(traceback.format_exc())
    print(result)
    
        

        
ws.close()
