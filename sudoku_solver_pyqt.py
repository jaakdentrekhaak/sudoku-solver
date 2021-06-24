from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QProgressBar, QLineEdit, QFileDialog
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

import sudoku_solver

class Window(QWidget):
	def __init__(self):
		super().__init__()

		self.title = "Sudoku solver by jaakdentrekhaak"

		self.screen_dim = (1600, 900)

		self.width = 500
		self.height = 400

		self.left = int(self.screen_dim[0] / 2 - self.width / 2)
		self.top = int(self.screen_dim[1] / 2 - self.height / 2)

		self.init_window()

	def init_window(self):
		self.setWindowIcon(QtGui.QIcon('sudoku_logo.png'))
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.setStyleSheet('background-color: rgb(52, 50, 51);')

		self.create_layout()

		self.show()

	def submit(self):
		# Construct matrix to work with
		counter = 0
		index = 0
		matrix = [[], [], [], [], [], [], [], [], []]
		for num in self.widget_list:
			if counter > 8:
				index += 1
				counter = 0
			
			if num.text() == '':
				matrix[index].append(None)
			else:
				matrix[index].append(int(num.text()))

			counter += 1

		# Solve the sudoku matrix
		solution = sudoku_solver.solve(matrix)

		# Fill the roster with the solutions (in another color)
		cur_pos = 0
		for row in range(9):
			for col in range(9):
				if self.widget_list[cur_pos].text() == '':
					self.widget_list[cur_pos].setText(str(solution[row][col]))
					self.widget_list[cur_pos].setStyleSheet("color: green; background-color: rgb(255, 255, 255); font-size: 20px;")
				else:
					self.widget_list[cur_pos].setText(str(solution[row][col]))
				cur_pos += 1

	def clear(self):
		# Clear the roster
		for w in self.widget_list:
			w.setText('')


	def create_layout(self):

		# buttons
		button_dim = (80, 40)
		window_dim = (self.width, self.height)

		self.button_submit = QPushButton('Submit', self)
		self.button_submit.setGeometry(100, 350,
									  button_dim[0], button_dim[1])
		self.button_submit.setStyleSheet("color: rgb(52, 50, 51); background-color: rgb(255, 209, 82);"
										"border-width: 1.5px; border-radius: 5px; border-color: rgb(255, 209, 82);"
										"font-size: 20px; font-family: Verdana;")
		self.button_submit.clicked.connect(self.submit)
		self.button_submit.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

		self.button_submit = QPushButton('Clear', self)
		self.button_submit.setGeometry(285, 350,
									  button_dim[0], button_dim[1])
		self.button_submit.setStyleSheet("color: rgb(52, 50, 51); background-color: rgb(255, 209, 82);"
										"border-width: 1.5px; border-radius: 5px; border-color: rgb(255, 209, 82);"
										"font-size: 20px; font-family: Verdana;")
		self.button_submit.clicked.connect(self.clear)
		self.button_submit.setCursor(QCursor(QtCore.Qt.PointingHandCursor))


		# line edits
		x_first_input = 100
		y_first_input = 50

		self.widget_list = []

		# Create roster inputs
		for i in range(9):
			for j in range(9):
				le = QLineEdit(self)
				le.setGeometry(x_first_input + i*30, y_first_input + j*30, 25, 25)
				le.setStyleSheet("color: black; background-color: rgb(255, 255, 255); font-size: 20px;")
				le.setMaxLength(1)
				self.widget_list.append(le)

		# labels
		self.label1 = QLabel(self)
		self.label1.setText('Fill in the given numbers and leave the rest unfilled.')
		self.label1.setGeometry(int(window_dim[0] / 2 - (self.width - 50) / 2), 0,
								self.width - 50, 30)
		self.label1.setStyleSheet('color: beige; font-size: 16px; font-family: Verdana')



if __name__ == '__main__':
	App = QApplication(sys.argv)
	window = Window()
	sys.exit(App.exec())
