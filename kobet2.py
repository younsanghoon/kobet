import requests
import xmltodict
import json
import mechanicalsoup
import string
import random
import time
from websocket import create_connection

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
Content-Length: 117
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

wshead1 = '''Accept-Encoding: gzip, deflate, br
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
Cache-Control: no-cache
Connection: Upgrade
Host: livecasino.eg88play.com
Origin: https://livecasino.eg88play.com
Pragma: no-cache
Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits
Sec-WebSocket-Key: hdg3RSO8LvPXCFcaDsafTQ==
Sec-WebSocket-Version: 13
Upgrade: websocket
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36
'''

data = 'GameName=&Email=can741&Password=1q2w3e4r!!'
addr1 = 'https://kobet-1.com/Mobile/IsMobile?IsMobile=true'
addr2 = 'https://kobet-1.com/ko/Login/Login'
addr3 = 'https://kobet-1.com/LiveCasino/GetLiveCasinoUrl?url='
browser = mechanicalsoup.StatefulBrowser()


browser = mechanicalsoup.StatefulBrowser()

with requests.session() as sess:
    r1 = sess.get(addr1, headers=pharseHeaders(head1), verify=False)
    #print (r1,'r1')
    if r1.status_code == 200:
        r2 = sess.post(addr2, verify=False, headers=pharseHeaders(head2), data=data.encode())
        #print (r2,'r2')
        if r2.status_code == 200:
            r3 = sess.get(addr3, headers=pharseHeaders(head3), verify=False)
            #print (r3,'r3')
            if r3.status_code == 200:
                addr4 = json.loads(r3.content.decode())["Message"]
                r4 = sess.get(addr4, headers=pharseHeaders(head4), verify=False)
                #print (r4, 'r4')
                r = browser.get(addr4, verify=False, headers=pharseHeaders(head4))
                #print (r,'r')


                #print(browser.get_cookiejar().keys())
                sessionId = str(browser.get_cookiejar()["EVOSESSIONID"])
                #str(sessionId)
                
    ws = create_connection("wss://livecasino.eg88play.com/public/lobby/player/socket?messageFormat=json&EVOSESSIONID="+sessionId, headers = pharseHeaders(wshead1))
    false = False
    null = 0
    true = True
    ymd = time.strftime('%Y-%m-%d')
    ims = time.strftime('%I:%M:%S')
    
    
    ws.send(json.dumps({"id":wid(),"type":"lobby.updateSubscriptions","args":{"subscribeTopics":[{"topic":"lobby","game":"live-casino-custom-build-flash"}],"unsubscribeTopics":[]}}))
    ws.send(json.dumps({"id":wid(),"type":"settings.read","args":{"key":"lobby.common"}}))
    ws.send(json.dumps({"id":wid(),"type":"settings.read","args":{"key":"generic.mobile"}}))
    ws.send(json.dumps({"id":wid(),"type":"settings.read","args":{"key":"generic.common"}}))
    ws.send(json.dumps({"id":wid(),"type":"settings.read","args":{"key":"lobby.common"}}))
    ws.send(json.dumps({"id":wid(),"type":"settings.read","args":{"key":"roulette.common"}}))
    ws.send(json.dumps({"log":{"type":"CLIENT_SOCKET_CONNECTION_ESTABLISHED","latency":-1,"value":{"currency":"KRW","gameType":"lobby","channel":"PCMac","orientation":"landscape","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36","inGame":false}}}))
    ws.send(json.dumps({"log":{"type":"CLIENT_APP_LOADING_TIME","value":{"fastSwitching":false,"appLoading":1572602927553,"domInteractive":1572602929425,"appLoaded":1572602931696,"requestCDNDataStart":2211.8549999995594,"requestCDNDataSession":false,"requestSetupDataStart":2214.364999999816,"requestSetupDataSession":false,"requestSetupDataEnd":2604.910000000018,"requestSetupDataDuration":390.545000000202,"requestStyleDataStart":2215.1300000004994,"requestStyleDataSession":false,"requestStyleDataEnd":2604.090000000724,"requestStyleDataDuration":388.9600000002247,"requestI18nDataStart":2215.584999999919,"requestI18nDataSession":false,"requestI18nDataEnd":2606.2849999998434,"requestI18nDataDuration":390.69999999992433,"loadBundleCSSStart":2608.9150000007066,"loadBundleCSSEnd":2865.975000000617,"loadBundleCSSDuration":257.05999999991036,"loadGameBundleStart":2866.2750000003143,"loadGameBundleEnd":6351.850000000923,"loadGameBundleDuration":3485.5750000006083,"domInteractiveTime":1872,"domContentLoadedTime":null,"domLoadedTime":null,"appLoadedTime":4143,"typeApp":"lobby","timeLoading":4203,"device":"desktop","firstTimeLoad":false,"buildId":"Build Version: 6.20191028.110947-3f0961fa at 2019-10-28 11:39:57","wasLoadedOverCDN":true,"serviceWorker":true,"videoUpdate":false,"waitForVideo":false,"frameHeight":754.4000244140625,"frameWidth":636,"screenWidth":1536,"screenHeight":864,"currency":"KRW","gameType":"lobby","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36","inGame":false,"channel":"PCMac","orientation":"landscape"}}}))
    ws.send(json.dumps({"log":{"type":"CLIENT_GAME_LOADED","value":{"typeApp":"lobby","offline":true,"buildId":"Build Version: 6.20191028.110947-3f0961fa at 2019-10-28 11:39:57","currency":"KRW","gameType":"lobby","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36","inGame":false,"channel":"PCMac","orientation":"landscape"}}}))
    ws.send(json.dumps({"log":{"type":"CLIENT_BALANCE_UPDATED","value":{"currency":"KRW","balance":0,"gameType":"lobby","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36","inGame":false,"channel":"PCMac","orientation":"landscape"}}}))
    ws.send(json.dumps({"id":wid(),"type":"lobby.updateSubscriptions","args":{"subscribeTopics":[{"topic":"table","tables":[{"tableId":"LightningTable01"},{"tableId":"vctlz20yfnmp1ylr"},{"tableId":"MOWDream00000001"},{"tableId":"7x0b1tgh7agmf6hv"},{"tableId":"HoldemTable00001"},{"tableId":"leqhceumaq6qfoug"},{"tableId":"TopCard000000001"}]}],"unsubscribeTopics":[]}}))
    ws.send(json.dumps({"log":{"type":"CLIENT_LOBBY_CATEGORY_CHANGE","latency":-1,"value":{"currency":"KRW","gameType":"lobby","buildId":"Build Version: 6.20191028.110947-3f0961fa at 2019-10-28 11:39:57","device":"Desktop","typeApp":"lobby4","categoryId":"top_games","category":"top_games","previousCategory":null,"previousTablesCount":0,"timeInLobby":3210,"channel":"PCMac","orientation":"landscape","balance":0,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36","inGame":false}}}))
    ws.send(json.dumps({"log":{"type":"CLIENT_BALANCE_UPDATED","latency":-1,"value":{"currency":"KRW","gameType":"lobby","buildId":"Build Version: 6.20191028.110947-3f0961fa at 2019-10-28 11:39:57","device":"Desktop","typeApp":"lobby4","categoryId":"top_games","timeInLobby":3288,"channel":"PCMac","orientation":"landscape","balance":0,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36","inGame":false}}}))
    ws_rof = False
    #while ws_rof == False :
    for s in range(1):
        ws.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
        for s in range(1):
            result =  ws.recv()
            data = json.loads(result)
            if data["type"] != "lobby.seatsUpdated" and data["type"] != "metrics.pong":
                if data["type"] == "lobby.rouletteNumbersUpdated":
                    if ["tableId"]  == "7x0b1tgh7agmf6hv":
                        print ('이머징 룰렛')
                    elif ["tableId"] == "LightningTable01":
                        print ('라이트링 룰렛')
                    elif ["tableId"] == "vctlz20yfnmp1ylr":
                        print ('룰렛')
                elif data["type"] == "lobby.topCardHistoryUpdated":
                    print ('top2','카지노 홀덤?')
                elif data["type"] == "lobby.moneyWheelHistoryUpdated":
                    print ('머니휠')
                elif data["type"] == "lobby.baccaratRoadUpdated":
                    print ('바카라')
                
              
            
            








    
