#For Döngüsü

ogrenci = ["ali", "veli", "irem", "berk"]

for i in ogrenci:
    print(i)
    
    #for = dön i=eleman indexi temsili 

#For Döngüsü Örnek

maaslar = [8000,7000,1000,2000,3000,4000,5000,1000]

for i in maaslar:
    print("maaşınız "+ str(i))
    
    
#Döngü ve Fonksiyonların Birlikte Kullanımı

def zam(x):
    print(x*0.20+x)

for i in maaslar:
    zam(i)
    
#Uygulama: if, for ve Fonksiyonların Birlikte Kullanımı

def maas_ust(x):
    print(x*0.10 + x)
    
def maas_alt(x):
    print(x*0.20 + x)
    
for i in maaslar:
    if i < 3000:
        maas_alt(i)
    else: 
        maas_ust(i)
        
#Break ve Continue

dir(maaslar)
maaslar.sort()
maaslar 
maaslar = [8000,7000,1000,2000,3000,4000,5000,1000]
for i in maaslar:
    if i == 3000: #continue bu değeri atlar, break de bu değere gelince durur, dahil etmez.
        continue
    print(i)
    
#While 

#Bu şart sağlandığı sürece demek

sayi = 1
while sayi < 10: #Sayı 10'dan küçükse devam et
    sayi +=1
    print(sayi)
    
    
    



