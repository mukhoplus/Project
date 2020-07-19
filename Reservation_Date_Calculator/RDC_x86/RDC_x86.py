#-*- coding:utf-8 -*-
# ... iss Crew
# ... Made By Mukho
# ... 2020-07-16 THU
# ... 23Div Reservation Date Calculation

# Import
import sys
from PyQt4.QtCore import QDate, Qt, pyqtSlot
from PyQt4 import QtGui
from PyQt4.QtGui import *

class MyApp(QWidget):
    # MyApp 생성자
    def __init__(self):
        super(MyApp, self).__init__()
        self.initUI()
    
    # 초기 UI
    def initUI(self):
        # Made By Mukho
        self.lbl = QLabel(self)
        self.lbl.setText("Made By Mukho")

        # 메인 달력
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.setVerticalHeaderFormat(0)
        cal.clicked.connect(self.showDate)

        # 글자 크기 변경
        font = QtGui.QFont()
        font.setPointSize(18)

        # 오늘 날짜
        self.lbl_today = QLabel(self)
        today = QDate.currentDate()
        self.lbl_today.setText("++Today : " + today.toString('yyyy-MM-dd dddd'))
        self.lbl_today.setFont(font)

        # 오늘 기준 23사단 간부 예약일자 계산
        self.lbl_div23 = QLabel(self)
        div23 = today.addDays(13)
        self.lbl_div23.setText(" +div23 : " + div23.toString('yyyy-MM-dd dddd'))
        self.lbl_div23.setFont(font)

        # 오늘 기준 타 사단 간부 예약일자 계산
        self.lbl_divAnother = QLabel(self)
        divAnother = today.addDays(9)
        self.lbl_divAnother.setText(" +divAnother : " + divAnother.toString('yyyy-MM-dd dddd'))
        self.lbl_divAnother.setFont(font)

        # 선택된 날짜
        self.lbl_select_day = QLabel(self)
        date = cal.selectedDate()
        self.lbl_select_day.setText("**Selected Date : " + date.toString('yyyy-MM-dd dddd'))
        self.lbl_select_day.setFont(font)

        # 23사단 간부의 경우 선택된 날짜는 언제 예약이 가능한가?
        self.lbl_select_div23 = QLabel(self)
        div23_select = date.addDays(-13)
        self.lbl_select_div23.setText(" *div23 can : " + div23_select.toString('yyyy-MM-dd dddd'))
        self.lbl_select_div23.setFont(font)

        # 타사단 간부의 경우 선택된 날짜는 언제 예약이 가능한가?
        self.lbl_select_divAnother = QLabel(self)
        divAnother_select = date.addDays(-9)
        self.lbl_select_divAnother.setText(" *divAnother can : " + divAnother_select.toString('yyyy-MM-dd dddd'))
        self.lbl_select_divAnother.setFont(font)

        # 위젯들을 수직 방향으로 배치하는 레이아웃 사용
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl)
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl_today)
        vbox.addWidget(self.lbl_div23)
        vbox.addWidget(self.lbl_divAnother)
        vbox.addWidget(self.lbl_select_day)
        vbox.addWidget(self.lbl_select_div23)
        vbox.addWidget(self.lbl_select_divAnother)

        # 설정
        self.setLayout(vbox)

        # 제목, 아이콘, 초기 위치 + 창 크기 설정 및 프로그램 실행
        self.setWindowTitle('Reservation Date Calculator')
        self.setWindowIcon(QIcon('23Div.jpg'))
        self.setGeometry(300, 300, 350, 450)
        self.show()

    # 달력에서 날짜를 선택했을 때, 출력되는 날짜들 계산
    def showDate(self, date):
        #date = cal.selectedDate() # 선택한 날짜

        self.lbl_select_day.setText("**Selected Date : " + date.toString('yyyy-MM-dd dddd'))

        # 23사단 간부
        div23_select = date.addDays(-13)
        self.lbl_select_div23.setText(" *div23 can : " + div23_select.toString('yyyy-MM-dd dddd'))

        # 타사단 간부
        divAnother_select = date.addDays(-9)
        self.lbl_select_divAnother.setText(" *divAnother can : " + divAnother_select.toString('yyyy-MM-dd dddd'))

# 무코무코니
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())