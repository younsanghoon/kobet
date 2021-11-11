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


while Lof == False:
    ws.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
    for s in range(10):
        result =  ws.recv()
        dataR = json.loads(result)
        if dataR["type"] == "lobby.rouletteNumbersUpdated":
            x = dataR['args']["tableId"]
            for o in List:
                o.x = x
