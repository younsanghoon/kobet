import requests
import xmltodict
import json
import mechanicalsoup

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
#addr4 = json.loads(r.test)[메시지]

def tt():
    return str(time.time()).replace("." , "")[:13]
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
Accept-Encoding: gzip, deflate,
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
Accept-Encoding: gzip, deflate,
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
Accept-Encoding: gzip, deflate,
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

#data = 'GameName=&Email=can741&Password=1q2w3e4r!!&captcha-guid=6b9422aa16e546a990ee6ec757a6f87c&Captcha=&gameUrl=&loginHref='
data = 'Email=can741&Password=1q2w3e4r!!'
addr1 = 'https://kobet-1.com/Mobile/IsMobile?IsMobile=true'
addr2 = 'https://kobet-1.com/ko/Login/Login'
addr3 = 'https://kobet-1.com/LiveCasino/GetLiveCasinoUrl?url='
addr4 = 'https://livecasino.eg88play.com/cgibin/UserAuthentication?cCode=REQ&output=0&uaID=totogaming000002ml7f99a9xvjj1dkq&uaID_pass=u2sOVTykAkj5Q38j&euID=878048&country=UK&currency=KRW&lang=ko&ac=1&nickname=can741&firstname=%EC%83%81%ED%9B%88&lastname=%EC%9C%A4&page=100&site=1&tid=w105y73iv1r8fnzv&sid=bb15d2cba6304c06b77f3dd8b867d26b&gtype=live-casino-custom-build-flash'
addr5 = 'https://livecasino.eg88play.com/entry?cc=1&JSESSIONID=e5e61c581ffda03e0cade2caeb5b1522ae54df4c&params=Z2FtZT1saXZlLWNhc2luby1jdXN0b20tYnVpbGQtZmxhc2gKc2l0ZT0x'
browser = mechanicalsoup.StatefulBrowser()

with requests.session() as sess:
    r1 = sess.get(addr1, headers=pharseHeaders(head1), verify=False)
    print (r1,'r1')
    if r1.status_code == 200:
        r2 = sess.post(addr2, verify=False, headers=pharseHeaders(head2), data=data.encode())
        print (r2,'r2')
        if r2.status_code == 200:
            r3 = sess.get(addr3, headers=pharseHeaders(head3), verify=False)
            print (r3,'r3')
            if r3.status_code == 200:
                gameURL = r3.content.decode()
                print (gameURL)
                b = sess.get(gameURL, verify=False, headers=head3)
                print (b,'b')
                if b.status_code == 200:
                    c = sess.get(addr5, verify=False, headers=head1)
                    print (c,'c')
                    if c.status_code == 200:
                        if "EVOSESSIONID" in browser.get_cookiejar().keys():
                        #break
                            print("EVOSESSIONID" , browser.get_cookiejar()['EVOSESSIONID'])
                            input("...")

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

