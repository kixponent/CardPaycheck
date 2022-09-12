# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paycheck.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import json
from bs4 import BeautifulSoup
import csv
import requests
import socket
import sys
from PyQt5 import QtWidgets
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

header = {
"Host": "newnibs.nicevan.co.kr",
"Connection": "keep-alive",
"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
"sec-ch-ua-mobile": "?0",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Sec-Fetch-Site": "none",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-User": "?1",
"Sec-Fetch-Dest": "document",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6"}

response = requests.get("https://newnibs.nicevan.co.kr/websquare/login.jsp")
response.encoding = 'euc-kr'
soup = BeautifulSoup(response.text, 'html.parser')
eternal_cookie = response.headers._store.get('set-cookie')[1][:response.headers._store.get('set-cookie')[1].find(";")]
eternal_logintime = response.cookies._now

############################################로그인전 기본 쿠키 얻기 #############################################
today_now = datetime.today().strftime("%Y%m%d")
header_login={
"Accept": "application/json",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6",
"Connection": "keep-alive",
"Content-Length": "106",
"Content-Type": 'application/json; charset="UTF-8"',
"Cookie": eternal_cookie,
"Host": "newnibs.nicevan.co.kr",
"Origin": "https://newnibs.nicevan.co.kr",
"Referer": "https://newnibs.nicevan.co.kr/websquare/login.jsp",
"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
"sec-ch-ua-mobile": "?0",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-origin",
"submissionid": "sbm_UserLogin",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

    # "Host": "newnibs.nicevan.co.kr",
    #   "Connection": "keep-alive",
    #   "Content-Length": "106",
    #   # "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    #   "Accept": "application/json",
    #   "submissionid": "sbm_UserLogin",
    #   "sec-ch-ua-mobile": "?0",
    #   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    #   "Content-Type": "application/json charset = UTF-8",
    #   "Origin": "https://newnibs.nicevan.co.kr",
    #   "Sec-Fetch-Site": "same-origin",
    #   "Sec-Fetch-Mode": "cors",
    #   "Sec-Fetch-Dest": "empty",
    #   "Referer": "https://newnibs.nicevan.co.kr/websquare/login.jsp",
    #   "Accept-Encoding": "gzip, deflate, br",
    #   "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6",
    #   "Cookie": "lastAccess=1621173277622; globalDebug=false; JSESSIONID=BA75789B625C73E61E60870F0DDED071}"}

login_data = {"userInfo":{"userId":"hm2021","pwd":"2021gml!","clientIp":"211.216.104.226","authKey":"","authValue":""}}

# with requests.Session() as s:
#     res = s.post("https://newnibs.nicevan.co.kr/login/userLogin.do", data=json.dumps(login_data), verify=False, allow_redirects=False)
#     redirect_cookie = res.headers['Set-Cookie']
#     # redirect_url = res.headers['Location']
#     headers = {"Cookie": redirect_cookie}
#
#
#
#
# response_login = requests.post("https://newnibs.nicevan.co.kr/login/userLogin.do", data=login_data)
# response_login.encoding = 'euc-kr'
# "https://newnibs.nicevan.co.kr/CodReg010/selectFavoriteList.do" \
# "https://newnibs.nicevan.co.kr/common/getSessionValue.jsp"
#
# response = requests.get("https://newnibs.nicevan.co.kr/websquare/index.jsp")
# response.encoding = 'euc-kr'
# soup = BeautifulSoup(response.text, 'html.parser')
response_login = requests.post("https://newnibs.nicevan.co.kr/websquare/login.jsp",data=json.dumps(login_data), headers=header_login, verify=False, allow_redirects=False)
response_login.encoding = 'euc-kr'
soup_login = BeautifulSoup(response_login.text, 'html.parser')

"https://newnibs.nicevan.co.kr/websquare/index.jsp?w2xPath=/main/kr/co/nibs/management/Trn/TrnCrd/TrnCrd001.xml&w2xHome=/main/kr/co/nibs/common/&w2xDocumentRoot="

data_fetch = {"searchInfo":{"pageIndex":1,"pageUnit":"500","pageSize":10,"totalCnt":"","allSelectYn":"Y","excelLimitCount":"","menuCode":"","USER_GROUP_CODE":"U","USER_AGENT_CODE":"null","DATE_KEY":"TRANSACTION_DATE","DATE_FROM":today_now,"DATE_TO":today_now,"TIME_FROM":"0000","TIME_TO":"2359","SELECT_KEY":"CAT_ID","SELECT_VALUE":"","BC_INCLUDE_YN":"N","SERVICE_CATEGORY_CODE":"","RESPONSE_YN":"","CARD_KIND_CODE":"","ACQUIRE_COMPANY_CODE":"","ISSUE_COMPANY_CODE":"","HOLD_REASON_CODE":"","ACQUIRE_STATUS_CODE":"","TAX_FREE":"","ISARANG":"ALL","CARD_FULL_NO":"Y","USER_ID":"hm2021","CAT_ID":"","AGENT_CODE":"","niceSerialNo":"","srcAmount":"","srcAmount2":"","srcAmt":"AMT1","srcAmtType":"A","ACQUIRE_METHOD_CODE":"","GROUP_AGENT_CODE":"","GROUP_CODE":""}}
cookie_data = {"lastAccess="+str(eternal_logintime), "globalDebug=false", "JSESSIONID="+str(eternal_cookie)}
header_fetch =  {
"Host": "newnibs.nicevan.co.kr",
"Connection": "keep-alive",
"Content-Length": "747",
"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
"Accept": "application/json",
"submissionid": "sbm_searchMain",
"sec-ch-ua-mobile": "?0",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
"Content-Type": 'application/json; charset="UTF-8"',
"Origin": "https://newnibs.nicevan.co.kr",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://newnibs.nicevan.co.kr/websquare/index.jsp?w2xPath=/main/kr/co/nibs/management/Trn/TrnCrd/TrnCrd001T1.xml&w2xHome=/main/kr/co/nibs/common/&w2xDocumentRoot=",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6',
"Cookie": str(cookie_data)
}
response_find = requests.post("https://newnibs.nicevan.co.kr/TrnCrd001/selectMainList.do",data=json.dumps(data_fetch), headers=header_fetch, verify=False, allow_redirects=False)
data_raw = response_find.text
data_json = json.loads(data_raw)
def relogin():
    header = {
        "Host": "newnibs.nicevan.co.kr",
        "Connection": "keep-alive",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        "sec-ch-ua-mobile": "?0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6"}

    response = requests.get("https://newnibs.nicevan.co.kr/websquare/login.jsp")
    response.encoding = 'euc-kr'
    soup = BeautifulSoup(response.text, 'html.parser')
    eternal_cookie = response.headers._store.get('set-cookie')[1][
                     :response.headers._store.get('set-cookie')[1].find(";")]
    eternal_logintime = response.cookies._now

    ############################################로그인전 기본 쿠키 얻기 #############################################
    today_now = datetime.today().strftime("%Y%m%d")
    header_login = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6",
        "Connection": "keep-alive",
        "Content-Length": "106",
        "Content-Type": 'application/json; charset="UTF-8"',
        "Cookie": eternal_cookie,
        "Host": "newnibs.nicevan.co.kr",
        "Origin": "https://newnibs.nicevan.co.kr",
        "Referer": "https://newnibs.nicevan.co.kr/websquare/login.jsp",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        "sec-ch-ua-mobile": "?0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "submissionid": "sbm_UserLogin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

    # "Host": "newnibs.nicevan.co.kr",
    #   "Connection": "keep-alive",
    #   "Content-Length": "106",
    #   # "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    #   "Accept": "application/json",
    #   "submissionid": "sbm_UserLogin",
    #   "sec-ch-ua-mobile": "?0",
    #   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    #   "Content-Type": "application/json charset = UTF-8",
    #   "Origin": "https://newnibs.nicevan.co.kr",
    #   "Sec-Fetch-Site": "same-origin",
    #   "Sec-Fetch-Mode": "cors",
    #   "Sec-Fetch-Dest": "empty",
    #   "Referer": "https://newnibs.nicevan.co.kr/websquare/login.jsp",
    #   "Accept-Encoding": "gzip, deflate, br",
    #   "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6",
    #   "Cookie": "lastAccess=1621173277622; globalDebug=false; JSESSIONID=BA75789B625C73E61E60870F0DDED071}"}

    login_data = {"userInfo": {"userId": "hm2021", "pwd": "2021gml!", "clientIp": "211.216.104.226", "authKey": "",
                               "authValue": ""}}

def refresh():
    today_now = datetime.today().strftime("%Y%m%d")
    header_login = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6",
        "Connection": "keep-alive",
        "Content-Length": "106",
        "Content-Type": 'application/json; charset="UTF-8"',
        "Cookie": eternal_cookie,
        "Host": "newnibs.nicevan.co.kr",
        "Origin": "https://newnibs.nicevan.co.kr",
        "Referer": "https://newnibs.nicevan.co.kr/websquare/login.jsp",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        "sec-ch-ua-mobile": "?0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "submissionid": "sbm_UserLogin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

    # "Host": "newnibs.nicevan.co.kr",
    #   "Connection": "keep-alive",
    #   "Content-Length": "106",
    #   # "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    #   "Accept": "application/json",
    #   "submissionid": "sbm_UserLogin",
    #   "sec-ch-ua-mobile": "?0",
    #   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    #   "Content-Type": "application/json charset = UTF-8",
    #   "Origin": "https://newnibs.nicevan.co.kr",
    #   "Sec-Fetch-Site": "same-origin",
    #   "Sec-Fetch-Mode": "cors",
    #   "Sec-Fetch-Dest": "empty",
    #   "Referer": "https://newnibs.nicevan.co.kr/websquare/login.jsp",
    #   "Accept-Encoding": "gzip, deflate, br",
    #   "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6",
    #   "Cookie": "lastAccess=1621173277622; globalDebug=false; JSESSIONID=BA75789B625C73E61E60870F0DDED071}"}

    login_data = {"userInfo": {"userId": "hm2021", "pwd": "2021gml!", "clientIp": "211.216.104.226", "authKey": "",
                               "authValue": ""}}

    # with requests.Session() as s:
    #     res = s.post("https://newnibs.nicevan.co.kr/login/userLogin.do", data=json.dumps(login_data), verify=False, allow_redirects=False)
    #     redirect_cookie = res.headers['Set-Cookie']
    #     # redirect_url = res.headers['Location']
    #     headers = {"Cookie": redirect_cookie}
    #
    #
    #
    #
    # response_login = requests.post("https://newnibs.nicevan.co.kr/login/userLogin.do", data=login_data)
    # response_login.encoding = 'euc-kr'
    # "https://newnibs.nicevan.co.kr/CodReg010/selectFavoriteList.do" \
    # "https://newnibs.nicevan.co.kr/common/getSessionValue.jsp"
    #
    # response = requests.get("https://newnibs.nicevan.co.kr/websquare/index.jsp")
    # response.encoding = 'euc-kr'
    # soup = BeautifulSoup(response.text, 'html.parser')
    response_login = requests.post("https://newnibs.nicevan.co.kr/websquare/login.jsp", data=json.dumps(login_data),
                                   headers=header_login, verify=False, allow_redirects=False)
    response_login.encoding = 'euc-kr'
    soup_login = BeautifulSoup(response_login.text, 'html.parser')

    "https://newnibs.nicevan.co.kr/websquare/index.jsp?w2xPath=/main/kr/co/nibs/management/Trn/TrnCrd/TrnCrd001.xml&w2xHome=/main/kr/co/nibs/common/&w2xDocumentRoot="

    data_fetch = {"searchInfo": {"pageIndex": 1, "pageUnit": "500", "pageSize": 10, "totalCnt": "", "allSelectYn": "Y",
                                 "excelLimitCount": "", "menuCode": "", "USER_GROUP_CODE": "U",
                                 "USER_AGENT_CODE": "null", "DATE_KEY": "TRANSACTION_DATE", "DATE_FROM": today_now,
                                 "DATE_TO": today_now, "TIME_FROM": "0000", "TIME_TO": "2359", "SELECT_KEY": "CAT_ID",
                                 "SELECT_VALUE": "", "BC_INCLUDE_YN": "N", "SERVICE_CATEGORY_CODE": "",
                                 "RESPONSE_YN": "", "CARD_KIND_CODE": "", "ACQUIRE_COMPANY_CODE": "",
                                 "ISSUE_COMPANY_CODE": "", "HOLD_REASON_CODE": "", "ACQUIRE_STATUS_CODE": "",
                                 "TAX_FREE": "", "ISARANG": "ALL", "CARD_FULL_NO": "Y", "USER_ID": "hm2021",
                                 "CAT_ID": "", "AGENT_CODE": "", "niceSerialNo": "", "srcAmount": "", "srcAmount2": "",
                                 "srcAmt": "AMT1", "srcAmtType": "A", "ACQUIRE_METHOD_CODE": "", "GROUP_AGENT_CODE": "",
                                 "GROUP_CODE": ""}}
    cookie_data = {"lastAccess=" + str(eternal_logintime), "globalDebug=false", "JSESSIONID=" + str(eternal_cookie)}
    header_fetch = {
        "Host": "newnibs.nicevan.co.kr",
        "Connection": "keep-alive",
        "Content-Length": "747",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        "Accept": "application/json",
        "submissionid": "sbm_searchMain",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Content-Type": 'application/json; charset="UTF-8"',
        "Origin": "https://newnibs.nicevan.co.kr",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://newnibs.nicevan.co.kr/websquare/index.jsp?w2xPath=/main/kr/co/nibs/management/Trn/TrnCrd/TrnCrd001T1.xml&w2xHome=/main/kr/co/nibs/common/&w2xDocumentRoot=",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6',
        "Cookie": str(cookie_data)
    }
    response_find = requests.post("https://newnibs.nicevan.co.kr/TrnCrd001/selectMainList.do",
                                  data=json.dumps(data_fetch), headers=header_fetch, verify=False,
                                  allow_redirects=False)
    data_raw = response_find.text
    data_json = json.loads(data_raw)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435,725)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 10, 80, 25))
        self.pushButton.setObjectName("pushButton")
        self.tableView = TableWidget()
        self.tableView.setGeometry(QtCore.QRect(5, 40, 425, 680))
        self.tableView.setObjectName("tableView")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(5, 10, 95, 25))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2021, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(105, 10, 80, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        TotalAmt = 0
        for i in range(0, data_json['dsSum'].__len__()):
            a = data_json['dsSum'][i]['approvalAmt']
            TotalAmt = TotalAmt + a

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(210, 10, 135, 25))
        self.listView.setObjectName("listView")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "희망약국 카드 사용 결제 내역 조회"))
        self.pushButton.setText(_translate("MainWindow", "새로고침"))
        self.pushButton_2.setText(_translate("MainWindow", "날짜 변경"))

class TableWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('희망약국 카드 결제 확인 앱')
        # self.initUI()

        """
        표 위젯 초기화
        """
        # table_sum = QtWidgets.QTableWidget(self)
        # table_sum.resize(450,120)
        # table_sum.setColumnCount(1)
        # table_sum.setRowCount(1)
        # table_sum.setHorizontalHeaderLabels(
        #     ['총합']
        # )
        #
        TotalAmt = 0
        for i in range(0, data_json['dsSum'].__len__()):
            a = data_json['dsSum'][i]['approvalAmt']
            TotalAmt = TotalAmt + a
        # table_sum.setItem(0,0,QtWidgets.QTableWidgetItem(str(TotalAmt)))



        table = QtWidgets.QTableWidget(self)
        table.resize(450, 900)
        # 표의 크기를 지정
        table.setColumnCount(4)
        table.setRowCount(data_json['dsMain'].__len__()+1)
        # 열 제목 지정
        table.setHorizontalHeaderLabels(
            ['거래시간', '승인번호', '카드회사', '총합 : '+str(TotalAmt)]
        )

        # 셀 내용 채우기
        # table.setItem(0, 0, QtWidgets.QTableWidgetItem(str(TotalAmt)))
        for i in range(0, data_json['dsMain'].__len__()):
            table.setItem(i, 0, QtWidgets.QTableWidgetItem(data_json['dsMain'][i]['transactionTime']))
            table.setItem(i, 1, QtWidgets.QTableWidgetItem(data_json['dsMain'][i]['approvalNo']))
            table.setItem(i, 2, QtWidgets.QTableWidgetItem(data_json['dsMain'][i]['acqCompanyCode']))
            table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(data_json['dsMain'][i]['settlementAmount'])))


# if __name__ == "__main__":
#     APP = QtWidgets.QApplication(sys.argv)
#     WINDOW = TableWidget()
#     WINDOW.show()
#     APP.exec()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
