import threading
import requests
import xmltodict
import json
import mechanicalsoup
import string
import random
import time
from websocket import create_connection
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

Lof = False

def pharseHeaders(headerStr):
    headers = []
    tmp = []

    headers = headerStr.split('\n')
    for h in headers:
        if len(h.strip()) > 0:
            tmp.append(h)

    headers = {}
    for h in tmp:
        headers[h.split(":")[0]] = ': '.join(h.split(": ")[1:])
    return headers

def tt():
    return int(str(time.time()).replace("." , "")[:13])
def wid():
    strCase = string.ascii_lowercase+string.ascii_uppercase+string.digits
    return ''.join(random.choice(strCase) for x in range(10))

class KoBeting(threading.Thread):
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        self.nm = 0
        self.nm1 = []
        self.nmaa1 = 0
        self.ups = 0
        self.douns = 0
        self.Blacks = 0
        self.Rads = 0
        self.Nber1s = 0
        self.Nber2s = 0
        self.Rad = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        self.Black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
        
    def Lroom1 (self) :
        if self.nmaa1 == 0:
            if self.x == self.y:#'7x0b1tgh7agmf6hv': 
                for i in range(len(dataR['args']['numbers']['results'])):
                    self.nm1.append(int(dataR['args']['numbers']['results'][i][0]['number']))
                    self.nmaa1 +=1
                    if self.nmaa1 == 12:
                        self.nmaa1 +=1
                        self.nm1.reverse()
                        
    def Lroom2 (slef)    
        if self.nmaa1 > 12:
            if self.x == self.y:#'7x0b1tgh7agmf6hv': 
                self.nm = int(dataR['args']['numbers']['results'][0][0]['number'])
                
class CNB(threading.Thread):
    def __init__ (self):
        self.ups = 0
        self.douns = 0
        self.Blacks = 0
        self.Rads = 0
        self.Nber1s = 0
        self.Nber2s = 0
        self.Rad = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        self.Black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
        
    def CounT(self)
        for Cmn in range(len(nm1)):
            Cmns = int(nm1[Cmn])
            self.Countnumber(Cmns)
            
    def Countnumber(self,qwe) :
        if qwe == 0:
            self.Rads +=1
            self.Blacks +=1
            self.Nber1s +=1
            self.Nber2s +=1
            self.ups +=1
            self.douns +=1
            #print('홀수:',self.Nber1s, '짝수:',self.Nber2s, '레드:',self.Rads, '블랙:', self.Blacks, '업:',self.ups, '다운:',self.douns)
        else:
            if qwe%2==1:
                self.Nber1s +=1
                self.Nber2s =0
                #print('홀수:',self.Nber1s, '짝수:',self.Nber2s, '레드:',self.Rads, '블랙:', self.Blacks, '업:',self.ups, '다운:',self.douns)
            else:
                self.Nber1s =0
                self.Nber2s +=1
            if self.Rad.count(qwe):
                self.Rads +=1
                self.Blacks = 0
                #print('홀수:',self.Nber1s, '짝수:',self.Nber2s, '레드:',self.Rads, '블랙:', self.Blacks, '업:',self.ups, '다운:',self.douns)
            else:
                self.Blacks +=1
                self.Rads = 0
            if qwe >= 1 and qwe <= 18:
                self.douns +=1
                self.ups =0
                #print('홀수:',self.Nber1s, '짝수:',self.Nber2s, '레드:',self.Rads, '블랙:', self.Blacks, '업:',self.ups, '다운:',self.douns)
            else:
                self.ups +=1
                self.doun = 0
        

