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
    ws.send(json.dumps({"id":wid(),"type":"lobby.updateSubscriptions","args":{"subscribeTopics":[{"topic":"category","categoryId":"roulette","features":[]}],"unsubscribeTopics":[{"topic":"category","categoryId":"top_games","features":[]},{"topic":"table","tables":[{"tableId":"LightningTable01"},{"tableId":"vctlz20yfnmp1ylr"},{"tableId":"MOWDream00000001"},{"tableId":"7x0b1tgh7agmf6hv"},{"tableId":"HoldemTable00001"},{"tableId":"leqhceumaq6qfoug"},{"tableId":"TopCard000000001"}]}]}}))
    ws.send(json.dumps({"log":{"type":"CLIENT_LOBBY_CATEGORY_CHANGE","latency":296,"value":{"currency":"KRW","gameType":"lobby","buildId":"Build Version: 6.20191031.112952-9d0a9738 at 2019-10-31 12:07:40","device":"Desktop","typeApp":"lobby4","categoryId":"top_games","category":"roulette","previousCategory":"top_games","previousTablesCount":7,"timeInLobby":13181,"channel":"PCMac","orientation":"landscape","balance":0,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36","inGame":false}}}))
    ws.send(json.dumps({"id":wid(),"type":"lobby.updateSubscriptions","args":{"subscribeTopics":[{"topic":"table","tables":[{"tableId":"LightningTable01"},{"tableId":"7x0b1tgh7agmf6hv"},{"tableId":"vctlz20yfnmp1ylr"},{"tableId":"r5aw9yumyaxgnd90"},{"tableId":"zosmk25g2f768o52"},{"tableId":"wzg6kdkad1oe7m5k"},{"tableId":"wzg6kdkad1oe7m5k","vtId":"979uwb2tdni7dmp4"}]}],"unsubscribeTopics":[]}}))
    ws.send(json.dumps({"id":wid(),"type":"lobby.updateSubscriptions","args":{"subscribeTopics":[{"topic":"table","tables":[{"tableId":"48z5pjps3ntvqc1b"},{"tableId":"01rb77cq1gtenhmo"},{"tableId":"f1f4rm9xgh4j3u2z"},{"tableId":"q0a470up68p2b81p"},{"tableId":"DoubleBallRou001"},{"tableId":"lkcbrbdckjxajdol"},{"tableId":"lr6t4k3lcd4qgyrk"},{"tableId":"AmericanTable001"},{"tableId":"mvrcophqscoqosd6"}]}],"unsubscribeTopics":[]}}))
    ws.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
    ws.send(json.dumps({"log":{"type":"CLIENT_APP_LOADING_TIME_V2","value":{"version":7,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36","game":"lobby","device":"desktop","build":"6.20191031.112952-9d0a9738","waitForVideo":false,"entries":{"navigation":[{"name":{"href":"https://livecasino.eg88play.com/mobile/#game=live-casino-custom-build-flash","hostname":"livecasino.eg88play.com","pathname":"/mobile/"},"duration":470.57,"initiatorType":"navigation","nextHopProtocol":"","fetchStart":1.81,"domainLookupStart":1.81,"domainLookupEnd":1.81,"connectStart":1.81,"connectEnd":1.81,"requestStart":3.16,"responseStart":4.08,"responseEnd":7.625,"transferSize":0,"encodedBodySize":43676,"decodedBodySize":177057,"domInteractive":331.775,"domContentLoadedEventStart":331.825,"domContentLoadedEventEnd":331.825,"domComplete":470.505,"loadEventStart":470.515,"loadEventEnd":470.57,"type":"navigate"}],"paint":[{"name":"first-paint","startTime":141.53},{"name":"first-contentful-paint","startTime":557.725}],"resource":[{"name":{"href":"https://static.egcdn.com/mobile/@6.20191031.112952-9d0a9738@.json?_=1573043253247","hostname":"static.egcdn.com","pathname":"/mobile/@6.20191031.112952-9d0a9738@.json"},"startTime":305.81,"duration":81.435,"initiatorType":"fetch","nextHopProtocol":"h2","fetchStart":305.81,"responseEnd":387.245,"transferSize":0},{"name":{"href":"https://livecasino.eg88play.com/setup?device=desktop&wrapped=false","hostname":"livecasino.eg88play.com","pathname":"/setup"},"startTime":306.73,"duration":2.205,"initiatorType":"fetch","nextHopProtocol":"","fetchStart":306.73,"domainLookupStart":306.73,"domainLookupEnd":306.73,"connectStart":306.73,"connectEnd":306.73,"requestStart":307.5,"responseStart":307.865,"responseEnd":308.935,"transferSize":0,"encodedBodySize":1053,"decodedBodySize":1053},{"name":{"href":"https://livecasino.eg88play.com/style?json=true","hostname":"livecasino.eg88play.com","pathname":"/style"},"startTime":307.13,"duration":4.025,"initiatorType":"fetch","nextHopProtocol":"","fetchStart":307.13,"domainLookupStart":307.13,"domainLookupEnd":307.13,"connectStart":307.13,"connectEnd":307.13,"requestStart":307.835,"responseStart":309.745,"responseEnd":311.155,"transferSize":0,"encodedBodySize":675,"decodedBodySize":675},{"name":{"href":"https://static.egcdn.com/player/games/languages/ko.json?6.20191031.112952-9d0a9738","hostname":"static.egcdn.com","pathname":"/player/games/languages/ko.json"},"startTime":307.535,"duration":8.135,"initiatorType":"fetch","nextHopProtocol":"h2","fetchStart":307.535,"responseEnd":315.67,"transferSize":0},{"name":{"href":"https://livecasino.eg88play.com/mobile-video/video_version_v5.js?436956","hostname":"livecasino.eg88play.com","pathname":"/mobile-video/video_version_v5.js"},"startTime":310.915,"initiatorType":"script","nextHopProtocol":"","fetchStart":310.915,"domainLookupStart":310.915,"domainLookupEnd":310.915,"connectStart":310.915,"connectEnd":310.915,"requestStart":310.915,"responseStart":310.915,"responseEnd":310.915,"transferSize":0,"encodedBodySize":554,"decodedBodySize":1283},{"name":{"href":"https://livecasino.eg88play.com/mobile-video/video_desktop_v5.js?v5.128.3_5.20191031.190907_2056f64a","hostname":"livecasino.eg88play.com","pathname":"/mobile-video/video_desktop_v5.js"},"startTime":314.13,"initiatorType":"script","nextHopProtocol":"","fetchStart":314.13,"domainLookupStart":314.13,"domainLookupEnd":314.13,"connectStart":314.13,"connectEnd":314.13,"requestStart":314.13,"responseStart":314.13,"responseEnd":314.13,"transferSize":0,"encodedBodySize":217492,"decodedBodySize":1047231},{"name":{"href":"https://livecasino.eg88play.com/mobile/images/powered_by.35e87.svg","hostname":"livecasino.eg88play.com","pathname":"/mobile/images/powered_by.svg"},"startTime":332.21,"duration":1.845,"initiatorType":"css","nextHopProtocol":"","fetchStart":332.21,"domainLookupStart":332.21,"domainLookupEnd":332.21,"connectStart":332.21,"connectEnd":332.21,"requestStart":333.07,"responseStart":333.325,"responseEnd":334.055,"transferSize":0,"encodedBodySize":2620,"decodedBodySize":7957},{"name":{"href":"https://static.egcdn.com/mobile/js/vendor.a149b.js","hostname":"static.egcdn.com","pathname":"/mobile/js/vendor.js"},"startTime":479.665,"duration":110.995,"initiatorType":"script","nextHopProtocol":"h2","fetchStart":479.665,"responseEnd":590.66,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/commons.desktop.86462.js","hostname":"static.egcdn.com","pathname":"/mobile/js/commons.desktop.js"},"startTime":480.12,"duration":136.87,"initiatorType":"script","nextHopProtocol":"h2","fetchStart":480.12,"responseEnd":616.99,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/lobby.desktop.2fbb5.js","hostname":"static.egcdn.com","pathname":"/mobile/js/lobby.desktop.js"},"startTime":480.76,"duration":11.775,"initiatorType":"script","nextHopProtocol":"h2","fetchStart":480.76,"responseEnd":492.535,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/commons.desktop.86462.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/commons.desktop.css"},"startTime":482.62,"duration":105.11,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":482.62,"responseEnd":587.73,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/lobby.desktop.2fbb5.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/lobby.desktop.css"},"startTime":483.52,"duration":7.295,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":483.52,"responseEnd":490.815,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/bundles/lobby-3_0.55150.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/bundles/lobby-3_0.css"},"startTime":484.635,"duration":5.795,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":484.635,"responseEnd":490.43,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/bundles/lobby.1ae87.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/bundles/lobby.css"},"startTime":485.575,"duration":5.155,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":485.575,"responseEnd":490.73,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/fonts/AvenirNextCyr-Regular.9ec59.woff2","hostname":"static.egcdn.com","pathname":"/mobile/fonts/AvenirNextCyr-Regular.woff2"},"startTime":650.205,"duration":2.275,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":650.205,"responseEnd":652.48,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/assets/sounds/clickUIButton.cdbdb.mp3","hostname":"static.egcdn.com","pathname":"/mobile/assets/sounds/clickUIButton.mp3"},"startTime":1701.51,"duration":2.43,"initiatorType":"xmlhttprequest","nextHopProtocol":"h2","fetchStart":1701.51,"responseEnd":1703.94,"transferSize":0},{"name":{"href":"https://static.egcdn.com/lobby-brandings/totogaming-bg-tablet.565cfca.jpg","hostname":"static.egcdn.com","pathname":"/lobby-brandings/totogaming-bg-tablet.565cfca.jpg"},"startTime":1702.41,"duration":4.46,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":1702.41,"responseEnd":1706.87,"transferSize":0},{"name":{"href":"https://static.egcdn.com/lobby-brandings/totogaming-header-baccarat-squeeze.1e2e213.jpg","hostname":"static.egcdn.com","pathname":"/lobby-brandings/totogaming-header-baccarat-squeeze.1e2e213.jpg"},"startTime":1705.01,"duration":5.235,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":1705.01,"responseEnd":1710.245,"transferSize":0},{"name":{"href":"https://static.egcdn.com/#","hostname":"static.egcdn.com","pathname":"/"},"startTime":1707.065,"duration":85.615,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":1707.065,"responseEnd":1792.68,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/fonts/AvenirNextCyr-Medium.50e09.woff2","hostname":"static.egcdn.com","pathname":"/mobile/fonts/AvenirNextCyr-Medium.woff2"},"startTime":1710.52,"duration":5.06,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":1710.52,"responseEnd":1715.58,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/baccarat-active.fabec.svg","hostname":"static.egcdn.com","pathname":"/mobile/images/baccarat-active.svg"},"startTime":3880.895,"duration":3.25,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":3880.895,"responseEnd":3884.145,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/baccarat-passive.17669.svg","hostname":"static.egcdn.com","pathname":"/mobile/images/baccarat-passive.svg"},"startTime":3881.21,"duration":3.165,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":3881.21,"responseEnd":3884.375,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/poker-active.96179.svg","hostname":"static.egcdn.com","pathname":"/mobile/images/poker-active.svg"},"startTime":3881.495,"duration":3.685,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":3881.495,"responseEnd":3885.18,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/poker-passive.dd6de.svg","hostname":"static.egcdn.com","pathname":"/mobile/images/poker-passive.svg"},"startTime":3881.885,"duration":3.97,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":3881.885,"responseEnd":3885.855,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/chp.78b89.png","hostname":"static.egcdn.com","pathname":"/mobile/images/chp.png"},"startTime":3921.225,"duration":2.93,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":3921.225,"responseEnd":3924.155,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/lobby-lightning-spritesheet.dc183.png","hostname":"static.egcdn.com","pathname":"/mobile/images/lobby-lightning-spritesheet.png"},"startTime":4018.34,"duration":3.07,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":4018.34,"responseEnd":4021.41,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/vendor.a149b.js","hostname":"static.egcdn.com","pathname":"/mobile/js/vendor.js"},"startTime":4064.965,"duration":104.055,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4064.965,"responseEnd":4169.02,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/commons.desktop.86462.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/commons.desktop.css"},"startTime":4065.735,"duration":99.125,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4065.735,"responseEnd":4164.86,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/commons.desktop.86462.js","hostname":"static.egcdn.com","pathname":"/mobile/js/commons.desktop.js"},"startTime":4066.55,"duration":113.91,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4066.55,"responseEnd":4180.46,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/desktopRoulette.af511.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/desktopRoulette.css"},"startTime":4067.43,"duration":9.205,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4067.43,"responseEnd":4076.635,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/desktopRoulette.af511.js","hostname":"static.egcdn.com","pathname":"/mobile/js/desktopRoulette.js"},"startTime":4068.325,"duration":43.865,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4068.325,"responseEnd":4112.19,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/desktopMoneyWheel.f7ce6.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/desktopMoneyWheel.css"},"startTime":4069.325,"duration":13.955,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4069.325,"responseEnd":4083.28,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/desktopMoneyWheel.f7ce6.js","hostname":"static.egcdn.com","pathname":"/mobile/js/desktopMoneyWheel.js"},"startTime":4070.355,"duration":25.045,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4070.355,"responseEnd":4095.4,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/poker.casino-holdem.desktop.2d3e5.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/poker.casino-holdem.desktop.css"},"startTime":4071.915,"duration":13.25,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4071.915,"responseEnd":4085.165,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/poker.casino-holdem.desktop.2d3e5.js","hostname":"static.egcdn.com","pathname":"/mobile/js/poker.casino-holdem.desktop.js"},"startTime":4073.825,"duration":36.645,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4073.825,"responseEnd":4110.47,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/baccarat.desktop.bf36b.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/baccarat.desktop.css"},"startTime":4075.035,"duration":20.545,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4075.035,"responseEnd":4095.58,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/baccarat.desktop.bf36b.js","hostname":"static.egcdn.com","pathname":"/mobile/js/baccarat.desktop.js"},"startTime":4076,"duration":30.39,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4076,"responseEnd":4106.39,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/dragonTiger.desktop.6afa4.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/dragonTiger.desktop.css"},"startTime":4077.28,"duration":17.885,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4077.28,"responseEnd":4095.165,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/dragonTiger.desktop.6afa4.js","hostname":"static.egcdn.com","pathname":"/mobile/js/dragonTiger.desktop.js"},"startTime":4078.39,"duration":25.415,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":4078.39,"responseEnd":4103.805,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/lightr1_imrs_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/lightr1_imrs_med_L.jpg"},"startTime":4114.94,"duration":1404.465,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":4114.94,"responseEnd":5519.405,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/green_imrs_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/green_imrs_med_L.jpg"},"startTime":4115.455,"duration":1405.175,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":4115.455,"responseEnd":5520.63,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/dc1_mw_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/dc1_mw_med_L.jpg"},"startTime":4115.89,"duration":1405.375,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":4115.89,"responseEnd":5521.265,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/immersive_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/immersive_med_L.jpg"},"startTime":4116.42,"duration":1669.275,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":4116.42,"responseEnd":5785.695,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/pk_gen_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/pk_gen_med_L.jpg"},"startTime":5527.08,"duration":1401.575,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":5527.08,"responseEnd":6928.655,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/bac5_bs_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/bac5_bs_med_L.jpg"},"startTime":5529.76,"duration":14.735,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":5529.76,"responseEnd":5544.495,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/topcr1_bs_med_L.jpg?q=1573043256953","hostname":"lob.egcvi.com","pathname":"/thumbnail/topcr1_bs_med_L.jpg"},"startTime":5532.01,"duration":1409.665,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":5532.01,"responseEnd":6941.675,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/dragonara.4963e.png","hostname":"static.egcdn.com","pathname":"/mobile/images/dragonara.png"},"startTime":14528.305,"duration":4.92,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":14528.305,"responseEnd":14533.225,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/ribbon-roti.f8409.png","hostname":"static.egcdn.com","pathname":"/mobile/images/ribbon-roti.png"},"startTime":14529.22,"duration":5.61,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":14529.22,"responseEnd":14534.83,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/dbr.bfc36.png","hostname":"static.egcdn.com","pathname":"/mobile/images/dbr.png"},"startTime":14529.78,"duration":5.26,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":14529.78,"responseEnd":14535.04,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/grand_casino.1de3d.png","hostname":"static.egcdn.com","pathname":"/mobile/images/grand_casino.png"},"startTime":14533.15,"duration":2.795,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":14533.15,"responseEnd":14535.945,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/tk2_imr_med_L.jpg?q=1573043267462","hostname":"lob.egcvi.com","pathname":"/thumbnail/tk2_imr_med_L.jpg"},"startTime":14621.31,"duration":1398.24,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":14621.31,"responseEnd":16019.55,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/rugent1_imrs_med_L.jpg?q=1573043267463","hostname":"lob.egcvi.com","pathname":"/thumbnail/rugent1_imrs_med_L.jpg"},"startTime":14621.91,"duration":1402.615,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":14621.91,"responseEnd":16024.525,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/vipr1_imrs_med_L.jpg?q=1573043267463","hostname":"lob.egcvi.com","pathname":"/thumbnail/vipr1_imrs_med_L.jpg"},"startTime":14622.255,"duration":1419.045,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":14622.255,"responseEnd":16041.3,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/gen1_ss_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/gen1_ss_med_L.jpg"},"startTime":14622.69,"duration":1400.93,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":14622.69,"responseEnd":16023.62,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/vip1_ss_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/vip1_ss_med_L.jpg"},"startTime":16043.85,"duration":299.085,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16043.85,"responseEnd":16342.935,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/spa_ss_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/spa_ss_med_L.jpg"},"startTime":16048.985,"duration":301.195,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16048.985,"responseEnd":16350.18,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/drago_imr_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/drago_imr_med_L.jpg"},"startTime":16053.505,"duration":297.48,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16053.505,"responseEnd":16350.985,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/dbr_imr_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/dbr_imr_med_L.jpg"},"startTime":16065.795,"duration":1671.09,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16065.795,"responseEnd":17736.885,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/speed1_imr_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/speed1_imr_med_L.jpg"},"startTime":16350.93,"duration":1400.73,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16350.93,"responseEnd":17751.66,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/gcro1_imr_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/gcro1_imr_med_L.jpg"},"startTime":16359.13,"duration":586.325,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16359.13,"responseEnd":16945.455,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/dzerot1_imr_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/dzerot1_imr_med_L.jpg"},"startTime":16362.055,"duration":295.87,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16362.055,"responseEnd":16657.925,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/casmlt1_imr_med_L.jpg?q=1573043267499","hostname":"lob.egcvi.com","pathname":"/thumbnail/casmlt1_imr_med_L.jpg"},"startTime":16660.43,"duration":1400.97,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":16660.43,"responseEnd":18061.4,"transferSize":0}],"mark":[{"name":"socketOpen","startTime":2647.735},{"name":"socketOpen","startTime":3541.3},{"name":"evoLoaderClosed","startTime":3916.65},{"name":"_evoReportGenerated","startTime":18920.025}],"first-input":[{"name":"mousedown","startTime":13975.19,"duration":8,"processingStart":13977.455,"processingEnd":13977.55,"cancelable":true}]},"evoLoaderClosed":3916.65}}}))
    ws.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
    ws.send(json.dumps({"id":wid(),"type":"lobby.updateSubscriptions","args":{"subscribeTopics":[],"unsubscribeTopics":[{"topic":"table","tables":[{"tableId":"lkcbrbdckjxajdol"},{"tableId":"lr6t4k3lcd4qgyrk"},{"tableId":"AmericanTable001"},{"tableId":"mvrcophqscoqosd6"}]}]}}))
    ws.send(json.dumps({"id":wid(),"type":"lobby.updateSubscriptions","args":{"subscribeTopics":[{"topic":"table","tables":[{"tableId":"lkcbrbdckjxajdol"},{"tableId":"lr6t4k3lcd4qgyrk"},{"tableId":"AmericanTable001"},{"tableId":"mvrcophqscoqosd6"}]}],"unsubscribeTopics":[]}}))
    ws.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
    ws_rof = False
    #while ws_rof == False :
    oo=0
    mn = []
    nm = 0
    nm1 = []
    nmaa1 = 0
    ups = 0
    douns = 0
    Blacks = 0
    Rads = 0
    Nber1s = 0
    Nber2s = 0
    Rad = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    Black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    for s in range(300):
        ws.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
        for s in range(10):
            #time.sleep(1)
            result =  ws.recv()
            data = json.loads(result)
            if data["type"] == "lobby.rouletteNumbersUpdated":
                x = data['args']["tableId"]
                if x == '7x0b1tgh7agmf6hv':
                    nm = int(data['args']['numbers']['results'][0][0]['number'])
                    #print ('이머징 룰렛',nm)
                    #print(data['args']['numbers']['results'])
                    if nmaa1 == 0:
                        for i in range(len(data['args']['numbers']['results'])):
                            nm1.append(int(data['args']['numbers']['results'][i][0]['number']))
                            nmaa1 +=1
                            if nmaa1 == 12:
                                #print(nm1)
                                nm1.reverse()
                                #print(nm1)
                                for Cmn in range(len(nm1)):
                                    Cmns = int(nm1[Cmn])
                                    print(nm1[Cmn])
                                    if Cmns == 0:
                                        Rads +=1
                                        Blacks +=1
                                        Nber1s +=1
                                        Nber2s +=1
                                        ups +=1
                                        douns +=1
                                        print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                                    else:
                                        if Cmns%2==1:
                                            Nber1s +=1
                                            Nber2s =0
                                            print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                                        else:
                                            Nber1s =0
                                            Nber2s +=1
                                        if Rad.count(Cmns):
                                            Rads +=1
                                            Blacks = 0
                                            print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                                        else:
                                            Blacks +=1
                                            Rads = 0
                                        if Cmns >= 1 and Cmns <= 18:
                                            douns +=1
                                            ups =0
                                            print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                                        else:
                                            ups +=1
                                            douns = 0
                    else:
                        if nm == 0:
                            Rads +=1
                            Blacks +=1
                            Nber1s +=1
                            Nber2s +=1
                            ups +=1
                            douns +=1
                            print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                        else:
                            if nm%2==1:
                                Nber1s +=1
                                Nber2s =0
                                print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                            else:
                                Nber1s =0
                                Nber2s +=1
                            if Rad.count(nm):
                                Rads +=1
                                Blacks = 0
                                print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                            else:
                                Blacks +=1
                                Rads = 0
                            if nm >= 1 and nm <= 18:
                                douns +=1
                                ups =0
                                print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                            else:
                                ups +=1
                                douns = 0
                            if Nber1s == 4 :
                                print ('짝수 배팅','홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                            elif Nber1s > 4 :
                                print ('짝수 2배 배팅','홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                            else:
                                ws.send(json.dumps({"log":{"type":"CLIENT_APP_LOADING_TIME_V2","value":{"version":7,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36","game":"lobby","device":"desktop","build":"6.20191121.111140-2c066ecb","waitForVideo":false,"entries":{"navigation":[{"name":{"href":"https://livecasino.eg88play.com/mobile/#game=live-casino-custom-build-flash","hostname":"livecasino.eg88play.com","pathname":"/mobile/"},"duration":5009.7,"initiatorType":"navigation","nextHopProtocol":"","redirectStart":19.02,"redirectEnd":2907.52,"fetchStart":2907.52,"domainLookupStart":2907.52,"domainLookupEnd":2907.52,"connectStart":2907.52,"connectEnd":2907.52,"secureConnectionStart":2907.52,"requestStart":2913.83,"responseStart":3297.02,"responseEnd":3306.52,"transferSize":1506,"encodedBodySize":43835,"decodedBodySize":177606,"domInteractive":3448.19,"domContentLoadedEventStart":3448.265,"domContentLoadedEventEnd":3448.275,"domComplete":5009.575,"loadEventStart":5009.625,"loadEventEnd":5009.7,"type":"navigate","redirectCount":3}],"paint":[{"name":"first-paint","startTime":3390.12},{"name":"first-contentful-paint","startTime":3906.165}],"resource":[{"name":{"href":"https://static.egcdn.com/mobile/@6.20191121.111140-2c066ecb@.json?_=1574516817439","hostname":"static.egcdn.com","pathname":"/mobile/@6.20191121.111140-2c066ecb@.json"},"startTime":3412.975,"duration":207.145,"initiatorType":"fetch","nextHopProtocol":"h2","fetchStart":3412.975,"responseEnd":3620.12,"transferSize":0},{"name":{"href":"https://livecasino.eg88play.com/setup?device=desktop&wrapped=false","hostname":"livecasino.eg88play.com","pathname":"/setup"},"startTime":3415.23,"duration":408.695,"initiatorType":"fetch","nextHopProtocol":"http/1.1","fetchStart":3415.23,"domainLookupStart":3415.23,"domainLookupEnd":3415.23,"connectStart":3415.23,"connectEnd":3415.23,"secureConnectionStart":3415.23,"requestStart":3416.63,"responseStart":3822.955,"responseEnd":3823.925,"transferSize":1256,"encodedBodySize":1053,"decodedBodySize":1053},{"name":{"href":"https://livecasino.eg88play.com/style?json=true","hostname":"livecasino.eg88play.com","pathname":"/style"},"startTime":3415.665,"duration":389.2,"initiatorType":"fetch","nextHopProtocol":"http/1.1","fetchStart":3415.665,"domainLookupStart":3415.665,"domainLookupEnd":3415.665,"connectStart":3415.665,"connectEnd":3415.665,"secureConnectionStart":3415.665,"requestStart":3417.09,"responseStart":3803.4,"responseEnd":3804.865,"transferSize":877,"encodedBodySize":675,"decodedBodySize":675},{"name":{"href":"https://static.egcdn.com/player/games/languages/ko.json?6.20191121.111140-2c066ecb","hostname":"static.egcdn.com","pathname":"/player/games/languages/ko.json"},"startTime":3416.06,"duration":5.015,"initiatorType":"fetch","nextHopProtocol":"h2","fetchStart":3416.06,"responseEnd":3421.075,"transferSize":0},{"name":{"href":"https://livecasino.eg88play.com/mobile-video/video_version_v5.js?437366","hostname":"livecasino.eg88play.com","pathname":"/mobile-video/video_version_v5.js"},"startTime":3417.435,"duration":774.505,"initiatorType":"script","nextHopProtocol":"","fetchStart":3417.435,"domainLookupStart":3417.435,"domainLookupEnd":3417.435,"connectStart":3417.435,"connectEnd":3417.435,"secureConnectionStart":3417.435,"requestStart":3805.17,"responseStart":4190.51,"responseEnd":4191.94,"transferSize":311,"encodedBodySize":555,"decodedBodySize":1277},{"name":{"href":"https://livecasino.eg88play.com/mobile-video/video_desktop_v5.js?v5.128.3_5.20191031.190907_2056f64a","hostname":"livecasino.eg88play.com","pathname":"/mobile-video/video_desktop_v5.js"},"startTime":3418.415,"duration":109.57,"initiatorType":"script","nextHopProtocol":"","fetchStart":3418.415,"domainLookupStart":3418.415,"domainLookupEnd":3418.415,"connectStart":3418.415,"connectEnd":3418.415,"requestStart":3419.88,"responseStart":3421.51,"responseEnd":3527.985,"transferSize":0,"encodedBodySize":270382,"decodedBodySize":1038042},{"name":{"href":"https://livecasino.eg88play.com/mobile/images/powered_by.35e87.svg","hostname":"livecasino.eg88play.com","pathname":"/mobile/images/powered_by.svg"},"startTime":3448.95,"duration":1.9,"initiatorType":"css","nextHopProtocol":"","fetchStart":3448.95,"domainLookupStart":3448.95,"domainLookupEnd":3448.95,"connectStart":3448.95,"connectEnd":3448.95,"requestStart":3449.725,"responseStart":3449.995,"responseEnd":3450.85,"transferSize":0,"encodedBodySize":2620,"decodedBodySize":7957},{"name":{"href":"https://static.egcdn.com/mobile/js/vendor.6f3d2.js","hostname":"static.egcdn.com","pathname":"/mobile/js/vendor.js"},"startTime":3829.07,"duration":20.835,"initiatorType":"script","nextHopProtocol":"h2","fetchStart":3829.07,"responseEnd":3849.905,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/commons.desktop.3eb80.js","hostname":"static.egcdn.com","pathname":"/mobile/js/commons.desktop.js"},"startTime":3829.6,"duration":34.28,"initiatorType":"script","nextHopProtocol":"h2","fetchStart":3829.6,"responseEnd":3863.88,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/lobby.desktop.290c2.js","hostname":"static.egcdn.com","pathname":"/mobile/js/lobby.desktop.js"},"startTime":3830.515,"duration":25.225,"initiatorType":"script","nextHopProtocol":"h2","fetchStart":3830.515,"responseEnd":3855.74,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/commons.desktop.3eb80.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/commons.desktop.css"},"startTime":3832.745,"duration":18.97,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":3832.745,"responseEnd":3851.715,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/lobby.desktop.290c2.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/lobby.desktop.css"},"startTime":3834.155,"duration":13.655,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":3834.155,"responseEnd":3847.81,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/bundles/lobby-3_0.c2d98.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/bundles/lobby-3_0.css"},"startTime":3834.935,"duration":11.635,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":3834.935,"responseEnd":3846.57,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/bundles/lobby.15389.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/bundles/lobby.css"},"startTime":3835.63,"duration":11.28,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":3835.63,"responseEnd":3846.91,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/fonts/AvenirNextCyr-Regular.9ec59.woff2","hostname":"static.egcdn.com","pathname":"/mobile/fonts/AvenirNextCyr-Regular.woff2"},"startTime":3953.26,"duration":3.21,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":3953.26,"responseEnd":3956.47,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/assets/sounds/clickUIButton.cdbdb.mp3","hostname":"static.egcdn.com","pathname":"/mobile/assets/sounds/clickUIButton.mp3"},"startTime":4847.925,"duration":2.21,"initiatorType":"xmlhttprequest","nextHopProtocol":"h2","fetchStart":4847.925,"responseEnd":4850.135,"transferSize":0},{"name":{"href":"https://static.egcdn.com/lobby-brandings/totogaming-bg-tablet.565cfca.jpg","hostname":"static.egcdn.com","pathname":"/lobby-brandings/totogaming-bg-tablet.565cfca.jpg"},"startTime":4850.135,"duration":3.115,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":4850.135,"responseEnd":4853.25,"transferSize":0},{"name":{"href":"https://static.egcdn.com/lobby-brandings/totogaming-header-baccarat-squeeze.1e2e213.jpg","hostname":"static.egcdn.com","pathname":"/lobby-brandings/totogaming-header-baccarat-squeeze.1e2e213.jpg"},"startTime":4853.095,"duration":3.815,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":4853.095,"responseEnd":4856.91,"transferSize":0},{"name":{"href":"https://static.egcdn.com/#","hostname":"static.egcdn.com","pathname":"/"},"startTime":4854.95,"duration":61.295,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":4854.95,"responseEnd":4916.245,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/fonts/AvenirNextCyr-Medium.50e09.woff2","hostname":"static.egcdn.com","pathname":"/mobile/fonts/AvenirNextCyr-Medium.woff2"},"startTime":4858.575,"duration":2.625,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":4858.575,"responseEnd":4861.2,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/baccarat-active.fabec.svg","hostname":"static.egcdn.com","pathname":"/mobile/images/baccarat-active.svg"},"startTime":8811.185,"duration":2.77,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":8811.185,"responseEnd":8813.955,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/baccarat-passive.17669.svg","hostname":"static.egcdn.com","pathname":"/mobile/images/baccarat-passive.svg"},"startTime":8811.425,"duration":2.88,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":8811.425,"responseEnd":8814.305,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/poker-active.96179.svg","hostname":"static.egcdn.com","pathname":"/mobile/images/poker-active.svg"},"startTime":8811.66,"duration":2.835,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":8811.66,"responseEnd":8814.495,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/poker-passive.dd6de.svg","hostname":"static.egcdn.com","pathname":"/mobile/images/poker-passive.svg"},"startTime":8811.86,"duration":3.395,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":8811.86,"responseEnd":8815.255,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/chp.78b89.png","hostname":"static.egcdn.com","pathname":"/mobile/images/chp.png"},"startTime":8877.745,"duration":1.795,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":8877.745,"responseEnd":8879.54,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/lobby-lightning-spritesheet.dc183.png","hostname":"static.egcdn.com","pathname":"/mobile/images/lobby-lightning-spritesheet.png"},"startTime":8930.4,"duration":2.965,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":8930.4,"responseEnd":8933.365,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/vendor.6f3d2.js","hostname":"static.egcdn.com","pathname":"/mobile/js/vendor.js"},"startTime":8973.81,"duration":95.22,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":8973.81,"responseEnd":9069.03,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/commons.desktop.3eb80.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/commons.desktop.css"},"startTime":8974.865,"duration":90.315,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":8974.865,"responseEnd":9065.18,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/commons.desktop.3eb80.js","hostname":"static.egcdn.com","pathname":"/mobile/js/commons.desktop.js"},"startTime":8975.795,"duration":110.085,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":8975.795,"responseEnd":9085.88,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/desktopRoulette.e1829.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/desktopRoulette.css"},"startTime":8976.835,"duration":83.17,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":8976.835,"responseEnd":9060.005,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/desktopRoulette.e1829.js","hostname":"static.egcdn.com","pathname":"/mobile/js/desktopRoulette.js"},"startTime":8977.81,"duration":105.55,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":8977.81,"responseEnd":9083.36,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/desktopMoneyWheel.8110f.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/desktopMoneyWheel.css"},"startTime":8979.275,"duration":4.815,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":8979.275,"responseEnd":8984.09,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/desktopMoneyWheel.8110f.js","hostname":"static.egcdn.com","pathname":"/mobile/js/desktopMoneyWheel.js"},"startTime":8980.83,"duration":12.775,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":8980.83,"responseEnd":8993.605,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/poker.casino-holdem.desktop.aa756.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/poker.casino-holdem.desktop.css"},"startTime":8982.19,"duration":15.53,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":8982.19,"responseEnd":8997.72,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/poker.casino-holdem.desktop.aa756.js","hostname":"static.egcdn.com","pathname":"/mobile/js/poker.casino-holdem.desktop.js"},"startTime":8983.56,"duration":36.635,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":8983.56,"responseEnd":9020.195,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/baccarat.desktop.26578.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/baccarat.desktop.css"},"startTime":8984.515,"duration":18.72,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":8984.515,"responseEnd":9003.235,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/baccarat.desktop.26578.js","hostname":"static.egcdn.com","pathname":"/mobile/js/baccarat.desktop.js"},"startTime":8985.655,"duration":30.46,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":8985.655,"responseEnd":9016.115,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/styles/js/dragonTiger.desktop.8f775.css","hostname":"static.egcdn.com","pathname":"/mobile/styles/js/dragonTiger.desktop.css"},"startTime":8987.545,"duration":15.005,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":8987.545,"responseEnd":9002.55,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/js/dragonTiger.desktop.8f775.js","hostname":"static.egcdn.com","pathname":"/mobile/js/dragonTiger.desktop.js"},"startTime":8989.1,"duration":22.495,"initiatorType":"link","nextHopProtocol":"h2","fetchStart":8989.1,"responseEnd":9011.595,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/lightr1_imrs_med_L.jpg?q=1574516822949","hostname":"lob.egcvi.com","pathname":"/thumbnail/lightr1_imrs_med_L.jpg"},"startTime":9031.785,"duration":1245.19,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":9031.785,"responseEnd":10276.975,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/green_imrs_med_L.jpg?q=1574516822949","hostname":"lob.egcvi.com","pathname":"/thumbnail/green_imrs_med_L.jpg"},"startTime":9032.28,"duration":1281.255,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":9032.28,"responseEnd":10313.535,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/dc1_mw_med_L.jpg?q=1574516822950","hostname":"lob.egcvi.com","pathname":"/thumbnail/dc1_mw_med_L.jpg"},"startTime":9032.59,"duration":1275.755,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":9032.59,"responseEnd":10308.345,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/immersive_med_L.jpg?q=1574516822950","hostname":"lob.egcvi.com","pathname":"/thumbnail/immersive_med_L.jpg"},"startTime":9032.895,"duration":1231.41,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":9032.895,"responseEnd":10264.305,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/pk_gen_med_L.jpg?q=1574516822950","hostname":"lob.egcvi.com","pathname":"/thumbnail/pk_gen_med_L.jpg"},"startTime":10267.205,"duration":1195.355,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":10267.205,"responseEnd":11462.56,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/bac5_bs_med_L.jpg?q=1574516822950","hostname":"lob.egcvi.com","pathname":"/thumbnail/bac5_bs_med_L.jpg"},"startTime":10279.625,"duration":15.27,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":10279.625,"responseEnd":10294.895,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/topctm1_bs_med_L.jpg?q=1574516822950","hostname":"lob.egcvi.com","pathname":"/thumbnail/topctm1_bs_med_L.jpg"},"startTime":10297.14,"duration":1199.81,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":10297.14,"responseEnd":11496.95,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/fonts/AvenirNextCyr-Demi.19191.woff2","hostname":"static.egcdn.com","pathname":"/mobile/fonts/AvenirNextCyr-Demi.woff2"},"startTime":12080.205,"duration":3.52,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":12080.205,"responseEnd":12083.725,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/dragonara.4963e.png","hostname":"static.egcdn.com","pathname":"/mobile/images/dragonara.png"},"startTime":15883.025,"duration":2.445,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":15883.025,"responseEnd":15885.47,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/ribbon-roti.f8409.png","hostname":"static.egcdn.com","pathname":"/mobile/images/ribbon-roti.png"},"startTime":15883.475,"duration":2.435,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":15883.475,"responseEnd":15885.91,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/dbr.bfc36.png","hostname":"static.egcdn.com","pathname":"/mobile/images/dbr.png"},"startTime":15883.815,"duration":2.65,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":15883.815,"responseEnd":15886.465,"transferSize":0},{"name":{"href":"https://static.egcdn.com/mobile/images/grand_casino.1de3d.png","hostname":"static.egcdn.com","pathname":"/mobile/images/grand_casino.png"},"startTime":15884.53,"duration":2.68,"initiatorType":"css","nextHopProtocol":"h2","fetchStart":15884.53,"responseEnd":15887.21,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/tk2_imr_med_L.jpg?q=1574516829905","hostname":"lob.egcvi.com","pathname":"/thumbnail/tk2_imr_med_L.jpg"},"startTime":15979.485,"duration":1194.64,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":15979.485,"responseEnd":17174.125,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/rugent1_imrs_med_L.jpg?q=1574516829905","hostname":"lob.egcvi.com","pathname":"/thumbnail/rugent1_imrs_med_L.jpg"},"startTime":15979.835,"duration":1236.675,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":15979.835,"responseEnd":17216.51,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/vipr1_imrs_med_L.jpg?q=1574516829905","hostname":"lob.egcvi.com","pathname":"/thumbnail/vipr1_imrs_med_L.jpg"},"startTime":15980.03,"duration":1200.855,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":15980.03,"responseEnd":17180.885,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/gen1_ss_med_L.jpg?q=1574516829928","hostname":"lob.egcvi.com","pathname":"/thumbnail/gen1_ss_med_L.jpg"},"startTime":15980.22,"duration":1196.325,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":15980.22,"responseEnd":17176.545,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/vip1_ss_med_L.jpg?q=1574516829928","hostname":"lob.egcvi.com","pathname":"/thumbnail/vip1_ss_med_L.jpg"},"startTime":17177.59,"duration":255.22,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":17177.59,"responseEnd":17432.81,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/spa_ss_med_L.jpg?q=1574516829929","hostname":"lob.egcvi.com","pathname":"/thumbnail/spa_ss_med_L.jpg"},"startTime":17190.4,"duration":1200.16,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":17190.4,"responseEnd":18390.56,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/drago_imr_med_L.jpg?q=1574516829929","hostname":"lob.egcvi.com","pathname":"/thumbnail/drago_imr_med_L.jpg"},"startTime":17193.2,"duration":1161.935,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":17193.2,"responseEnd":18355.135,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/dbr_imr_med_L.jpg?q=1574516829929","hostname":"lob.egcvi.com","pathname":"/thumbnail/dbr_imr_med_L.jpg"},"startTime":17224.88,"duration":1201.415,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":17224.88,"responseEnd":18426.295,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/speed1_imr_med_L.jpg?q=1574516829929","hostname":"lob.egcvi.com","pathname":"/thumbnail/speed1_imr_med_L.jpg"},"startTime":17435.82,"duration":261.57,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":17435.82,"responseEnd":17697.39,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/gcro1_imr_med_L.jpg?q=1574516829929","hostname":"lob.egcvi.com","pathname":"/thumbnail/gcro1_imr_med_L.jpg"},"startTime":17701.39,"duration":258.29,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":17701.39,"responseEnd":17959.68,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/dzerot1_imr_med_L.jpg?q=1574516829929","hostname":"lob.egcvi.com","pathname":"/thumbnail/dzerot1_imr_med_L.jpg"},"startTime":17967.31,"duration":1184.035,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":17967.31,"responseEnd":19151.345,"transferSize":0},{"name":{"href":"https://lob.egcvi.com/thumbnail/casmlt1_imr_med_L.jpg?q=1574516829929","hostname":"lob.egcvi.com","pathname":"/thumbnail/casmlt1_imr_med_L.jpg"},"startTime":18360.265,"duration":264.03,"initiatorType":"img","nextHopProtocol":"h2","fetchStart":18360.265,"responseEnd":18624.295,"transferSize":0}],"mark":[{"name":"socketOpen","startTime":6894.395},{"name":"socketOpen","startTime":7840.5},{"name":"evoLoaderClosed","startTime":8857.63},{"name":"_evoReportGenerated","startTime":23861.11}],"first-input":[{"name":"mousedown","startTime":14477.695,"duration":16,"processingStart":14479.585,"processingEnd":14479.975,"cancelable":true}]},"evoLoaderClosed":8857.63}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
                                ws.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')
                                ws.send(json.dumps({"log":{"type":"CLIENT_LOBBY_TABLE_JOIN_CLICK","latency":615,"value":{"currency":"KRW","gameType":"lobby","buildId":"Build Version: 6.20191108.112731-c9cf0c5d at 2019-11-08 12:30:13","device":"Desktop","typeApp":"lobby4","categoryId":"roulette","tablesCount":16,"layout":"Medium","filter":"NotAvailable","timeInLobby":12376,"tableId":"7x0b1tgh7agmf6hv","tableName":"이머지브 룰렛","tableOrder":1,"channel":"PCMac","orientation":"landscape","balance":0,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36","inGame":false}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('qqqqqqqqqqqqqqqqqqqqqqqqq')
                                ws.send(json.dumps({"log":{"type":"CLIENT_PRESSED_INGAME_LOBBY_CLOSE","latency":615,"value":{"currency":"KRW","gameType":"lobby","buildId":"Build Version: 6.20191108.112731-c9cf0c5d at 2019-11-08 12:30:13","device":"Desktop","typeApp":"lobby4","categoryId":"roulette","target":"InGame Lobby","timeInLobby":12379,"channel":"PCMac","orientation":"landscape","balance":0,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36","inGame":true}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('222222222222222222222222222')
                                ws.send(json.dumps({"log":{"type":"CLIENT_LOBBY_EXIT","latency":615,"value":{"currency":"KRW","gameType":"lobby","buildId":"Build Version: 6.20191108.112731-c9cf0c5d at 2019-11-08 12:30:13","device":"Desktop","typeApp":"lobby4","categoryId":"roulette","timeInLobby":12380,"channel":"PCMac","orientation":"landscape","balance":0,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36","inGame":true}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('333333333333333333333333333')
                                ws.send(json.dumps({"id":wid(),"type":"settings.read","args":{"key":"generic.common"}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('111111111111111111111111111111')
                                ws.send(json.dumps({"id":wid(),"type":"settings.read","args":{"key":"generic.mobile"}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('4444444444444444444444444444444')
                                ws.send(json.dumps({"id":wid(),"type":"settings.read","args":{"key":"roulette.common"}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('555555555555555555555555555555555')
                                ws.send(json.dumps({"log":{"type":"CLIENT_GAME_LOADED","value":{"typeApp":"roulette","buildId":"6.20191121.111140-2c066ecb","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36","url":"https://livecasino.eg88play.com/mobile/#table_id=LightningTable01&category=roulette&game=roulette","channel":"PCMac","orientation":"landscape"}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('6666666666666666666666666666666')
                                ws.send(json.dumps({"log":{"type":"CLIENT_SOCKET_CONNECTION_ESTABLISHED","value":{"offline":false,"channel":"PCMac","orientation":"landscape"}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('77777777777777777777777777777777777')
                                ws.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('88888888888888888888888888888888888')
                                ws.send(json.dumps({"id":wid(),"type":"favouriteBets.loadBets","args":{"queryString":{"tableId":"LightningTable01"}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('999999999999999999999999999999999999999')
                                ws.send(json.dumps({"log":{"type":"CLIENT_BALANCE_UPDATED","value":{"currency":"₩","balance":0,"channel":"PCMac","orientation":"landscape"}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                                ws.send(json.dumps({"id":wid(),"type":"settings.update","args":{"key":"generic.common.gameSoundVolume","data":1}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
                                ws.send(json.dumps({"id":wid(),"type":"settings.update","args":{"key":"generic.common.studioSoundVolume","data":1}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('sssssssssssssssssssssssssssssssssssss')
                                ws.send(json.dumps({"log":{"type":"CLIENT_RECEIVE_ON_BOARDING","value":{"channel":"PCMac","sessionData":{"game":"roulette"},"orientation":"landscape"}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('ddddddddddddddddddddddddddddddddddddddddd')
                                ws.send(json.dumps({"log":{"type":"CLIENT_POPUP_DISPLAYED","value":{"popupId":"PopupId.LOW_BALANCE","channel":"PCMac","orientation":"landscape"}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('ffffffffffffffffffffffffffffffffffffffffff')
                                ws.send(json.dumps({"log":{"type":"CLIENT_VIDEO_V2_INITIALIZED","value":{"device":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36","screenSize":"","type":"desktop","name":"unknown","browser":{"family":"Chrome","version":"78.0.3904.108"},"os":{"family":"Windows","version":"10.0"}},"client":{"pointInTime":0,"videoSessionId":"nx54o66tzywcx35y-98d41fcfa58b84ac3ef0670738bf09d2b009fb039b2f65c2018d51771997d4e799f8bae75073d499-LightningTable01-856bd4","referer":"livecasino.eg88play.com","componentLoadingTime":3081},"component":{"version":"v5.132.6_5.20191121.133411_aed9d4c6","scenario":""},"video":{"masterHost":"live1.egcvi.com"},"channel":"PCMac","orientation":"landscape"}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                                ws.send(json.dumps({"log":{"type":"CLIENT_VIDEO_PLAYBACK_EVENT","value":{"playbackEventData":{"timestamp":tt(),"playbackEventType":"PLAYER_ATTEMPT","data":{"playerEventHistory":"flvjs","firstVideoSessionId":"nx54o66tzywcx35y-98d41fcfa58b84ac3ef0670738bf09d2b009fb039b2f65c2018d51771997d4e799f8bae75073d499-LightningTable01-856bd4"},"reason":"PLAYER_ATTEMPT"},"sessionData":{"game":"roulette","videoSessionId":"nx54o66tzywcx35y-98d41fcfa58b84ac3ef0670738bf09d2b009fb039b2f65c2018d51771997d4e799f8bae75073d499-LightningTable01-856bd4"},"channel":"PCMac","orientation":"landscape"}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzf')
                                ws.send(json.dumps({"log":{"type":"CLIENT_VIDEO_V2_PLAYBACK_ATTEMPT","value":{"game":"roulette","sessionData":{"game":"roulette","videoSessionId":"nx54o66tzywcx35y-98d41fcfa58b84ac3ef0670738bf09d2b009fb039b2f65c2018d51771997d4e799f8bae75073d499-LightningTable01-856bd4"},"channel":"PCMac","orientation":"landscape"}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('ccccccccccccccccccccccccccccccccccccccccccccccccccc')
                                ws.send(json.dumps({"log":{"type":"CLIENT_PRESSED_START_VIDEO","value":{"sessionData":{"game":"roulette","videoSessionId":"nx54o66tzywcx35y-98d41fcfa58b84ac3ef0670738bf09d2b009fb039b2f65c2018d51771997d4e799f8bae75073d499-LightningTable01-856bd4"},"channel":"PCMac","pressedStart":true,"orientation":"landscape"}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv')
                                ws.send(json.dumps({"log":{"type":"CLIENT_EXITED_RFB_EDIT_MODE","value":{"channel":"PCMac","orientation":"landscape"}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
                                ws.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print('nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn')
                                ws.send(json.dumps({"log":{"type":"CLIENT_VIDEO_V2_FIRST_FRAME","value":{"timestamp":tt(),"deviceType":"desktop","qualityType":"MEDIUM","streamName":"lightr1_imr_med","videoInitTime":2832,"sessionData":{"game":"roulette","videoSessionId":"nx54o66tzywcx35y-98d41fcfa58b84ac3ef0670738bf09d2b009fb039b2f65c2018d51771997d4e799f8bae75073d499-LightningTable01-856bd4"},"channel":"PCMac","orientation":"landscape"}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
                                ws.send(json.dumps({"log":{"type":"CLIENT_VIDEO_LOADING_TIME","value":{"timestamp":tt(),"deviceType":"desktop","qualityType":"MEDIUM","streamName":"lightr1_imr_med","videoInitTime":2834,"sessionData":{"game":"roulette","videoSessionId":"nx54o66tzywcx35y-98d41fcfa58b84ac3ef0670738bf09d2b009fb039b2f65c2018d51771997d4e799f8bae75073d499-LightningTable01-856bd4"},"channel":"PCMac","orientation":"landscape"}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                                ws.send(json.dumps({"log":{"type":"CLIENT_VIDEO_HANDSHAKE","value":{"sessionData":{"game":"roulette","videoSessionId":"nx54o66tzywcx35y-98d41fcfa58b84ac3ef0670738bf09d2b009fb039b2f65c2018d51771997d4e799f8bae75073d499-LightningTable01-856bd4"},"systemInfo":{"timestamp":tt(),"systemLanguage":"ko","deviceType":"desktop","videoPlayerName":"flvjs","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36","deviceName":"unknown","os":"Windows 10.0","browser":"Chrome 78.0.3904.108","pixelAspectRatio":1.25,"videoSettingsVersion":"","videoSettingsLogic":""},"channel":"PCMac","orientation":"landscape"}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                                ws.send(json.dumps({"log":{"type":"CLIENT_VIDEO_PLAYBACK_EVENT","value":{"playbackEventData":{"timestamp":tt(),"playbackEventType":"PLAYER_STARTED","data":{"playerEventHistory":"flvjs","firstVideoSessionId":"nx54o66tzywcx35y-98d41fcfa58b84ac3ef0670738bf09d2b009fb039b2f65c2018d51771997d4e799f8bae75073d499-LightningTable01-856bd4"},"reason":"PLAYER_STARTED"},"sessionData":{"game":"roulette","videoSessionId":"nx54o66tzywcx35y-98d41fcfa58b84ac3ef0670738bf09d2b009fb039b2f65c2018d51771997d4e799f8bae75073d499-LightningTable01-856bd4"},"channel":"PCMac","orientation":"landscape"}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
                                ws.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
                                ws.send(json.dumps({"log":{"type":"CLIENT_VIDEO_PLAYBACK_EVENT","value":{"playbackEventData":{"timestamp":tt(),"playbackEventType":"UPGRADE","data":{"prev":"MEDIUM","next":"HIGH","playerEventHistory":"flvjs","firstVideoSessionId":"nx54o66tzywcx35y-98d41fcfa58b84ac3ef0670738bf09d2b009fb039b2f65c2018d51771997d4e799f8bae75073d499-LightningTable01-856bd4"},"reason":"SUFFICIENT_BANDWIDTH"},"sessionData":{"game":"roulette","videoSessionId":"nx54o66tzywcx35y-98d41fcfa58b84ac3ef0670738bf09d2b009fb039b2f65c2018d51771997d4e799f8bae75073d499-LightningTable01-856bd4"},"channel":"PCMac","orientation":"landscape"}}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print("GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
                                ws.send(json.dumps({"id":wid(),"type":"metrics.ping","args":{"t":tt()}}))
                                for oo in range(50):
                                    result =  ws.recv()
                                    print(result)
                                print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
                            if Rads == 4:
                                print('블랙 배팅','홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                            elif Rads > 4:
                                print('블랙 2배 배팅','홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                            else:
                                print("qq")
                            if ups == 4:
                                print('다운 배팅','홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                            elif ups > 4:
                                print('다운 2배 배팅','홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                            else:
                                print("rr")
'''                            
elif x == 'lkcbrbdckjxajdol':
                    nm2.append(int(data['args']['numbers']['results'][i][0]['number']))
                    nmaa2 +=1
                    if nma2 == 0 and nmaa2 == 12:
                        nma2 +=1
                        print ()
                elif x == 'r5aw9yumyaxgnd90':
                    for i in range(len(data['args']['numbers']['results'])):
                            nm3.append(int(data['args']['numbers']['results'][i][0]['number']))
                            nmaa3 +=1
                        if nma3 == 0 and nmaa3 == 12:
                            nma3 +=1
                            print ()
                elif x == 'wzg6kdkad1oe7m5k':
                    for i in range(len(data['args']['numbers']['results'])):
                            nm4.append(int(data['args']['numbers']['results'][i][0]['number']))
                            nmaa4 +=1
                        if nma4 == 0 and nmaa4 == 12:
                            nma4 +=1
                            print ()
                elif x == 'zosmk25g2f768o52':
                    for i in range(len(data['args']['numbers']['results'])):
                            nm5.append(int(data['args']['numbers']['results'][i][0]['number']))
                            nmaa5 +=1
                        if nma5 == 0 and nmaa5 == 12:
                            nma5 +=1
                            print ()
                elif x == 'vctlz20yfnmp1ylr':
                    for i in range(len(data['args']['numbers']['results'])):
                            nm6.append(int(data['args']['numbers']['results'][i][0]['number']))
                            nmaa6 +=1
                        if nma6 == 0 and nmaa6 == 12:
                            nma6 +=1
                            print ('룰렛')
                elif x == 'AmericanTable001':
                    for i in range(len(data['args']['numbers']['results'])):
                            nm7.append(int(data['args']['numbers']['results'][i][0]['number']))
                            nmaa7 +=1
                        if nma1 == 0 and nmaa7 == 12:
                            nma1 +=1
                            print ()
                elif x == 'LightningTable01':
                    for i in range(len(data['args']['numbers']['results'])):
                            nm8.append(int(data['args']['numbers']['results'][i][0]['number']))
                            nmaa8 +=1
                        if nma8 == 0 and nmaa8 == 12:
                            nma8 +=1
                            print ('라이트링 룰렛')
                elif x == 'DoubleBallRou001':
                    for i in range(len(data['args']['numbers']['results'])):
                            nm9.append(int(data['args']['numbers']['results'][i][0]['number']))
                            nmaa9 +=1
                        if nma9 == 0 and nmaa9 == 12:
                            nma9 +=1
                            print ()
                elif x == '01rb77cq1gtenhmo':
                    for i in range(len(data['args']['numbers']['results'])):
                            nm10.append(int(data['args']['numbers']['results'][i][0]['number']))
                            nmaa10 +=1
                        if nma10 == 0 and nmaa10 == 12:
                            nma10 +=1
                            print ()
                elif x == '48z5pjps3ntvqc1b':
                    for i in range(len(data['args']['numbers']['results'])):
                            nm11.append(int(data['args']['numbers']['results'][i][0]['number']))
                            nmaa11 +=1
                        if nma11 == 0 and nmaa11 == 12:
                            nma11 +=1
                            print ()
                elif x == 'f1f4rm9xgh4j3u2z':
                    for i in range(len(data['args']['numbers']['results'])):
                            nm12.append(int(data['args']['numbers']['results'][i][0]['number']))
                            nmaa12 +=1
                        if nma12 == 0 and nmaa12 == 12:
                            nma12 +=1
                            print ()
                elif x == 'q0a470up68p2b81p':
                    for i in range(len(data['args']['numbers']['results'])):
                            nm13.append(int(data['args']['numbers']['results'][i][0]['number']))
                            nmaa13 +=1
                        if nma13 == 0 and nmaa13 == 12:
                            nma13 +=1
                            print ()
                elif x == 'mvrcophqscoqosd6':
                    for i in range(len(data['args']['numbers']['results'])):
                            nm14.append(int(data['args']['numbers']['results'][i][0]['number']))
                            nmaa14 +=1
                        if nma14 == 0 and nmaa14 == 12:
                            nma14 +=1
                            print ()
                elif x == 'lr6t4k3lcd4qgyrk':
                    for i in range(len(data['args']['numbers']['results'])):
                            nm15.append(int(data['args']['numbers']['results'][i][0]['number']))
                            nmaa15 +=1
                        if nma15 == 0 and nmaa15 == 12:
                            nma15 +=1
                            print ()
                elif x == 'lobby.tableDetails':
                    for i in range(len(data['args']['numbers']['results'])):
                            nm16.append(int(data['args']['numbers']['results'][i][0]['number']))
                            nmaa16 +=1
                        if nma16 == 0 and nmaa16 == 12:
                            nma16 +=1
                            print ()  
                else:
                    print (x)'''

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
              
            
            








    
