'''
保留 ui 引用版本代碼


path = os.getcwd()
qtCreatorFile = path + os.sep + "ui" + os.sep + "Main_Window.ui"  # 設計好的ui檔案路徑

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)   # 讀入用Qt Designer設計的GUI layout
'''

import math
import sys
from ui import Window 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
Ui_MainWindow = Window.Ui_MainWindow




class MainUi(QMainWindow, Ui_MainWindow):  #  MainUi 繼承自兩個類別(Python的多重繼承)
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_onClick) 
        self.times = 0
        self.bmi_list = []




    def msg(self):  
        reply = QMessageBox.warning(self, "警告", "請輸入數值", QMessageBox.Yes,  QMessageBox.Yes ) 

    def pushButton_onClick(self):
        self.times += 1
        
        try:
            weight = float(self.weight.text())
            height = float(self.height.text())
            bmi = round(weight/(math.pow(height/100,2)),2)
            self.BMI.setText(str(bmi))  #計算
            self.bmi_list.append(str(bmi))

            if self.times > 1:
                self.bmi_last.setText(self.bmi_list[self.times-2])
            
            if bmi < 18.5:
                self.label_4.setText("體重過輕")
            elif 18 <= bmi < 24:
                self.label_4.setText("體重正常")
            elif 24 <= bmi < 27:
                self.label_4.setText("過重")
            elif 27 <= bmi < 30:
                self.label_4.setText("輕度肥胖")
            elif 30 <= bmi < 35:
                self.label_4.setText("中度肥胖")
            elif 35 <= bmi  :                       #不採用else保持新增的方便性
                self.label_4.setText("重度肥胖")
                
        except ValueError:
            self.msg()


            
            
            
if __name__ == "__main__":
    def run_app():
        app = QApplication(sys.argv)
        window = MainUi()
        window.show()
        app.exec_()
    run_app()


