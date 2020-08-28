import sys
from PyQt5 import QtWidgets,QtGui

uygulama = QtWidgets.QApplication(sys.argv)

pencere = QtWidgets.QWidget()
pencere.setWindowTitle("Horizontal ve Vertical Box Layout")

dikey = QtWidgets.QVBoxLayout()
yatay = QtWidgets.QHBoxLayout()

dugme1 = QtWidgets.QPushButton("Programa Giriş")
dugme2 = QtWidgets.QPushButton("Programdan Çıkış")

yatay.addStretch()  #butonlar yatay alanın tamamını kaplamasın diye, esneklik ekler
yatay.addWidget(dugme1)
yatay.addWidget(dugme2)

dikey.addStretch()  
dikey.addLayout(yatay)

pencere.setLayout(dikey)
pencere.setGeometry(100,100,600,600)
pencere.show()

sys.exit(uygulama.exec_())

