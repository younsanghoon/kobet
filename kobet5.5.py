import requests
import xmltodict
import json
import mechanicalsoup
import string
import random
import time
from websocket import create_connection

Cdoun = 0
Cup = 0
Nber2s = 0
Nber1s = 0
Rads = 0
Blacks = 0
nm1 = []
nm2 = []
nm3 = []
nm4 = []
nm5 = []
nm6 = []
nm7 = []
nm8 = []
nm9 = []
nm10 = []
nm11 = []
nm12 = []
nm13 = []
nm14 = []
nm15 = []
nm16 = []

nma1 = 0
nma2 = 0
nma3 = 0
nma4 = []
nma5 = []
nma6 = []
nma7 = []
nma8 = []
nma9 = []
nma10 = []
nma11 = []
nma12 = []
nma13 = []
nma14 = []
nma15 = []
nma16 = []

nmaa1 = 0
nmaa2 = 0
nmaa3 = 0
nmaa4 = 0
nmaa5 = 0
nmaa6 = 0
nmaa7 = 0
nmaa8 = 0
nmaa9 = 0
nmaa10 = 0
nmaa11 = 0
nmaa12 = 0
nmaa13 = 0
nmaa14 = 0
nmaa15 = 0
nmaa16 = 0
Nber1 = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
Nber2 = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
Rad = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
Black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]

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
def op(nm,nma,nmaa,x):
    for i in range(len(data['args']['numbers']['results'])):
        nm.append(int(data['args']['numbers']['results'][i][0]['number']))
        nmaa +=1
        if nma == 0 and nmaa == 12:
            nma +=1
            qqq = nm.reverse()
            for pop in len(qqq):
                if 18 >= qqq[pop] and 1 <= qqq :
                    Cdoun += 1
                    Cup = 0
                elif 19 <= qqq[pop] and 36 >= qqq:
                    Cdoun = 0
                    Cup +=1
            for pop1 in len(qqq):
                if Nber2 in qqq[pop1]:
                    Nber2s +=1
                    Nber1s = 0
                else:
                    Nber2s = 0
                    Nber1s +=1
            for pop2 in len(qqq):
                if Rad in qqq[pop2] :
                    Rads +=1
                    Blacks = 0
                else :
                    Rads = 0
                    Blacks +=1  
                    
            print (x)  

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
    time.sleep(1)
    ws.send(json.dumps({"id":"dknoirmajn","type":"lobby.updateSubscriptions","args":{"subscribeTopics":[{"topic":"category","categoryId":"roulette","features":[]}],"unsubscribeTopics":[{"topic":"category","categoryId":"top_games","features":[]},{"topic":"table","tables":[{"tableId":"LightningTable01"},{"tableId":"vctlz20yfnmp1ylr"},{"tableId":"MOWDream00000001"},{"tableId":"7x0b1tgh7agmf6hv"},{"tableId":"HoldemTable00001"},{"tableId":"leqhceumaq6qfoug"},{"tableId":"TopCard000000001"}]}]}}))
    ws.send(json.dumps({"log":{"type":"CLIENT_LOBBY_CATEGORY_CHANGE","latency":296,"value":{"currency":"KRW","gameType":"lobby","buildId":"Build Version: 6.20191031.112952-9d0a9738 at 2019-10-31 12:07:40","device":"Desktop","typeApp":"lobby4","categoryId":"top_games","category":"roulette","previousCategory":"top_games","previousTablesCount":7,"timeInLobby":13181,"channel":"PCMac","orientation":"landscape","balance":0,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36","inGame":false}}}))
    ws.send(json.dumps({"id":"k1k8t2z9c0","type":"lobby.updateSubscriptions","args":{"subscribeTopics":[{"topic":"table","tables":[{"tableId":"LightningTable01"},{"tableId":"7x0b1tgh7agmf6hv"},{"tableId":"vctlz20yfnmp1ylr"},{"tableId":"r5aw9yumyaxgnd90"},{"tableId":"zosmk25g2f768o52"},{"tableId":"wzg6kdkad1oe7m5k"},{"tableId":"wzg6kdkad1oe7m5k","vtId":"979uwb2tdni7dmp4"}]}],"unsubscribeTopics":[]}}))
    ws.send(json.dumps({"id":"dk7bxkeras","type":"lobby.updateSubscriptions","args":{"subscribeTopics":[{"topic":"table","tables":[{"tableId":"48z5pjps3ntvqc1b"},{"tableId":"01rb77cq1gtenhmo"},{"tableId":"f1f4rm9xgh4j3u2z"},{"tableId":"q0a470up68p2b81p"},{"tableId":"DoubleBallRou001"},{"tableId":"lkcbrbdckjxajdol"},{"tableId":"lr6t4k3lcd4qgyrk"},{"tableId":"AmericanTable001"},{"tableId":"mvrcophqscoqosd6"}]}],"unsubscribeTopics":[]}}))
    ws.send(json.dumps({"id":"lnt05lexrk","type":"metrics.ping","args":{"t":1573043268977}}))
    ws.send(json.dumps({"log":{"type":"CLIENT_APP_LOADING_TIME_V2","value":{"version":7,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36","game":"lobby","device":"desktop","build":"6.20191031.112952-9d0a9738","waitForVideo":false,"entries":{"navigation":[{"name":{"href":"https://livecasino.eg88play.com/mobile/#game=live-casino-custom-build-flash","hostname":"livecasino.eg88play.com","pathname":"/mobile/"},"duration":470.57,"initiatorType":"navigation","nextHopProtocol":"","fetchStart":1.81,"domainLookupStart":1.81,"domainLookupEnd":1.81,"connectStart":1.81,"connectEnd":1.81,"requestStart":3.16,"responseStart":4.08,"responseEnd":7.625,"transferSize":0,"encodedBodySize":43676,"decodedBodySize":177057,"domInteractive":331.775,"domContentLoadedEventStart":331.825,"domContentLoadedEventEnd":331.825,"domComplete":470.505,"loadEventStart":470.515,"loadEventEnd":470.57,"type":"navigate"}],"paint":[{"name":"first-paint","startTime":141.53},{"name":"first-contentful-paint","startTime":557.725}],"resource":[{"name":{"href":"https://static.egcdn.com/mobile/@6.20191031.112952-9d0a9738@.json?_=1573043253247","hostname":"static.egcdn.com","pathname":"/mobile/@6.20191031.112952-9d0a9738@.json"},"startTime":305.81,"duration":81.435,"initiatorType":"fetch","nextHopProtocol":"h2","fetchStart":305.81,"responseEnd":387.245,"transferSize":0},{"name":{"href":"https://livecasino.eg88play.com/setup?device=desktop&wrapped=false","hostname":"livecasino.eg88play.com","pathname":"/setup"},"startTime":306.73,"duration":2.205,"initiatorType":"fetch","nextHopProtocol":"","fetchStart":306.73,"domainLookupStart":306.73,"domainLookupEnd":306.73,"connectStart":306.73,"connectEnd":306.73,"requestStart":307.5,"responseStart":307.865,"responseEnd":308.935,"transferSize":0,"encodedBodySize":1053,"decodedBodySize":1053},{"name":{"href":"https://livecasino.eg88play.com/style?json=true","hostname":"livecasino.eg88play.com","pathname":"/style"},"startTime":307.13,"duration":4.025,"initiatorType":"fetch","nextHopProtocol":"","fetchStart":307.13,"domainLookupStart":307.13,"domainLookupEnd":307.13,"connectStart":307.13,"connectEnd":307.13,"requestStart":307.835,"responseStart":309.745,"responseEnd":311.155,"transferSize":0,"encodedBodySize":675,"decodedBodySize":675},{"name":{"href":"https://static.egcdn.com/player/games/languages/ko.json?6.20191031.112952-9d0a9738","hostname":"static.egcdn.com","pathname":"/player/games/languages/ko.json"},"startTime":307.535,"duration":8.135,"initiatorType":"fetch","nextHopProtocol":"h2","fetchStart":307.535,"responseEnd":315.67,"transferSize":0},{"name":{"href":"https://livecasino.eg88play.com/mobile-video/video_version_v5.js?436956","hostname":"livecasino.eg88play.com","pathname":"/mobile-video/video_version_v5.js"},"startTime":310.915,"initiatorType":"script","nextHopProtocol":"","fetchStart":310.915,"domainLookupStart":310.915,"domainLookupEnd":310.915,"connectStart":310.915,"connectEnd":310.915,"requestStart":310.915,"responseStart":310.915,"responseEnd":310.915,"transferSize":0,"encodedBodySize":554,"decodedBodySize":1283},{"name":{"href":"https://livecasino.eg88play.com/mobile-video/video_desktop_v5.js?v5.128.3_5.20191031.190907_2056f64a","hostname":"livecasino.eg88play.com","pathname":"/mobile-video/video_desktop_v5.js"},"startTime":314.13,"initiatorType":"script","nextHopProtocol":"","fetchStart":314.13,"domainLookupStart":314.13,"domainLookupEnd":314.13,"connectStart":314.13,"connectEnd":314.13,"requestStart":314.13,"responseStart":314.13,"responseEnd":314.13,"transferSize":0,"encodedBodySize":217492,"decodedBodySize":1047231},{"name":{"href":"https://livecasino.eg88play.com/mobile/images/powered_by.35e87.svg","hostname":"livecasino.eg88play.com","pathname":"/mobile/images/powered_by.svg"},"startTime":332.21,"duration":1.845,"initiatorType":"css","nextHopProtocol":"","fetchStart":332.21,"domainLookupStart":332.21,"domainLookupEnd":332.21,"connectStart":332.21,"connectEnd":332.21,"requestStart":333.07,"responseStart":333.325,"responseEnd":334.055,"transferSize":0,"encodedBodySize":2620,"decodedBodySize":7957},{"name":{"href":"https://static.egcdn.com/mobile/js/vendor.a149b.js","hostname":"static.egcdn.com","pathname":"/mobile/js/vendor.js"},"startTime":479.665,"duration":110.995,"initiatorType":"script","nextHopProtocol":"h2","fetchStart":479.665,"responseEnd":590.66,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/commons.desktop.86462.js","hostname":"static.egcdn.com","pathname":"/mobile/js/commons.desktop.js"},"startTime":480.12,"duration":136.87,"initiatorType":"script","nextHopProtocol":"h2","fetchStart":480.12,"responseEnd":616.99,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/lobby.desktop.2fbb5.js","hostname":"static.egcdn.com","pathname":"/mobile/js/lobby.desktop.js"},"startTime":480.76,"duration":11.775,"initiatorType":"script","nextHopProtocol":"h2","fetchStart":480.76,"responseEnd":492.535,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/commons.desktop.86462.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/commons.desktop.css"},"startTime":482.62,"duration":105.11,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":482.62,"responseEnd":587.73,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/lobby.desktop.2fbb5.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/lobby.desktop.css"},"startTime":483.52,"duration":7.295,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":483.52,"responseEnd":490.815,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/bundles/lobby-3_0.55150.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/bundles/lobby-3_0.css"},"startTime":484.635,"duration":5.795,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":484.635,"responseEnd":490.43,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/bundles/lobby.1ae87.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/bundles/lobby.css"},"startTime":485.575,"duration":5.155,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":485.575,"responseEnd":490.73,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/fonts/AvenirNextCyr-Regular.9ec59.woff2","hostname":"static.egcdn.com","pathname":"/mobile/fonts/AvenirNextCyr-Regular.woff2"},"startTime":650.205,"duration":2.275,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":650.205,"responseEnd":652.48,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/assets/sounds/clickUIButton.cdbdb.mp3","hostname":"static.egcdn.com","pathname":"/mobile/assets/sounds/clickUIButton.mp3"},"startTime":1701.51,"duration":2.43,"initiatorType":"xmlhttprequest","nextHopProtocol":"h2","fetchStart":1701.51,"responseEnd":1703.94,"transferSize":0},{"name":{"href":"https://static.egcdn.com/lobby-brandings/totogaming-bg-tablet.565cfca.jpg","hostname":"static.egcdn.com","pathname":"/lobby-brandings/totogaming-bg-tablet.565cfca.jpg"},"startTime":1702.41,"duration":4.46,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":1702.41,"responseEnd":1706.87,"transferSize":0},{"name":{"href":"https://static.egcdn.com/lobby-brandings/totogaming-header-baccarat-squeeze.1e2e213.jpg","hostname":"static.egcdn.com","pathname":"/lobby-brandings/totogaming-header-baccarat-squeeze.1e2e213.jpg"},"startTime":1705.01,"duration":5.235,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":1705.01,"responseEnd":1710.245,"transferSize":0},{"name":{"href":"https://static.egcdn.com/#","hostname":"static.egcdn.com","pathname":"/"},"startTime":1707.065,"duration":85.615,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":1707.065,"responseEnd":1792.68,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/fonts/AvenirNextCyr-Medium.50e09.woff2","hostname":"static.egcdn.com","pathname":"/mobile/fonts/AvenirNextCyr-Medium.woff2"},"startTime":1710.52,"duration":5.06,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":1710.52,"responseEnd":1715.58,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/baccarat-active.fabec.svg","hostname":"static.egcdn.com","pathname":"/mobile/images/baccarat-active.svg"},"startTime":3880.895,"duration":3.25,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":3880.895,"responseEnd":3884.145,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/baccarat-passive.17669.svg","hostname":"static.egcdn.com","pathname":"/mobile/images/baccarat-passive.svg"},"startTime":3881.21,"duration":3.165,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":3881.21,"responseEnd":3884.375,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/poker-active.96179.svg","hostname":"static.egcdn.com","pathname":"/mobile/images/poker-active.svg"},"startTime":3881.495,"duration":3.685,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":3881.495,"responseEnd":3885.18,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/poker-passive.dd6de.svg","hostname":"static.egcdn.com","pathname":"/mobile/images/poker-passive.svg"},"startTime":3881.885,"duration":3.97,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":3881.885,"responseEnd":3885.855,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/chp.78b89.png","hostname":"static.egcdn.com","pathname":"/mobile/images/chp.png"},"startTime":3921.225,"duration":2.93,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":3921.225,"responseEnd":3924.155,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/lobby-lightning-spritesheet.dc183.png","hostname":"static.egcdn.com","pathname":"/mobile/images/lobby-lightning-spritesheet.png"},"startTime":4018.34,"duration":3.07,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":4018.34,"responseEnd":4021.41,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/vendor.a149b.js","hostname":"static.egcdn.com","pathname":"/mobile/js/vendor.js"},"startTime":4064.965,"duration":104.055,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4064.965,"responseEnd":4169.02,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/commons.desktop.86462.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/commons.desktop.css"},"startTime":4065.735,"duration":99.125,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4065.735,"responseEnd":4164.86,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/commons.desktop.86462.js","hostname":"static.egcdn.com","pathname":"/mobile/js/commons.desktop.js"},"startTime":4066.55,"duration":113.91,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4066.55,"responseEnd":4180.46,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/desktopRoulette.af511.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/desktopRoulette.css"},"startTime":4067.43,"duration":9.205,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4067.43,"responseEnd":4076.635,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/desktopRoulette.af511.js","hostname":"static.egcdn.com","pathname":"/mobile/js/desktopRoulette.js"},"startTime":4068.325,"duration":43.865,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4068.325,"responseEnd":4112.19,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/desktopMoneyWheel.f7ce6.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/desktopMoneyWheel.css"},"startTime":4069.325,"duration":13.955,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4069.325,"responseEnd":4083.28,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/desktopMoneyWheel.f7ce6.js","hostname":"static.egcdn.com","pathname":"/mobile/js/desktopMoneyWheel.js"},"startTime":4070.355,"duration":25.045,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4070.355,"responseEnd":4095.4,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/poker.casino-holdem.desktop.2d3e5.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/poker.casino-holdem.desktop.css"},"startTime":4071.915,"duration":13.25,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4071.915,"responseEnd":4085.165,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/poker.casino-holdem.desktop.2d3e5.js","hostname":"static.egcdn.com","pathname":"/mobile/js/poker.casino-holdem.desktop.js"},"startTime":4073.825,"duration":36.645,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4073.825,"responseEnd":4110.47,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/baccarat.desktop.bf36b.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/baccarat.desktop.css"},"startTime":4075.035,"duration":20.545,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4075.035,"responseEnd":4095.58,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/baccarat.desktop.bf36b.js","hostname":"static.egcdn.com","pathname":"/mobile/js/baccarat.desktop.js"},"startTime":4076,"duration":30.39,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4076,"responseEnd":4106.39,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/dragonTiger.desktop.6afa4.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/dragonTiger.desktop.css"},"startTime":4077.28,"duration":17.885,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4077.28,"responseEnd":4095.165,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/dragonTiger.desktop.6afa4.js","hostname":"static.egcdn.com","pathname":"/mobile/js/dragonTiger.desktop.js"},"startTime":4078.39,"duration":25.415,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4078.39,"responseEnd":4103.805,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/lightr1_imrs_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/lightr1_imrs_med_L.jpg"},"startTime":4114.94,"duration":1404.465,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":4114.94,"responseEnd":5519.405,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/green_imrs_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/green_imrs_med_L.jpg"},"startTime":4115.455,"duration":1405.175,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":4115.455,"responseEnd":5520.63,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/dc1_mw_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/dc1_mw_med_L.jpg"},"startTime":4115.89,"duration":1405.375,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":4115.89,"responseEnd":5521.265,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/immersive_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/immersive_med_L.jpg"},"startTime":4116.42,"duration":1669.275,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":4116.42,"responseEnd":5785.695,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/pk_gen_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/pk_gen_med_L.jpg"},"startTime":5527.08,"duration":1401.575,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":5527.08,"responseEnd":6928.655,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/bac5_bs_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/bac5_bs_med_L.jpg"},"startTime":5529.76,"duration":14.735,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":5529.76,"responseEnd":5544.495,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/topcr1_bs_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/topcr1_bs_med_L.jpg"},"startTime":5532.01,"duration":1409.665,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":5532.01,"responseEnd":6941.675,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/dragonara.4963e.png","hostname":"static.egcdn.com","pathname":"/mobile/images/dragonara.png"},"startTime":14528.305,"duration":4.92,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":14528.305,"responseEnd":14533.225,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/ribbon-roti.f8409.png","hostname":"static.egcdn.com","pathname":"/mobile/images/ribbon-roti.png"},"startTime":14529.22,"duration":5.61,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":14529.22,"responseEnd":14534.83,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/dbr.bfc36.png","hostname":"static.egcdn.com","pathname":"/mobile/images/dbr.png"},"startTime":14529.78,"duration":5.26,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":14529.78,"responseEnd":14535.04,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/grand_casino.1de3d.png","hostname":"static.egcdn.com","pathname":"/mobile/images/grand_casino.png"},"startTime":14533.15,"duration":2.795,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":14533.15,"responseEnd":14535.945,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/tk2_imr_med_L.jpg?q=1573043267462","hostname":"lob.egcvi.com","pathname":"/thumbnail/tk2_imr_med_L.jpg"},"startTime":14621.31,"duration":1398.24,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":14621.31,"responseEnd":16019.55,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/rugent1_imrs_med_L.jpg?q=1573043267463","hostname":"lob.egcvi.com","pathname":"/thumbnail/rugent1_imrs_med_L.jpg"},"startTime":14621.91,"duration":1402.615,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":14621.91,"responseEnd":16024.525,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/vipr1_imrs_med_L.jpg?q=1573043267463","hostname":"lob.egcvi.com","pathname":"/thumbnail/vipr1_imrs_med_L.jpg"},"startTime":14622.255,"duration":1419.045,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":14622.255,"responseEnd":16041.3,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/gen1_ss_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/gen1_ss_med_L.jpg"},"startTime":14622.69,"duration":1400.93,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":14622.69,"responseEnd":16023.62,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/vip1_ss_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/vip1_ss_med_L.jpg"},"startTime":16043.85,"duration":299.085,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16043.85,"responseEnd":16342.935,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/spa_ss_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/spa_ss_med_L.jpg"},"startTime":16048.985,"duration":301.195,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16048.985,"responseEnd":16350.18,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/drago_imr_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/drago_imr_med_L.jpg"},"startTime":16053.505,"duration":297.48,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16053.505,"responseEnd":16350.985,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/dbr_imr_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/dbr_imr_med_L.jpg"},"startTime":16065.795,"duration":1671.09,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16065.795,"responseEnd":17736.885,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/speed1_imr_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/speed1_imr_med_L.jpg"},"startTime":16350.93,"duration":1400.73,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16350.93,"responseEnd":17751.66,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/gcro1_imr_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/gcro1_imr_med_L.jpg"},"startTime":16359.13,"duration":586.325,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16359.13,"responseEnd":16945.455,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/dzerot1_imr_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/dzerot1_imr_med_L.jpg"},"startTime":16362.055,"duration":295.87,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16362.055,"responseEnd":16657.925,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/casmlt1_imr_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/casmlt1_imr_med_L.jpg"},"startTime":16660.43,"duration":1400.97,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16660.43,"responseEnd":18061.4,"transferSize":0}],"mark":[{"name":"socketOpen","startTime":2647.735},{"name":"socketOpen","startTime":3541.3},{"name":"evoLoaderClosed","startTime":3916.65},{"name":"_evoReportGenerated","startTime":18920.025}],"first-input":[{"name":"mousedown","startTime":13975.19,"duration":8,"processingStart":13977.455,"processingEnd":13977.55,"cancelable":true}]},"evoLoaderClosed":3916.65}}}))
    ws.send(json.dumps({"id":"ntfdpz09mf","type":"metrics.ping","args":{"t":1573043273956}}))
    ws.send(json.dumps({"id":"duzedoxjw3","type":"lobby.updateSubscriptions","args":{"subscribeTopics":[],"unsubscribeTopics":[{"topic":"table","tables":[{"tableId":"lkcbrbdckjxajdol"},{"tableId":"lr6t4k3lcd4qgyrk"},{"tableId":"AmericanTable001"},{"tableId":"mvrcophqscoqosd6"}]}]}}))
    ws.send(json.dumps({"id":"3vieafqqh8","type":"lobby.updateSubscriptions","args":{"subscribeTopics":[{"topic":"table","tables":[{"tableId":"lkcbrbdckjxajdol"},{"tableId":"lr6t4k3lcd4qgyrk"},{"tableId":"AmericanTable001"},{"tableId":"mvrcophqscoqosd6"}]}],"unsubscribeTopics":[]}}))
    ws.send(json.dumps({"id":"2skbvqpj3j","type":"metrics.ping","args":{"t":1573043278957}}))
    ws_rof = False
    #while ws_rof == False :
    oo=0

    for s in range(150):
        ws.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
        for s in range(10):
            #time.sleep(1)
            result =  ws.recv()
            data = json.loads(result)
            #if data["type"] != "lobby.seatsUpdated" and data["type"] != "metrics.pong":
            if data["type"] == "lobby.rouletteNumbersUpdated":
                x = data['args']["tableId"]
                if x == '7x0b1tgh7agmf6hv':
                    op(nm1,nma1,nmaa1,'이머징 룰렛')
                elif x == 'lkcbrbdckjxajdol':
                    op(nm2,nma2,nmaa2,'스피드 룰렛')
                elif x == 'r5aw9yumyaxgnd90':
                    op(nm3,nma3,nmaa3,'터키 룰렛')
                elif x == 'wzg6kdkad1oe7m5k':
                    op(nm4,nma4,nmaa4,'VIP 룰렛, 프렌치 롤렛 골드')
                elif x == 'zosmk25g2f768o52':
                    op(nm5,nma5,nmaa5,'룰렛 라이브')
                elif x == 'vctlz20yfnmp1ylr':
                    op(nm6,nma6,nmaa6,'룰렛')
                elif x == 'AmericanTable001':
                    op(nm7,nma7,nmaa7,'아메리카 룰렛')
                elif x == 'LightningTable01':
                    op(nm8,nma8,nmaa8,'라이트링 룰렛')
                elif x == 'DoubleBallRou001':
                    op(nm9,nma9,nmaa9,'더블 볼 룰')
                elif x == '01rb77cq1gtenhmo':
                    op(nm10,nma10,nmaa10,'VIP 오토 룰렛')
                elif x == '48z5pjps3ntvqc1b':
                    op(nm11,nma11,nmaa11,'오토 룰렛')
                elif x == 'f1f4rm9xgh4j3u2z':
                    op(nm12,nma12,nmaa12,'라 팔타지 자동 룰렛')
                elif x == 'q0a470up68p2b81p':
                    op(nm13,nma13,nmaa13,'드라고나 룰렛')
                elif x == 'mvrcophqscoqosd6':
                    op(nm14,nma14,nmaa14,'Casino Malta Roulette')
                elif x =='lr6t4k3lcd4qgyrk':
                    op(nm15,nma15,nmaa15,'그랜드 카지노 룰렛')
                else:
                    print (x)
                '''#print('oo',data)
                if data['args']["tableId"]  == '7x0b1tgh7agmf6hv':
                    r1data = data
                    for i in range(len(data['args']['numbers']['results'])):
                        nm1.append(int(data['args']['numbers']['results'][i][0]['number']))
                        nmaa1 +=1
                        if nma1 == 0 and nmaa1 == 12:
                            nma1 +=1
                            print ('이머징 룰렛', nm1)
                            
                    #data['args']['numbers']
                elif data['args']["tableId"] == 'LightningTable01':
                    r2data = data
                    for i in range(len(data['args']['numbers']['results'])):
                        nm2.append(int(data['args']['numbers']['results'][i][0]['number']))
                        nmaa2 +=1
                        if nma2 == 0 and nmaa2 == 12:
                            nma2 +=1
                            print ('라이트링 룰렛', nm2)
                elif data['args']["tableId"] == 'vctlz20yfnmp1ylr':
                    r3data = data
                    for i in range(len(data['args']['numbers']['results'])):
                        nm3.append(int(data['args']['numbers']['results'][i][0]['number']))
                        nmaa3 +=1
                        if nma3 == 0 and nmaa3 == 12:
                            nma3 +=1
                            print ('룰렛', nm3)
            elif data["type"] == "lobby.moneyWheelHistoryUpdated":
                mdata = data
                print ('머니휠')
            elif data["type"] == "lobby.baccaratRoadUpdated":
                bdata = data
                print ('바카라')
            '''
              
            
            








    
