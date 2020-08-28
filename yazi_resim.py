import sys   #Sistemsel işleri yapan sys dahil edilir
from PyQt5 import QtWidgets,QtGui

uygulama = QtWidgets.QApplication(sys.argv) #uygulama nesnesi uygulamanın bizzat kendisidir.
#sys.arg = komut satırından çalıştırılırken argüman gönderilebilsin diye
pencere = QtWidgets.QWidget()   #yazı buton gibi araç gereçlerin tamamına widget denir.
pencere.setWindowTitle("Yazı ve Resim Ekleme")  #Pencereye isim verdik.

font = QtGui.QFont("Times",16)  #yazı tipi ve boyu belirlendi
font2 = QtGui.QFont("Century Gothic",14)    #yazı tipi ve boyu belirlendi

icerik1 = QtWidgets.QLabel(pencere)
icerik1.setText("Kader - Python 3.5 ile sıfırdan ileri seviyeye programlama - Udemy")
        #setText ile pencerede gösterilecek yazı belirtildi.
icerik1.move(40,50)     #yazının pencerede nerede duracağı konumlandırıldı
icerik1.setFont(font)

icerik2 = QtWidgets.QLabel(pencere)
icerik2.setPixmap(QtGui.QPixmap("resim.jpg"))
icerik2.move(50,100)

icerik3 = QtWidgets.QLabel(pencere)
icerik3.setText("Python ile Programlama")
icerik3.move(40,325)
icerik3.setFont(font)

dugme1 = QtWidgets.QPushButton(pencere) #Tıklama Butonunu pencere koyacağımızı bildirdik
dugme1.setText("Programa Giriş")    #Butona isim verdik
dugme1.move(40,400)     #butonu konumlandırdık
dugme1.setFont(font2)   #butondaki yazının fontunu belirledik

dugme2 = QtWidgets.QPushButton(pencere)
dugme2.setText("Çıkış")
dugme2.move(200,400)
dugme2.setFont(font2)

pencere.setGeometry(100,100,600,600)  #ilk iki parametre encerenin nereden baslayacağı; diğer ikisi pencerenin boyutu
pencere.show()  #pencereyi ekranda göstermek için.

sys.exit(uygulama.exec_())  #uygulama çalıştığı sürece programı kapatma demek.

