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
from PyQt4 import QtCore, QtGui
import webSocket
from websocket import create_connection
import math
import datetime
from telepot import Bot, glance
from telepot.loop import MessageLoop
from time import sleep
import pprint








def date_diff_in_seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds

def dhms_from_seconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


def tt():
    return str(time.time()).replace("." , "")[:13]
def wid(length=10):
    strCase = string.ascii_lowercase+string.ascii_uppercase+string.digits
    return ''.join(random.choice(strCase) for x in range(length))


class kibetWebsocket():
    def __init__(self , sessId = ''  , host = '' , roomCnt = 0):
        self.loop = True
        self.Alive = True
        self.host = host
        self.sessId = sessId
        self.betDiv = {}
        self.history = {}
        self.tableIdbyTname = {}
        self.roomCnt = roomCnt
        self.saving = False
        self.savedDayBefore = time.localtime()[2]

    def run(self):
        try:
            self.wd = time.time()
            self.betPattern = [ 2**i for i in range(50)]
            self.betPatterns = {}
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



            #'livecasino.kibet-3.com'
            ws = create_connection("wss://%s/public/lobby/player/socket?messageFormat=json"%self.host, header=headers)

            webSocket.init(ws)

            self.betMin = {}
            self.betMax = {}




            i = 0
            while self.loop:
                try:
                    i+=1
                    if ( time.time() - self.wd) > 5:
                        break

                    result = ws.recv()
                    data = json.loads(result)

                    if data["type"] == "lobby.tables":
                        for t in data['args']['tables']:
                            if t['name'] not in ['VIP 룰렛', '더블 볼 룰렛', "룰렛 라이브"]:
                                self.tables[t['tableId']] = t['name']
                                #self.tableIdbyTname[t['name']] == t['tableId']
                                self.answers[t['tableId']] = [0]
                                self.history[ t['name']] = []
                                #print(t['name'])
                                self.betMin[t['name']] = int(t['betLimits']['min'])
                                self.betMax[t['name']] = int(t['betLimits']['max'])
                                if self.betMin[t['name']] == 160:
                                    self.betDiv[t['name']] = 0
                                else:
                                    if  t['name']  =='아메리칸 룰렛':
                                        self.betDiv[t['name']] = int(math.log2(self.betMin[t['name']] / 160)) + 2
                                    else:
                                        self.betDiv[t['name']] = int( math.log2(self.betMin[t['name']] / 160) ) +1

                                self.tableIds.append(t['tableId'])
                                self.betPatterns[t['name']] = 'ready'



                    if data["type"] == "lobby.rouletteNumbersUpdated":
                        self.answers[data["args"]['tableId']] = [ int(x[0]['number']) for x in data['args']['numbers']['results']]
                        tid = data["args"]['tableId']


                        try:
                            if tid not in ['DoubleBallRou001' ,'zosmk25g2f768o52' ]:
                                tname = self.tables[tid]
                                if tname not in ['VIP 룰렛', '더블 볼 룰렛' , "룰렛 라이브"]:
                                    self.history[tname].append(self.answers[data["args"]['tableId']][0])
                        except:
                            print("history error" , tname , traceback.format_exc())
                        lc = time.localtime()
                        today = "%d_%02d_%02d"%(lc[0] , lc[1] , lc[2])
                        if os.path.isdir("./history") == False:
                            os.mkdir("./history")
                        if time.localtime()[2] != self.savedDayBefore:
                            with open("./history/%s.pkl"%today , 'wb') as f:
                                pickle.dump(self.history , f)
                                self.savedDayBefore = time.localtime()[2]
                                for tn in self.history:
                                    self.history[tn] = []





                    if data['type'] == 'lobby.tableDetails':
                        for tx in data['args']['tables']:
                            #print("2" ,tx['tableId'])
                            self.answers[tx['tableId']] = [ int(x[0]['number']) for x in  tx['roulette']['numbers']['results']]

                    if i % self.roomCnt == 0:
                        i = 0
                        ws.send(json.dumps('{"id":"%s","type":"metrics.ping","args":{"t":%s}}' % (wid(), tt())))

                except:
                    print("seesion loop fail", traceback.format_exc())
                    #print(result)
        except:
            print("seesion die" , traceback.format_exc())
            print(result)
        self.Alive = False
        ws.close()