class KoBet(threading.Thread) :
    def __init__ (self,ws,ROMS,NOBER,x,y,sessionId,wshead2):
        self.sessionId = sessionId
        self.wshead2 = wshead2
        self.ws = ws
        self.x = x
        self.y = y
        self.ROMS = ROMS
        self.NOBER = NOBER
        self.Q1 = 1
        self.Q2 = 1
        self.Q3 = 1
        self.nm = 0
        self.nm1 = []
        self.nm2 = []
        self.nmaa1 = 0
        self.ups = 0
        self.douns = 0
        self.Blacks = 0
        self.Rads = 0
        self.Nber1s = 0
        self.Nber2s = 0
        self.Rad = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        self.Black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    def tt(self):
        return int(str(time.time()).replace("." , "")[:13])
    def wid(self):
        strCase = string.ascii_lowercase+string.ascii_uppercase+string.digits
        return ''.join(random.choice(strCase) for x in range(10))
    def gameIdS(self):
        strCase = string.ascii_lowercase+string.ascii_uppercase+string.digits
        return ''.join(random.choice(strCase) for x in range(24))
        
    def Lroom (self) :
        if self.nmaa1 == 0:
            if self.x == self.y:#'7x0b1tgh7agmf6hv': 
                #self.nm = int(dataR['args']['numbers']['results'][0][0]['number'])
                for i in range(len(dataR['args']['numbers']['results'])):
                    self.nm1.append(int(dataR['args']['numbers']['results'][i][0]['number']))
                    self.nmaa1 +=1
                    if self.nmaa1 == 12:
                        self.nmaa1 +=1
                        self.nm1.reverse()
                        for Cmn in range(len(self.nm1)):
                            self.Cmns = int(self.nm1[Cmn])
                            self.Countnumber(self.Cmns)
                            self.Room500()
        elif self.nmaa1 > 12:
            if self.x == self.y:#'7x0b1tgh7agmf6hv': 
                self.nm = int(dataR['args']['numbers']['results'][0][0]['number'])
                self.Countnumber(self.nm)
                self.Room500()
                
    def Countnumber(self,qwe) :
        if qwe == 0:
            self.Rads +=1
            self.Blacks +=1
            self.Nber1s +=1
            self.Nber2s +=1
            self.ups +=1
            self.douns +=1
            #print('홀수:',self.Nber1s, '짝수:',self.Nber2s, '레드:',self.Rads, '블랙:', self.Blacks, '업:',self.ups, '다운:',self.douns)
        else:
            if qwe%2==1:
                self.Nber1s +=1
                self.Nber2s =0
                #print('홀수:',self.Nber1s, '짝수:',self.Nber2s, '레드:',self.Rads, '블랙:', self.Blacks, '업:',self.ups, '다운:',self.douns)
            else:
                self.Nber1s =0
                self.Nber2s +=1
            if self.Rad.count(qwe):
                self.Rads +=1
                self.Blacks = 0
                #print('홀수:',self.Nber1s, '짝수:',self.Nber2s, '레드:',self.Rads, '블랙:', self.Blacks, '업:',self.ups, '다운:',self.douns)
            else:
                self.Blacks +=1
                self.Rads = 0
            if qwe >= 1 and qwe <= 18:
                self.douns +=1
                self.ups =0
                #print('홀수:',self.Nber1s, '짝수:',self.Nber2s, '레드:',self.Rads, '블랙:', self.Blacks, '업:',self.ups, '다운:',self.douns)
            else:
                self.ups +=1
                self.doun = 0
                            
    def betin(self):
        if self.Nber1s == 4 :
            self.Q1 = 1
            self.UI = 1
            self.RoomIn ()
            self.Wsoc()
            self.BetingTime()
            #print ('짝수 배팅','홀수:',self.Nber1s, '짝수:',self.Nber2s, '레드:',self.Rads, '블랙:', self.Blacks, '업:',self.ups, '다운:',self.douns)
        elif self.Nber1s > 4 :
            self.Q1 *= 2
            self.UI = 1
            self.RoomIn ()
            self.Wsoc()
            for O in range(self.Q1):
                self.BetingTime()
            #print ('짝수 2배 배팅','홀수:',self.Nber1s, '짝수:',self.Nber2s, '레드:',self.Rads, '블랙:', self.Blacks, '업:',self.ups, '다운:',self.douns)
        else:
            pass
        if self.Rads == 4:
            self.Q2 = 1
            self.UI = 2
            self.RoomIn ()
            self.Wsoc()
            self.BetingTime()
            #print('블랙 배팅','홀수:',self.Nber1s, '짝수:',self.Nber2s, '레드:',self.Rads, '블랙:', self.Blacks, '업:',self.ups, '다운:',self.douns)
        elif self.Rads > 4:
            self.Q2 *= 2
            self.UI = 2
            self.RoomIn ()
            self.Wsoc()
            for O in range(self.Q2):
                self.BetingTime()
            #print('블랙 2배 배팅','홀수:',self.Nber1s, '짝수:',self.Nber2s, '레드:',self.Rads, '블랙:', self.Blacks, '업:',self.ups, '다운:',self.douns)
        else:
            pass
        if self.ups == 4:
            self.Q3 = 1
            self.UI = 3
            self.RoomIn ()
            self.Wsoc()
            self.BetingTime()
            #print('다운 배팅','홀수:',self.Nber1s, '짝수:',self.Nber2s, '레드:',self.Rads, '블랙:', self.Blacks, '업:',self.ups, '다운:',self.douns)
        elif self.ups > 4:
            self.Q3 *= 2
            self.UI = 3
            self.RoomIn ()
            self.Wsoc()
            for O in range(self.Q3):
                self.BetingTime()
            #print('다운 2배 배팅','홀수:',self.Nber1s, '짝수:',self.Nber2s, '레드:',self.Rads, '블랙:', self.Blacks, '업:',self.ups, '다운:',self.douns)
        else:
            pass

    def RoomIn (self):#self.Money 현재 돈 ------------------------------------------------------------
        La = random.random(-200,500)
        if ROM == "LightningTable01":
            PPjfjhg = self.ROMS
            self.ws.send(json.dumps({"log":{"type":"CLIENT_LOBBY_TABLE_JOIN_CLICK","latency":La,"value":{"currency":"KRW","gameType":"lobby","buildId":"Build Version: 6.20191219.84546-f3434ac8 at 2019-12-19 09:02:37","device":"Desktop","typeApp":"lobby4","categoryId":"roulette","tablesCount":17,"layout":"Medium","filter":"NotAvailable","timeInLobby":34347,"tableId":"LightningTable01","tableName":"라이트닝 룰렛","channel":"PCMac","orientation":"landscape","balance":Money,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36","inGame":false}}}))
        else:
            self.ws.send(json.dumps({"log":{"type":"CLIENT_LOBBY_TABLE_JOIN_CLICK","latency":La,"value":{"currency":"KRW","gameType":"lobby","buildId":"Build Version: 6.20191219.84546-f3434ac8 at 2019-12-19 09:02:37","device":"Desktop","typeApp":"lobby4","categoryId":"roulette","tablesCount":17,"layout":"Medium","filter":"NotAvailable","timeInLobby":11770,"tableId":"%s","tableName":"%s","tableOrder":self.NOBER,"channel":"PCMac","orientation":"landscape","balance":Money,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36","inGame":false}}}))%(x,self.ROMS)
        self.ws.send(json.dumps({"log":{"type":"CLIENT_PRESSED_INGAME_LOBBY_CLOSE","latency":La,"value":{"currency":"KRW","gameType":"lobby","buildId":"Build Version: 6.20191219.84546-f3434ac8 at 2019-12-19 09:02:37","device":"Desktop","typeApp":"lobby4","categoryId":"roulette","target":"InGame Lobby","timeInLobby":11773,"channel":"PCMac","orientation":"landscape","balance":Money,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36","inGame":true}}}))
        self.ws.send(json.dumps({"log":{"type":"CLIENT_LOBBY_EXIT","latency":La,"value":{"currency":"KRW","gameType":"lobby","buildId":"Build Version: 6.20191219.84546-f3434ac8 at 2019-12-19 09:02:37","device":"Desktop","typeApp":"lobby4","categoryId":"roulette","timeInLobby":11775,"channel":"PCMac","orientation":"landscape","balance":Money,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36","inGame":true}}}))


    def Wsoc(self) :#x = 7x0b1tgh7agmf6hv
        #룸 들어가기 함수
        self.CT = False
        wss = create_connection("wss://livecasino.eg88play.com/public/roulette/player/game/%s/socket?messageFormat=json&instance=wrw3g-nx54o66tzywcx35y-%s&tableConfig=&EVOSESSIONID="+self.sessionId, headers = pharseHeaders(self.wshead2))%(self.x,self.x)

        wss.send(json.dumps({"id":wid(),"type":"settings.read","args":{"key":"generic.common"}}))

        wss.send(json.dumps({"id":wid(),"type":"settings.read","args":{"key":"generic.mobile"}}))

        wss.send(json.dumps({"id":wid(),"type":"settings.read","args":{"key":"roulette.common"}}))

        wss.send(json.dumps({"log":{"type":"CLIENT_GAME_LOADED","value":{"typeApp":"roulette","buildId":"6.20191121.111140-2c066ecb","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36","url":"https://livecasino.eg88play.com/mobile/#table_id=%s&category=roulette&game=roulette","channel":"PCMac","orientation":"landscape"}}}))%self.x

        wss.send(json.dumps({"log":{"type":"CLIENT_SOCKET_CONNECTION_ESTABLISHED","value":{"offline":false,"channel":"PCMac","orientation":"landscape"}}}))

        wss.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
        while self.CT == False:
            time.sleep(0.1)
            result =  wss.recv()
            data = json.loads(result)
            #print(data)
            asd = {"id":"1575370639752-9918","type":"roulette.recentResults","args":{"recentResults":[["16"],["17"],["4"],["25"]],"lastGameId":"15dcd7322a687df88ee15880"},"time":1575370639752}
            asdd = asd.keys()
            if data.keys() == asdd:
                if data["type"] == "roulette.recentResults":
                    self.dataa = data
                    self.CT = True
        wss.send(json.dumps({"id":wid(),"type":"favouriteBets.loadBets","args":{"queryString":{"tableId":"%s"}}}))%self.x
        result =  wss.recv()
        data3 = json.loads(result)
        if data3["args"] == "balance":
            self.E = int(data3["args"]["balance"])
        #data = json.loads(result)
        #print(result)
        #print('vvvvvvvvvv')
        time.sleep(0.1)
        wss.send(json.dumps({"log":{"type":"CLIENT_BALANCE_UPDATED","value":{"currency":"₩","balance":self.E,"channel":"PCMac","orientation":"landscape"}}}))
        #for ii in range(11):
        result =  wss.recv()
        data = json.loads(result)
        #print(result)
        #print('cccccccccc')
        time.sleep(0.2)
        wss.send(json.dumps({"id":wid(),"type":"settings.update","args":{"key":"generic.common.gameSoundVolume","data":1}}))
        time.sleep(0.1)
        wss.send(json.dumps({"id":wid(),"type":"settings.update","args":{"key":"generic.common.studioSoundVolume","data":1}}))
        time.sleep(0.1)
        wss.send(json.dumps({"log":{"type":"CLIENT_POPUP_DISPLAYED","value":{"popupId":"PopupId.LOW_BALANCE","channel":"PCMac","orientation":"landscape"}}}))
        time.sleep(0.1)
        wss.send(json.dumps({"log":{"type":"CLIENT_VIDEO_V2_INITIALIZED","value":{"device":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36","screenSize":"","type":"desktop","name":"unknown","browser":{"family":"Chrome","version":"78.0.3904.108"},"os":{"family":"Windows","version":"10.0"}},"client":{"pointInTime":0,"videoSessionId":"nx54o66tzywcx35y-fb52cf79925c2bbce56c6fad42b80724242579185a842f2ca669685a50dafbdde26001d203aedd48-%s-559865","referer":"livecasino.eg88play.com","componentLoadingTime":6539},"component":{"version":"v5.132.8_5.20191125.114720_28dda211","scenario":""},"video":{"masterHost":"live1.egcvi.com"},"channel":"PCMac","orientation":"landscape"}}}))%self.x
        time.sleep(0.1)
        wss.send(json.dumps({"log":{"type":"CLIENT_VIDEO_PLAYBACK_EVENT","value":{"playbackEventData":{"timestamp":tt(),"playbackEventType":"PLAYER_ATTEMPT","data":{"playerEventHistory":"flvjs","firstVideoSessionId":"nx54o66tzywcx35y-fb52cf79925c2bbce56c6fad42b80724242579185a842f2ca669685a50dafbdde26001d203aedd48-%s-559865"},"reason":"PLAYER_ATTEMPT"},"sessionData":{"game":"roulette","videoSessionId":"nx54o66tzywcx35y-fb52cf79925c2bbce56c6fad42b80724242579185a842f2ca669685a50dafbdde26001d203aedd48-%s-559865"},"channel":"PCMac","orientation":"landscape"}}}))%(self.x,self.x)
        time.sleep(0.1)
        wss.send(json.dumps({"log":{"type":"CLIENT_VIDEO_V2_PLAYBACK_ATTEMPT","value":{"behaviour":{"autoPlayAllowed":true},"logic":{"currentPlayer":"flvjs"},"client":{"pointInTime":42,"videoSessionId":"nx54o66tzywcx35y-fb52cf79925c2bbce56c6fad42b80724242579185a842f2ca669685a50dafbdde26001d203aedd48-%s-559865"},"channel":"PCMac","orientation":"landscape"}}}))%self.x
        time.sleep(0.1)
        wss.send(json.dumps({"log":{"type":"CLIENT_PRESSED_START_VIDEO","value":{"sessionData":{"game":"roulette","videoSessionId":"nx54o66tzywcx35y-fb52cf79925c2bbce56c6fad42b80724242579185a842f2ca669685a50dafbdde26001d203aedd48-%s-559865"},"channel":"PCMac","pressedStart":true,"orientation":"landscape"}}}))%self.x
        time.sleep(0.1)
        result =  wss.recv()
        #print(result)
        #print("aaaaadddddddddddddddd")
        wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
        time.sleep(0.1)
        result =  ws.recv()
        #print(result)
        time.sleep(0.1)
        result =  wss.recv()
        #print(result)
        #print("asssssssssssssssssdddddd")
        wss.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
        time.sleep(0.1)
        result =  wss.recv()
        #print(result)
        time.sleep(0.1)
        result =  wss.recv()
        #print(result)
        #print("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")
        wss.send(json.dumps({"log":{"type":"CLIENT_VIDEO_V2_FIRST_FRAME","value":{"logic":{"currentPlayer":"flvjs"},"video":{"streamHost":"seoa-wow-e01.egcvi.com"},"client":{"pointInTime":1970,"videoSessionId":"nx54o66tzywcx35y-fb52cf79925c2bbce56c6fad42b80724242579185a842f2ca669685a50dafbdde26001d203aedd48-%s-559865"},"metrics":{"timeToVideo":1928},"channel":"PCMac","orientation":"landscape"}}}))%self.x
        time.sleep(0.1)
        wss.send(json.dumps({"log":{"type":"CLIENT_VIDEO_LOADING_TIME","value":{"timestamp":tt(),"deviceType":"desktop","qualityType":"MEDIUM","streamName":"immersive_med","videoInitTime":1932,"sessionData":{"game":"roulette","videoSessionId":"nx54o66tzywcx35y-fb52cf79925c2bbce56c6fad42b80724242579185a842f2ca669685a50dafbdde26001d203aedd48-%s-559865"},"channel":"PCMac","orientation":"landscape"}}}))%self.x
        time.sleep(0.1)
        wss.send(json.dumps({"log":{"type":"CLIENT_VIDEO_HANDSHAKE","value":{"sessionData":{"game":"roulette","videoSessionId":"nx54o66tzywcx35y-fb52cf79925c2bbce56c6fad42b80724242579185a842f2ca669685a50dafbdde26001d203aedd48-%s-559865"},"systemInfo":{"timestamp":tt(),"systemLanguage":"ko","deviceType":"desktop","videoPlayerName":"flvjs","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36","deviceName":"unknown","os":"Windows 10.0","browser":"Chrome 78.0.3904.108","pixelAspectRatio":1.25,"videoSettingsVersion":"","videoSettingsLogic":""},"channel":"PCMac","orientation":"landscape"}}}))%self.x
        time.sleep(0.1)
        wss.send(json.dumps({"log":{"type":"CLIENT_VIDEO_PLAYBACK_EVENT","value":{"playbackEventData":{"timestamp":tt(),"playbackEventType":"PLAYER_STARTED","data":{"playerEventHistory":"flvjs","firstVideoSessionId":"nx54o66tzywcx35y-fb52cf79925c2bbce56c6fad42b80724242579185a842f2ca669685a50dafbdde26001d203aedd48-%s-559865"},"reason":"PLAYER_STARTED"},"sessionData":{"game":"roulette","videoSessionId":"nx54o66tzywcx35y-fb52cf79925c2bbce56c6fad42b80724242579185a842f2ca669685a50dafbdde26001d203aedd48-%s-559865"},"channel":"PCMac","orientation":"landscape"}}}))%(self.x,self.x)
        time.sleep(0.1)
        result =  wss.recv()
        #print(result)
        time.sleep(0.1)
        result =  wss.recv()
        #print(result)
        #print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        wss.send(json.dumps({"log":{"type":"CLIENT_VIDEO_PLAYBACK_EVENT","value":{"playbackEventData":{"timestamp":tt(),"playbackEventType":"UPGRADE","data":{"prev":"MEDIUM","next":"HIGH","playerEventHistory":"flvjs","firstVideoSessionId":"nx54o66tzywcx35y-fb52cf79925c2bbce56c6fad42b80724242579185a842f2ca669685a50dafbdde26001d203aedd48-%s-559865"},"reason":"SUFFICIENT_BANDWIDTH"},"sessionData":{"game":"roulette","videoSessionId":"nx54o66tzywcx35y-fb52cf79925c2bbce56c6fad42b80724242579185a842f2ca669685a50dafbdde26001d203aedd48-%s-559865"},"channel":"PCMac","orientation":"landscape"}}}))%(self.x,self.x)
        time.sleep(0.1)
        wss.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
        time.sleep(0.1)
        result =  wss.recv()
        #print(result)
        time.sleep(0.1)
        result =  wss.recv()
        #print(result)
        #print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        wss.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
        time.sleep(0.1)
        result =  wss.recv()
        #print(result)
        #print("OOOOOOOOOOOOOOOOOOOOOOOOOOO")
        wss.send(json.dumps({"log":{"type":"CLIENT_APP_LOADING_TIME_V2","value":{"version":7,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36","game":"roulette","device":"desktop","build":"6.20191121.111140-2c066ecb","waitForVideo":false,"entries":{"navigation":[{"name":{"href":"https://livecasino.eg88play.com/mobile/#game=live-casino-custom-build-flash","hostname":"livecasino.eg88play.com","pathname":"/mobile/"},"duration":3890.115,"initiatorType":"navigation","nextHopProtocol":"","redirectStart":8.675,"redirectEnd":1900.25,"fetchStart":1900.25,"domainLookupStart":1900.25,"domainLookupEnd":1900.25,"connectStart":1900.25,"connectEnd":1900.25,"secureConnectionStart":1900.25,"requestStart":1906.025,"responseStart":2195.765,"responseEnd":2205.075,"transferSize":1506,"encodedBodySize":43835,"decodedBodySize":177606,"domInteractive":2341.355,"domContentLoadedEventStart":2341.6,"domContentLoadedEventEnd":2341.625,"domComplete":3889.255,"loadEventStart":3889.47,"loadEventEnd":3890.115,"type":"navigate","redirectCount":3}],"paint":[{"name":"first-paint","startTime":2290.6},{"name":"first-contentful-paint","startTime":2890.1}],"first-input":[{"name":"mousedown","startTime":84324.195,"duration":16,"processingStart":84325.175,"processingEnd":84325.565,"cancelable":true}],"mark":[{"name":"evoAppSwitchStarted","startTime":96500.01},{"name":"socketOpen","startTime":100099.12},{"name":"socketOpen","startTime":101008.02},{"name":"evoLoaderClosed","startTime":103085.795},{"name":"evoVideoPlaying","startTime":105009.31},{"name":"_evoReportGenerated","startTime":118087.245}],"resource":[{"name":{"href":"https://livecasino.eg88play.com/config?table_id=%s","hostname":"livecasino.eg88play.com","pathname":"/config"},"startTime":96930.9,"duration":1586.435,"initiatorType":"fetch","nextHopProtocol":"http/1.1","fetchStart":96930.9,"domainLookupStart":96935.185,"domainLookupEnd":96935.855,"connectStart":96935.855,"connectEnd":97722.655,"secureConnectionStart":97325.035,"requestStart":97722.74,"responseStart":98130.06,"responseEnd":98517.335,"transferSize":5243,"encodedBodySize":5043,"decodedBodySize":5043},{"name":{"href":"https://static.egcdn.com/mobile/js/desktopRoulette.e1829.js","hostname":"static.egcdn.com","pathname":"/mobile/js/desktopRoulette.js"},"startTime":98521.345,"duration":72.295,"initiatorType":"script","nextHopProtocol":"h2","fetchStart":98521.345,"responseEnd":98593.64,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/desktopRoulette.e1829.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/desktopRoulette.css"},"startTime":98522.04,"duration":70.45,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":98522.04,"responseEnd":98592.49,"transferSize":0},{"name":{"href":"https://static.egcdn.com/game-brandings/immersive-roulette_ro_loading-screen.a17da8f.jpg","hostname":"static.egcdn.com","pathname":"/game-brandings/immersive-roulette_ro_loading-screen.a17da8f.jpg"},"startTime":98523.375,"duration":4.38,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":98523.375,"responseEnd":98527.755,"transferSize":0},{"name":{"href":"https://livecasino.eg88play.com/api/player/screenName","hostname":"livecasino.eg88play.com","pathname":"/api/player/screenName"},"startTime":98877.575,"duration":393.03,"initiatorType":"fetch","nextHopProtocol":"http/1.1","fetchStart":98877.575,"domainLookupStart":98877.575,"domainLookupEnd":98877.575,"connectStart":98877.575,"connectEnd":98877.575,"secureConnectionStart":98877.575,"requestStart":98879.06,"responseStart":99269.17,"responseEnd":99270.605,"transferSize":224,"encodedBodySize":23,"decodedBodySize":23},{"name":{"href":"https://static.egcdn.com/mobile/js/singleBallStandardLandscape.grid.b1c5b.js","hostname":"static.egcdn.com","pathname":"/mobile/js/singleBallStandardLandscape.grid.js"},"startTime":98881.645,"duration":5.925,"initiatorType":"script","nextHopProtocol":"h2","fetchStart":98881.645,"responseEnd":98887.57,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/singleBallSpecialLandscape.grid.62b6a.js","hostname":"static.egcdn.com","pathname":"/mobile/js/singleBallSpecialLandscape.grid.js"},"startTime":98882.71,"duration":5.175,"initiatorType":"script","nextHopProtocol":"h2","fetchStart":98882.71,"responseEnd":98887.885,"transferSize":0},{"name":{"href":"https://livecasino.eg88play.com/mobile/#category=roulette&game=roulette","hostname":"livecasino.eg88play.com","pathname":"/mobile/"},"startTime":102723.26,"duration":1403.225,"initiatorType":"iframe","nextHopProtocol":"","fetchStart":102723.26,"domainLookupStart":102723.26,"domainLookupEnd":102723.26,"connectStart":102723.26,"connectEnd":102723.26,"secureConnectionStart":102723.26,"requestStart":102729.96,"responseStart":104122.85,"responseEnd":104126.485,"transferSize":310,"encodedBodySize":43835,"decodedBodySize":177606},{"name":{"href":"https://static.egcdn.com/mobile/images/TotalBetBackground.213e6.svg","hostname":"static.egcdn.com","pathname":"/mobile/images/TotalBetBackground.svg"},"startTime":102917.585,"duration":1.655,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":102917.585,"responseEnd":102919.24,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/fonts/AvenirNextCyr-Demi.19191.woff2","hostname":"static.egcdn.com","pathname":"/mobile/fonts/AvenirNextCyr-Demi.woff2"},"startTime":102920.98,"duration":2.435,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":102920.98,"responseEnd":102923.415,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/assets/sounds/undo.33b28.mp3","hostname":"static.egcdn.com","pathname":"/mobile/assets/sounds/undo.mp3"},"startTime":103005.665,"duration":2.14,"initiatorType":"xmlhttprequest","nextHopProtocol":"h2","fetchStart":103005.665,"responseEnd":103007.805,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/assets/sounds/repeatDouble.108c2.mp3","hostname":"static.egcdn.com","pathname":"/mobile/assets/sounds/repeatDouble.mp3"},"startTime":103006.77,"duration":2.55,"initiatorType":"xmlhttprequest","nextHopProtocol":"h2","fetchStart":103006.77,"responseEnd":103009.32,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/assets/sounds/openPopup.13714.mp3","hostname":"static.egcdn.com","pathname":"/mobile/assets/sounds/openPopup.mp3"},"startTime":103008.265,"duration":3.41,"initiatorType":"xmlhttprequest","nextHopProtocol":"h2","fetchStart":103008.265,"responseEnd":103011.675,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/assets/sounds/startAutoPlay.c578e.mp3","hostname":"static.egcdn.com","pathname":"/mobile/assets/sounds/startAutoPlay.mp3"},"startTime":103009.73,"duration":4.25,"initiatorType":"xmlhttprequest","nextHopProtocol":"h2","fetchStart":103009.73,"responseEnd":103013.98,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/assets/sounds/selectChip.1dede.mp3","hostname":"static.egcdn.com","pathname":"/mobile/assets/sounds/selectChip.mp3"},"startTime":103011.18,"duration":3.705,"initiatorType":"xmlhttprequest","nextHopProtocol":"h2","fetchStart":103011.18,"responseEnd":103014.885,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/assets/sounds/clickingFail.4b8c6.mp3","hostname":"static.egcdn.com","pathname":"/mobile/assets/sounds/clickingFail.mp3"},"startTime":103012.97,"duration":3.92,"initiatorType":"xmlhttprequest","nextHopProtocol":"h2","fetchStart":103012.97,"responseEnd":103016.89,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/assets/sounds/clickUIButton.cdbdb.mp3","hostname":"static.egcdn.com","pathname":"/mobile/assets/sounds/clickUIButton.mp3"},"startTime":103014.445,"duration":3.43,"initiatorType":"xmlhttprequest","nextHopProtocol":"h2","fetchStart":103014.445,"responseEnd":103017.875,"transferSize":0},{"name":{"href":"https://livecasino.eg88play.com/player/games/assets/ui3.0_audio/audio/clickingFail.mp3","hostname":"livecasino.eg88play.com","pathname":"/player/games/assets/ui3.0_audio/audio/clickingFail.mp3"},"startTime":103015.955,"duration":3.725,"initiatorType":"xmlhttprequest","nextHopProtocol":"","fetchStart":103015.955,"domainLookupStart":103015.955,"domainLookupEnd":103015.955,"connectStart":103015.955,"connectEnd":103015.955,"requestStart":103017.29,"responseStart":103017.955,"responseEnd":103019.68,"transferSize":0,"encodedBodySize":20106,"decodedBodySize":20106},{"name":{"href":"https://lob.egcvi.com/thumbnail/immersive_med_L.jpg?q=1574773898316","hostname":"lob.egcvi.com","pathname":"/thumbnail/immersive_med_L.jpg"},"startTime":103030.005,"duration":1182.685,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":103030.005,"responseEnd":104212.69,"transferSize":0},{"name":{"href":"https://static.egcdn.com/game-brandings/immersivelive3_ro_logo.4261eb0.png","hostname":"static.egcdn.com","pathname":"/game-brandings/immersivelive3_ro_logo.4261eb0.png"},"startTime":103030.255,"duration":2.42,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":103030.255,"responseEnd":103032.675,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/sbr_wheel_dark.49126.png","hostname":"static.egcdn.com","pathname":"/mobile/images/sbr_wheel_dark.png"},"startTime":103032.365,"duration":2.69,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":103032.365,"responseEnd":103035.055,"transferSize":0},{"name":{"href":"https://a-fds.youborafds01.com/data?apiVersion=v7&outputformat=json&system=evolutiongaming&pluginVersion=6.5.18-adapterless&requestNumber=0.535164910563872&username=nx54o66tzywcx35y&timemark=1574773898624","hostname":"a-fds.youborafds01.com","pathname":"/data"},"startTime":103044.16,"duration":1119.57,"initiatorType":"xmlhttprequest","nextHopProtocol":"http/1.1","fetchStart":103044.16,"responseEnd":104163.73,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/fonts/evo-mobile.a5517.woff2","hostname":"static.egcdn.com","pathname":"/mobile/fonts/evo-mobile.woff2"},"startTime":103117.995,"duration":1.97,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":103117.995,"responseEnd":103119.965,"transferSize":0},{"name":{"href":"https://live1.egcvi.com/cdn/app/10/amlst:immersive_auto/manifest-ws.json?videoSessionId=***&videoToken=eyJraWQiOiJsaXZlMTAxIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJpbW1lcnNpdmUiLCJleHAiOjE1NzQ3NzQxNDZ9.E_AIIzrYj2SJ51zginqvwpdKc5wjP3CCueKzL8EGpml1QSCG2tg_7aII9H8sabSk_HQ8S9JjADQYvRI5q2JFyBoLuvmtqi6pFvb4pOx5sC6igaIaBiijQ8z2dURXJ-flSQFUF8LrVTMdBFTQhzDlKI0VykoA0vY_uwYZhuJin6iWorr94L5mRA-uGHkV_12BJgBu6qkE2rY0HAqbosIsoalLSInggXH3xdgft0bIIQ-ickoU6FjIfLs7bqO5haU_g1gcA_O8PaVBEZM6mzsNEUyGEN9SI-7P-2CxRj1CkvZaM6TLBC2yPcX1p7VpkBxSA91o0usNaaBTI9RREJ7q_Q","hostname":"live1.egcvi.com","pathname":"/cdn/app/10/amlst:immersive_auto/manifest-ws.json"},"startTime":103196.5,"duration":18.82,"initiatorType":"fetch","nextHopProtocol":"h2","fetchStart":103196.5,"responseEnd":103215.32,"transferSize":0},{"name":{"href":"https://infinity-c8.youboranqs01.com/infinity/session/start?accountCode=evolutiongaming&username=nx54o66tzywcx35y&navContext=Default&route=https%3A%2F%2Flivecasino.eg88play.com%2Fmobile%2F%23table_id%3D%s%26category%3Droulette%26game%3Droulette&page=Live%20Casino%3A%20%EC%9D%B4%EB%A8%B8%EC%A7%80%EB%B8%8C%20%EB%A3%B0%EB%A0%9B&referer=https%3A%2F%2Flivecasino.eg88play.com%2Fmobile%2F%23table_id%3D%s%26category%3Droulette%26game%3Droulette&referral=https%3A%2F%2Fkobet-1.com%2FHome%2FIndex&language=ko-KR&deviceUUID=7c11387b18d4ab46ece0ac965bd86581&libVersion=6.5.18&timemark=1574773898626&system=evolutiongaming&sessionRoot=U_20000777_3ikocvi42qyqqiby&sessionId=***","hostname":"infinity-c8.youboranqs01.com","pathname":"/infinity/session/start"},"startTime":104196.615,"duration":266.05,"initiatorType":"xmlhttprequest","nextHopProtocol":"h2","fetchStart":104196.615,"responseEnd":104462.665,"transferSize":0},{"name":{"href":"https://infinity-c8.youboranqs01.com/infinity/session/event?name=onVolumeChange&dimensions=%7B%22volume%22%3A%221.00%22%7D&accountCode=evolutiongaming&navContext=Default&timemark=1574773899156&system=evolutiongaming&sessionRoot=U_20000777_3ikocvi42qyqqiby&sessionId=***","hostname":"infinity-c8.youboranqs01.com","pathname":"/infinity/session/event"},"startTime":104197.865,"duration":266.665,"initiatorType":"xmlhttprequest","nextHopProtocol":"h2","fetchStart":104197.865,"responseEnd":104464.53,"transferSize":0},{"name":{"href":"https://infinity-c8.youboranqs01.com/start?accountCode=evolutiongaming&username=nx54o66tzywcx35y&rendition=MEDIUM&player=evo-video-components&title=%s&live=true&mediaResource=https%3A%2F%2Flive1.egcvi.com%2Fcdn%2Fapp%2F10%2Famlst%3Aimmersive_auto%2Fmanifest-ws.json%3FvideoSessionId%3D***%26videoToken%3DeyJraWQiOiJsaXZlMTAxIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJpbW1lcnNpdmUiLCJleHAiOjE1NzQ3NzQxNDZ9.E_AIIzrYj2SJ51zginqvwpdKc5wjP3CCueKzL8EGpml1QSCG2tg_7aII9H8sabSk_HQ8S9JjADQYvRI5q2JFyBoLuvmtqi6pFvb4pOx5sC6igaIaBiijQ8z2dURXJ-flSQFUF8LrVTMdBFTQhzDlKI0VykoA0vY_uwYZhuJin6iWorr94L5mRA-uGHkV_12BJgBu6qkE2rY0HAqbosIsoalLSInggXH3xdgft0bIIQ-ickoU6FjIfLs7bqO5haU_g1gcA_O8PaVBEZM6mzsNEUyGEN9SI-7P-2CxRj1CkvZaM6TLBC2yPcX1p7VpkBxSA91o0usNaaBTI9RREJ7q_Q&properties=%7B%22cast%22%3A%22FLVJS%22%7D&cdn=WOWZACDN&playerVersion=v5.132.8_5.20191125.114720_28dda211&param1=totogaming000002&param2=roulette&param3=nx54o66tzywcx35y_%s_fb52cf79925c2bbce56c6fad42b80724242579185a842f2ca669685a50dafbdde26001d203aedd48&param8=undefined&obfuscateIp=false&pluginVersion=6.5.4-html5-js&pluginInfo=%7B%22lib%22%3A%226.5.18%22%2C%22adapter%22%3A%226.5.4-html5-js%22%2C%22adAdapter%22%3Anull%7D&referer=https%3A%2F%2Flivecasino.eg88play.com%2Fmobile%2F%23table_id%3D%s%26category%3Droulette%26game%3Droulette&streamingProtocol=FLVJS&adsExpected=false&deviceUUID=7c11387b18d4ab46ece0ac965bd86581&libVersion=6.5.18&playbackType=Live&timemark=1574773899204&parsedResource=https%3A%2F%2Flive1.egcvi.com%2Fcdn%2Fapp%2F10%2Famlst%3Aimmersive_auto%2Fmanifest-ws.json%3FvideoSessionId%3D***%26videoToken%3DeyJraWQiOiJsaXZlMTAxIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJpbW1lcnNpdmUiLCJleHAiOjE1NzQ3NzQxNDZ9.E_AIIzrYj2SJ51zginqvwpdKc5wjP3CCueKzL8EGpml1QSCG2tg_7aII9H8sabSk_HQ8S9JjADQYvRI5q2JFyBoLuvmtqi6pFvb4pOx5sC6igaIaBiijQ8z2dURXJ-flSQFUF8LrVTMdBFTQhzDlKI0VykoA0vY_uwYZhuJin6iWorr94L5mRA-uGHkV_12BJgBu6qkE2rY0HAqbosIsoalLSInggXH3xdgft0bIIQ-ickoU6FjIfLs7bqO5haU_g1gcA_O8PaVBEZM6mzsNEUyGEN9SI-7P-2CxRj1CkvZaM6TLBC2yPcX1p7VpkBxSA91o0usNaaBTI9RREJ7q_Q&system=evolutiongaming&sessionRoot=U_20000777_3ikocvi42qyqqiby&pingTime=10&code=U_20000777_3ikocvi42qyqqiby_1574773899202&parentId=U_20000777_3ikocvi42qyqqiby&navContext=Default","hostname":"infinity-c8.youboranqs01.com","pathname":"/start"},"startTime":104199.805,"duration":266.875,"initiatorType":"xmlhttprequest","nextHopProtocol":"h2","fetchStart":104199.805,"responseEnd":104466.68,"transferSize":0},{"name":{"href":"https://infinity-c8.youboranqs01.com/joinTime?joinDuration=1629&timemark=1574773900832&system=evolutiongaming&sessionRoot=U_20000777_3ikocvi42qyqqiby&code=U_20000777_3ikocvi42qyqqiby_1574773899202","hostname":"infinity-c8.youboranqs01.com","pathname":"/joinTime"},"startTime":105253.485,"duration":273.415,"initiatorType":"xmlhttprequest","nextHopProtocol":"h2","fetchStart":105253.485,"responseEnd":105526.9,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/fonts/AvenirNextCyr-Bold.ca116.woff2","hostname":"static.egcdn.com","pathname":"/mobile/fonts/AvenirNextCyr-Bold.woff2"},"startTime":107070.695,"duration":2.985,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":107070.695,"responseEnd":107073.68,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/sprite.6dd6f.png","hostname":"static.egcdn.com","pathname":"/mobile/images/sprite.png"},"startTime":107090.21,"duration":2.34,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":107090.21,"responseEnd":107092.55,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/dolly.e42e9.svg","hostname":"static.egcdn.com","pathname":"/mobile/images/dolly.svg"},"startTime":107090.72,"duration":2.52,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":107090.72,"responseEnd":107093.24,"transferSize":0},{"name":{"href":"https://infinity-c8.youboranqs01.com/ping?diffTime=5001&entities=%7B%22rendition%22%3A%22HIGH%22%2C%22param5%22%3A%22seoa-wow-e01.egcvi.com%22%7D&bitrate=365025&throughput=20662649&droppedFrames=6&playrate=1&latency=1962&timemark=1574773904205&system=evolutiongaming&sessionRoot=U_20000777_3ikocvi42qyqqiby&pingTime=10&code=U_20000777_3ikocvi42qyqqiby_1574773899202","hostname":"infinity-c8.youboranqs01.com","pathname":"/ping"},"startTime":108624.82,"duration":279.545,"initiatorType":"xmlhttprequest","nextHopProtocol":"h2","fetchStart":108624.82,"responseEnd":108904.365,"transferSize":0}]},"evoAppSwitchStarted":96500.01,"evoLoaderClosed":6585.785,"evoVideoPlaying":8509.3}}}))%(self.x,self.x,self.x,self.x,self.x,self.x)
        time.sleep(0.1)
        wss.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
        time.sleep(0.1)
        result =  wss.recv()
        
    def Room500:
        for op in range(len(self.dataa['args']['recentResults'])):
            self.nm2.append(int(self.dataa['args']['recentResults'][op][0]))
            self.nm2.reverse()
            print(self.nm2)
            for Cmn2 in range(len(nm2)):
                self.Cmns2 = int(self.nm2[Cmn2])
                self.Countnumber(self.Cmns2)

    def BetingTime(self):
        self.TTa = False
        while self.TTa == False:
            if self.UI == 1:
                self.B = bet_even
                self.D = ROU_Even
            else:
                pass
            if self.UI == 2:
                self.B = bet_black
                self.D = ROU_Black
            else:
                pass
            if self.UI == 3:
                self.B = bet_from1to18
                self.D = ROU_118
            else:
                pass
            if self.x == "LightningTable01":#라이트링 룰렛 48  B= bet_black D = ROU_Black  E = 남은 돈
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":200,"type":"%s","chips":"200@%s","codes":{"%s":200},"balance":self.E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[200,1000,4000,20000,100000,400000],"defaultChip":1,"tableMinLimit":200,"tableMaxLimit":2000000,"channel":"PCMac","orientation":"landscape"}}}))%(self.B,self.B,self.D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":200}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"lightr1_imr_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "7x0b1tgh7agmf6hv":#이머징 룰렛
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":1000,"type":"%s","chips":"1000@%s","codes":{"%s":1000},"balance":self.E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[1000,2000,10000,20000,1000000,2000000],"defaultChip":1,"tableMinLimit":1000,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(self.B,self.B,self.D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":1000}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"immersive_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "vctlz20yfnmp1ylr": #룰렛
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":400,"type":"%s","chips":"400@%s","codes":{"%s":400},"balance":self.E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[400,800,2000,10000,20000,1000000],"defaultChip":1,"tableMinLimit":400,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(self.B,self.B,self.D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":400}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"green_imr_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "r5aw9yumyaxgnd90" :#터키 룰렛
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":1000,"type":"%s","chips":"1000@%s","codes":{"%s":1000},"balance":self.E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[1000,2000,5000,25000,100000,500000],"defaultChip":1,"tableMinLimit":1000,"tableMaxLimit":2000000,"channel":"PCMac","orientation":"landscape"}}}))%(self.B,self.B,self.D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":1000}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"tk2_imr_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "zosmk25g2f768o52" : #룰렛 라이브
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":800,"type":"%s","chips":"800@%s","codes":{"%s":800},"balance":self.E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[800,2000,10000,20000,1000000,2000000],"defaultChip":1,"tableMinLimit":800,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(self.B,self.B,self.D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":800}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"rugent1_imr_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "48z5pjps3ntvqc1b" : #오토 룰렛
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":160,"type":"%s","chips":"160@%s","codes":{"%s":160},"balance":self.E,"viewType":"Slingshot","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[160,1000,4000,20000,100000,400000],"defaultChip":1,"tableMinLimit":160,"tableMaxLimit":2000000,"channel":"PCMac","orientation":"landscape"}}}))%(self.B,self.B,self.D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":160}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"slingshot","btVideoQuality":"gen1_ss_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"id":self.wid(),"type":"metrics.ping","args":{"t":self.tt()}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "01rb77cq1gtenhmo" : #vip 오토 룰렛
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":300,"type":"%s","chips":"300@%s","codes":{"%s":300},"balance":self.E,"viewType":"Slingshot","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[300,1000,2000,10000,20000,1000000],"defaultChip":1,"tableMinLimit":300,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(self.B,self.B,self.D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":300}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"slingshot","btVideoQuality":"vip1_ss_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                #wss.send(json.dumps(
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "f1f4rm9xgh4j3u2z" : #라 팔타지 자동 룰렛 french_bet_black
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":160,"type":"french_%s","chips":"160@french_%s","codes":{"%s50ReturnOn0":160},"balance":self.E,"viewType":"Slingshot","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[160,1000,4000,20000,100000,400000],"defaultChip":1,"tableMinLimit":160,"tableMaxLimit":2000000,"channel":"PCMac","orientation":"landscape"}}}))%(self.B,self.B,self.D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"162":160}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"slingshot","btVideoQuality":"spa_ss_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                #wss.send(json.dumps(
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "q0a470up68p2b81p" : #드라고나 룰렛
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":1000,"type":"%s","chips":"1000@%s","codes":{"%s":1000},"balance":self.E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[1000,2000,10000,20000,1000000,2000000],"defaultChip":1,"tableMinLimit":1000,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(self.B,self.B,self.D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":1000}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"drago_imr_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "lkcbrbdckjxajdol" : #스피드 룰렛
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":1000,"type":"%s","chips":"1000@%s","codes":{"%s":1000},"balance":self.E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[500,1000,2000,10000,20000,1000000],"defaultChip":2,"tableMinLimit":500,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(self.B,self.B,self.D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":1000}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"speed1_imr_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "lr6t4k3lcd4qgyrk" : #그랜드 카지노 룰렛
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":1000,"type":"%s","chips":"1000@%s","codes":{"%s":1000},"balance":self.E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[1000,2000,10000,20000,1000000,2000000],"defaultChip":1,"tableMinLimit":1000,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(self.B,self.B,self.D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":1000}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"gcro1_imr_med","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "AmericanTable001":#아메리칸 룰렛 D = RoDZ_Black
                if self.UI == 1:
                    self.B = bet_even
                    self.D = RoDZ_Even
                else:
                    pass
                if self.UI == 2:
                    self.B = bet_black
                    self.D = RoDZ_Black
                else:
                    pass
                if self.UI == 3:
                    self.B = bet_from1to18
                    self.D = RoDZ_118
                else:
                    pass
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":1000,"type":"%s","chips":"1000@%s","codes":{"%s":1000},"balance":self.E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"americanroulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[200,1000,2000,10000,20000,1000000],"defaultChip":2,"tableMinLimit":200,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(self.B,self.B,self.D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"408":1000}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"dzerot1_imr_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "mvrcophqscoqosd6": #카지노 몰타 룰렛
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":1000,"type":"%s","chips":"1000@%s","codes":{"%s":1000},"balance":self.E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[1000,2000,10000,20000,1000000,2000000],"defaultChip":1,"tableMinLimit":1000,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(self.B,self.B,self.D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":1000}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"casmlt1_imr_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "m2ghpkmua5jarg4t": #Resorts Atlantic City D = RoDZ_Black
                if self.UI == 1:
                    self.B = bet_even
                    self.D = RoDZ_Even
                else:
                    pass
                if self.UI == 2:
                    self.B = bet_black
                    self.D = RoDZ_Black
                else:
                    pass
                if self.UI == 3:
                    self.B = bet_from1to18
                    self.D = RoDZ_118
                else:
                    pass
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":1000,"type":"%s","chips":"1000@%s","codes":{"%s":1000},"balance":self.E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"americanroulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[1000,2000,10000,20000,1000000,2000000],"defaultChip":1,"tableMinLimit":1000,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(self.B,self.B,self.D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"408":1000}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"rcac1_imr_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
                        

head1 = '''Host: kobet-1.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36
Sec-Fetch-Mode: navigate
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Sec-Fetch-Site: none
Accept-Encoding: gzip, deflate
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'''

head2 = '''Host: kobet-1.com
Connection: keep-alive
Accept: */*
Origin: https://kobet-1.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36
Sec-Fetch-Mode: cors
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Sec-Fetch-Site: same-origin
Referer: https://kobet-1.com/Home/Index
Accept-Encoding: gzip, deflate
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
'''
head3 = '''Host: kobet-1.com
Connection: keep-alive
Accept: */*
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36
Sec-Fetch-Mode: cors
Content-Type: application/json; charset=utf-8
Sec-Fetch-Site: same-origin
Referer: https://kobet-1.com/ko/
Accept-Encoding: gzip, deflate
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
'''
head4 = '''Host: livecasino.eg88play.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36
Sec-Fetch-User: ?1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Referer: https://kobet-1.com/ko/Home/Index
Accept-Encoding: gzip, deflate, br
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
'''
head5 = '''Accept-Encoding: gzip, deflate
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
Upgrade-Insecure-Requests: 1
Sec-Fetch-User: ?1
Referer: https://kobet-1.com/ko/Home/Index
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: cross-site
Host: livecasino.eg88play.com
'''
wshead1 = '''Accept-Encoding: gzip, deflate
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
Cache-Control: no-cache
Connection: Upgrade
Host: livecasino.eg88play.com
Origin: https://livecasino.eg88play.com
Pragma: no-cache
Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits
Sec-WebSocket-Version: 13
Upgrade: websocket
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36
'''
wshead2 = '''Host: livecasino.eg88play.com
Connection: Upgrade
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
Upgrade: websocket
Origin: https://livecasino.eg88play.com
Sec-WebSocket-Version: 13
Accept-Encoding: gzip, deflate, br
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits
'''
data = 'GameName=&Email=can741&Password=1q2w3e4r!!'
addr1 = 'https://kobet-1.com/Mobile/IsMobile?IsMobile=true'
addr2 = 'https://kobet-1.com/ko/Login/Login'
addr3 = 'https://kobet-1.com/LiveCasino/GetLiveCasinoUrl?url='
browser = mechanicalsoup.StatefulBrowser()

x = 1


with requests.session() as sess:
    r1 = sess.get(addr1, headers=pharseHeaders(head1), verify=False)
    if r1.status_code == 200:
        r2 = sess.post(addr2, verify=False, headers=pharseHeaders(head2), data=data.encode())
        if r2.status_code == 200:
            r3 = sess.get(addr3, headers=pharseHeaders(head3), verify=False)
            if r3.status_code == 200:
                addr4 = json.loads(r3.content.decode())["Message"]
                r4 = sess.get(addr4, headers=pharseHeaders(head4), verify=False)
                r = browser.get(addr4, verify=False, headers=pharseHeaders(head4))

                sessionId = str(browser.get_cookiejar()["EVOSESSIONID"])
                ws = create_connection("wss://livecasino.eg88play.com/public/lobby/player/socket?messageFormat=json&EVOSESSIONID="+sessionId, headers = pharseHeaders(wshead1))
                
                KB0 = KoBet(ws,"라이트닝 룰렛",1,x,"LightningTable01",sessionId,wshead2)
                KB1 = KoBet(ws,"이머지브 룰렛",1,x,"7x0b1tgh7agmf6hv",sessionId,wshead2)
                KB2 = KoBet(ws,"룰렛",2,x,"vctlz20yfnmp1ylr",sessionId,wshead2)
                KB3 = KoBet(ws,"터키 룰렛",3,x,"r5aw9yumyaxgnd90",sessionId,wshead2)
                KB4 = KoBet(ws,"룰렛 라이브",4,x,"zosmk25g2f768o52",sessionId,wshead2)
                KB7 = KoBet(ws,"오토 룰렛",7,x,"48z5pjps3ntvqc1b",sessionId,wshead2)
                KB8 = KoBet(ws,"VIP 오토 룰렛",8,x,"01rb77cq1gtenhmo",sessionId,wshead2)
                KB9 = KoBet(ws,"라 팔타지 자동 룰렛",9,x,"f1f4rm9xgh4j3u2z",sessionId,wshead2)
                KB10 = KoBet(ws,"드라고나 룰렛",10,x,"q0a470up68p2b81p",sessionId,wshead2)
                KB12 = KoBet(ws,"스피드 룰렛",12,x,"lkcbrbdckjxajdol",sessionId,wshead2)
                KB13 = KoBet(ws,"그랜드 카지노 룰렛",13,x,"lr6t4k3lcd4qgyrk",sessionId,wshead2)
                KB14 = KoBet(ws,"아메리칸 룰렛",14,x,"AmericanTable001",sessionId,wshead2)
                KB15 = KoBet(ws,"카지노 몰타 룰렛",15,x,"mvrcophqscoqosd6",sessionId,wshead2)
                KB16 = KoBet(ws,"Resorts Atlantic City",16,x,"m2ghpkmua5jarg4t",sessionId,wshead2)
                List = (KB0,KB1,KB2,KB3,KB4,KB7,KB8,KB9,KB10,KB12,KB13,KB14,KB15,KB16)
    while True: 
        
        ws.send(json.dumps({"id":wid(),"type":"lobby.updateSubscriptions","args":{"subscribeTopics":[{"topic":"lobby","game":"live-casino-custom-build-flash"}],"unsubscribeTopics":[]}}))
        ws.send(json.dumps({"id":wid(),"type":"settings.read","args":{"key":"lobby.common"}}))
        ws.send(json.dumps({"id":wid(),"type":"settings.read","args":{"key":"generic.mobile"}}))
        ws.send(json.dumps({"id":wid(),"type":"settings.read","args":{"key":"generic.common"}}))
        ws.send(json.dumps({"id":wid(),"type":"settings.read","args":{"key":"lobby.common"}}))
        ws.send(json.dumps({"id":wid(),"type":"settings.read","args":{"key":"roulette.common"}}))
        for i in range(9):
            result =  ws.recv()
        ws.send(json.dumps({"log":{"type":"CLIENT_SOCKET_CONNECTION_ESTABLISHED","latency":-1,"value":{"currency":"KRW","gameType":"lobby","channel":"PCMac","orientation":"landscape","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36","inGame":false}}}))
        result =  ws.recv()
        ws.send(json.dumps({"log":{"type":"CLIENT_APP_LOADING_TIME","value":{"fastSwitching":false,"appLoading":tt(),"domInteractive":tt(),"appLoaded":tt(),"requestCDNDataStart":2211.8549999995594,"requestCDNDataSession":false,"requestSetupDataStart":2214.364999999816,"requestSetupDataSession":false,"requestSetupDataEnd":2604.910000000018,"requestSetupDataDuration":390.545000000202,"requestStyleDataStart":2215.1300000004994,"requestStyleDataSession":false,"requestStyleDataEnd":2604.090000000724,"requestStyleDataDuration":388.9600000002247,"requestI18nDataStart":2215.584999999919,"requestI18nDataSession":false,"requestI18nDataEnd":2606.2849999998434,"requestI18nDataDuration":390.69999999992433,"loadBundleCSSStart":2608.9150000007066,"loadBundleCSSEnd":2865.975000000617,"loadBundleCSSDuration":257.05999999991036,"loadGameBundleStart":2866.2750000003143,"loadGameBundleEnd":6351.850000000923,"loadGameBundleDuration":3485.5750000006083,"domInteractiveTime":1872,"domContentLoadedTime":null,"domLoadedTime":null,"appLoadedTime":4143,"typeApp":"lobby","timeLoading":4203,"device":"desktop","firstTimeLoad":false,"buildId":"Build Version: 6.20191028.110947-3f0961fa at 2019-10-28 11:39:57","wasLoadedOverCDN":true,"serviceWorker":true,"videoUpdate":false,"waitForVideo":false,"frameHeight":754.4000244140625,"frameWidth":636,"screenWidth":1536,"screenHeight":864,"currency":"KRW","gameType":"lobby","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36","inGame":false,"channel":"PCMac","orientation":"landscape"}}}))
        ws.send(json.dumps({"log":{"type":"CLIENT_GAME_LOADED","value":{"typeApp":"lobby","offline":true,"buildId":"Build Version: 6.20191028.110947-3f0961fa at 2019-10-28 11:39:57","currency":"KRW","gameType":"lobby","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36","inGame":false,"channel":"PCMac","orientation":"landscape"}}}))
        result =  ws.recv()
        dataM = json.loads(result)
        if dataM["type"] == "balanceUpdated":
            Money = int(self.dataM['args']['balance'])
        ws.send(json.dumps({"log":{"type":"CLIENT_BALANCE_UPDATED","value":{"currency":"KRW","balance":Money,"gameType":"lobby","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36","inGame":false,"channel":"PCMac","orientation":"landscape"}}}))
        ws.send(json.dumps({"id":wid(),"type":"lobby.updateSubscriptions","args":{"subscribeTopics":[{"topic":"table","tables":[{"tableId":"LightningTable01"},{"tableId":"vctlz20yfnmp1ylr"},{"tableId":"MOWDream00000001"},{"tableId":"7x0b1tgh7agmf6hv"},{"tableId":"HoldemTable00001"},{"tableId":"leqhceumaq6qfoug"},{"tableId":"TopCard000000001"}]}],"unsubscribeTopics":[]}}))
        result =  ws.recv()
        ws.send(json.dumps({"log":{"type":"CLIENT_LOBBY_CATEGORY_CHANGE","latency":-1,"value":{"currency":"KRW","gameType":"lobby","buildId":"Build Version: 6.20191028.110947-3f0961fa at 2019-10-28 11:39:57","device":"Desktop","typeApp":"lobby4","categoryId":"top_games","category":"top_games","previousCategory":null,"previousTablesCount":0,"timeInLobby":3210,"channel":"PCMac","orientation":"landscape","balance":Money,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36","inGame":false}}}))
        ws.send(json.dumps({"log":{"type":"CLIENT_BALANCE_UPDATED","latency":-1,"value":{"currency":"KRW","gameType":"lobby","buildId":"Build Version: 6.20191028.110947-3f0961fa at 2019-10-28 11:39:57","device":"Desktop","typeApp":"lobby4","categoryId":"top_games","timeInLobby":3288,"channel":"PCMac","orientation":"landscape","balance":Money,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36","inGame":false}}}))
        for i in range(9):
            result =  ws.recv()
        ws.send(json.dumps({"id":wid(),"type":"lobby.updateSubscriptions","args":{"subscribeTopics":[{"topic":"category","categoryId":"roulette","features":[]}],"unsubscribeTopics":[{"topic":"category","categoryId":"top_games","features":[]},{"topic":"table","tables":[{"tableId":"LightningTable01"},{"tableId":"vctlz20yfnmp1ylr"},{"tableId":"MOWDream00000001"},{"tableId":"7x0b1tgh7agmf6hv"},{"tableId":"HoldemTable00001"},{"tableId":"leqhceumaq6qfoug"},{"tableId":"TopCard000000001"}]}]}}))
        result =  ws.recv()
        ws.send(json.dumps({"log":{"type":"CLIENT_LOBBY_CATEGORY_CHANGE","latency":random.random(-200,500),"value":{"currency":"KRW","gameType":"lobby","buildId":"Build Version: 6.20191031.112952-9d0a9738 at 2019-10-31 12:07:40","device":"Desktop","typeApp":"lobby4","categoryId":"top_games","category":"roulette","previousCategory":"top_games","previousTablesCount":7,"timeInLobby":13181,"channel":"PCMac","orientation":"landscape","balance":Money,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36","inGame":false}}}))
        ws.send(json.dumps({"id":wid(),"type":"lobby.updateSubscriptions","args":{"subscribeTopics":[{"topic":"table","tables":[{"tableId":"LightningTable01"},{"tableId":"7x0b1tgh7agmf6hv"},{"tableId":"vctlz20yfnmp1ylr"},{"tableId":"r5aw9yumyaxgnd90"},{"tableId":"zosmk25g2f768o52"},{"tableId":"wzg6kdkad1oe7m5k"},{"tableId":"wzg6kdkad1oe7m5k","vtId":"979uwb2tdni7dmp4"}]}],"unsubscribeTopics":[]}}))
        result =  ws.recv()
        ws.send(json.dumps({"id":wid(),"type":"lobby.updateSubscriptions","args":{"subscribeTopics":[{"topic":"table","tables":[{"tableId":"48z5pjps3ntvqc1b"},{"tableId":"01rb77cq1gtenhmo"},{"tableId":"f1f4rm9xgh4j3u2z"},{"tableId":"q0a470up68p2b81p"},{"tableId":"DoubleBallRou001"},{"tableId":"lkcbrbdckjxajdol"},{"tableId":"lr6t4k3lcd4qgyrk"},{"tableId":"AmericanTable001"},{"tableId":"mvrcophqscoqosd6"}]}],"unsubscribeTopics":[]}}))
        ws.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
        ws.send(json.dumps({"log":{"type":"CLIENT_APP_LOADING_TIME_V2","value":{"version":7,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36","game":"lobby","device":"desktop","build":"6.20191031.112952-9d0a9738","waitForVideo":false,"entries":{"navigation":[{"name":{"href":"https://livecasino.eg88play.com/mobile/#game=live-casino-custom-build-flash","hostname":"livecasino.eg88play.com","pathname":"/mobile/"},"duration":470.57,"initiatorType":"navigation","nextHopProtocol":"","fetchStart":1.81,"domainLookupStart":1.81,"domainLookupEnd":1.81,"connectStart":1.81,"connectEnd":1.81,"requestStart":3.16,"responseStart":4.08,"responseEnd":7.625,"transferSize":0,"encodedBodySize":43676,"decodedBodySize":177057,"domInteractive":331.775,"domContentLoadedEventStart":331.825,"domContentLoadedEventEnd":331.825,"domComplete":470.505,"loadEventStart":470.515,"loadEventEnd":470.57,"type":"navigate"}],"paint":[{"name":"first-paint","startTime":141.53},{"name":"first-contentful-paint","startTime":557.725}],"resource":[{"name":{"href":"https://static.egcdn.com/mobile/@6.20191031.112952-9d0a9738@.json?_=1573043253247","hostname":"static.egcdn.com","pathname":"/mobile/@6.20191031.112952-9d0a9738@.json"},"startTime":305.81,"duration":81.435,"initiatorType":"fetch","nextHopProtocol":"h2","fetchStart":305.81,"responseEnd":387.245,"transferSize":0},{"name":{"href":"https://livecasino.eg88play.com/setup?device=desktop&wrapped=false","hostname":"livecasino.eg88play.com","pathname":"/setup"},"startTime":306.73,"duration":2.205,"initiatorType":"fetch","nextHopProtocol":"","fetchStart":306.73,"domainLookupStart":306.73,"domainLookupEnd":306.73,"connectStart":306.73,"connectEnd":306.73,"requestStart":307.5,"responseStart":307.865,"responseEnd":308.935,"transferSize":0,"encodedBodySize":1053,"decodedBodySize":1053},{"name":{"href":"https://livecasino.eg88play.com/style?json=true","hostname":"livecasino.eg88play.com","pathname":"/style"},"startTime":307.13,"duration":4.025,"initiatorType":"fetch","nextHopProtocol":"","fetchStart":307.13,"domainLookupStart":307.13,"domainLookupEnd":307.13,"connectStart":307.13,"connectEnd":307.13,"requestStart":307.835,"responseStart":309.745,"responseEnd":311.155,"transferSize":0,"encodedBodySize":675,"decodedBodySize":675},{"name":{"href":"https://static.egcdn.com/player/games/languages/ko.json?6.20191031.112952-9d0a9738","hostname":"static.egcdn.com","pathname":"/player/games/languages/ko.json"},"startTime":307.535,"duration":8.135,"initiatorType":"fetch","nextHopProtocol":"h2","fetchStart":307.535,"responseEnd":315.67,"transferSize":0},{"name":{"href":"https://livecasino.eg88play.com/mobile-video/video_version_v5.js?436956","hostname":"livecasino.eg88play.com","pathname":"/mobile-video/video_version_v5.js"},"startTime":310.915,"initiatorType":"script","nextHopProtocol":"","fetchStart":310.915,"domainLookupStart":310.915,"domainLookupEnd":310.915,"connectStart":310.915,"connectEnd":310.915,"requestStart":310.915,"responseStart":310.915,"responseEnd":310.915,"transferSize":0,"encodedBodySize":554,"decodedBodySize":1283},{"name":{"href":"https://livecasino.eg88play.com/mobile-video/video_desktop_v5.js?v5.128.3_5.20191031.190907_2056f64a","hostname":"livecasino.eg88play.com","pathname":"/mobile-video/video_desktop_v5.js"},"startTime":314.13,"initiatorType":"script","nextHopProtocol":"","fetchStart":314.13,"domainLookupStart":314.13,"domainLookupEnd":314.13,"connectStart":314.13,"connectEnd":314.13,"requestStart":314.13,"responseStart":314.13,"responseEnd":314.13,"transferSize":0,"encodedBodySize":217492,"decodedBodySize":1047231},{"name":{"href":"https://livecasino.eg88play.com/mobile/images/powered_by.35e87.svg","hostname":"livecasino.eg88play.com","pathname":"/mobile/images/powered_by.svg"},"startTime":332.21,"duration":1.845,"initiatorType":"css","nextHopProtocol":"","fetchStart":332.21,"domainLookupStart":332.21,"domainLookupEnd":332.21,"connectStart":332.21,"connectEnd":332.21,"requestStart":333.07,"responseStart":333.325,"responseEnd":334.055,"transferSize":0,"encodedBodySize":2620,"decodedBodySize":7957},{"name":{"href":"https://static.egcdn.com/mobile/js/vendor.a149b.js","hostname":"static.egcdn.com","pathname":"/mobile/js/vendor.js"},"startTime":479.665,"duration":110.995,"initiatorType":"script","nextHopProtocol":"h2","fetchStart":479.665,"responseEnd":590.66,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/commons.desktop.86462.js","hostname":"static.egcdn.com","pathname":"/mobile/js/commons.desktop.js"},"startTime":480.12,"duration":136.87,"initiatorType":"script","nextHopProtocol":"h2","fetchStart":480.12,"responseEnd":616.99,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/lobby.desktop.2fbb5.js","hostname":"static.egcdn.com","pathname":"/mobile/js/lobby.desktop.js"},"startTime":480.76,"duration":11.775,"initiatorType":"script","nextHopProtocol":"h2","fetchStart":480.76,"responseEnd":492.535,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/commons.desktop.86462.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/commons.desktop.css"},"startTime":482.62,"duration":105.11,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":482.62,"responseEnd":587.73,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/lobby.desktop.2fbb5.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/lobby.desktop.css"},"startTime":483.52,"duration":7.295,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":483.52,"responseEnd":490.815,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/bundles/lobby-3_0.55150.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/bundles/lobby-3_0.css"},"startTime":484.635,"duration":5.795,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":484.635,"responseEnd":490.43,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/bundles/lobby.1ae87.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/bundles/lobby.css"},"startTime":485.575,"duration":5.155,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":485.575,"responseEnd":490.73,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/fonts/AvenirNextCyr-Regular.9ec59.woff2","hostname":"static.egcdn.com","pathname":"/mobile/fonts/AvenirNextCyr-Regular.woff2"},"startTime":650.205,"duration":2.275,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":650.205,"responseEnd":652.48,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/assets/sounds/clickUIButton.cdbdb.mp3","hostname":"static.egcdn.com","pathname":"/mobile/assets/sounds/clickUIButton.mp3"},"startTime":1701.51,"duration":2.43,"initiatorType":"xmlhttprequest","nextHopProtocol":"h2","fetchStart":1701.51,"responseEnd":1703.94,"transferSize":0},{"name":{"href":"https://static.egcdn.com/lobby-brandings/totogaming-bg-tablet.565cfca.jpg","hostname":"static.egcdn.com","pathname":"/lobby-brandings/totogaming-bg-tablet.565cfca.jpg"},"startTime":1702.41,"duration":4.46,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":1702.41,"responseEnd":1706.87,"transferSize":0},{"name":{"href":"https://static.egcdn.com/lobby-brandings/totogaming-header-baccarat-squeeze.1e2e213.jpg","hostname":"static.egcdn.com","pathname":"/lobby-brandings/totogaming-header-baccarat-squeeze.1e2e213.jpg"},"startTime":1705.01,"duration":5.235,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":1705.01,"responseEnd":1710.245,"transferSize":0},{"name":{"href":"https://static.egcdn.com/#","hostname":"static.egcdn.com","pathname":"/"},"startTime":1707.065,"duration":85.615,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":1707.065,"responseEnd":1792.68,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/fonts/AvenirNextCyr-Medium.50e09.woff2","hostname":"static.egcdn.com","pathname":"/mobile/fonts/AvenirNextCyr-Medium.woff2"},"startTime":1710.52,"duration":5.06,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":1710.52,"responseEnd":1715.58,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/baccarat-active.fabec.svg","hostname":"static.egcdn.com","pathname":"/mobile/images/baccarat-active.svg"},"startTime":3880.895,"duration":3.25,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":3880.895,"responseEnd":3884.145,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/baccarat-passive.17669.svg","hostname":"static.egcdn.com","pathname":"/mobile/images/baccarat-passive.svg"},"startTime":3881.21,"duration":3.165,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":3881.21,"responseEnd":3884.375,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/poker-active.96179.svg","hostname":"static.egcdn.com","pathname":"/mobile/images/poker-active.svg"},"startTime":3881.495,"duration":3.685,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":3881.495,"responseEnd":3885.18,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/poker-passive.dd6de.svg","hostname":"static.egcdn.com","pathname":"/mobile/images/poker-passive.svg"},"startTime":3881.885,"duration":3.97,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":3881.885,"responseEnd":3885.855,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/chp.78b89.png","hostname":"static.egcdn.com","pathname":"/mobile/images/chp.png"},"startTime":3921.225,"duration":2.93,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":3921.225,"responseEnd":3924.155,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/lobby-lightning-spritesheet.dc183.png","hostname":"static.egcdn.com","pathname":"/mobile/images/lobby-lightning-spritesheet.png"},"startTime":4018.34,"duration":3.07,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":4018.34,"responseEnd":4021.41,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/vendor.a149b.js","hostname":"static.egcdn.com","pathname":"/mobile/js/vendor.js"},"startTime":4064.965,"duration":104.055,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4064.965,"responseEnd":4169.02,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/commons.desktop.86462.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/commons.desktop.css"},"startTime":4065.735,"duration":99.125,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4065.735,"responseEnd":4164.86,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/commons.desktop.86462.js","hostname":"static.egcdn.com","pathname":"/mobile/js/commons.desktop.js"},"startTime":4066.55,"duration":113.91,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4066.55,"responseEnd":4180.46,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/desktopRoulette.af511.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/desktopRoulette.css"},"startTime":4067.43,"duration":9.205,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4067.43,"responseEnd":4076.635,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/desktopRoulette.af511.js","hostname":"static.egcdn.com","pathname":"/mobile/js/desktopRoulette.js"},"startTime":4068.325,"duration":43.865,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4068.325,"responseEnd":4112.19,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/desktopMoneyWheel.f7ce6.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/desktopMoneyWheel.css"},"startTime":4069.325,"duration":13.955,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4069.325,"responseEnd":4083.28,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/desktopMoneyWheel.f7ce6.js","hostname":"static.egcdn.com","pathname":"/mobile/js/desktopMoneyWheel.js"},"startTime":4070.355,"duration":25.045,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4070.355,"responseEnd":4095.4,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/poker.casino-holdem.desktop.2d3e5.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/poker.casino-holdem.desktop.css"},"startTime":4071.915,"duration":13.25,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4071.915,"responseEnd":4085.165,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/poker.casino-holdem.desktop.2d3e5.js","hostname":"static.egcdn.com","pathname":"/mobile/js/poker.casino-holdem.desktop.js"},"startTime":4073.825,"duration":36.645,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4073.825,"responseEnd":4110.47,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/baccarat.desktop.bf36b.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/baccarat.desktop.css"},"startTime":4075.035,"duration":20.545,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4075.035,"responseEnd":4095.58,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/baccarat.desktop.bf36b.js","hostname":"static.egcdn.com","pathname":"/mobile/js/baccarat.desktop.js"},"startTime":4076,"duration":30.39,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4076,"responseEnd":4106.39,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/dragonTiger.desktop.6afa4.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/dragonTiger.desktop.css"},"startTime":4077.28,"duration":17.885,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4077.28,"responseEnd":4095.165,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/dragonTiger.desktop.6afa4.js","hostname":"static.egcdn.com","pathname":"/mobile/js/dragonTiger.desktop.js"},"startTime":4078.39,"duration":25.415,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4078.39,"responseEnd":4103.805,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/lightr1_imrs_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/lightr1_imrs_med_L.jpg"},"startTime":4114.94,"duration":1404.465,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":4114.94,"responseEnd":5519.405,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/green_imrs_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/green_imrs_med_L.jpg"},"startTime":4115.455,"duration":1405.175,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":4115.455,"responseEnd":5520.63,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/dc1_mw_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/dc1_mw_med_L.jpg"},"startTime":4115.89,"duration":1405.375,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":4115.89,"responseEnd":5521.265,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/immersive_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/immersive_med_L.jpg"},"startTime":4116.42,"duration":1669.275,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":4116.42,"responseEnd":5785.695,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/pk_gen_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/pk_gen_med_L.jpg"},"startTime":5527.08,"duration":1401.575,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":5527.08,"responseEnd":6928.655,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/bac5_bs_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/bac5_bs_med_L.jpg"},"startTime":5529.76,"duration":14.735,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":5529.76,"responseEnd":5544.495,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/topcr1_bs_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/topcr1_bs_med_L.jpg"},"startTime":5532.01,"duration":1409.665,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":5532.01,"responseEnd":6941.675,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/dragonara.4963e.png","hostname":"static.egcdn.com","pathname":"/mobile/images/dragonara.png"},"startTime":14528.305,"duration":4.92,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":14528.305,"responseEnd":14533.225,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/ribbon-roti.f8409.png","hostname":"static.egcdn.com","pathname":"/mobile/images/ribbon-roti.png"},"startTime":14529.22,"duration":5.61,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":14529.22,"responseEnd":14534.83,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/dbr.bfc36.png","hostname":"static.egcdn.com","pathname":"/mobile/images/dbr.png"},"startTime":14529.78,"duration":5.26,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":14529.78,"responseEnd":14535.04,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/grand_casino.1de3d.png","hostname":"static.egcdn.com","pathname":"/mobile/images/grand_casino.png"},"startTime":14533.15,"duration":2.795,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":14533.15,"responseEnd":14535.945,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/tk2_imr_med_L.jpg?q=1573043267462","hostname":"lob.egcvi.com","pathname":"/thumbnail/tk2_imr_med_L.jpg"},"startTime":14621.31,"duration":1398.24,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":14621.31,"responseEnd":16019.55,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/rugent1_imrs_med_L.jpg?q=1573043267463","hostname":"lob.egcvi.com","pathname":"/thumbnail/rugent1_imrs_med_L.jpg"},"startTime":14621.91,"duration":1402.615,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":14621.91,"responseEnd":16024.525,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/vipr1_imrs_med_L.jpg?q=1573043267463","hostname":"lob.egcvi.com","pathname":"/thumbnail/vipr1_imrs_med_L.jpg"},"startTime":14622.255,"duration":1419.045,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":14622.255,"responseEnd":16041.3,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/gen1_ss_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/gen1_ss_med_L.jpg"},"startTime":14622.69,"duration":1400.93,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":14622.69,"responseEnd":16023.62,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/vip1_ss_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/vip1_ss_med_L.jpg"},"startTime":16043.85,"duration":299.085,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16043.85,"responseEnd":16342.935,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/spa_ss_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/spa_ss_med_L.jpg"},"startTime":16048.985,"duration":301.195,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16048.985,"responseEnd":16350.18,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/drago_imr_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/drago_imr_med_L.jpg"},"startTime":16053.505,"duration":297.48,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16053.505,"responseEnd":16350.985,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/dbr_imr_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/dbr_imr_med_L.jpg"},"startTime":16065.795,"duration":1671.09,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16065.795,"responseEnd":17736.885,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/speed1_imr_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/speed1_imr_med_L.jpg"},"startTime":16350.93,"duration":1400.73,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16350.93,"responseEnd":17751.66,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/gcro1_imr_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/gcro1_imr_med_L.jpg"},"startTime":16359.13,"duration":586.325,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16359.13,"responseEnd":16945.455,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/dzerot1_imr_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/dzerot1_imr_med_L.jpg"},"startTime":16362.055,"duration":295.87,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16362.055,"responseEnd":16657.925,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/casmlt1_imr_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/casmlt1_imr_med_L.jpg"},"startTime":16660.43,"duration":1400.97,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16660.43,"responseEnd":18061.4,"transferSize":0}],"mark":[{"name":"socketOpen","startTime":2647.735},{"name":"socketOpen","startTime":3541.3},{"name":"evoLoaderClosed","startTime":3916.65},{"name":"_evoReportGenerated","startTime":18920.025}],"first-input":[{"name":"mousedown","startTime":13975.19,"duration":8,"processingStart":13977.455,"processingEnd":13977.55,"cancelable":true}]},"evoLoaderClosed":3916.65}}}))
        ws.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
        ws.send(json.dumps({"id":wid(),"type":"lobby.updateSubscriptions","args":{"subscribeTopics":[],"unsubscribeTopics":[{"topic":"table","tables":[{"tableId":"lkcbrbdckjxajdol"},{"tableId":"lr6t4k3lcd4qgyrk"},{"tableId":"AmericanTable001"},{"tableId":"mvrcophqscoqosd6"}]}]}}))
        ws.send(json.dumps({"id":wid(),"type":"lobby.updateSubscriptions","args":{"subscribeTopics":[{"topic":"table","tables":[{"tableId":"lkcbrbdckjxajdol"},{"tableId":"lr6t4k3lcd4qgyrk"},{"tableId":"AmericanTable001"},{"tableId":"mvrcophqscoqosd6"}]}],"unsubscribeTopics":[]}}))
        ws.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))

        while Lof == False:
            ws.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
            for s in range(10):
                result =  ws.recv()
                dataR = json.loads(result)
                if dataR["type"] == "lobby.rouletteNumbersUpdated":
                    x = dataR['args']["tableId"]
                    for o in List:
                        o.x = x
                    
