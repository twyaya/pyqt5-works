# -*- coding: utf-8 -*-

"""
    【簡介】
    自動化測試案例


"""

import sys
import unittest
import HTMLTestRunner
import time
from PyQt5.QtWidgets import *
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt , QThread  ,  pyqtSignal
import main 

# 繼承 QThread 類別
class BackWorkThread(QThread):  
	# 宣告一個訊號，同時返回一個str
	finishSignal = pyqtSignal(str)
	# 建構函數裡增加形參
	def __init__(self, sleepTime,parent=None):
		super(BackWorkThread, self).__init__(parent)
		# 儲存參數
		self.sleepTime = sleepTime

	#重寫run()函數，在裡面定時執行任務。
	def run(self):
		# 休眠一段時間
		time.sleep(self.sleepTime)
		# 休眠結束，傳送一個訊號告訴主執行緒視窗
		self.finishSignal.emit('ok , begin to close Window')
		
class WeatherWindowTest(unittest.TestCase):  
    # 初始化工作  
    def setUp(self):  
        print('*** setUp ***')
        self.app = QApplication(sys.argv)	
        self.form = main.MainUi()
        self.form.show()		
		
		# 新建物件，傳入參數。每5秒關閉一個測試案例
        self.bkThread = BackWorkThread(int( 5 ))
		# 連接子處理序的訊號和槽函數
        self.bkThread.finishSignal.connect(self.closeWindow)
		#self.bkThread.finishSignal.connect(self.app.exec_)
		
		# 啟動執行緒，開始執行run()函數的內容
        self.bkThread.start()
		        
        # 退出清理工作
    def tearDown(self):  
        print('*** tearDown ***')
        self.app.exec_()  		
        
        # 關閉視窗
    def closeWindow(self):
        print( '*  關閉視窗')
        self.app.quit()
        
        
    def setFormToZero(self):
        print('* setFormToZero *') 
        self.form.ui.weatherComboBox.setCurrentText('臺北市')
        self.form.ui.resultText.setText(" ")
        
        
        
        
    # 測試用例-在預設狀態下測試GUI	
    def test_defaults(self):
        '''測試GUI處於預設狀態'''
        print('*** testCase test_defaults begin ***')
        self.form.setWindowTitle('開始測試用例 test_defaults ')

        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '臺北市')

        print('*** 查詢的是='+ self.form.ui.weatherComboBox.currentText() )
	
        # 用滑鼠左鍵按OK		
        okWidget = self.form.ui.queryBtn
        QTest.mouseClick(okWidget, Qt.LeftButton)
		
        print('*** testCase test_defaults end ***')
		

	# 測試案例-測試計數器控制項
    def test_weatherComboBox(self):
        '''	測試用例 test_weatherComboBox '''	
        print('*** testCase test_weatherComboBox begin ***')
        self.form.setWindowTitle('開始測試用例 test_weatherComboBox ')	
        self.setFormToZero()
        ''' 測試修改ComboBox元件 '''
        self.form.ui.weatherComboBox.setCurrentText('臺北市')
        #self.form.queryWeather()
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '臺北市')
        
        
        self.form.ui.weatherComboBox.setCurrentText('新北市')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '新北市')
        
        self.form.ui.weatherComboBox.setCurrentText('基隆市')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '基隆市')
        
        
        self.form.ui.weatherComboBox.setCurrentText('桃園市')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '桃園市')
        
        self.form.ui.weatherComboBox.setCurrentText('臺中市')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '臺中市')
        
        self.form.ui.weatherComboBox.setCurrentText('臺南市')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '臺南市')
        
        self.form.ui.weatherComboBox.setCurrentText('高雄市')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '高雄市')
        
        self.form.ui.weatherComboBox.setCurrentText('新竹縣')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '新竹縣')
        
        self.form.ui.weatherComboBox.setCurrentText('新竹市')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '新竹市')
        
        self.form.ui.weatherComboBox.setCurrentText('苗栗縣')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '苗栗縣')
        
        self.form.ui.weatherComboBox.setCurrentText('彰化縣')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '彰化縣')
        
        self.form.ui.weatherComboBox.setCurrentText('南投縣')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '南投縣')
        
        self.form.ui.weatherComboBox.setCurrentText('雲林縣')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '雲林縣')
        
        self.form.ui.weatherComboBox.setCurrentText('嘉義縣')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '嘉義縣')
        
        self.form.ui.weatherComboBox.setCurrentText('嘉義市')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '嘉義市')
        
        self.form.ui.weatherComboBox.setCurrentText('屏東縣')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '屏東縣')
        
        self.form.ui.weatherComboBox.setCurrentText('宜蘭縣')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '宜蘭縣')
        
        self.form.ui.weatherComboBox.setCurrentText('花蓮縣')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '花蓮縣')
        
        self.form.ui.weatherComboBox.setCurrentText('臺東縣')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '臺東縣')
        
        self.form.ui.weatherComboBox.setCurrentText('澎湖縣')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '澎湖縣')
        
        self.form.ui.weatherComboBox.setCurrentText('金門縣')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '金門縣')
        
        self.form.ui.weatherComboBox.setCurrentText('連江縣')
        self.form.ui.queryBtn.click()
        self.assertEqual(self.form.ui.weatherComboBox.currentText(), '連江縣')
        




def runUnitTest1(  ):
	# 預設測試所有的測試用例
	unittest.main() 	

def runUnitTest2(  ):
	# 按照指定順序執行測試用例
	suite = unittest.TestSuite()
	suite.addTest(WeatherWindowTest("test_defaults"))
	suite.addTest(WeatherWindowTest("test_weatherComboBox"))
	runner = unittest.TextTestRunner()
	runner.run(suite)
	
if __name__ == "__main__":  
	runUnitTest1()
    #runUnitTest2()

