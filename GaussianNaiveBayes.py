import pandas 
import xlrd 
import numpy
from sklearn.model_selection import train_test_split
import statistics #ortalama almak icin...
import math #pi ve euler sayisi icin...

def hesaplama(x): #Burada siniflardan olma olasiliklari hesaplaniyor.
    global sekerOrtalama, sekerStandartSapma, barbunyaOrtalama, barbunyaStandartSapma, caliOrtalama, caliStandartSapma, dermasonOrtalama, dermasonStandartSapma
    global siraOrtalama, siraStandartSapma, bombayOrtalama, bombayStandartSapma, horozOrtalama, horozStandartSapma
    global sekerOlasiligi, barbunyaOlasiligi, caliOlasiligi, dermasonOlasiligi, siraOlasiligi,bombayOlasiligi, horozOlasiligi
    toplamCarpim1=1
    toplamCarpim2=1
    toplamCarpim3=1
    toplamCarpim4=1
    toplamCarpim5=1
    toplamCarpim6=1
    toplamCarpim7=1
    for i in range(16):
        carpim1=(1/(sekerStandartSapma[i]*((2*math.pi)**0.5)))*(math.e**(((-1)/2)*(((x[i]-sekerOrtalama[i])/sekerStandartSapma[i])**2))) #Formul...
        toplamCarpim1*=carpim1
        carpim2=(1/(barbunyaStandartSapma[i]*((2*math.pi)**0.5)))*(math.e**(((-1)/2)*(((x[i]-barbunyaOrtalama[i])/barbunyaStandartSapma[i])**2)))
        toplamCarpim2*=carpim2
        carpim3=(1/(caliStandartSapma[i]*((2*math.pi)**0.5)))*(math.e**(((-1)/2)*(((x[i]-caliOrtalama[i])/caliStandartSapma[i])**2)))
        toplamCarpim3*=carpim3
        carpim4=(1/(dermasonStandartSapma[i]*((2*math.pi)**0.5)))*(math.e**(((-1)/2)*(((x[i]-dermasonOrtalama[i])/dermasonStandartSapma[i])**2)))
        toplamCarpim4*=carpim4
        carpim5=(1/(siraStandartSapma[i]*((2*math.pi)**0.5)))*(math.e**(((-1)/2)*(((x[i]-siraOrtalama[i])/siraStandartSapma[i])**2)))
        toplamCarpim5*=carpim5
        carpim6=(1/(bombayStandartSapma[i]*((2*math.pi)**0.5)))*(math.e**(((-1)/2)*(((x[i]-bombayOrtalama[i])/bombayStandartSapma[i])**2)))
        toplamCarpim6*=carpim6
        carpim7=(1/(horozStandartSapma[i]*((2*math.pi)**0.5)))*(math.e**(((-1)/2)*(((x[i]-horozOrtalama[i])/horozStandartSapma[i])**2)))
        toplamCarpim7*=carpim7
    return ((toplamCarpim1*sekerOlasiligi),(toplamCarpim2*barbunyaOlasiligi),(toplamCarpim3*caliOlasiligi),(toplamCarpim4*dermasonOlasiligi),(toplamCarpim5*siraOlasiligi),(toplamCarpim6*bombayOlasiligi),(toplamCarpim7*horozOlasiligi))
    #Siniflardan olma olasiliklari donduruluyor.

excelVerileri=pandas.read_excel('Dry_Bean_Dataset.xlsx') #Excel dosyasi okunuyor.

y=excelVerileri["Class"] #y olusturuluyor.
x=excelVerileri.drop(columns="Class") #Class sutunu siliniyor ve x olusturuluyor.

(xEgitimVerisi, xTestVerisi, yEgitimVerisi, yTestVerisi)=train_test_split(x, y, random_state=42, test_size=0.3) #Test ve egitim verileri ayriliyor.

yEgitimVerisiListesi=yEgitimVerisi.tolist() #Test ve egitim verileri liste formuna donusturuluyor.
yTestVerisiListesi=yTestVerisi.tolist()
xEgitimVerisiListesi=xEgitimVerisi.values.tolist()
xTestVerisiListesi=xTestVerisi.values.tolist()

sekerIndeksler=[] #siniflarin hangi indesklerde olduklarini tutacaklar.
barbunyaIndeksler=[]
caliIndeksler=[]
dermasonIndeksler=[]
siraIndeksler=[]
bombayIndeksler=[]
horozIndeksler=[]

