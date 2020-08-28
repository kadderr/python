# 1 -> toplama 2 -> çıkarma 3 -> çarpma 4 -> faktöriyel

import random
import time
import math

skor = 0 #her doğru cevap için +1, her yanlış cevap için -3 puan

while  True:

    a = random.randint(1,4)
    print("Lütfen bekleyin yeni soru hazırlanıyor...")
    time.sleep(2)

    if a == 1:
        print("Toplama işlemi -> ")
        ilksayi = random.randint(1,20)
        ikincisayi = random.randint(1,20)
        print("lütfen",ilksayi,"ile",ikincisayi,"sayılarının toplamını yazınız. ")
        sonuc = int(input("Cevap: "))

        if (sonuc == ilksayi+ikincisayi):
            print("Tebrikler doğru bildiniz!")
            skor = skor + 1
            print("Mevcut skor: ",skor)
            time.sleep(2)

        else:
            print("Yanlış! Doğru cevap: ", ilksayi+ ikincisayi )
            skor = skor - 3
            print("Mevcut skor: ", skor)
            time.sleep(2)
    elif a==2:
        print("Çıkarma işlemi -> ")
        ilksayi = random.randint(1,20)
        ikincisayi = random.randint(1,20)
        if(ilksayi>=ikincisayi):
            print("lütfen",ilksayi,"ile",ikincisayi,"sayılarının farkını yazınız. ")
            sonuc = int(input("Cevap: "))

            if (sonuc == ilksayi - ikincisayi):
                print("Tebrikler doğru bildiniz!")
                skor = skor + 1
                print("Mevcut skor: ", skor)
                time.sleep(2)

            else:
                print("Yanlış! Doğru cevap: ", ilksayi - ikincisayi)
                skor = skor - 3
                print("Mevcut skor: ", skor)
                time.sleep(2)
        else:
            print("lütfen", ikincisayi, "ile", ilksayi, "sayılarının farkını yazınız. ")
            sonuc = int(input("Cevap: "))

            if (sonuc == ikincisayi - ilksayi):
                print("Tebrikler doğru bildiniz!")
                skor = skor + 1
                print("Mevcut skor: ", skor)
                time.sleep(2)

            else:
                print("Yanlış! Doğru cevap: ", ikincisayi - ilksayi)
                skor = skor - 3
                print("Mevcut skor: ", skor)
                time.sleep(2)

    elif a == 3:
        print("Çarpma işlemi -> ")
        ilksayi = random.randint(1,20)
        ikincisayi = random.randint(1,20)
        print("lütfen",ilksayi,"ile",ikincisayi,"sayılarının çarpımını yazınız. ")
        sonuc = int(input("Cevap: "))

        if (sonuc == ilksayi*ikincisayi):
            print("Tebrikler doğru bildiniz!")
            skor = skor + 1
            print("Mevcut skor: ", skor)
            time.sleep(2)

        else:
            print("Yanlış! Doğru cevap: ", ilksayi * ikincisayi )
            skor = skor - 3
            print("Mevcut skor: ", skor)
            time.sleep(2)

    else:
        print("Faktöriyel işlemi ->")
        sayi = random.randint(1, 5)
        print("lütfen", sayi, "sayısının faktöriyelini hesaplayınız ")
        sonuc = int(input("Cevap: "))

        if (sonuc == math.factorial(sayi)):
            print("Tebrikler doğru bildiniz!")
            skor = skor + 1
            print("Mevcut skor: ", skor)
            time.sleep(2)

        else:
            print("Yanlış! Doğru cevap: ", math.factorial(sayi))
            skor = skor - 3
            print("Mevcut skor: ", skor)
            time.sleep(2)
