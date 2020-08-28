import sqlite3

baglanti = sqlite3.connect("veriler.db")

if(baglanti):
    print("Bağlantı başarılı")
else:
    print("Bağlantı başarısız")

print("*"*15)
kalem = baglanti.cursor()   #kalem bir nesnedir.  Her işlem bu kalemle yapılacak. Bu kaleme sql kodları göndereceğiz ve çalıştıracağız.



baglanti.commit()
baglanti.close()
"""

**************************************************************************************************
kalem.execute(''' 

CREATE TABLE kitaplar(  #kitaplar tablosu oluşturuldu
kitap_no INTEGER PRIMARY KEY,   kitap numarası integer veri tipindedir ve bu birincil anahtardır yani bu tablodaki benzersiz anahtar bu
kitap_adı VARCHAR(50),  #varchar: her türlü karakter olabilir sayı yazı virgül gibi ve 50 karakter uzunluğunda olabilir
kitap_kategori INTEGER(2))  #kategoriler numaralandırılmıs ve 2 karakterli int tipinde 
''')

baglanti.commit()   #kodları sql-e iletmek(commit etmek)için
baglanti.close()    #bağlantıyı kapatmalıyız, güvenlik için

**************************************************************************************************
kalem.execute('''

CREATE TABLE kategoriler(
kategori_no INTEGER PRIMARY KEY,
kategori_adi VARCHAR(50)
)
''')

**************************************************************************************************
kalem.execute('''

CREATE TABLE calisanlar(
calisan_no INTEGER PRIMARY KEY,
calisan_adi VARCHAR(50),
calisan_maas INTEGER(5)
)
''')

**************************************************************************************************
kalem.execute('''

INSERT INTO calisanlar(calisan_adi,calisan_maas) VALUES ("Sevgi Doğan",3000)    #tabloya veri  ekledik!!!

''')

**************************************************************************************************
kitaplar = kalem.execute("SELECT * FROM kitaplar")  #kitaplar nesnesine kitaplar tablosundaki tüm verileri çektik
print (kitaplar.fetchall()) #verileri ekrana bastık. * tüm verileri çeker. kitap_no yazsaydık sadece noları çekerdi

BUNUN YERİNE AŞAĞIDAKİNİ YAPABİLİRİZ:

kitaplar = kalem.execute("SELECT * FROM kitaplar")

for kitaplar in kitaplar.fetchall():
    print("Kitap no: %s || Kitap ismi: %s || Kitap kategorisi: %s "%kitaplar)   #daha düzenli bir görünüm sunar

**************************************************************************************************
calisanlar = kalem.execute("SELECT * FROM calisanlar WHERE calisan_maas = 2000 ")


for calisanlar in calisanlar.fetchall():
    print("Çalışan no: %s || Çalışan ismi: %s || Çalışan maaşı: %s "%calisanlar)
**************************************************************************************************
kalem.execute("UPDATE kitaplar SET kitap_adı = 'Savaş ve Barış' WHERE kitap_adı='Suç ve Ceza'")
# adı Suç ve Ceza olan kitabı savaş ve barış olarak güncelledik

**************************************************************************************************
kitaplar = kalem.execute("SELECT * FROM kitaplar ORDER BY kitap_adı DESC ")
        # ORDER BY ile sıralama yaptık, DESC büyükten küçüğe, ASC küçükten büyüğe sıralar!
for i in kitaplar.fetchall():
    print(i[1])

**************************************************************************************************
kitaplar = kalem.execute("SELECT * FROM kitaplar LIMIT 2")
for i in kitaplar.fetchall():
    print(i[1])

#LIMIT 2 ile kitaplardan sadece 2 tane veri çekmek istediğimi belirttim!!!

**************************************************************************************************
kalem.execute("DELETE FROM calisanlar WHERE calisan_maas=2000")
#calisanlar tablosundan çalışan maaşı 2000 tl olanları siler, kaç tane 2000 varsa hepsini siler!
"""




kalem = baglanti.cursor()

def ogrenciBilgi(ogrenciAdi):
    bilgi = kalem.execute("SELECT * FROM ogrenciler WHERE ogrenci_ad=?",(ogrenciAdi,))
    print(bilgi.fetchall())

print("Hoşgeldiniz.")

print("Öğrenci Bilgilerinigörmek için -> 1\n Yeni öğrenci eklemek için -> 2\n Ders notu eklemek için -> 3\nDevamsızlık eklmek için -> 4")

secim = input("Numara giriniz: ")

if(secim == "1"):
    isim = input("Ögrencinin adını giriniz: ")
    ogrenciBilgi(isim)

baglanti.commit()
baglanti.close()
