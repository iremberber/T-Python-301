print("a", "b", sep = "_")

#fonksiyon nasıl yazılır?

def kare_al(x):
    print(x**2)
    
kare_al(3)

#Bilgi notuyla çıktı üretmek

def kare_al(x):
    print("girilen sayı:"+ str(x)+ " karesi:" + str(x**2))
    
kare_al(3)

#İki Argümanlı Fonksiyon Tanımlama

def carpma_yap(x,y):
    print(x*y)
    
carpma_yap(5,3)

#Ön Tanımlı Argümanlar

def carpma_yap(x,y =5):
    print(x*y)
    
carpma_yap(5)

#argümanların sıralamasını bilmiyorsak

def carpma_yap(x,y):
    print(x*y)
    
carpma_yap(y=5, x=3)

#ne zaman fonksiyon yazılır?

def sokak_lambasi (isi,nem,sarj):
    print((isi+nem)/sarj)

sokak_lambasi(25, 34, 60)

#Fonksiyon Çıktısını Girdi Olarak Kullanmak (Return)

def sokak_lambasi (isi,nem,sarj):
    return ((isi+nem)/sarj)

cikti= sokak_lambasi(25, 34, 60)

cikti

#Local etki alanından Global etki alanını değiştirmek

x=[]

def eleman_ekle(y):
    x.append(y)
    print(str(y) + " ifadesi eklendi")
    
    eleman_ekle("ali")

x 
