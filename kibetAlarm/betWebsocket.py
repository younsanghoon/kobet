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
    return int(str(time.time()).replace("." , "")[:13])
def wid(length=10):
    strCase = string.ascii_lowercase+string.ascii_uppercase+string.digits
    return ''.join(random.choice(strCase) for x in range(length))


class kibetWebsocket():
    def __init__(self , sessId = ''  , host = '',tableID = ''):
        self.loop = True
        self.Alive = True
        self.host = host
        self.sessId = sessId
        self.tableId = tableID


    def run(self):
        try:
            self.wd = time.time()
            self.logInheaders = {}
            self.tables = {}
            self.tableIds = []
            self.answers = {}
            self.logInheaders['Host'] = self.host
            self.logInheaders['Connection'] = 'Upgrade'
            self.logInheaders['Pragma'] = 'no-cache'
            self.logInheaders['Cache-Control'] = 'no-cache'
            self.logInheaders['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
            self.logInheaders['Upgrade'] = 'websocket'
            self.logInheaders['Origin'] = 'https://%s'%self.host
            self.logInheaders['Sec-WebSocket-Version'] = '13'
            self.logInheaders['Accept-Encoding'] = 'gzip, deflate, br'
            self.logInheaders['Accept-Language'] = 'ko,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,zh-TW;q=0.5,de;q=0.4,de-CH;q=0.3,de-AT;q=0.2,ja;q=0.1'
            self.logInheaders['Cookie'] = 'EVOSESSIONID=%s'%self.sessId
            self.logInheaders['Sec-WebSocket-Key'] = wid(24)+'=='
            self.logInheaders['Sec-WebSocket-Extensions'] = 'permessage-deflate; client_max_window_bits'


            #'livecasino.kibet-3.com'
            ws = create_connection("wss://%s/public/lobby/player/socket?messageFormat=json"%self.host, header=self.logInheaders)

            webSocket.init(ws)


            i = 0
            while self.loop:
                i+=1
                if ( time.time() - self.wd) > 10:
                    break

                result = ws.recv()
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
                    ws.send(json.dumps('{"id":"%s","type":"metrics.ping","args":{"t":%d}}' % (wid(), tt())))

        except:
            print("seesion die" , traceback.format_exc())
            print(result)
        self.Alive = False
        ws.close()



class batRoomPlay():
    def __init__(self , sessId = ''  , host = '' , userId ='', tableId =''):
        self.wd = time.time()
        self.bal = ''
        self.loop = True
        self.Alive = True
        self.betOpen = False
        self.host = host
        self.sessId = sessId
        self.userId = userId
        self.tableId = tableId
        self.getPlayIdHeaders = {}
        self.getPlayIdHeaders['Host'] = self.host
        self.getPlayIdHeaders['Connection'] = 'Upgrade'
        self.getPlayIdHeaders['Pragma'] = 'no-cache'
        self.getPlayIdHeaders['Cache-Control'] = 'no-cache'
        self.getPlayIdHeaders['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        self.getPlayIdHeaders['Upgrade'] = 'websocket'
        self.getPlayIdHeaders['Origin'] = 'https://%s' % self.host
        self.getPlayIdHeaders['Sec-WebSocket-Version'] = '13'
        self.getPlayIdHeaders['Accept-Encoding'] = 'gzip, deflate, br'
        self.getPlayIdHeaders['Accept-Language'] = 'ko,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,zh-TW;q=0.5,de;q=0.4,de-CH;q=0.3,de-AT;q=0.2,ja;q=0.1'
        self.getPlayIdHeaders['Cookie'] = 'EVOSESSIONID=%s' % self.sessId
        self.getPlayIdHeaders['Sec-WebSocket-Key'] = wid(24)+'=='
        self.getPlayIdHeaders['Sec-WebSocket-Extensions'] = 'permessage-deflate; client_max_window_bits'


    def run(self):

        true = True
        false = False
        null = 0
        self.address = 'wss://%s/public/roulette/player/game/%s/socket?messageFormat=json&tableConfig='%(self.host , self.tableId  )
        self.ws = create_connection(self.address, header=self.getPlayIdHeaders)

        self.roomInit()

        i = 0
        tb = 0
        while self.loop:
            try:
                i += 1
                if (time.time() - self.wd) > 120:
                    break

                result = self.ws.recv()
                data = json.loads(result)
                print(result[:200])
                if 'BETS_OPEN' in result:
                    self.betOpen = True
                    if 'roulette.tablestate' in result.lower():
                        self.gameId = data['args']['gameId']
                    time.sleep(5)
                    self.bet()
                elif 'BETS_CLOSED' in result:
                    self.betOpen = False
                elif 'balance' in result.lower():
                    if data['type'] == 'roulette.betsAccepted' or data['type'] == 'balanceUpdated':
                        self.bal = data['args']['balance']
                        msg = {"log":{"type":"CLIENT_BALANCE_UPDATED","value":{"currency":"₩","balance":self.bal,"channel":"PCMac","orientation":"landscape"}}}
                        print("Send" , str(msg)[:200])
                        self.ws.send(json.dumps(msg))

                if time.time() - tb > 3:
                    msg = {"id":wid(),"type":"metrics.ping","args":{"t":tt()}}
                    print("Send" , str(msg)[:200])
                    self.ws.send(json.dumps(msg))
                    if random.randint(0 , 30) < 2:
                        self.sendVideoStat()
                    tb = time.time()
            except:
                print("seesion die", traceback.format_exc())
                break
        print("session closed")
        self.roomClose()
        self.ws.close()



    def roomInit(self):
        true = True
        false = False
        null = 0
        msg = {"id":wid(),"type":"settings.read","args":{"key":"generic.common"}}
        print("send", msg)
        self.ws.send(json.dumps(msg))
        msg = {"id":wid(),"type":"settings.read","args":{"key":"generic.mobile"}}
        print("send" , msg)
        self.ws.send(json.dumps(msg))
        msg = {"id":wid(),"type":"settings.read","args":{"key":"generic.desktop"}}
        print("send" , msg)
        self.ws.send(json.dumps(msg))
        msg = {"id":wid(),"type":"settings.read","args":{"key":"roulette.common"}}
        print("send" , msg)
        self.ws.send(json.dumps(msg))
        msg = {"id": wid(), "type": "settings.read", "args": {"key": "roulette.doubleBall"}}
        print("send" , msg)
        self.ws.send(json.dumps(msg))
        msg = {"log": {"type": "CLIENT_SOCKET_CONNECTION_ESTABLISHED", "value": {"offline": false, "channel": "PCMac", "orientation": "landscape"}}}
        print("send" , msg)
        self.ws.send(json.dumps(msg))

        while 1:
            time.sleep(1)
            msg = {"id": wid(), "type": "metrics.ping", "args": {"t": tt()}}
            print("send" , msg)
            self.ws.send(json.dumps(msg))
            result = self.ws.recv()
            data = json.loads(result)
            print(self.loop , "recv" , result[:200])
            if 'balance' in result.lower():
                if data['type'] == 'roulette.betsAccepted' or data['type'] == 'balanceUpdated':
                    self.bal = data['args']['balance']
                    self.bal = data['args']['balance']
                    msg = {"log": {"type": "CLIENT_BALANCE_UPDATED", "value": {"currency": "₩", "balance": self.bal, "channel": "PCMac", "orientation": "landscape"}}}
                    print("Send", str(msg)[:200])
                    self.ws.send(json.dumps(msg))
            if "success" in str(result):
                print("sucess!!!!!!!")
                time.sleep(2)
                break
            if self.loop != True:
                self.roomClose()
                self.ws.close()
                return


        msg = {"id": wid(), "type": "favouriteBets.loadBets", "args": {"queryString": {"tableId": self.tableId }}}
        print("send" , msg)
        self.ws.send(json.dumps(msg))
        result = self.ws.recv()
        data = json.loads(result)
        print("recv" , result[:200])
        if 'balance' in result.lower():
            if data['type'] == 'roulette.betsAccepted' or data['type'] == 'balanceUpdated':
                self.bal = data['args']['balance']
                msg = {"log": {"type": "CLIENT_BALANCE_UPDATED", "value": {"currency": "₩", "balance": self.bal, "channel": "PCMac", "orientation": "landscape"}}}
                print("Send", str(msg)[:200])
                self.ws.send(json.dumps(msg))
        #msg = {"log": {"type": "CLIENT_BALANCE_UPDATED", "value": {"currency": "₩", "balance": 390500, "channel": "PCMac", "orientation": "landscape"}}}
        #print("send" , msg)
        #self.ws.send(json.dumps(msg))

        msg = {"id": wid(), "type": "settings.update", "args": {"key": "generic.common.previousSessionID", "data": self.sessId[:40]}}
        print("send" , msg)
        self.ws.send(json.dumps(msg))

    def roomClose(self):
        true = True
        false = False
        null = 0
        msg = {"log": {"type": "CLIENT_GAME_CLOSE_CLICK", "value": {"channel": "PCMac", "orientation": "landscape"}}}
        self.ws.send(json.dumps(msg))
        msg = {"id": wid(), "type": "connection.unsubscribe", "args": {}}
        self.ws.send(json.dumps(msg))


    def bet(self):
        true = True
        false = False
        null = 0
        msg = {"log": {"type": "CLIENT_BALANCE_UPDATED", "value": {"currency": "₩", "balance": self.bal, "channel": "PCMac", "orientation": "landscape"}}}
        print("Send", str(msg)[:200])
        self.ws.send(json.dumps(msg))
        msg = {"log": {"type": "CLIENT_BET_CHIP",
                 "value": {"amount": 160, "type": "bet_from1to18", "chips": "160@bet_from1to18", "codes": {"ROU_118": 160}, "balance": self.bal, "maxTouchPoints": 0, "currency": "KRW", "chipStack": [160, 1000, 4000, 20000, 100000, 400000],
                           "defaultChip": 1, "tableMinLimit": 160, "tableMaxLimit": 2000000, "channel": "PCMac", "orientation": "landscape"}}}
        print("bet!" , msg)
        self.ws.send(json.dumps(msg))
        msg = {"args": {"gameId":self.gameId, "action": {"type": "PLACE", "value": {"46": 160}}, "timestamp": tt(),
                  "betTags": {"openMwTables": 1, "mwLayout": 8, "latency": 279, "videoProtocol": "flvjs", "btTableView": "view2", "btVideoQuality": "gen1_ss_low", "btMiniGame": 0, "appVersion": 4, "orientation": "landscape"}}, "id": "byhxs4zoz8",
         "type": "roulette.betAction"}
        print("bet2!", msg)
        self.ws.send(json.dumps(msg))

        time.sleep(3)

    def logToServer(self):
        true = True
        false = False
        null = 0
    
    def sendVideoStat(self):
        true = True
        false = False
        null = 0
        msg = {"log":{"type":"CLIENT_VIDEO_HEARTBEAT",
                      "value":{"heartbeat":{"timestamp":tt(),"currentQuality":"MEDIUM","framerate":24,
                                            "framerateAverage":23.787,"droppedFrames":3434,"droppedFramesAverage":31,
                                            "bufferLength":2528.471,"currentStreamName":"gen1_ss_med","playbackBitrate":483,
                                            "playbackFormat":"flvjs","expectedBitrate":464,"soundVolume":1,"streamLatency":3.137,"bandwidth":26256},
                               "sessionData":{"game":"roulette","videoSessionId":self.sessId},
                               "channel":"PCMac","orientation":"landscape"}}}
        print("send" , msg)
        self.ws.send(json.dumps(msg))
        


class Ui_Form(object):
    def __init__(self, Form):
        QtGui.QMainWindow.__init__(Form, None, QtCore.Qt.WindowStaysOnTopHint)
        self.Form = Form
        self.get_mac()

    def get_mac(self):
        mac_num = hex(uuid.getnode()).replace('0x', '').upper()
        # print(mac_num)

        mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
        print(mac)
        if mac not in ["E8-03-9A-6D-CD-FF", 'B0-6E-BF-BA-95-B0']:
            QtGui.QMessageBox.about(self.Form, "알람", "허가되지 않은 PC 입니다")
            sys.exit(-1)
        # print(mac)
        # return mac

    def setupUi(self, width, height):

        self.reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
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
        self.sessionHeaders[
            "User-Agent"] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        # self.sessionHeaders[
        #    "Cookie"] = "__cfduid=df8173b98d327c558872349c4f09ad0e01540947177; ASP.NET_SessionId=hgfyocqaqokvbgjyeit2ue1n; comm100_guid2_228800=oqUUEVQHiEWfBNU0MjQXfQ"
        self.browser = mechanicalsoup.StatefulBrowser()

        Form = self.Form
        Form.setObjectName(_fromUtf8("Form"))
        Form.setGeometry(QtCore.QRect(width / 2 - 900, height - 300, 1800, 170))
        Form.setFixedSize(1800, 170)
        # QtGui.QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)

        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(600, 10, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.setText(_fromUtf8("시작"))
        # self.pushButton.setDisabled(True)

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
        self.lineEdit.setGeometry(QtCore.QRect(60, 11, 50, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 11, 60, 20))
        self.label.setText(_fromUtf8("방 갯수"))
        self.label.show()
        self.label2 = QtGui.QLabel(Form)
        self.label2.setGeometry(QtCore.QRect(130, 11, 60, 20))
        self.label2.setText(_fromUtf8("몇 단계"))
        self.label2.show()
        self.stepLimitVal = QtGui.QLineEdit(Form)
        self.stepLimitVal.setGeometry(QtCore.QRect(190, 11, 30, 20))
        self.stepLimitVal.setObjectName(_fromUtf8("lineEdit"))
        self.stepLimitVal.setText(_translate("Form", "0", None))
        #self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.lineEdit.setText(_translate("Form", str(14), None))
        self.lineEdit.setDisabled(True)
        self.wd = time.time()
        self.scoreEle = [[''] * 10 for i in range(14)]
        self.currentAnswer = ['0' for i in range(10)]
        self.currentAnswers = ['__wait__' for i in range(14)]
        self.beforeAnswers = [copy.deepcopy(self.currentAnswer) for i in range(14)]
        self.history = [{"br": {"fwd": [1, 0, 0], "bwd": [1, 0, 0]},
                         "eo": {"fwd": [1, 0, 0], "bwd": [1, 0, 0]},
                         "ud": {"fwd": [1, 0, 0], "bwd": [1, 0, 0]}} for i in range(14)]

        self.answers = [{"br": [],
                         "eo": [],
                         "ud": []} for i in range(14)]

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
        self.sessionId = ["", ""]
        self.sessionInint = False
        self.sessionUdate = "ready"
        self.sessions = ['', '']

        # self.ssThread = threading.Thread(target = self.getSession)
        # self.ssThread.start()

        self.base = []
        self.roomName = []
        self.step = []
        self.step2 = []
        self.step3 = []
        self.steps = {"br": self.step, "eo": self.step2, "ud": self.step3}
        self.renew = False

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start)

        #QtCore.QObject.connect(self.showDetail, QtCore.SIGNAL(_fromUtf8("clicked()")), self.changeDetail)

        self.renewTime = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.betUpdate)
        self.timer2.start(100)


    def start(self):
        self.th = threading.Thread(target=self.runWebsocket)
        self.th.start()

    def betUpdate(self):
        if self.sessions[-1] != '':
            if self.sessions[-1].betOpen:
                self.showDetail.setStyleSheet(_fromUtf8('background-color: rgb(50, 255, 100)'))
            else:
                self.showDetail.setStyleSheet(_fromUtf8(''))


    def update(self):
        if self.sessionInint:
            self.pushButton.setStyleSheet(_fromUtf8('background-color: rgb(50, 255, 100)'))

    def runWebsocket(self,init = True , dummy= ''):
        self.tableId = '48z5pjps3ntvqc1b'
        self.sessionInint = False
        try:
            myInfo = b"Email=%s&Password=%s&gameUrl=" % (str(self.myIdInput.text()).strip().encode(), str(self.myPassInput.text()).strip().encode())
            print(myInfo)
            self.sessionUdate = "ready"
            for i in range(5):
                if time.time() > self.wd + 10:
                    break
                r = self.browser.get("https://kibet-3.com/ko/", verify=False)
                if r.status_code == 200:
                    r = self.browser.post("https://kibet-3.com/ko/Login/Login", data=myInfo, headers=self.sessionHeaders, verify=False)
                    print(1, r)
                    if r.status_code == 200:
                        b = self.browser.get("https://kibet-3.com/LiveCasino/GetLiveCasinoUrl", verify=False, headers=self.sessionHeaders)
                        print(2, b)
                        if b.status_code == 200:
                            self.gameURL = b.content.decode()
                            print(3, self.gameURL)
                            if 'https://livecasino.kibet-3.com/cgibin/UserAuthentication?' in self.gameURL:
                                b = self.browser.get(self.gameURL, verify=False, headers=self.sessionHeaders)
                                print(4, b)
                                if b.status_code == 200:
                                    b = self.browser.get('https://livecasino.kibet-3.com/mobile/', verify=False, headers=self.sessionHeaders)
                                    print(5, b)
                                    if b.status_code == 200:
                                        print(self.browser.get_cookiejar().keys())
                                        if "EVOSESSIONID" in self.browser.get_cookiejar().keys():
                                            self.sessionId.append(self.browser.get_cookiejar()["EVOSESSIONID"])
                                            b= self.browser.get('https://livecasino.kibet-3.com/setup?device=desktop&wrapped=false' , verify=False, headers=self.sessionHeaders)
                                            if b.status_code == 200:
                                                self.userId = json.loads(b.content.decode())['user_id']
                                                print(7, self.sessionId,self.userId)
                                                time.sleep(10)
                                                self.sessions.append(batRoomPlay(self.sessionId[-1], 'livecasino.kibet-3.com' , self.userId ,self.tableId ))
                                                print("self.sessions" , self.sessions , self.sessions.__init__)
                                                #input("....")
                                                threading.Thread(target=self.sessions[2].run).start()
                                                tb = time.time()
                                                ####check Session Status
                                                '''while 1:
                                                    
                                                    if (time.time() - tb) > 180:
                                                        self.sessionUdate = "fail"
                                                        self.sessions.pop(2)
                                                        self.sessionId.pop(2)
                                                        return
                                                    time.sleep(1)
                                                    print(len(self.sessions[2].tables))
                                                    if len(self.sessions[2].tables) > 0:
                                                        self.sessionInint = True
                                                        try:
                                                            self.sessions[0].loop = False
                                                        except:
                                                            pass
                                                        self.sessions = self.sessions[1:]
                                                        self.sessionId = self.sessionId[1:]
                                                        print("self.sessions" , self.sessions)
                                                        break
                                                break'''
        except:
            print("except")
            self.sessions.pop(2)
            self.sessionId.pop(2)
            self.sessionUdate = "fail"




    def closeEvent(self,event):

        try:
            if True:#self.numOfRoom > 0:
                reply = QtGui.QMessageBox.question(Form, 'Message',
                    "모든 창을 닫고 게임을 끝내시겠습니까?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        except:
            reply = QtGui.QMessageBox.Yes

        if reply == QtGui.QMessageBox.Yes:
            print("close")
            print("self.session" , self.sessions,self.sessions.__init__)
            for ss in self.sessions:
                try:
                    ss.loop = False
                    print("ss is terminated")
                except:
                    print(traceback.format_exc())

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


        else:
            event.ignore()



if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()
    width, height = screen_resolution.width(), screen_resolution.height()
    Form = QtGui.QWidget()
    ui = Ui_Form(Form)
    ui.setupUi(width, height)
    Form.closeEvent = ui.closeEvent
    Form.show()

    sys.exit(app.exec_())


