import getpass
print("########################")
print("##                    ##")
print("##                    ##")
print("##    ADMİN PANELİ    ##")
print("##                    ##")
print("##                    ##")
print("########################")

sifre=""
ad=""
#admin kullanici adi ve sifre kurma
def sifre_guncelle():
    while True:
        ad=input("kullanici adi girin ")
        sifre=input("sifre girin: ")
        dogrulama=input("sifre tekrar: ")
        if sifre==dogrulama:
            print("kullanici adi sifre kuruldu")
            print("panele erismek icin kullanici adi ve sifreyi kullanabilirsiniz")
            break;
        else:
            print("sifreler eslesmiyor tekrar dene")
#bitti
print(sifre)




#panele giris
def giris():
    basarisizlik_sayisi=0
    while True:
        girdi1=input("kullanici adi girin: ")
        girdi2=getpass.getpass("sifre adi girin: ")
        if girdi1==ad and girdi2==sifre:
            break;
        if basarisizlik_sayisi==3:
            print("cok fazla basarisiz deneme")
            exit();
        basarisizlik_sayisi+=1
#bitti


#panel secenekleri
def panel():
    while True:
        print("urun guncellemek icin 1 sepete urun eklemek icin 2 sifre guncellemek icin 3 cikis icin 4 girin")
        secim=input("seciminizi yapin")
        if secim==1:
            urun_guncelle();
        if secim==2:
            sepete_urun_ekle()
        if secim==3:
            sifre_guncelle()
        if secim==4:
            exit()
# secim uc olarak sifre guncellemeyi ekle
        print("hatali secim") 
#bitti

class Urun:
    def __init__(self,ad,aciklama,fiyat):
        self.ad=ad
        self.aciklama=aciklama
        self.fiyat=fiyat

def urun_guncelle():
    while True:
        islem=input("panel icin 1 cikis icin 2 urun eklemek icin 3 girin")
        if islem==1: 
            panel() 
        if islem==2:
            exit()
        if islem ==3:
            ad=input("urun ismini girin")
            aciklama=input("urun aciklamasi girin")
            fiyat=input("urun fiyati girin")
            ad=Urun(ad,aciklama,fiyat)
            with open("urun.txt","a") as f:
                f.write(ad+" "+aciklama+" "+fiyat)
        else:
            print("hatali islem")

fiyat=0
urun=""
def  sepete_urun_ekle():
    while True:
        islem=input("satin almak icin 1 urun eklemek icin 2 panel icin 3 girin")
        if islem==1:
            print(fiyat+"a"+urun+"urunu aldiniz")
        if islem==2:
            girdi=input("urun girin")
            text=with open("urun.txt","r").split("\n")
            urun,fiyat+=map(sec,[girdi,text])
        if islem==3:
            panel()
        else:
            print("hatali islem")




def sec(str,text):
    for i in text:
        if str==i.split(" ")[0]
            return  [" "+str,int(i.split(" ")[2])]
