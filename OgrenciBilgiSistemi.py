import sqlite3

def ogrenciBilgi(ogrenciAdi):
    bilgi = kalem.execute("SELECT * FROM ogrenciler WHERE ogrenci_ad = ? ",(ogrenciAdi,))
    for i in bilgi.fetchall():
        print("Öğrenci numarası:",i[0],"Öğrenci ismi:",i[1])

def yeniOgrenci(ogrenciAdi):
    kalem.execute("INSERT INTO ogrenciler (ogrenci_ad) VALUES (?)",(ogrenciAdi,))
    print(ogrenciAdi, "isimli öğrenci başarıyla kaydedilmiştir.")

def notEkle(ogrenciNo,ders,dersNotu):
    if(ders=="M"):
        kalem.execute("INSERT INTO dersNotlari (ogrenci_no,matematik) VALUES (?,?)",(ogrenciNo,dersNotu))
    if(ders=="F"):
        kalem.execute("INSERT INTO dersNotlari (ogrenci_no,fizik) VALUES (?,?)",(ogrenciNo,dersNotu))
    if(ders=="K"):
        kalem.execute("INSERT INTO dersNotlari (ogrenci_no,kimya) VALUES (?,?)",(ogrenciNo,dersNotu))
    if(ders=="B"):
        kalem.execute("INSERT INTO dersNotlari (ogrenci_no,biyoloji) VALUES (?,?)",(ogrenciNo,dersNotu))
    print("Ders notu başarıyla girilmiştir!")

def devamsizlikEkle(ogrenciNo,tarih):
    kalem.execute("INSERT INTO devamsizlik VALUES (?,?)",(ogrenciNo,tarih))

print("Hoşgeldiniz!")
while True:

    baglanti = sqlite3.connect("ogrenciBilgi.db")
    kalem = baglanti.cursor()

    print("Öğrenci Bilgilerini görmek için -> 1\n Yeni öğrenci eklemek için -> 2\n Ders notu eklemek için -> 3\nDevamsızlık eklmek için -> 4")
    secim = input("Numara giriniz: ")

    if(secim == "1"):
        isim = input("Öğrencinin adını giriniz: ")
        ogrenciBilgi(isim)

    elif(secim == "2"):
        isim = input("Eklemek istediğiniz öğrencinin adını giriniz: ")
        yeniOgrenci(isim)

    elif(secim == "3"):
        numara = input("Ders notu eklemek istediğiniz öğrencinin numarasını giriniz: ")
        print("Matematik için -> M\nFizik için -> F\nKimya için -> K\nBiyoloji için ->B")
        secim = input("Seçiminizi giriniz: ")
        dersNotu = input("Bu ders için notunuzu giriniz: ")
        notEkle(numara,secim,dersNotu)

    elif(secim == "4"):
        numara = input("Devamsızlığını girmek istediğiniz öprencinin numarasını giriniz: ")
        tarih = input("Devamsızlık yaptığı tarihi giriniz: ")
        devamsizlikEkle(numara,tarih,)
        print("Devamsızlık başarıyla kaydedildi!")

    baglanti.commit()
    baglanti.close()