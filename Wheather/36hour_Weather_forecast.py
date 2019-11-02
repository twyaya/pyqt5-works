# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#下載json檔案
import sys
from urllib.request import urlretrieve
import json
from WeatherWindow import Ui_Form
from PyQt5.QtWidgets import QApplication , QMainWindow 
from PyQt5 import QtGui

data_url = "https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=CWB-54BBDDF9-E30A-4218-9F60-07D8D4F44EA0&downloadType=WEB&format=JSON"
urlretrieve(data_url,'./wheather.json') #儲存氣象局天氣預報json檔案
with open("wheather.json","r",encoding="utf-8") as f:
    data = json.load(f) 
"""
轉換成dict
"""


class MainUi(QMainWindow, Ui_Form):  #  MainUi 繼承自兩個類別(Python的多重繼承)
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("天氣查詢頁面")


    def clearResult(self):
        print('* clearResult  ')
        self.ui.resultText.clear()
        


    def transCityName(self ,cityName):
        if cityName == '臺北市' :
            number = 0
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
            
            
        elif cityName == '新北市' :
            number = 1
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
        elif cityName == '桃園市' :
            number = 2
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
        elif cityName == '臺中市' :
            number = 3
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
        elif cityName == '臺南市' :
            number = 4
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
        elif cityName == '高雄市' :
            number = 5
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
        elif cityName == '基隆市' :
            number = 6
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
        elif cityName == '新竹縣' :
            number = 7
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
        elif cityName == '新竹市' :
            number = 8
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
        elif cityName == '苗栗縣' :
            number = 9
            today = cityName + "今日: "+ data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            tomorrow = cityName +"明日: "+ data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            the_day_after_tomorrow = cityName +"後天: "+ data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
        elif cityName == '彰化縣' :
            number = 10
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
        elif cityName == '南投縣' :
            number = 11
            today = cityName + "今日: "+ data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            tomorrow = cityName +"明日: "+ data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            the_day_after_tomorrow = cityName +"後天: "+ data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
        elif cityName == '雲林縣' :
            number = 12
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
        elif cityName == '嘉義縣' :
            number = 13
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
        elif cityName == '嘉義市' :
            number = 14
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
        elif cityName == '屏東縣' :
            number = 15
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
        elif cityName == '宜蘭縣' :
            number = 16
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
        elif cityName == '花蓮縣' :
            number = 17
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
        elif cityName == '臺東縣':
            number = 18
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
        elif cityName == '澎湖縣' :
            number = 19
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
        elif cityName == '金門縣' :
            number = 20
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
        elif cityName == '連江縣' :
            number = 21
            today_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][0]['parameter']['parameterName']
            today_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][0]['parameter']['parameterName']
            today_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][0]['parameter']['parameterName']
            today_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][0]['parameter']['parameterName']
            today_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][1]['parameter']['parameterName']
            tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][1]['parameter']['parameterName']
            tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][1]['parameter']['parameterName']
            tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][1]['parameter']['parameterName']
            tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][1]['parameter']['parameterName']
            
            
            the_day_after_tomorrow_wheather = data['cwbopendata']['dataset']['location'][number]['weatherElement'][0]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_maxTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][1]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_minTemperature = data['cwbopendata']['dataset']['location'][number]['weatherElement'][2]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_comfort_index = data['cwbopendata']['dataset']['location'][number]['weatherElement'][3]['time'][2]['parameter']['parameterName']
            the_day_after_tomorrow_probability_of_precipitation = data['cwbopendata']['dataset']['location'][number]['weatherElement'][4]['time'][2]['parameter']['parameterName']
            
            today = cityName + "今日天氣: "+ today_wheather + "\n" + "最高溫(攝氏): " + today_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + today_minTemperature + "°C" + "\n" + "舒適度: " + today_comfort_index + "\n" + "降雨機率: " + today_probability_of_precipitation + "%"+ "\n" 
            tomorrow = cityName + "明日天氣: "+ tomorrow_wheather + "\n" + "最高溫(攝氏): " + tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + tomorrow_comfort_index + "\n" + "降雨機率: " + tomorrow_probability_of_precipitation + "%"+ "\n" 
            the_day_after_tomorrow = cityName + "後天天氣: "+ the_day_after_tomorrow_wheather + "\n" + "最高溫(攝氏): " + the_day_after_tomorrow_maxTemperature + "°C" + "\n" + "最低溫(攝氏): " + the_day_after_tomorrow_minTemperature + "°C" + "\n" + "舒適度: " + the_day_after_tomorrow_comfort_index + "\n" + "降雨機率: " + the_day_after_tomorrow_probability_of_precipitation + "%"
        
        return today,tomorrow,the_day_after_tomorrow

    def queryWeather(self):
        print('* queryWeather  ')
        cityName = self.ui.weatherComboBox.currentText()
        whe1 = str(self.transCityName(cityName)[0]) + "\n"
        whe2 = str(self.transCityName(cityName)[1]) + "\n"
        whe3 = str(self.transCityName(cityName)[2]) + "\n"
        
        
        result = whe1 + whe2 + whe3
        self.ui.resultText.setText(result)
        self.ui.resultText.setFont(QtGui.QFont('標楷體', 16))
        
if __name__ == "__main__":
    def run_app():
        app = QApplication(sys.argv)
        window = MainUi()
        window.show()
        app.exec_()
    run_app()





