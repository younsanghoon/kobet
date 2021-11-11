class BTing:
    def gameIdS(self):
        strCase = string.ascii_lowercase+string.ascii_uppercase+string.digits
    return ''.join(random.choice(strCase) for x in range(24))

    def tt(self):
    return int(str(time.time()).replace("." , "")[:13])

    def wid(self):
    strCase = string.ascii_lowercase+string.ascii_uppercase+string.digits
    return ''.join(random.choice(strCase) for x in range(10))

    def BetingTime(self,E):
        self.TTa = False
        while self.TTa == False:
            if self.UI == 1:
                B = bet_even
                D = ROU_Even
            else:
                pass
            if self.UI == 2:
                B = bet_black
                D = ROU_Black
            else:
                pass
            if self.UI == 3:
                B = bet_from1to18
                D = ROU_118
            else:
                pass
            if self.x == "LightningTable01":#라이트링 룰렛 48  B= bet_black D = ROU_Black  E = 남은 돈
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":200,"type":"%s","chips":"200@%s","codes":{"%s":200},"balance":E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[200,1000,4000,20000,100000,400000],"defaultChip":1,"tableMinLimit":200,"tableMaxLimit":2000000,"channel":"PCMac","orientation":"landscape"}}}))%(B,B,D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":200}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"lightr1_imr_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "7x0b1tgh7agmf6hv":#이머징 룰렛
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":1000,"type":"%s","chips":"1000@%s","codes":{"%s":1000},"balance":E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[1000,2000,10000,20000,1000000,2000000],"defaultChip":1,"tableMinLimit":1000,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(B,B,D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":1000}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"immersive_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "vctlz20yfnmp1ylr": #룰렛
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":400,"type":"%s","chips":"400@%s","codes":{"%s":400},"balance":E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[400,800,2000,10000,20000,1000000],"defaultChip":1,"tableMinLimit":400,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(B,B,D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":400}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"green_imr_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "r5aw9yumyaxgnd90" :#터키 룰렛
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":1000,"type":"%s","chips":"1000@%s","codes":{"%s":1000},"balance":E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[1000,2000,5000,25000,100000,500000],"defaultChip":1,"tableMinLimit":1000,"tableMaxLimit":2000000,"channel":"PCMac","orientation":"landscape"}}}))%(B,B,D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":1000}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"tk2_imr_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "zosmk25g2f768o52" : #룰렛 라이브
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":800,"type":"%s","chips":"800@%s","codes":{"%s":800},"balance":E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[800,2000,10000,20000,1000000,2000000],"defaultChip":1,"tableMinLimit":800,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(B,B,D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":800}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"rugent1_imr_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "48z5pjps3ntvqc1b" : #오토 룰렛
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":160,"type":"%s","chips":"160@%s","codes":{"%s":160},"balance":E,"viewType":"Slingshot","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[160,1000,4000,20000,100000,400000],"defaultChip":1,"tableMinLimit":160,"tableMaxLimit":2000000,"channel":"PCMac","orientation":"landscape"}}}))%(B,B,D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":160}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"slingshot","btVideoQuality":"gen1_ss_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"id":self.wid(),"type":"metrics.ping","args":{"t":self.tt()}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "01rb77cq1gtenhmo" : #vip 오토 룰렛
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":300,"type":"%s","chips":"300@%s","codes":{"%s":300},"balance":E,"viewType":"Slingshot","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[300,1000,2000,10000,20000,1000000],"defaultChip":1,"tableMinLimit":300,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(B,B,D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":300}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"slingshot","btVideoQuality":"vip1_ss_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "f1f4rm9xgh4j3u2z" : #라 팔타지 자동 룰렛 french_bet_black
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":160,"type":"french_%s","chips":"160@french_%s","codes":{"%s50ReturnOn0":160},"balance":E,"viewType":"Slingshot","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[160,1000,4000,20000,100000,400000],"defaultChip":1,"tableMinLimit":160,"tableMaxLimit":2000000,"channel":"PCMac","orientation":"landscape"}}}))%(B,B,D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"162":160}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"slingshot","btVideoQuality":"spa_ss_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "q0a470up68p2b81p" : #드라고나 룰렛
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":1000,"type":"%s","chips":"1000@%s","codes":{"%s":1000},"balance":E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[1000,2000,10000,20000,1000000,2000000],"defaultChip":1,"tableMinLimit":1000,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(B,B,D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":1000}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"drago_imr_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "lkcbrbdckjxajdol" : #스피드 룰렛
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":1000,"type":"%s","chips":"1000@%s","codes":{"%s":1000},"balance":E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[500,1000,2000,10000,20000,1000000],"defaultChip":2,"tableMinLimit":500,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(B,B,D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"49":1000}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"speed1_imr_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "lr6t4k3lcd4qgyrk" : #그랜드 카지노 룰렛
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":1000,"type":"%s","chips":"1000@%s","codes":{"%s":1000},"balance":E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[1000,2000,10000,20000,1000000,2000000],"defaultChip":1,"tableMinLimit":1000,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(B,B,D)
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
                    B = bet_even
                    D = RoDZ_Even
                else:
                    pass
                if self.UI == 2:
                    B = bet_black
                    D = RoDZ_Black
                else:
                    pass
                if self.UI == 3:
                    B = bet_from1to18
                    D = RoDZ_118
                else:
                    pass
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":1000,"type":"%s","chips":"1000@%s","codes":{"%s":1000},"balance":self.E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"americanroulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[200,1000,2000,10000,20000,1000000],"defaultChip":2,"tableMinLimit":200,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(B,B,D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"408":1000}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"dzerot1_imr_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
            if self.x == "mvrcophqscoqosd6": #카지노 몰타 룰렛
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":1000,"type":"%s","chips":"1000@%s","codes":{"%s":1000},"balance":self.E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"roulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[1000,2000,10000,20000,1000000,2000000],"defaultChip":1,"tableMinLimit":1000,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(B,B,D)
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
                    B = bet_even
                    D = RoDZ_Even
                else:
                    pass
                if self.UI == 2:
                    B = bet_black
                    D = RoDZ_Black
                else:
                    pass
                if self.UI == 3:
                    B = bet_from1to18
                    D = RoDZ_118
                else:
                    pass
                wss.send(json.dumps({"log":{"type":"CLIENT_BET_CHIP","value":{"amount":1000,"type":"%s","chips":"1000@%s","codes":{"%s":1000},"balance":self.E,"viewType":"Immersive (Overlay, Full screen, Multi-camera View)","gameType":"americanroulette","appVersion":4,"maxTouchPoints":0,"currency":"KRW","chipStack":[1000,2000,10000,20000,1000000,2000000],"defaultChip":1,"tableMinLimit":1000,"tableMaxLimit":3000000,"channel":"PCMac","orientation":"landscape"}}}))%(B,B,D)
                wss.send(json.dumps({"args":{"gameId":self.gameIdS(),"action":{"type":"PLACE","value":{"408":1000}},"timestamp":self.tt(),"betTags":{"mwLayout":8,"openMwTables":1,"latency":random.random(-200,500),"videoProtocol":"flvjs","btTableView":"hd1","btVideoQuality":"rcac1_imr_hi","btMiniGame":0,"appVersion":4,"orientation":"landscape"}},"id":self.wid(),"type":"roulette.betAction"}))
                wss.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                result =  wss.recv()
                data1 = json.loads(result)
                if data1["type"] == "roulette.betActionResponse":
                    self.TTa = True
            else:
                pass
