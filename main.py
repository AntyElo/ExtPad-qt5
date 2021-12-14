from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

class App():
	def __init__(self):
		Form, Window = uic.loadUiType("main.ui")
		self.app = QApplication([])
		self.window = Window()
		self.form = Form()
		self.form.setupUi(self.window)
		
		#self.form.wbutton.clicked.connect(self.add_listItem)
		self.init()

	#def add_listItem(self): 
		#self.form.mtree.addItem(self.form.written.text())

	def init(self):
		self.window.show()
		self.app.exec_()

if __name__ == "__main__":
	newApp = App()
