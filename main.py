from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import csv
import GUI as ui
import GUI_1 as ui_1
import layout as lay

class Second(QWidget, ui_1.Ui_SecondWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.price_input_count = 0
		self.phone_input_count = 0
	def add_rental_data(self):
    	# 拿來讀入csv的list
	    data_list = []

	    #讀取地區
	    location=str(self.comboBox.currentText())
	    data_list.append(location)

	    #讀取價格
	    price=str(self.lineEdit.text())
	    #檢查價格是否為正整數
	    if not price.isdecimal():
	        self.label_9.setText('價格請輸入正整數噢!')
	        self.price_input_count += 1
	    else:
	    	self.label_9.setText('')
	    	data_list.append(price)

	    #讀取房型
	    room_type=str(self.comboBox_2.currentText())
	    data_list.append(room_type)
	    
	    #讀取是否含水電
	    water_elec=str(self.comboBox_3.currentText())
	    data_list.append(water_elec)

	    #讀取房東稱呼
	    landlord=str(self.lineEdit_2.text())
	    data_list.append(landlord)

	    #讀取房東手機
	    phone=str(self.lineEdit_3.text())
	    #檢查手機是否是正整數且是十位數
	    if not phone.isdecimal():
	        self.label_11.setText('手機請輸入正整數噢!')
	        self.phone_input_count += 1
	    else:
	    	if not len(phone) == 10:
	    		self.label_11.setText('手機請輸入十位數噢!')
	    		self.phone_input_count += 1
	    	else:
	    		self.label_11.setText('')
	    		data_list.append(phone)

	    #讀取地址
	    address=str(self.lineEdit_4.text())
	    #檢查地址是否符合格式
	    if ("市" not in address) or ("區" not in address) or ("路" not in address and "街" not in address) or ("號" not in address):
	        self.label_12.setText('請輸入台北或新北市噢!')
	    else:
	    	if "區" not in address:
	    		self.label_12.setText('請輸入所屬區噢!')
	    	else:
	    		if "路" not in address and "街" not in address:
	    			self.label_12.setText('請輸入所屬路或街噢!')
	    		else:
	    			if "號" not in address:
	    				self.label_12.setText('請輸入所屬的號噢!')
	    			else:
	    				self.label_12.setText('')
	    				data_list.append(address)
	    
	    #資料皆正確則寫入csv檔案
	    if len(data_list)==7:
		    with open("houses_price.csv", "a", encoding='utf-8', newline = "") as file:
		        writer = csv.writer(file)
		        writer.writerow(data_list)
		        self.label_12.setText("新增成功！")
	    else:
	    	#資料有誤
	    	self.label_12.setText('資料格式有誤')
class Main(QWidget, ui.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.price_input_count = 0
		
	def query(self):
		#開啟一個檔案，把檔案中的資料都讀進來
		file1=open('houses_price.csv', 'r', encoding='utf-8')
		list_lines=file1.readlines() #把檔案內所有的內容讀進一個串列中
		file1.close()

		# 拿來讀入csv的list
		self.houses_data=[]

		#檔案中讀取出的每一行資料成為一個有七個元素的串列並加入到houses_data這個串列中
		for line in list_lines:
		    self.houses_data.append(line.strip().split(','))

		#去掉第一行的欄目名稱
		self.houses_data=self.houses_data[1:]

		#data長度
		self.len_data=len(self.houses_data)

		#讀取地區、房型、水電輸入的資料
		location=str(self.comboBox.currentText())
		room_type=str(self.comboBox_2.currentText())
		water_elec=str(self.comboBox_3.currentText())

		#讀取價格
		price=str(self.lineEdit.text())
		#檢查價格是否是正整數
		if not price.isdecimal():
			self.label_5.setText('價格請輸入正整數噢!')
			self.price_input_count += 1
		else:
			#初始化搜尋結果
			result=[]
			#搜尋每行資料是否符合條件
			for i in range(self.len_data):
				if location in self.houses_data[i] or location=='皆可':
					if price=='不限' or int(price)>=int(self.houses_data[i][1]):
						if room_type=='皆可' or room_type == self.houses_data[i][2]:
							if water_elec=='皆可' or water_elec in self.houses_data[i]:
								#若皆符合條件，就放入搜尋結果中
								result.append(self.houses_data[i])

			#長度為0，即無符合的資料
			if len(result)==0:
				self.textBrowser.setPlainText('系統查無資料')
			#印出搜尋結果
			else:
				longstr=[]
				for line in result:
					longstr.append(', '.join(line))
				self.textBrowser.setPlainText('\n'.join(longstr))

class Layout(QMainWindow, lay.Ui_NCCU_Rent):
	def __init__(self):
		#初始化視窗格式
		super().__init__() 
		self.setupUi(self)
		#設定視窗名稱
		self.setWindowTitle("NCCU_Rent_pro_premium")

		#建立左側工具列
		toolBar = QToolBar(self)
		toolBar.setIconSize(QSize(200, 200))
		self.addToolBar(Qt.LeftToolBarArea, toolBar)
		#將點擊按鈕動作設定為切換分頁
		self.toolButton_1.clicked.connect(lambda: self.SwitchWindow(0))
		self.toolButton_2.clicked.connect(lambda: self.SwitchWindow(1))
		#將按鈕加進工具列
		toolBar.addWidget(self.toolButton_1)
		toolBar.addWidget(self.toolButton_2)

		#建立分頁
		self.MainWidget = Main()
		self.SecondWidget=Second()
		
		#建立視窗排版，將分頁加進去
		lay_widget=QWidget(self)
		self.stack = QStackedLayout(lay_widget)
		self.stack.addWidget(self.MainWidget)
		self.stack.addWidget(self.SecondWidget)
		#設定視窗排版
		lay_widget.setLayout(self.stack)
		self.setCentralWidget(lay_widget)

		#將租房分頁的按鈕設定為查詢
		self.MainWidget.pushButton.clicked.connect(self.MainWidget.query)
		#將出租分頁的按鈕設定為新增
		self.SecondWidget.pushButton.clicked.connect(self.SecondWidget.add_rental_data)
		
	#定義切換分頁的函式
	def SwitchWindow(self, index):
		self.stack.setCurrentIndex(index)
	
#主程式
if __name__ == '__main__':
    import sys
    #建立應用程式
    app = QtWidgets.QApplication(sys.argv)
    #建立視窗
    window = Layout()
    #開啟視窗
    window.show()
    #結束程式後釋放資源
    sys.exit(app.exec_())