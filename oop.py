#Nesne yönelimli programlama-OOP

#her şey bir nesnedir
#her nesne bir veya birden fazla sınıfa mensuptur, hem baba hem çalışan
#nesnelerin özellikleri ve fonksiyonları vardır, göz rengin özellik yürümen fonksiyon
#sınıflar biribirini kapsayabilir;bazı özellikleri miras alabilir

class Personel():
    mesai = "9 - 18"
    sirket = "python'la güzel günler"
    def __init__(self,isim,maas,yetenekler):
        print("Yeni bir personel oluşturuldu, ismi: ", isim)
        self.isim = isim
        self.maas = 1600
        self.yetenekler = yetenekler
        self.gunsayisi = 0

    def calis(self):
        print(self.isim,"şu an çalışıyor,çalıştığı gün sayısı: ",self.gunsayisi)
        self.gunsayisi += 1

    def terfi(self):
        print("Tebrikler!", self.isim, "terfi aldı. Yeni maaşı: ",self.maas+200)
        self.maas += 200

    def BilgileriGöster(self):
        print("*"*15)
        print("Personelin ismi: ",self.isim)
        print("Personelin yetenekleri: ", self.yetenekler)
        print("Personelin maaşı: ", self.maas)
        print("Personelin çalıştığı toplam gün: ", self.gunsayisi)
        print("*" * 15)

class Yönetici(Personel)
    def terfi(self):
        print("Tebrikler!", self.isim, "terfi aldı. Yeni maaşı: ",self.maas + 500)
        self.maas += 500
mustafa = Yönetici("Mustafa",2000,["yönetici"])
mustafa.calis()
mustafa.terfi()
mustafa.BilgileriGöster()