for indeks, deger in enumerate(yEgitimVerisiListesi): #Egitim verilerinin siniflarinin indeksleri bulunuyor.
    if deger=='SEKER':
        sekerIndeksler.append(indeks)
    elif deger=='BARBUNYA':
        barbunyaIndeksler.append(indeks)
    elif deger=='CALI':
        caliIndeksler.append(indeks)
    elif deger=='DERMASON':
        dermasonIndeksler.append(indeks)
    elif deger=='SIRA':
        siraIndeksler.append(indeks)
    elif deger=='BOMBAY':
        bombayIndeksler.append(indeks)
    elif deger=='HOROZ':
        horozIndeksler.append(indeks)

sekerStandartSapma=[] #Olasilik hesaplamada gerekli degiskenler...
barbunyaStandartSapma=[]
caliStandartSapma=[]
dermasonStandartSapma=[]
siraStandartSapma=[]
bombayStandartSapma=[]
horozStandartSapma=[]

sekerOrtalama=[]
barbunyaOrtalama=[]
caliOrtalama=[]
dermasonOrtalama=[]
siraOrtalama=[]
bombayOrtalama=[]
horozOrtalama=[]

for j in range(16):
    sekerStandartSapma.append(numpy.nanvar([xEgitimVerisiListesi[i][j] for i in sekerIndeksler])**0.5) #Degiskenler hesaplaniyor.
    barbunyaStandartSapma.append(numpy.nanvar([xEgitimVerisiListesi[i][j] for i in barbunyaIndeksler])**0.5)
    caliStandartSapma.append(numpy.nanvar([xEgitimVerisiListesi[i][j] for i in caliIndeksler])**0.5)
    dermasonStandartSapma.append(numpy.nanvar([xEgitimVerisiListesi[i][j] for i in dermasonIndeksler])**0.5)
    siraStandartSapma.append(numpy.nanvar([xEgitimVerisiListesi[i][j] for i in siraIndeksler])**0.5)
    bombayStandartSapma.append(numpy.nanvar([xEgitimVerisiListesi[i][j] for i in bombayIndeksler])**0.5)
    horozStandartSapma.append(numpy.nanvar([xEgitimVerisiListesi[i][j] for i in horozIndeksler])**0.5)

    sekerOrtalama.append(statistics.mean([xEgitimVerisiListesi[i][j] for i in sekerIndeksler]))
    barbunyaOrtalama.append(statistics.mean([xEgitimVerisiListesi[i][j] for i in barbunyaIndeksler]))
    caliOrtalama.append(statistics.mean([xEgitimVerisiListesi[i][j] for i in caliIndeksler]))
    dermasonOrtalama.append(statistics.mean([xEgitimVerisiListesi[i][j] for i in dermasonIndeksler]))
    siraOrtalama.append(statistics.mean([xEgitimVerisiListesi[i][j] for i in siraIndeksler]))
    bombayOrtalama.append(statistics.mean([xEgitimVerisiListesi[i][j] for i in bombayIndeksler]))
    horozOrtalama.append(statistics.mean([xEgitimVerisiListesi[i][j] for i in horozIndeksler]))

sekerOlasiligi=(len(sekerIndeksler)/len(xEgitimVerisi)) #Siniflarin, toplam siniflara orani bulunuyor.
barbunyaOlasiligi=(len(barbunyaIndeksler)/len(xEgitimVerisi))
caliOlasiligi=(len(caliIndeksler)/len(xEgitimVerisi))
dermasonOlasiligi=(len(dermasonIndeksler)/len(xEgitimVerisi))
siraOlasiligi=(len(siraIndeksler)/len(xEgitimVerisi))
bombayOlasiligi=(len(bombayIndeksler)/len(xEgitimVerisi))
horozOlasiligi=(len(horozIndeksler)/len(xEgitimVerisi))

dogru=0 #dogru tahmin sayisi
yanlis=0 #yanlis tahmin sayisi
dict={0: 'SEKER', 1: 'BARBUNYA', 2: 'CALI', 3: 'DERMASON', 4: 'SIRA', 5: 'BOMBAY', 6: 'HOROZ'}
for i in range(len(xTestVerisiListesi)):
    carpimlar=hesaplama(xTestVerisiListesi[i]) #Test verisinin, siniflara gore olasilik verisi donuyor.
    indeksler=numpy.argsort(carpimlar) #Kucukten buyuge siralandiginda hangi indekse hangi indeskteki sayilarin donecegi bulunuyor. (Bize sonuncu indeksteki sayi gerekiyor.)
    tahminEdilenSinif=dict[indeksler[6]] #En yuksek olasiliga sahip sinif bulunuyor.
    if yTestVerisiListesi[i]==tahminEdilenSinif:
        print("Sinif dogru tahmin edildi!")
        dogru+=1
    else:
        print("Sinif yanlis tahmin edildi!")
        yanlis+=1
    print("Dogru: ", dogru, "Yanlis: ", yanlis)
print("Dogruluk Orani: %", dogru*100/(dogru+yanlis))