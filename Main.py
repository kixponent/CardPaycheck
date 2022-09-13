import json
from bs4 import BeautifulSoup
import requests
import sys
from PyQt5 import QtWidgets
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QAbstractItemView
today_now = datetime.today().strftime("%Y%m%d")

response = requests.get("https://newnibs.nicevan.co.kr/websquare/login.jsp")
cookie=response.cookies

login_data = {"userInfo":{"userId":"hm2021","pwd":"2021gmlakd!","clientIp":"211.216.104.226","authKey":"","authValue":""}}
response_login = requests.post("https://newnibs.nicevan.co.kr/websquare/login.jsp",data=json.dumps(login_data), cookies=cookie, verify=False, allow_redirects=False)
cookie.update(response_login.cookies)

response_ready1 = requests.post("https://newnibs.nicevan.co.kr/login/transactionTime.do", cookies=cookie)
cookie.update(response_ready1.cookies)

data_ready2 = {"menuId":"46","authId":"search","userId":"hm2021"}
response_ready2 = requests.post("https://newnibs.nicevan.co.kr/common/setSessionValue.jsp", data=json.dumps(data_ready2), cookies=cookie, verify=False, allow_redirects=False)
cookie.update(response_ready2.cookies)

data_fetch = {"searchInfo":{"pageIndex":1,"pageUnit":"500","pageSize":10,"totalCnt":"","allSelectYn":"Y","excelLimitCount":"","menuCode":"","USER_GROUP_CODE":"U","USER_AGENT_CODE":"null","DATE_KEY":"TRANSACTION_DATE","DATE_FROM":today_now,"DATE_TO":today_now,"TIME_FROM":"000000","TIME_TO":"235959","SELECT_KEY":"CAT_ID","SELECT_VALUE":"","BC_INCLUDE_YN":"N","SERVICE_CATEGORY_CODE":"","RESPONSE_YN":"","CARD_KIND_CODE":"","ACQUIRE_COMPANY_CODE":"","ISSUE_COMPANY_CODE":"","HOLD_REASON_CODE":"","ACQUIRE_STATUS_CODE":"","TAX_FREE":"","ISARANG":"ALL","CARD_FULL_NO":"Y","USER_ID":"hm2021","CAT_ID":"","AGENT_CODE":"","niceSerialNo":"","srcAmount":"","srcAmount2":"","srcAmt":"AMT1","srcAmtType":"A","ACQUIRE_METHOD_CODE":"","GROUP_AGENT_CODE":"","GROUP_CODE":"","NAVER_SELECT_KEY":"","NAVER_SELECT_VALUE":""}}
response_find = requests.post("https://newnibs.nicevan.co.kr/TrnCrd001/selectMainList.do",data=json.dumps(data_fetch), cookies=cookie, verify=False, allow_redirects=False)
data_raw = response_find.text
data_json = json.loads(data_raw)

def relogin():
    response = requests.get("https://newnibs.nicevan.co.kr/websquare/login.jsp")
    response.encoding = 'euc-kr'
    cookie.update(response.cookies)

def refresh():
    login_data = {"userInfo": {"userId": "hm2021", "pwd": "2021gmlakd!", "clientIp": "211.216.104.226", "authKey": "",
                               "authValue": ""}}
    response_login = requests.post("https://newnibs.nicevan.co.kr/websquare/login.jsp", data=json.dumps(login_data),
                                   cookies=cookie, verify=False, allow_redirects=False)
    response_login.encoding = 'euc-kr'
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
    response_find = requests.post("https://newnibs.nicevan.co.kr/TrnCrd001/selectMainList.do",
                                  data=json.dumps(data_fetch), cookies=cookie, verify=False,
                                  allow_redirects=False)
    data_raw = response_find.text
    data_json = json.loads(data_raw)

class TableWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('희망약국 카드 결제 확인 앱')
        self.initUI()
        """
        표 위
        """

    def initUI(self):
        TotalAmt = 0
        for i in range(0, data_json['dsSum'].__len__()):
            a = data_json['dsSum'][i]['approvalAmt']
            TotalAmt = TotalAmt + a
        # table_sum.setItem(0,0,QtWidgets.QTableWidgetItem(str(TotalAmt)))

        pushButton_refresh = QtWidgets.QPushButton(self)
        pushButton_refresh.resize(80,20)
        pushButton_refresh.move(0,5)
        pushButton_refresh.setObjectName("refresh")
        pushButton_refresh.setText("불러 오기")
        pushButton_refresh.clicked.connect(self.refresh2)

        self.Main_table = QtWidgets.QTableWidget(self)
        self.Main_table.resize(450, 900)
        self.Main_table.move(0, 30)
        # 표의 크기를 지정
        self.Main_table.setColumnCount(4)
        self.Main_table.setRowCount(data_json['dsMain'].__len__())
        # 열 제목 지정
        self.Main_table.setHorizontalHeaderLabels(
            ['거래시간', '승인번호', '카드회사', '총합 : '+str(TotalAmt)]
        )
        self.Main_table.setSortingEnabled(True)
        self.Main_table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 셀 edit 금지

    def refresh2(self):
        response_find = requests.post("https://newnibs.nicevan.co.kr/TrnCrd001/selectMainList.do",
                                      data=json.dumps(data_fetch), cookies=cookie, verify=False,
                                      allow_redirects=False)
        data_raw = response_find.text
        data_json = json.loads(data_raw)

        TotalAmt = 0
        for i in range(0, data_json['dsSum'].__len__()):
            a = data_json['dsSum'][i]['saleAmt']
            TotalAmt = TotalAmt + a

        # table = QtWidgets.QTableWidget(self)
        # table.resize(450, 700)
        # table.move(0, 30)
        # # 표의 크기를 지정
        # table.setColumnCount(4)
        self.Main_table.setRowCount(data_json['dsMain'].__len__())
        # 열 제목 지정
        self.Main_table.setHorizontalHeaderLabels(
            ['거래시간', '승인번호', '카드회사', '총합 : ' + format(TotalAmt, ',')]
        )
        for i in range(0, data_json['dsMain'].__len__()):
            self.Main_table.setItem(i, 0, QtWidgets.QTableWidgetItem(data_json['dsMain'][i]['transactionTime']))
            self.Main_table.setItem(i, 1, QtWidgets.QTableWidgetItem(data_json['dsMain'][i]['approvalNo']))
            self.Main_table.setItem(i, 2, QtWidgets.QTableWidgetItem(data_json['dsMain'][i]['acqCompanyCode']))
            self.Main_table.setItem(i, 3, QtWidgets.QTableWidgetItem(format(data_json['dsMain'][i]['settlementAmount'], ',')))

if __name__ == "__main__":
    APP = QtWidgets.QApplication(sys.argv)
    WINDOW = TableWidget()
    WINDOW.show()
    APP.exec()