class Ui_Form(object):
    def __init__(self,Form,teleUse = False):
        QtGui.QMainWindow.__init__(Form, None, QtCore.Qt.WindowStaysOnTopHint)
        self.Form = Form
        self.myid = None
        self.teleInit = False
        self.teleWd = time.time()
        self.get_mac()
        self.roomCnt = 14
        self.teleUse = teleUse
        self.triMart = [1, 1, 2, 3, 4, 6, 9, 14, 21, 31, 47, 70, 105, 158, 237, 355, 533, 799,
                        1199, 1798, 2697, 4046, 6069, 9103, 13655, 20482, 30723, 46085, 69127,
                        103691, 155536, 233304, 349956, 524934, 787401, 1181102, 1771653, 2657479,
                        3986219, 5979328, 8968992, 13453488]
    def get_mac(self):
        mac_num = hex(uuid.getnode()).replace('0x', '').upper()
        #print(mac_num)

        mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
        #print(mac)
        if mac.strip() not in ["E8-03-9A-6D-CD-FF", 'B0-6E-BF-BA-95-B0', 'C2-96-75-23-C-', 'D0-27-88-BB-78-84']:
            QtGui.QMessageBox.about(self.Form, "알람", "허가되지 않은 PC 입니다")
            sys.exit(-1)
        #print(mac)
        #return mac


    def teleInitLoop(self):
        self.teleInit = False

        while 1:
            time.sleep(1)
            if (time.time() - self.teleWd) > 5:
                break
            if self.myid:
                self.bot = Bot('534030291:AAFvzLTcpAGjpq9AQwyyK7t_QpDDFWZA23g')
                self.teleInit = True
                if self.teleUse:
                    self.bot.sendMessage(50808032, "시작")
                break
            


    def setupUi(self, width, height):

        self.reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

        self.browser = mechanicalsoup.StatefulBrowser()



        Form = self.Form
        Form.setObjectName(_fromUtf8("Form"))
        Form.setGeometry(QtCore.QRect(width/2 - 900, height- 360, 1800 , 350))
        Form.setFixedSize(1800 , 350)


        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(600, 10, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        #self.pushButton.setDisabled(True)

        self.showDetail = QtGui.QPushButton(Form)
        self.showDetail.setGeometry(QtCore.QRect(700, 10, 75, 23))
        self.showDetail.setText(_fromUtf8("자세히"))
        self.detail = False


        self.myid = QtGui.QLabel(Form)
        self.myid.setGeometry(QtCore.QRect(250, 11, 10, 20))
        self.myid.setText(_fromUtf8("ID"))
        self.myIdInput = QtGui.QLineEdit(Form)
        self.myIdInput.setGeometry(QtCore.QRect(270, 11, 120, 20))
        self.myIdInput.setObjectName(_fromUtf8("lineEdit"))


        self.mypass = QtGui.QLabel(Form)
        self.mypass.setGeometry(QtCore.QRect(400, 11, 30, 20))
        self.mypass.setText(_fromUtf8("Pass"))
        self.myPassInput = QtGui.QLineEdit(Form)
        self.myPassInput.setGeometry(QtCore.QRect(430, 11, 120, 20))
        self.myPassInput.setObjectName(_fromUtf8("lineEdit"))
        self.myPassInput.setEchoMode(QtGui.QLineEdit.Password)


        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 11, 50, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 11, 60, 20))
        self.label.setText(_fromUtf8("방 갯수"))

        self.pocketLabel = QtGui.QLabel(Form)
        self.pocketLabel.setGeometry(QtCore.QRect(230, 230, 300, 20))
        self.pocketLabel.setText(_fromUtf8("◎잔고 : 00000000000000000" ))

        self.sucessCntLabel = QtGui.QLabel(Form)
        self.sucessCntLabel.setGeometry(QtCore.QRect(400, 230, 300, 20))
        self.sucessCntLabel.setText(_fromUtf8("◎성공 횟수 : 00000"))

        self.skipPocketLabel = QtGui.QLabel(Form)
        self.skipPocketLabel.setGeometry(QtCore.QRect(600, 230, 300, 20))
        self.skipPocketLabel.setText(_fromUtf8("★단계 적용 잔고 : 00000000000000000"))

        self.sucessCntLabelSkip = QtGui.QLabel(Form)
        self.sucessCntLabelSkip.setGeometry(QtCore.QRect(850, 230, 300, 20))
        self.sucessCntLabelSkip.setText(_fromUtf8("★단계 적용 성공 횟수 : 00000"))

        self.historyStack = QtGui.QTextBrowser(Form)
        self.historyStack.setGeometry(QtCore.QRect(1500, 10,  280, 300))
        self.historyStack.setStyleSheet(_fromUtf8('background-color: rgb(255, 255, 255)'))

        self.totalCntLabel = QtGui.QLabel(Form)
        self.totalCntLabel.setGeometry(QtCore.QRect(10, 250, 300, 20))
        self.totalCntLabel.setText(_fromUtf8("◎총 횟수 : 0"))

        self.totalTime = QtGui.QLabel(Form)
        self.totalTime.setGeometry(QtCore.QRect(10, 230, 300, 20))
        self.totalTime.setText(_fromUtf8("◎경과시간: 00일 00시간 00분 00초"))

        self.maxbetSkipLabel = QtGui.QLabel(Form)
        self.maxbetSkipLabel.setGeometry(QtCore.QRect(600, 250, 200, 20))
        self.maxbetSkipLabel.setText(_fromUtf8("★단계 적용 최고 베팅 : 0"))

        self.maxbetLabel = QtGui.QLabel(Form)
        self.maxbetLabel.setGeometry(QtCore.QRect(120, 250, 200, 20))
        self.maxbetLabel.setText(_fromUtf8("◎최고 베팅 : 0"))

        self.testLabel = QtGui.QLabel(Form)
        self.testLabel.setGeometry(QtCore.QRect(120, 280, 200, 20))
        self.testLabel.setText(_fromUtf8("0"))


        self.testLabel2 = QtGui.QLabel(Form)
        self.testLabel2.setGeometry(QtCore.QRect(160, 280, 200, 20))
        self.testLabel2.setText(_fromUtf8("0"))

        self.label2 = QtGui.QLabel(Form)
        self.label2.setGeometry(QtCore.QRect(10, 11, 60, 20))
        self.label2.setText(_fromUtf8("몇 단계"))
        self.label2.show()
        self.stepLimitVal = QtGui.QLineEdit(Form)
        self.stepLimitVal.setGeometry(QtCore.QRect(60, 11, 30, 20))
        self.stepLimitVal.setObjectName(_fromUtf8("lineEdit"))
        self.stepLimitVal.setText(_translate("Form", "0", None))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.lineEdit.setText(_translate("Form", str(10), None))
        self.lineEdit.setDisabled(True)
        self.wd = time.time()
        self.scoreEle = [['']*self.roomCnt for i in range(self.roomCnt)]
        self.currentAnswer = ['0' for i in range(self.roomCnt)]
        self.currentAnswers = ['__wait__' for i in range(self.roomCnt)]
        self.beforeAnswers = [copy.deepcopy(self.currentAnswer) for i in range(self.roomCnt)]
        self.history = [ { "br" : { "fwd":[1,0,0] , "bwd":[1,0,0] } ,
                           "eo" : { "fwd":[1,0,0] , "bwd":[1,0,0] } ,
                           "ud": {"fwd":[1,0,0] , "bwd":[1,0,0] } } for i in range(self.roomCnt)]


        self.failCnt =  [ { "짝" : 0,
                            "홀" : 0 ,
                            "적": 0,
                            "흑": 0,
                            "언더": 0,
                            "오버": 0,
                            "짝2": 0,
                            "홀2": 0,
                            "적2": 0,
                            "흑2": 0,
                            "언더2": 0,
                            "오버2": 0,
                            } for i in range(self.roomCnt)]

        self.beforeAnswer =  [ '' for i in range(self.roomCnt)]

        self.totalWinCnt = 0
        self.totalWinCntSkip = 0
        self.totalFailCnt = 0
        self.totalFailCntSkip = 0
        self.totalCnt = 0
        self.startTime = datetime.datetime.now()

        self.pocket  = 0

        self.skipPocket = 0

        self.successCnt = 0

        self.maxbetSkip = 0
        self.maxBet = 0

        self.stack = {}
        for i in range(50):
            self.stack[i] = 0

        self.bet =  [  { "짝" : 0,
                            "홀" : 0 ,
                            "적": 0,
                            "흑": 0,
                            "언더": 0,
                            "오버": 0,
                            "짝2": 0,
                            "홀2": 0,
                            "적2": 0,
                            "흑2": 0,
                            "언더2": 0,
                            "오버2": 0,
                            } for i in range(self.roomCnt)]


        self.skippingBet =   [  { "짝" : 0,
                            "홀" : 0 ,
                            "적": 0,
                            "흑": 0,
                            "언더": 0,
                            "오버": 0,
                            "짝2": 0,
                            "홀2": 0,
                            "적2": 0,
                            "흑2": 0,
                            "언더2": 0,
                            "오버2": 0,
                            }  for i in range(self.roomCnt)]


        self.rbPocket = {"흑":0 , "적" :0}
        self.betPattern = [2**i  for i in range(50)]
        self.betPatterns = []
        self.answers = [[]  for i in range(self.roomCnt)]

        try:
            with open("data.dat", 'r') as f:
                save = f.read()
                mId = save.split("\n")[0]
                mPass = save.split("\n")[1]
                self.myIdInput.setText(_translate("Form", mId, None))
                self.myPassInput.setText(_translate("Form", mPass, None))
        except:
            pass



        self.timeExtent = time.time()
        self.sessionId = ["" , ""]
        self.sessionInint = False
        self.sessionUdate = "ready"
        self.seesions = ['' , '' ]


        self.base = []
        self.roomName = []
        self.step = []
        self.step2 = []
        self.step3 = []
        self.steps = { "br" : self.step , "eo" : self.step2 , "ud" : self.step3}
        self.renew = False


        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start)

        QtCore.QObject.connect(self.showDetail, QtCore.SIGNAL(_fromUtf8("clicked()")), self.changeDetail)

        self.renewTime = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timeCheck)
        self.timer.start(1000)



        self.timer3 = QtCore.QTimer()
        self.timer3.timeout.connect(self.update)
        self.timer3.start(3000)


        self.teleInitThread = threading.Thread(target = self.teleInitLoop)
        self.teleInitThread.start()


        self.roomNames = [ "__wait__" for i in range(self.roomCnt)]
        self.roomFound = False

        self.timeLimit = time.time()




        try:
            with open("save.dat", 'r') as f:
                save = f.read()
                rn = save.split("\n")[0]
                lm = save.split("\n")[1]
                #self.lineEdit.setText(_translate("Form", 10, None))
                self.stepLimitVal.setText(_translate("Form", lm, None))
        except:
            pass


    def timeCheck(self):

        self.pocketLabel.setText(  _translate("Form","◎잔고 : %d"%int(self.pocket) , None))
        self.skipPocketLabel.setText(_translate("Form", "◎단계 적용 잔고 : %d" % int(self.skipPocket), None))
        self.sucessCntLabel.setText(_translate("Form", "◎성공 횟수 : %d"%self.totalWinCnt, None))
        self.sucessCntLabelSkip.setText(_translate("Form", "◎단계 적용 성공 횟수 : %d"%self.totalWinCntSkip , None ))
        timeDiff = "◎경과시간: %2d일 %d시간 %d분 %d초" % dhms_from_seconds(date_diff_in_seconds(datetime.datetime.now(),self.startTime))
        self.totalTime.setText(_translate("Form",timeDiff , None ))
        self.maxbetSkipLabel.setText(_translate("Form",'◎단계 적용 최고 베팅 : %d'%int(self.maxbetSkip) , None ))
        self.maxbetLabel.setText(_translate("Form", '◎최고 베팅 : %d' % int(self.maxBet), None))




        self.teleWd = time.time()
        if self.renewTime%120 == 0:
            if self.teleInit:
                stack = copy.deepcopy(self.stack)
                for i in range(49, -1, -1):
                    if stack[i] == 0:
                        stack.pop(i)
                    else:
                        break

                stacStr = ''
                for s in sorted(stack)[-3:]:
                    stacStr += '%d : %d\n' % (s, stack[s])
                timeDiff = "◎경과시간: %2d일 %d시간 %d분 %d초" % dhms_from_seconds(date_diff_in_seconds(datetime.datetime.now(), self.startTime))
                if self.teleUse:
                    self.bot.sendMessage(50808032, "%s\nid:%s\n잔고:%d\n횟수:%d\n단계잔고:%d\n단계횟수:%d\n단계최대:%d\n%s"%(timeDiff,self.myid , int(self.pocket),int(self.totalWinCnt),int(self.skipPocket),int(self.totalWinCntSkip) , int(self.maxbetSkip),stacStr) )
                pass
        if self.renewTime == 600:
            self.th = threading.Thread(target=self.runWebsocket)
            self.th.start()
            self.renewTime = 0
        self.renewTime+=1








    def changeDetail(self):
        if self.detail == False:
            self.showDetail.setText(_translate("Form", "간단히", None))
            self.detail = True
            self.showInform()

        else:
            self.showDetail.setText(_translate("Form", "자세히", None))
            self.detail = False
            self.showInform()




    #def getSession(self):







    def runWebsocket(self,init = True , dummy= ''):
        self.sessionHeaders = {}
        self.sessionHeaders["Connection"] = "keep-alive"
        self.sessionHeaders["Origin"] = "https://kibet-3.com"
        # self.sessionHeaders['Content - Length'] =  '41'
        self.sessionHeaders['Accept'] = '*/*'
        self.sessionHeaders["X-Requested-With"] = "XMLHttpRequest"
        self.sessionHeaders["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        self.sessionHeaders["Referer"] = "https://kibet-3.com/"
        self.sessionHeaders["Accept-Encoding"] = "gzip, deflate, br"
        self.sessionHeaders["Accept-Language"] = "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
        self.sessionHeaders["User-Agent"] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        self.sessionInint = False
        try:
            myInfo = b"Email=%s&Password=%s&gameUrl=" % (str(self.myIdInput.text()).strip().encode(), str(self.myPassInput.text()).strip().encode())
            self.myid = str(self.myIdInput.text()).strip()
            #print(myInfo)
            self.sessionUdate = "ready"
            for i in range(5):
                if time.time() > self.wd + 5:
                    break
                r = self.browser.get("https://kibet-3.com/ko/", verify=False)
                if r.status_code == 200:
                    r = self.browser.post("https://kibet-3.com/ko/Login/Login", data=myInfo, headers=self.sessionHeaders, verify=False)
                    #print(1, r)
                    if r.status_code == 200:
                        b = self.browser.get("https://kibet-3.com/LiveCasino/GetLiveCasinoUrl", verify=False, headers=self.sessionHeaders)
                        #print(2, b)
                        if b.status_code == 200:
                            self.gameURL = b.content.decode()
                            print(self.gameURL)
                            self.sessionHeaders.pop("Referer")
                            self.sessionHeaders.pop("Origin")
                            if 'https://livecasino.kibet-1.com/cgibin/UserAuthentication?' in self.gameURL:
                                b = self.browser.get(self.gameURL, verify=False, headers=self.sessionHeaders)
                                #print(4, b)
                                if b.status_code == 200:
                                    b = self.browser.get('https://livecasino.kibet-1.com/mobile/', verify=False, headers=self.sessionHeaders)
                                    #print(5, b)
                                    if b.status_code == 200:
                                        print(self.browser.get_cookiejar().keys())
                                        if "EVOSESSIONID" in self.browser.get_cookiejar().keys():
                                            self.sessionId.append(self.browser.get_cookiejar()["EVOSESSIONID"])
                                            #print(7, self.sessionId)
                                            self.seesions.append(kibetWebsocket(self.sessionId[-1], 'livecasino.kibet-1.com' , self.roomCnt))
                                            threading.Thread(target=self.seesions[2].run).start()
                                            tb = time.time()
                                            while 1:
                                                if (time.time() - tb) > 180:
                                                    self.sessionUdate = "fail"
                                                    self.seesions.pop(2)
                                                    self.sessionId.pop(2)
                                                    return
                                                time.sleep(1)
                                                #print(len(self.seesions[2].tables))
                                                if len(self.seesions[2].tables) > 0:
                                                    self.sessionInint = True
                                                    try:
                                                        self.seesions[0].loop = False
                                                    except:
                                                        pass
                                                    self.seesions = self.seesions[1:]
                                                    self.sessionId = self.sessionId[1:]
                                                    if len(self.seesions) > 2:
                                                        try:
                                                            self.seesions.pop(0)
                                                        except:
                                                            pass
                                                        try:
                                                            self.sessionId.pop(0)
                                                        except:
                                                            pass
                                                    print("self.seesions" , self.seesions)
                                                    break
                                            break
        except:
            self.seesions.pop(2)
            self.sessionId.pop(2)
            self.sessionUdate = "fail"



    def getText(self ,xpath):
        try:
            return self.driver.find_element_by_xpath(xpath).text
        except:
            return "__wait__"




    def checkAnswer(self , ans):

        #if "\n" in ans:
        #    ans = ans.split("\n")[0]
        try:
            a = int(ans)
        except:
            err = traceback.format_exc()
            if "invalid literal for int() with base 10: '_'" not in err:
                if "invalid literal for int() with base 10: ''" not in err:
                    print("a",ans ,  err)

            return ''

        result = ''
        if a == 0:
            return '0'
        if a in self.reds:
            result+='적'
        else:
            result+='흑'
        if a%2 == 0:
            result += '짝'
        else:
            result += '홀'

        if a < 19:
            result += '언더'
        else:
            result += '오버'

        return result

    def showInform(self):
        self.pocketLabel.setText(  _translate("Form","◎잔고 : %d"%int(self.pocket) , None))
        self.skipPocketLabel.setText(_translate("Form", "◎단계 적용 잔고 : %d" % int(self.skipPocket), None))
        self.sucessCntLabel.setText(_translate("Form", "◎성공 횟수 : %d"%self.totalWinCnt, None))
        self.sucessCntLabelSkip.setText(_translate("Form", "◎단계 적용 성공 횟수 : %d"%self.totalWinCntSkip , None ))
        timeDiff = "◎경과시간: %2d일 %d시간 %d분 %d초" % dhms_from_seconds(date_diff_in_seconds(datetime.datetime.now(),self.startTime))
        self.totalTime.setText(_translate("Form",timeDiff , None ))
        self.maxbetSkipLabel.setText(_translate("Form",'◎단계 적용 최고 베팅 : %d'%int(self.maxbetSkip) , None ))
        self.maxbetLabel.setText(_translate("Form", '◎최고 베팅 : %d' % int(self.maxBet), None))


        stack = copy.deepcopy(self.stack)
        for i in range(49, -1, -1):
            if stack[i] == 0 :
                stack.pop(i)
            else:
                break

        stacStr = ''
        for s in sorted(stack):
            stacStr+= '%d : %d\n'%(s , stack[s])
        self.historyStack.setPlainText(_translate("Form",stacStr, None))

        self.totalCntLabel.setText(_translate("Form","◎총 횟수 : %d"%self.totalCnt, None))

        for gt in ["적", "흑", "짝", "홀", "언더", "오버"]:
            if self.detail:
                for j in range(self.roomCnt):

                    try:
                        self.step[j][gt].setText(_translate("Form", "%s %d-%d(%s[%d],%s[%d])" % (gt,int(self.history[j]["br"]["fwd"][0]), int(self.history[j]["br"]["fwd"][1]),
                                                                                             self.currentAnswers[j][0], self.answers[j]["br"][-1], self.currentAnswers[j][1], self.answers[j]["br"][-2]), None))
                    except:
                        try:
                            self.step[j][gt].setText(_translate("Form", "%s %d-%d(%s[%d],%s[%d])" % (gt,int(self.history[j]["br"]["fwd"][0]), int(self.history[j]["br"]["fwd"][1]),
                                                                                                 self.currentAnswers[j][0], -9, self.currentAnswers[j][1], self.answers[j]["br"][-2]), None))
                        except:
                            pass

            else:
                for j in range(self.roomCnt):
                    try:
                        self.step[j][gt].setText(_translate("Form", "%s %02d - %02d" % (gt,int(self.failCnt[j][gt]) ,int(self.failCnt[j][ gt+"2"])), None))
                    except:
                        try:
                            self.step[j][gt].setText(_translate("Form", "%s %02d - %02d" % (gt,int(self.failCnt[j][gt]) ,int(self.failCnt[j][ gt+"2"]) ), None))
                        except:
                            print(traceback.format_exc())

    def update(self):

        tbUdateError = 0
        err = ''
        for ss in [self.seesions[-1]]:
            try:
                ss.wd = time.time()
            except:
                pass
            try:
                cnt = 0
                for tb in ss.tableIds:

                    if ss.Alive:
                        try:
                            newRN = ss.tables[tb]
                            self.roomName[cnt].setText(_translate("Form", newRN , None))
                            self.roomNames[cnt] = self.roomName[cnt].text()
                            self.step[cnt]["최소배팅"].setText(_translate("Form", "최소금액 " +  str(ss.betMin[newRN]) , None))
                            self.step[cnt]["시작단계"].setText(_translate("Form", "옵셋 " + str(ss.betDiv[newRN]+int(self.stepLimitVal.text())), None))
                        except:
                            print("Exsc")
                            print(traceback.format_exc())
                        cnt += 1

                fcrCnt = 0

            except:
                tbUdateError+=1
                err+= "\n"
                err += traceback.format_exc()

        if tbUdateError == len(self.seesions):
            print("table Name Update Error \n" ,err )



        if self.sessionInint:
            self.pushButton.setStyleSheet(_fromUtf8('background-color: rgb(50, 255, 100)'))


        self.wd = time.time()


        self.chekRoomName = True
        for j in range(self.roomCnt):
            #print(self.roomName[j].text())
            try:
                if self.roomName[j].text() ==  "__wait__":
                    self.chekRoomName = False
            except:
                self.chekRoomName = False


        if self.chekRoomName:
            for ss in [self.seesions[-1]]:

                try:
                    cnt = 0
                    for rn in ss.tableIds:

                        if ss.Alive:
                            #print("rn", rn)
                            try:
                                #print("alive")
                                if rn not in ['VIP 룰렛', '더블 볼 룰렛', "룰렛 라이브"]:
                                    tbrn = ss.tables[rn]
                                    #print("tbrn" , tbrn)
                                    rindex = self.roomNames.index(tbrn)
                                    #print("rindx" , rindex)
                                    aasarn = ss.answers[rn]
                                    #print("aasarn" , aasarn)
                                    self.currentAnswers[rindex] = aasarn
                                    #print("curindex" , rindex )
                            except:
                                print("Exsc")
                                print(traceback.format_exc())
                            cnt += 1


                except:
                    tbUdateError += 1
                    err += "\n"
                    err += traceback.format_exc()

            if tbUdateError == len(self.seesions):
                print("answer Update Error \n", err)


            betPatternCheck = True
            for i in range(self.roomCnt):
                roomName = self.roomName[i].text()
                try:
                    if ss.betPatterns[roomName] == 'ready':
                        tmp = [0]* ( int(self.stepLimitVal.text()) + ss.betDiv[roomName]  )
                        tmp.extend(self.betPattern)
                        self.betPatterns.append(tmp)
                        #print(roomName ,self.betPatterns[i] )

                except:
                    betPatternCheck = False
                    return

            if betPatternCheck:
                for j in range(self.roomCnt):
                    roomName = self.roomName[j].text()
                    if self.beforeAnswers[j] != self.currentAnswers[j]:
                        #print(self.beforeAnswers[j])
                        #print(self.currentAnswers[j])
                        for gt in [["적",'흑'] , ["짝",'홀'] ,  ["언더",'오버']]:
                            for ii in range(2):
                                self.totalCnt +=1


                                ansTmp = self.checkAnswer( self.currentAnswers[j][0] )
                                ans = 'none'
                                tmp = False
                                if gt[ii] in ansTmp:
                                    self.answers[j].append(ansTmp)
                                    if len(self.answers[j]) > 5:
                                        self.answers[j] = self.answers[j][-5:]
                                    if len(self.answers[j]) > 2:
                                        ans = True
                                else:
                                    if len(self.answers[j]) > 2:
                                        ans = False
                                    #else:
                                    #    print("기록이 %d개 입니다.2개가 되면 시작합니다."%len(self.answers[j]))

                                if ans != 'none':
                                    self.testLabel2.setText(_fromUtf8("%s" % str(self.answers[j][-1][0])))
                                    if ans:
                                        tmp = True
                                        self.stack[self.failCnt[j][gt[ii]]] += 1
                                        self.totalWinCnt +=1
                                        self.failCnt[j][gt[ii]]=0

                                        self.pocket += (self.bet[j][gt[ii]]*2)
                                        #pb = self.rbPocket[gt[ii]]
                                        #self.rbPocket[gt[ii]] +=  (self.bet[j][gt[ii]]*2)
                                        self.skipPocket += (self.skippingBet[j][gt[ii]] * 2)

                                        if self.skippingBet[j][gt[ii]] >  0:
                                            self.totalWinCntSkip += 1
                                        #if gt[ii] == '적':
                                        #    print(gt[ii] , "111 적중 하였습니다. 현재 잔고는 %d 입니다."%(self.rbPocket[gt[ii]] ))

                                    else:
                                        #if gt[ii] == '적':
                                        #    print(gt[ii], "222 실패 하였습니다. 현재 잔고는 %d 입니다." % ( self.rbPocket[gt[ii]] ))
                                        self.failCnt[j][gt[ii]] += 1


                                    self.bet[j][gt[ii]] = ss.betMin[roomName]*self.betPattern[self.failCnt[j][gt[ii]]]
                                    #pb = self.rbPocket[gt[ii]]
                                    self.pocket -= self.bet[j][gt[ii]]
                                    #self.rbPocket[gt[ii]] -= self.bet[j][gt[ii]]
                                    #if gt[ii] == '적':
                                    #    print(gt[ii], "333 배팅 합니다. 이전 잔고는 %d 이며 , %d 배팅 했습니다. 현재 잔고는 %d 입니다."%(pb ,self.bet[j][gt[ii]] ,self.rbPocket[gt[ii]] ))
                                    self.skippingBet[j][gt[ii]] = ss.betMin[roomName]*self.betPatterns[j][self.failCnt[j][gt[ii]]]
                                    self.skipPocket -= self.skippingBet[j][gt[ii]]
                                    self.testLabel.setText(_fromUtf8("%d" % self.skippingBet[j][gt[ii]]))

                                    if self.maxBet < self.bet[j][gt[ii]]:
                                        self.maxBet = self.bet[j][gt[ii]]

                                    if self.skippingBet[j][gt[ii]] > self.maxbetSkip:
                                        self.maxbetSkip = self.skippingBet[j][gt[ii]]

                                    #failSkipCnt = self.failCnt[j][gt[ii]] - ss.betDiv[roomName] - int(self.stepLimitVal.text())
                                    if self.skippingBet[j][gt[ii]] > 0:
                                        self.step[j][gt[ii]].setStyleSheet(_fromUtf8("background-color: rgb(255, 200, 50);"))
                                    else:
                                        self.step[j][gt[ii]].setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))


                        for gt in ["적", "짝","언더"]:
                                pass
                        try:
                            #print(len(self.beforeAnswer) , len(self.answers))

                            self.beforeAnswer[j] = self.answers[j][-1]
                        except:
                            #print("roomCntExist", len(self.roomCnt) )
                            print(traceback.format_exc())
                    '''QtGui.QSound("./bd_made.wav").play()'''
                    self.showInform()

                    self.beforeAnswers[j] = copy.deepcopy(self.currentAnswers[j])















    def start(self):
        try:
            self.numOfRoom = 3
            try:
                self.stepLim = int(self.stepLimitVal.text())
            except:
                QtGui.QMessageBox.about(Form, "알람", "몇 단계 인지 입력하세요")
                return
            if self.numOfRoom > 4:
                QtGui.QMessageBox.about(Form, "알람", "방 숫자는 4 까지만 입력 가능합니다")
                return
            if self.numOfRoom == 0:
                QtGui.QMessageBox.about(Form, "알람", "방 숫자를 입력 하세요")
                return
            if self.stepLim == 0:
                QtGui.QMessageBox.about(Form, "알람", "몇 단계 인지 입력하세요")
                return
            self.lineEdit.setDisabled(True)
            self.pushButton.setDisabled(True)
            self.stepLimitVal.setDisabled(True)
            self.myIdInput.setDisabled(True)
            self.myPassInput.setDisabled(True)
            save = str(self.numOfRoom) + "\n" + str(self.stepLim)
            with open("./save.dat" , 'w') as f:
                f.write(save)
            save = str(self.myIdInput.text()) + "\n" + str(self.myPassInput.text())
            with open("./data.dat" , 'w') as f:
                f.write(save)
        except:
            pass

        self.numOfRoom = self.roomCnt
        for i in range(self.numOfRoom):
            self.base.append(QtGui.QLabel(Form))
            self.base[-1].setGeometry(QtCore.QRect(10+i*90, 40, 86, 180))
            self.base[-1].setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
            self.base[-1].setText(_fromUtf8(""))
            self.base[-1].setObjectName(_fromUtf8("label_3"))
            self.base[-1].show()
            self.roomName.append(QtGui.QLabel(self.base[-1]))
            self.roomName[-1].setGeometry(QtCore.QRect(2, 20, 75, 12))
            self.roomName[-1].setObjectName(_fromUtf8("label"))
            self.roomName[-1].setText(_translate("Form", "__wait__", None))
            self.roomName[-1].show()

            self.step.append({})
            for gti , gt in enumerate(["적" , "흑" , "짝","홀","언더","오버", "최소배팅" , "시작단계"]) :
                self.step[i][gt] = (QtGui.QLabel(self.base[-1]))
                self.step[i][gt].setGeometry(QtCore.QRect(2 ,40+gti*14, 118, 12))
                self.step[i][gt].setObjectName(_fromUtf8("label_2"))
                self.step[i][gt].setText(_translate("Form", "%s 00"%gt, None))
                self.step[i][gt].setStyleSheet(_fromUtf8('background-color: rgb(255, 255, 255)'))
                self.step[i][gt].show()
        self.th = threading.Thread(target = self.runWebsocket)
        self.th.start()

    def terminate(self):
        pass


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "시작", None))



    def pb1(self):
        pass



    def closeEvent(self, event):
        try:
            if self.numOfRoom > 0:
                reply = QtGui.QMessageBox.question(Form, 'Message',
                    "모든 창을 닫고 게임을 끝내시겠습니까?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        except:
            reply = QtGui.QMessageBox.Yes

        if reply == QtGui.QMessageBox.Yes:

            try:
                self.timer.stop()
            except:
                pass
            try:
                self.timer2.stop()
            except:
                pass
            try:
                self.timer3.stop()
            except:
                pass

            try:
                self.browser.close()
            except:
                print(traceback.format_exc())


        else:
            event.ignore()


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        teleUse = False
    else:
        teleUse = True


    app = QtGui.QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()
    width, height = screen_resolution.width(), screen_resolution.height()
    Form = QtGui.QWidget()
    ui = Ui_Form(Form,teleUse)
    ui.setupUi(width, height)
    Form.closeEvent = ui.closeEvent
    Form.show()

    sys.exit(app.exec_())










