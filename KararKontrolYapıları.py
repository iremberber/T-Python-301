#true-false sorgulaması

sinir= 50000

sinir== 4000 #== denk mi demek


#if yapısı

gelir = 40000

if sinir > gelir:
    print("gelir yeterli değil")
    print("Yeterli olması için " + str(sinir-gelir) + " kadar daha gelir olmalı")

    
#else yapısı

if sinir < gelir:
    print("gelir yeterli")
else:
    print("gelir yeterli değil")
    
#elif yapısı

if gelir == sinir:
    print("gelir sınıra eşit.")
elif gelir > sinir:
    print("gelir sınırdan büyüktür.")
else:
    print("takibe devam")

#uygulama: if ve input ile Kullanıcı Etkileşimli Program
sinirr = 60000
magaza_adi=input("mağaza adı nedir?")
gelirr = input("Aylık geliri nedir?")


if int(gelirr) < int(sinirr):
    print("Gelir yetersiz")
elif int(gelirr) > int(sinirr):
    print("Tebrikler! Ayın mağazası seçildiniz!")
else:
    print("Sınırdasınız.")