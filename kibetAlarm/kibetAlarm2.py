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



            #'livecasino.kobet-3.com'
            ws = create_connection("wss://%s/public/lobby/player/socket?messageFormat=json"%self.host, header=headers)

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
                    ws.send(json.dumps('{"id":"%s","type":"metrics.ping","args":{"t":%s}}' % (wid(), tt())))

        except:
            print("seesion die" , traceback.format_exc())
            print(result)
        self.Alive = False
        ws.close()




class Ui_Form(object):
    def __init__(self,Form):
        QtGui.QMainWindow.__init__(Form, None, QtCore.Qt.WindowStaysOnTopHint)
        self.Form = Form
        self.get_mac()

    def get_mac(self):
        mac_num = hex(uuid.getnode()).replace('0x', '').upper()
        #print(mac_num)

        mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
        print(mac)
        '''if mac not in  ["E8-03-9A-6D-CD-FF" , 'B0-6E-BF-BA-95-B0']:
            QtGui.QMessageBox.about(self.Form, "알람", "허가되지 않은 PC 입니다")
            sys.exit(-1)'''
        #print(mac)
        #return mac


    def setupUi(self, width, height):

        self.reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.sessionHeaders = {}
        self.sessionHeaders["Connection"] = "keep-alive"
        self.sessionHeaders["Origin"] = "https://kobet-3.com"
        # self.sessionHeaders['Content - Length'] =  '41'
        self.sessionHeaders['Accept'] = '*/*'
        self.sessionHeaders["X-Requested-With"] = "XMLHttpRequest"
        self.sessionHeaders["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        self.sessionHeaders["Referer"] = "https://kobet-3.com/"
        #self.sessionHeaders["Accept-Encoding"] = "gzip, deflate, br"
        self.sessionHeaders["Accept-Language"] = "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
        self.sessionHeaders["User-Agent"] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
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
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.lineEdit.setText(_translate("Form", str(14), None))
        self.lineEdit.setDisabled(True)
        self.wd = time.time()
        self.scoreEle = [['']*10 for i in range(14)]
        self.currentAnswer = ['0' for i in range(10)]
        self.currentAnswers = ['__wait__' for i in range(14)]
        self.beforeAnswers = [copy.deepcopy(self.currentAnswer) for i in range(14)]
        self.history = [ { "br" : { "fwd":[1,0,0] , "bwd":[1,0,0] } ,
                           "eo" : { "fwd":[1,0,0] , "bwd":[1,0,0] } ,
                           "ud": {"fwd":[1,0,0] , "bwd":[1,0,0] } } for i in range(14)]

        self.answers = [{"br":[],
                         "eo":[],
                         "ud":[] }  for i in range(14)]

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

        #self.timer2 = QtCore.QTimer()
        #self.timer2.timeout.connect(self.checkStatus)
        #self.timer2.start(1000)

        #self.chTh = threading.Thread(target = self.checkStatus)
        #self.chTh.start()

        self.timer3 = QtCore.QTimer()
        self.timer3.timeout.connect(self.update)
        self.timer3.start(3000)



        self.roomNames = [ "__wait__" for i in range(14)]
        self.roomFound = False

        self.timeLimit = time.time()




        try:
            with open("save.dat", 'r') as f:
                save = f.read()
                rn = save.split("\n")[0]
                lm = save.split("\n")[1]
                #self.lineEdit.setText(_translate("Form", 14, None))
                self.stepLimitVal.setText(_translate("Form", lm, None))
        except:
            pass


    def timeCheck(self):
        if self.renewTime == 600:
            self.th = threading.Thread(target=self.runWebsocket)
            self.th.start()
            self.renewTime = 0
        self.renewTime+=1






    def changeDetail(self):
        if self.detail == False:
            self.showDetail.setText(_translate("Form", "간단히 0", None))
            self.detail = True
            self.showInform()

        else:
            self.showDetail.setText(_translate("Form", "자세히 0", None))
            self.detail = False
            self.showInform()




    #def getSession(self):







    def runWebsocket(self,init = True , dummy= ''):
        #QtGui.QSound("./Alarm08.wav").play()
        print("~~~~")
        self.sessionInint = False
        try:
            myInfo = b"Email=%s&Password=%s&gameUrl=" % (str(self.myIdInput.text()).strip().encode(), str(self.myPassInput.text()).strip().encode())
            print(myInfo)
            self.sessionUdate = "ready"
            for i in range(1):
                if time.time() > self.wd + 10:
                    break
                r = self.browser.get("https://kobet-3.com/ko/", verify=False)
                if r.status_code == 200:
                    r = self.browser.post("https://kobet-3.com/ko/Login/Login", data=myInfo, headers=self.sessionHeaders, verify=False)
                    print(1, r)
                    if r.status_code == 200:
                        b = self.browser.get("https://kobet-3.com/LiveCasino/GetLiveCasinoUrl", verify=False, headers=self.sessionHeaders)
                        print(2, b)
                        if b.status_code == 200:
                            self.gameURL = json.loads(b.content.decode())["Message"]
                            print(3, self.gameURL)
                            if 'cgibin/UserAuthentication?' in self.gameURL:
                                b = self.browser.get(self.gameURL, verify=False, headers=self.sessionHeaders)
                                print(4, b)
                                if b.status_code == 200:
                                    #b = self.browser.get('https://livecasino.kobet-3.com/mobile/', verify=False, headers=self.sessionHeaders)
                                    #print(5, b)
                                    if b.status_code == 200:
                                        print(self.browser.get_cookiejar().keys())
                                        if "EVOSESSIONID" in self.browser.get_cookiejar().keys():
                                            self.sessionId.append(self.browser.get_cookiejar()["EVOSESSIONID"])
                                            print(7, self.sessionId)
                                            self.seesions.append(kibetWebsocket(self.sessionId[-1], 'livecasino.kobet-3.com'))
                                            threading.Thread(target=self.seesions[2].run).start()
                                            tb = time.time()
                                            while 1:
                                                if (time.time() - tb) > 180:
                                                    self.sessionUdate = "fail"
                                                    #self.seesions.pop(2)
                                                    #self.sessionId.pop(2)
                                                    return
                                                time.sleep(1)
                                                print(len(self.seesions[2].tables))
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
            print(traceback.format_exc())
            #self.seesions.pop(2)
            #self.sessionId.pop(2)
            self.sessionUdate = "fail"



    def getText(self ,xpath):
        try:
            return self.driver.find_element_by_xpath(xpath).text
        except:
            return "__wait__"

    def checkStatus(self):


        print("checkStatus!!!!!")
        while 1:
            try:
                tb = time.time()
                if time.time() > self.wd+5:
                    break
                time.sleep(1)
                myInfo = b''
                #bal = json.loads(self.browser.post('https://kobet-3.com/Common/GetBalanceStatus?id=', data=myInfo, headers=self.sessionHeaders, verify=False))
                #print("bal",bal.content.decode())
                try:
                    if self.roomFound == False:
                        roomNames = ['__wait__'  for i in range(14)]
                        for i in range(14):
                            roomNames[i] = self.getText('/html/body/div[5]/div/div/div[2]/div[3]/div/div/div/div[%d]/div/div[2]/div[1]'%(i+1))

                            if roomNames[i].strip() == '':
                                roomNames[i]= self.getText('/html/body/div[5]/div/div/div[2]/div[3]/div/div/div/div[%d]/div/div[2]/div[2]'%(i+1))


                        self.roomNames = copy.deepcopy(roomNames)
                except:
                    pass


                for j in range(14):
                    for k in range(10):
                        if self.scoreEle[j][k] == "":
                            self.currentAnswers[j][k] = self.getText('/html/body/div[5]/div/div/div[2]/div[3]/div/div/div/div[%d]/div/div[1]/div[5]/div/div/div[%d]/div'%(j+1 , k+1))
                            if self.currentAnswers[j][k] != "__wait__":
                                self.scoreEle[j][k] = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[3]/div/div/div/div[%d]/div/div[1]/div[5]/div/div/div[%d]/div'%(j+1 , k+1))
                        else:
                            self.currentAnswers[j][k] = self.scoreEle[j][k].text
            except:
                print(traceback.format_exc())


    def checkAnswer(self , ans , bef):

        #if "\n" in ans:
        #    ans = ans.split("\n")[0]
        try:
            a = int(ans)
        except:
            err = traceback.format_exc()
            if "invalid literal for int() with base 10: '_'" not in err:
                if "invalid literal for int() with base 10: ''" not in err:
                    print("a",ans ,  err)

            return {"br": -3 , "eo": -3, "ud": -3}

        try:
            b = int(bef)
        except:
            err = traceback.format_exc()
            if "invalid literal for int() with base 10: '__wait__'" not in err:
                if "invalid literal for int() with base 10: ''" not in err:
                    print("b", err)
            return {"br": -3, "eo": -3, "ud": -3}


        result = { "br" : 0 , "eo" : 0 , "ud" : 0 }
        if a == 0:
            return { "br" : -1*abs(b) , "eo" : -1*abs(b) , "ud" : -1*abs(b) }
        if a in self.reds:
            result["br"] = 1
        else:
            result["br"] = 2
        if a%2 == 0:
            result["eo"] = 1
        else:
            result["eo"] = 2

        if a < 19:
            result["ud"] = 1
        else:
            result["ud"] = 2

        return result

    def showInform(self):
        if self.detail:
            for j in range(14):
                try:
                    self.step[j].setText(_translate("Form", "흑적 %d-%d(%s[%d],%s[%d])" % (int(self.history[j]["br"]["fwd"][0]), int(self.history[j]["br"]["fwd"][1]),
                                                                                         self.currentAnswers[j][0], self.answers[j]["br"][-1], self.currentAnswers[j][1], self.answers[j]["br"][-2]), None))
                except:
                    try:
                        self.step[j].setText(_translate("Form", "흑적 %d-%d(%s[%d],%s[%d])" % (int(self.history[j]["br"]["fwd"][0]), int(self.history[j]["br"]["fwd"][1]),
                                                                                             self.currentAnswers[j][0], -9, self.currentAnswers[j][1], self.answers[j]["br"][-2]), None))
                    except:
                        pass

                try:
                    self.step2[j].setText(_translate("Form", "홀짝 %d-%d(%s[%d],%s[%d])" % (int(self.history[j]["eo"]["fwd"][0]), int(self.history[j]["eo"]["fwd"][1]),
                                                                                          self.currentAnswers[j][0], self.answers[j]["eo"][-1], self.currentAnswers[j][1], self.answers[j]["eo"][-2]), None))
                except:
                    try:
                        self.step2[j].setText(_translate("Form", "홀짝 %d-%d(%s[%d],%s[%d])" % (int(self.history[j]["eo"]["fwd"][0]), int(self.history[j]["eo"]["fwd"][1]),
                                                                                              self.currentAnswers[j][0], -9, self.currentAnswers[j][1], self.answers[j]["eo"][-2]), None))
                    except:
                        pass

                try:
                    self.step3[j].setText(_translate("Form", "언오버%d-%d(%s[%d],%s[%d])" % (int(self.history[j]["ud"]["fwd"][0]), int(self.history[j]["ud"]["fwd"][1]),
                                                                                          self.currentAnswers[j][0], self.answers[j]["ud"][-1], self.currentAnswers[j][1], self.answers[j]["ud"][-2]), None))
                except:
                    try:
                        self.step3[j].setText(_translate("Form", "언오버%d-%d(%s[%d],%s[%d])" % (int(self.history[j]["ud"]["fwd"][0]), int(self.history[j]["ud"]["fwd"][1]),
                                                                                                self.currentAnswers[j][0], -9, self.currentAnswers[j][1], self.answers[j]["ud"][-2]), None))
                    except:
                        pass
        else:
            for j in range(14):
                try:
                    self.step[j].setText(_translate("Form", "흑적 %d-%d" % (int(self.history[j]["br"]["fwd"][0]), int(self.history[j]["br"]["fwd"][1])), None))
                except:
                    try:
                        self.step[j].setText(_translate("Form", "흑적 %d-%d" % (int(self.history[j]["br"]["fwd"][0]), int(self.history[j]["br"]["fwd"][1])), None))
                    except:
                        pass

                try:
                    self.step2[j].setText(_translate("Form", "홀짝 %d-%d" % (int(self.history[j]["br"]["fwd"][0]), int(self.history[j]["eo"]["fwd"][1])), None))
                except:
                    try:
                        self.step2[j].setText(_translate("Form", "홀짝 %d-%d" % (int(self.history[j]["br"]["fwd"][0]), int(self.history[j]["eo"]["fwd"][1])), None))
                    except:
                        pass

                try:
                    self.step3[j].setText(_translate("Form", "언오버 %d-%d" % (int(self.history[j]["br"]["fwd"][0]), int(self.history[j]["ud"]["fwd"][1])), None))
                except:
                    try:
                        self.step3[j].setText(_translate("Form", "언오버 %d-%d" % (int(self.history[j]["br"]["fwd"][0]), int(self.history[j]["ud"]["fwd"][1])), None))
                    except:
                        pass
    def update(self):

        tbUdateError = 0
        err = ''
        #print("self.seesions1", self.seesions)
        for ss in [self.seesions[-1]]:
            try:
                ss.wd = time.time()
            except:
                pass
            try:
                cnt = 0
                for tb in ss.tableIds:

                    if ss.Alive:
                        #print(ss.tables[tb])
                        if ss.tables[tb] != "룰렛 라이브":
                            try:
                                if ss.tables[tb] == 'VIP 룰렛':
                                    newRN = '프렌치 룰렛 골드'
                                else:
                                    newRN = ss.tables[tb]
                                self.roomName[cnt].setText(_translate("Form", newRN, None))
                                self.roomNames[cnt] = self.roomName[cnt].text()
                            except:
                                print("Exsc")
                                print(traceback.format_exc())
                        cnt += 1


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
        for j in range(14):
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
                        ui.ss = ss

                        if ss.Alive:
                            #print("rn", rn)
                            try:
                                #print("alive")
                                tbrn = ss.tables[rn]
                                if tbrn != "룰렛 라이브":
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

            for j in range(14):
                if self.beforeAnswers[j] != self.currentAnswers[j]:

                    for gt in ["eo" , "br" , "ud"]:
                        if len(self.answers[j][gt])  > 0:
                            bef = self.answers[j][gt][-1]
                        else:
                            bef = 1
                        self.answers[j][gt].append( self.checkAnswer( self.currentAnswers[j][0] , bef )[gt] )
                        if len(self.answers[j][gt]) > 5:
                            self.answers[j][gt] = self.answers[j][gt][-5:]
                        if len(self.answers[j][gt]) > 2:
                            #if self.answers[j][gt][-2] != bef:
                            #print(gt , abs(bef) == self.answers[j][gt][-1] , self.roomNames[j], self.currentAnswers[j][0], self.currentAnswers[j][1] , self.answers[j][gt][-1] , self.answers[j][gt][-2] , bef)


                            if True:#(bef != "__wait__") and (self.answers[j][gt][-1]  != -3 ) and (bef != -3) and (self.currentAnswers[j][0] != "_") :
                                
                                if abs(bef) == self.answers[j][gt][-1]:
                                    #print("ok")
                                    self.history[j][gt]["fwd"][0]+=1
                                else:
                                    #print("fail")
                                    if self.history[j][gt]["fwd"][0] > 3:
                                        self.history[j][gt]["fwd"] = [1,0,0]
                                        self.steps[gt][j].setStyleSheet(_fromUtf8('background-color: rgb(255, 255, 255)'))
                                    else:
                                        if self.history[j][gt]["fwd"][0] < 2:
                                            self.history[j][gt]["fwd"][0] = 1
                                        else:
                                            self.history[j][gt]["fwd"][1] +=1
                                            self.history[j][gt]["fwd"][0] = 1
                                            if self.history[j][gt]["fwd"][1] >  (int(self.stepLimitVal.text())-1) :
                                                #print(j , gt , "alarm")
                                                self.steps[gt][j].setStyleSheet(_fromUtf8('background-color: rgb(255, 206, 80)'))
                                                self.timeLimit = time.time()
                                                QtGui.QSound("./bd_made.wav").play()
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

        self.numOfRoom = 14
        for i in range(self.numOfRoom):
            self.base.append(QtGui.QLabel(Form))
            self.base[-1].setGeometry(QtCore.QRect(10+i*128, 40, 120, 101))
            self.base[-1].setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
            self.base[-1].setText(_fromUtf8(""))
            self.base[-1].setObjectName(_fromUtf8("label_3"))
            self.base[-1].show()
            self.roomName.append(QtGui.QLabel(self.base[-1]))
            self.roomName[-1].setGeometry(QtCore.QRect(2, 20, 118, 12))
            self.roomName[-1].setObjectName(_fromUtf8("label"))
            self.roomName[-1].setText(_translate("Form", "__wait__", None))
            self.roomName[-1].show()
            self.step.append(QtGui.QLabel(self.base[-1]))
            self.step[-1].setGeometry(QtCore.QRect(2 ,40, 118, 12))
            self.step[-1].setObjectName(_fromUtf8("label_2"))
            self.step[-1].setText(_translate("Form", "흑적 0", None))
            self.step[-1].setStyleSheet(_fromUtf8('background-color: rgb(255, 255, 255)'))
            self.step[-1].show()
            self.step2.append(QtGui.QLabel(self.base[-1]))
            self.step2[-1].setGeometry(QtCore.QRect(2 ,63, 118, 12))
            self.step2[-1].setObjectName(_fromUtf8("label_2"))
            self.step2[-1].setText(_translate("Form", "홀짝 0", None))
            self.step2[-1].setStyleSheet(_fromUtf8('background-color: rgb(255, 255, 255)'))
            self.step2[-1].show()
            self.step3.append(QtGui.QLabel(self.base[-1]))
            self.step3[-1].setGeometry(QtCore.QRect(2 ,85, 118, 12))
            self.step3[-1].setObjectName(_fromUtf8("label_2"))
            self.step3[-1].setText(_translate("Form", "언더오버 0", None))
            self.step3[-1].setStyleSheet(_fromUtf8('background-color: rgb(255, 255, 255)'))
            self.step3[-1].show()
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










