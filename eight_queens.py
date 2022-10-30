import PyQt5
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# from PySide6 import QtWidgets
# from QtWidgets import *
import sys
import time


class View(QWidget):
    
    def __init__(self):
        super().__init__()
        self.definitions_layout = QHBoxLayout()
        self.size_label = QLabel("Choose the board size")
        self.size_input = QLineEdit("8")
        self.definitions_layout.addWidget(self.size_label)
        self.definitions_layout.addWidget(self.size_input)
        self.main_layout = QVBoxLayout()
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start)
        self.board = Board(8, False)
        self.main_layout.addLayout(self.definitions_layout)
        self.main_layout.addWidget(self.start_button)
        self.main_layout.addWidget(self.board)
        self.setLayout(self.main_layout)

    def start(self):
        self.main_layout.removeWidget(self.board)
        self.board = Board(int(self.size_input.text()), True)
        self.main_layout.addWidget(self.board)





class Square(QPushButton):

    def __init__(self, x, y, is_enabled):
        super().__init__()
        self.x = x
        self.y = y
        self.setEnabled(is_enabled)
        self.clicked.connect(self.turn)
        self.setBackground()

    def isLigal(self, queen1, queen2):
        x1, x2, y1, y2 = queen1.x, queen2.x, queen1.y, queen2.y
        return (x1 != x2) and (y1 != y2) and (x1 + y1 != x2 + y2) and (x1 - y1 != x2 - y2)

    def turn(self):
        if self.sender() in view.board.queen_list:
            view.board.queen_list.remove(self.sender())
            self.setText("")
        else:
            is_ligal = True
            for queen in view.board.queen_list:
                queen.setBackground()
                if not self.isLigal(queen, self.sender()):
                    queen.setStyleSheet("color:red")
                    is_ligal = False
            if is_ligal:
                view.board.queen_list.append(self.sender())
                # self.setIcon(QtGui.QIcon("queen.jpg"))
                self.setText("W")
                if len(view.board.queen_list) == view.board.size:
                    popup.show()




    def setBackground(self):
        self.setFont(QFont('Ariel', 30))
        if (self.x-self.y)%2:
            self.setStyleSheet('QPushButton {background-color: white; color: black;}')
        else:
            self.setStyleSheet('QPushButton {background-color: black; color: white;}')


class Board(QWidget):

    def __init__(self, size, is_enabled):
        super().__init__()
        self.size = size
        self.square_size = 800//self.size
        self.queen_list = []
        self.is_enabled = is_enabled
        self.buildBoard()


    def buildBoard(self):
        self.setFixedWidth(self.size*self.square_size)
        self.setFixedHeight(self.size*self.square_size)
        board = QVBoxLayout()
        board.setSpacing(0)
        rows = []
        for i in range(self.size):
            rows.append(QHBoxLayout())
            board.addLayout(rows[i])
            for j in range(self.size):
                sq = Square(i, j, self.is_enabled)
                sq.setFixedWidth(self.square_size)
                sq.setFixedHeight(self.square_size)
                rows[i].addWidget(sq)
        self.setLayout(board)


app = QApplication(sys.argv)
popup = QLabel("You win!")
view = View()
view.show()
app.exec()
