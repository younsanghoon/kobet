import time
import random
import copy
import threading
import traceback
import pickle
from datetime import datetime, timedelta
import requests
import json
import sys
import os
import requests
import mechanicalsoup
import uuid
import string
from PyQt5 import QtCore, QtGui
import webSocket
from websocket import create_connection
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


tb = time.time()
def tt():
    return str(time.time()).replace("." , "")[:13]
def wid(length=10):
    strCase = string.ascii_lowercase+string.ascii_uppercase+string.digits
    return ''.join(random.choice(strCase) for x in range(length))


class kibetWebsocket():
    def __init__(self , sessId = ''  , host = ''):
        self.loop = True
        self.Alive = True
        self.host = host
        self.sessId = sessId
    def run(self):
        global tb
        try:
            self.wd = time.time()
            headers = {}
            self.tables = {}
            self.tableIds = []
            self.answers = {}
            headers['Host'] = self.host
            headers['Connection'] = 'Upgrade'
            headers['Pragma'] = 'no-cache'
            headers['Cache-Control'] = 'no-cache'
            headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
            headers['Upgrade'] = 'websocket'
            headers['Origin'] = 'https://%s'%self.host
            headers['Sec-WebSocket-Version'] = '13'
            headers['Accept-Encoding'] = 'gzip, deflate, br'
            headers['Accept-Language'] = 'ko,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,zh-TW;q=0.5,de;q=0.4,de-CH;q=0.3,de-AT;q=0.2,ja;q=0.1'
            headers['Cookie'] = 'EVOSESSIONID=%s'%self.sessId
            headers['Sec-WebSocket-Key'] = wid(26)
            headers['Sec-WebSocket-Extensions'] = 'permessage-deflate; client_max_window_bits'



            #'livecasino.kibet-1.com'
            self.ws = create_connection("wss://livecasino.eg88play.com/public/lobby/player/socket?messageFormat=json"%self.host, header=headers)

            webSocket.init(self.ws)

            print(tb- time.time())
            i = 0
            while self.loop:
                
                i+=1
                if ( time.time() - self.wd) > 10:
                    break

                result = self.ws.recv()
                data = json.loads(result)

                if data["type"] == "lobby.tables":
                    for t in data['args']['tables']:
                        self.tables[t['tableId']] = t['name']
                        self.tableIds.append(t['tableId'])
                if data["type"] == "lobby.rouletteNumbersUpdated":
                    self.answers[data["args"]['tableId']] = [ int(x[0]['number']) for x in data['args']['numbers']['results']]
                if data['type'] == 'lobby.tableDetails':
                    for tx in data['args']['tables']:
                        self.answers[tx['tableId']] = [ int(x[0]['number']) for x in  tx['roulette']['numbers']['results']]

                if i % 10 == 0:
                    i = 0
                    self.ws.send(json.dumps('{"id":"%s","type":"metrics.ping","args":{"t":%s}}' % (wid(), tt())))

        except:
            print("seesion die" , traceback.format_exc())
            print(result)
        self.Alive = False
        self.ws.close()








sessionHeaders = {}
sessionHeaders["Connection"] = "keep-alive"
sessionHeaders["Origin"] = "https://kibet-1.com/en/"
sessionHeaders['Accept'] = '*/*'
sessionHeaders["X-Requested-With"] = "XMLHttpRequest"
sessionHeaders["Content-Type"] = "application/x-www-form-urlencoded;"# charset=UTF-8"
sessionHeaders["Referer"] = "https://kibet-1.com/en/"
sessionHeaders["Accept-Encoding"] = "gzip, deflate, br"
sessionHeaders["Accept-Language"] = "en-US;q=0.9,en;q=0.8"#"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
sessionHeaders["User-Agent"] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
browser = mechanicalsoup.StatefulBrowser()
r = browser.get('https://kobet-1.com/Mobile/IsMobile?IsMobile=true', verify=False)
cnt0 = r.content.find(b'Build Version: ')
cnt1 = r.content.find(b'" id="build"><' , cnt0)
buildVersion = r.content.decode()[cnt0:cnt1]
myInfo = b"Email=%s&Password=%s&gameUrl="%(b"can671" , b"1q2w3e4r!!")
r = browser.get("https://kobet-1.com/Mobile/IsMobile?IsMobile=true", verify=False)#https://kobet-1.com/en/
r = browser.post("https://kobet-1.com/ko/Login/Login", data=myInfo, headers=sessionHeaders, verify=False)
r = browser.get("https://kobet-1.com/LiveCasino/GetLiveCasinoUrl?url=", verify=False, headers=sessionHeaders)
gameURL = json.loads(r.content.decode())["Message"]
browser.get(gameURL, verify=False, headers=sessionHeaders)

sessionHeaders = {}
sessionHeaders["Upgrade-Insecure-Requests"]="1"
sessionHeaders["User-Agent"]="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
sessionHeaders["Accept"]="text/html"#,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
sessionHeaders["Referer"]="https://kibet-1.com/en/LiveCasino"
sessionHeaders["Accept-Encoding"]="gzip, deflate, br"
sessionHeaders["Content-Type"] = 'text/html'
sessionHeaders["Accept-Language"]="en-US;q=0.9,en;q=0.8"#"ko,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,zh-TW;q=0.5,de;q=0.4,de-CH;q=0.3,de-AT;q=0.2,ja;q=0.1,pt;q=0.1"

r = browser.get('https://livecasino.kibet-1.com/mobile/', verify=False, headers=sessionHeaders)


print(browser.get_cookiejar().keys())
sessionId = browser.get_cookiejar()["EVOSESSIONID"]
kws = kibetWebsocket(sessionId ,'kibet-1.com')
print(time.time() - tb)
kws.run()






