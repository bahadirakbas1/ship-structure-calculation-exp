import numpy as np
import pandas as pd
from scipy import integrate, interpolate
import matplotlib.pyplot as plt

length = 145.0 
breadth = length / 8.0 
draught = breadth / 2.5 
Cb = 0.7 
waterDensity = 1.025
Lamda = length
gravity = 9.81
D = draught * (3/2)
h = D / 6
H = Lamda / 20
r = H / 2
s = length / 100

volume = length * breadth * draught * Cb
displacement = volume * waterDensity 
s60txt = np.loadtxt("s60.txt")
def basamak(liste_adi):#basamak fonksiyonu ile gerekli yerlerde virgülden sonra 2 basamaklı olması sağlandı
    liste_adi = [round(num, 2) for num in liste_adi]
    return liste_adi
''' POSTALAR '''
waterLine = ['WL0','WL0.3','WL1','WL2','WL3','WL4','WL5','WL6']
postNumber = [0,0.5,1,2,3,4,5,6,7,8,9,9.5,10]
postNumber100 = np.linspace(0,10,101)
s60_withHalfBreadth = s60txt * (breadth/2)
df = pd.DataFrame(s60_withHalfBreadth,index = postNumber, columns=waterLine)
df2 = df.reindex(postNumber100)
result = df2.interpolate()
#10 posta için verilen ofset tablosunu interpole edip 100 posta için tablo oluşturulmuştur.
''' ALANLAR '''
wL0 = result['WL0'].to_numpy();wL03 = result['WL0.3'].to_numpy();wL1 = result['WL1'].to_numpy()
wL2 = result['WL2'].to_numpy();wL3 = result['WL3'].to_numpy();wL4 = result['WL4'].to_numpy();wL5 = result['WL5'].to_numpy();wL6 = result['WL6'].to_numpy()
listForWL03 = [];listForWL1 = []; listForWL2 = []; listForWL3 = []; listForWL4 = []; listForWL5 = []; listForWL6 = []
wl1_listForFirstRate = [] ; wl1_listForMidRate = [] ; wl1_listForLastRate = []
alanWl1 = []
for i in range(101):
    wl1_listForFirstRate.append(wL0[i] * 1)  
for i in range(101):
    wl1_listForMidRate.append(wL03[i] * 4)   
for i in range(101):
    wl1_listForLastRate.append(wL1[i] * 1)   
for i in range(101):
    listForWL1.append(wl1_listForFirstRate[i] + wl1_listForFirstRate[i] + wl1_listForFirstRate[i])
for i in range(101):
    alanWl1.append(listForWL1[i] * h * (2/3))
wl2_listForFirstRate = [] ; wl2_listForMidRate = [] ; wl2_listForLastRate = []
alanWl2 = []
for i in range(101):
    wl2_listForFirstRate.append(wL0[i] * 1)   
for i in range(101):
    wl2_listForMidRate.append(wL1[i] * 4)   
for i in range(101):
    wl2_listForLastRate.append(wL2[i] * 1)   
for i in range(101):
    listForWL2.append(wl2_listForFirstRate[i] + wl2_listForMidRate[i] + wl2_listForLastRate[i])
for i in range(101):
    alanWl2.append(listForWL2[i] * h * (2/3))
wl3_listFor05 = [];wl3_listFor2 = [];wl3_listFor15 = [];wl3_listFor4 = [];wl3_listFor1 = []
alanWl3 = []
for i in range(101):
    wl3_listFor05.append(wL0[i] * 0.5)  
for i in range(101):
    wl3_listFor2.append(wL03[i] * 2)    
for i in range(101):
    wl3_listFor15.append(wL1[i] * 1.5)       
for i in range(101):
    wl3_listFor4.append(wL2[i] * 4)   
for i in range(101):
    wl3_listFor1.append(wL3[i] * 1)   
for i in range(101):
    listForWL3.append(wl3_listFor05[i] + wl3_listFor2[i] + wl3_listFor15[i] + wl3_listFor4[i] + wl3_listFor1[i])
for i in range(101):
    alanWl3.append(listForWL3[i] * h * (2/3))
wl4_listFor0 = [];wl4_listFor1 = [];wl4_listFor2 = [];wl4_listFor3 = [];wl4_listFor4 = []
alanWl4 = []    
for i in range(101):
    wl4_listFor0.append(wL0[i] * 1)   
for i in range(101):
    wl4_listFor1.append(wL1[i] * 4)
for i in range(101):
    wl4_listFor2.append(wL2[i] * 2)       
for i in range(101):
    wl4_listFor3.append(wL3[i] * 4)   
for i in range(101):
    wl4_listFor4.append(wL4[i] * 1)    
for i in range(101):
    listForWL4.append(wl4_listFor0[i] + wl4_listFor1[i] + wl4_listFor2[i] + wl4_listFor3[i] + wl4_listFor4[i])
for i in range(101):
    alanWl4.append(listForWL4[i] * h * (2/3))
wl5_listFor0 = [];wl5_listFor05 = [];wl5_listFor1 = [];wl5_listFor2 = [];wl5_listFor3 = [];wl5_listFor4 = [];wl5_listFor5 = []
alanWl5 = [] 
for i in range(101):
    wl5_listFor0.append(wL0[i] * 0.5)   
for i in range(101):
    wl5_listFor05.append(wL1[i] * 2) 
for i in range(101):
    wl5_listFor1.append(wL2[i] * 1.5)
for i in range(101):
    wl5_listFor2.append(wL3[i] * 4)
for i in range(101):
    wl5_listFor3.append(wL4[i] * 2)
for i in range(101):
    wl5_listFor4.append(wL5[i] * 4)
for i in range(101):
    wl5_listFor5.append(wL6[i] * 1)
for i in range(101):
    listForWL5.append(wl5_listFor0[i] + wl5_listFor05[i] + wl5_listFor1[i] + wl5_listFor2[i] + wl5_listFor3[i] + wl5_listFor4[i] + wl5_listFor5[i])
for i in range(101):
    alanWl5.append(listForWL5[i] * h * (2/3))
wl6_listFor0 = [];wl6_listFor1 = [];wl6_listFor2 = [];wl6_listFor3 = [];wl6_listFor4 = [];wl6_listFor5 = [];wl6_listFor6 = []
alanWl6 = []
for i in range(101):
    wl6_listFor0.append(wL0[i] * 1)
for i in range(101):
    wl6_listFor1.append(wL1[i] * 4) 
for i in range(101):
    wl6_listFor2.append(wL2[i] * 2)
for i in range(101):
    wl6_listFor3.append(wL3[i] * 4)
for i in range(101):
    wl6_listFor4.append(wL4[i] * 2)
for i in range(101):
    wl6_listFor5.append(wL5[i] * 4)
for i in range(101):
    wl6_listFor6.append(wL6[i] * 1)
for i in range(101):
    listForWL6.append(wl6_listFor0[i] + wl6_listFor1[i] + wl6_listFor2[i] + wl6_listFor3[i] + wl6_listFor4[i] + wl6_listFor5[i] + wl6_listFor6[i])
for i in range(101):
    alanWl6.append(listForWL6[i] * h * (2/3))
frame1 =pd.DataFrame(alanWl1); frame2 = pd.DataFrame(alanWl2);frame3 = pd.DataFrame(alanWl3);frame4 = pd.DataFrame(alanWl4); frame5= pd.DataFrame(alanWl5)
frame6 = pd.DataFrame(alanWl6)
frames = basamak([frame1,frame2,frame3,frame4,frame5,frame6])
waterLineForAreas = ['WL1','WL2','WL3','WL4','WL5','WL6']
areas = pd.concat(frames, axis = 1)
areas.columns = waterLineForAreas
#Burada her su hattı alanını bulmak için 1/3 Simpson kuralını açık şekilde yazarak alanlar bulundu.
'''YÜK DAĞILIMLARI'''
'''
listPostaNoktaToplam = []
for i in range(101):
    listPostaNoktaToplam.append(alanWl1[i] + alanWl2[i] + alanWl3[i] + alanWl4[i] + alanWl5[i] + alanWl6[i])
listWl6_simpson = []
for i in range(101):
    if i == 0:
        listWl6_simpson.append(alanWl6[i] * 1)
    elif i%2 == 0:
        listWl6_simpson.append(alanWl6[i] * 4)
    elif i %2 == 1:
        listWl6_simpson.append(alanWl6[i] * 2) 
    elif i == 100:
        listWl6_simpson.append(alanWl6[i] * 1)
listHacimOran = []
for i in range(101):
    listHacimOran.append((listPostaNoktaToplam[i]* 1.45 * length * breadth * draught * 1.025 * Cb) / sum(listWl6_simpson))  
'''
# burada hacim oran yöntemini denendi ama başarılı olunamadı. simpson kuralını yine fonksiyon olarak değil de açık olarak yazma denendi.
q=displacement/length
ortaDogun=[0.68,1.185,0.58]
trok_deger = 2
newList = []
for i in range(3):
   newList.append(q * ortaDogun[i])
divided34 = np.linspace(0,1,34)
sectionBIndex = np.linspace(1,33,33)
sectionBRates = []
a = 1
while a < 34:
    sectionBRates.append(newList[1])
    a += 1 
sectionA = pd.DataFrame(newList[0:2])
sectionA_reindexed = sectionA.reindex(divided34)
sectionA_interpolated = sectionA_reindexed.interpolate()
sectionB = pd.DataFrame(sectionBRates,index=sectionBIndex)
sectionC = pd.DataFrame(newList[1:])
sectionC_reindexed = sectionC.reindex(divided34)
sectionC_interpolated = sectionC_reindexed.interpolate()
frames = [sectionA_interpolated,sectionB,sectionC_interpolated]
result = pd.concat(frames)
#Sakin su ve Dalga Tepesi problemlerini çözerken Prohaska yöntemini kullanıldı.
#burada yük dağılımını oluşturuldu.
# gemi uzunluğunu üç parçaya bölüp a,b,c değerleri verildi.
#her bölmeyi L/3 uzunlukta kabul edildi.
'''TABLO OLUŞTURMA '''
number0_100 = np.linspace(0,100,101)
postNumbers = np.linspace(0,100,101)
framePostNumber = pd.DataFrame(postNumbers,index= number0_100)
intervals = np.linspace(0,int(length),101)
#burada L/100 değerlerini bulundu.
frameIntervals = pd.DataFrame(intervals, index = number0_100)
yukDegerNumpy = result.to_numpy()
frameForQrates = pd.DataFrame(yukDegerNumpy, index = number0_100)
trokodials = [1,0.966,0.871,0.795,0.578,0.422,0.28,0.16,0.072,0.018,0,
              ((-1)*(-0.018)),((-1)*(-0.072)),((-1)*(-0.16)),((-1)*(-0.28)),((-1)*(-0.422)),
              ((-1)*(-0.578)),((-1)*(-0.795)),((-1)*(-0.871)),((-1)*(-0.966)), ((-1)*(-1))]
#trokodials = np.roll(trokodials,1) #burada trokodial değerlerini kaydırma denendi ama sadece 10un katları olarak postaları kaydırılabiliyordu
#trokodialsMirror = [-0.018, -0.072, -0.16, -0.28, -0.422, -0.578, -0.795, -0.871, -0.966, -1] #liste içinde aynı değerleri 2 defa kabul etmediği ayna olarak ikinci liste kullanılmaya çalışıldı
indexForKisi = [0,(length/20),(length/10),((3*length)/20),(length/5),(length/4),
                ((3*length)/10),((7*length)/20),((2*length)/5),((9*length)/20),(length/2),
                ((11*length)/20),((12*length)/20),((13*length)/20),((14*length)/20),((15*length)/20),
                ((16*length)/20),((17*length)/20),((18*length)/20),((19*length)/20),length]
'''YENİ ÇUKUR'''
trokodialZero_Half =np.linspace(0,length,101)
delta_h = 0.9560535
cukur = np.interp(trokodialZero_Half,indexForKisi,trokodials)
cukur = np.roll(cukur, -1) 
ksi_cukur = ((draught - r) + (H * cukur) + delta_h)
#burada artık değerleri %3 ve %6 değerlerinin altında kalması için birer posta kaydırılmnası yapılmıştır ve aşağıdaki
#önce paralel batırma veya yükseltme yaptıktan sonra hala linner düzeltme kuralı uygulanamıyorsa bu durum uygulanmıştır ve daha sonra lineer düzeltme yapılmıştır. 
for i in range(101):
    if ksi_cukur[i] > D : 
        ksi_cukur[i] = D
#kısi değeri güverteyi geçmemesi için bu kodla sınırlandırılmıştır
trokodialsFrame = pd.DataFrame(trokodials,index = indexForKisi)
trokodialsR = trokodialsFrame.reindex(trokodialZero_Half)
trokodials_inter = trokodialsR.interpolate()
trokNumpy = trokodials_inter.to_numpy()
'''
listeKisi = []
for i in range(101):
    listeKisi.append((draught-r) + (H * trokNumpy[i]) + delta_h)
listeKisi = np.array(listeKisi)
'''  
#ξ değerleri bulunmaya çalışıldı ama başarılı olunamadı
frameKisi = pd.DataFrame(ksi_cukur, index = number0_100)
#for i in range(101):
#    if listeKisi[i] > D:
#        listeKisi[i] = D
#trokodials_reindex = trokodials_inter.reindex(number0_100)
#trokodialsFrameMirror = pd.DataFrame(trokodialsMirror,index = indexForKisiMirror)
#trokodialsMirrR = trokodialsFrameMirror.reindex(trokodialHalf_Full)
#trokodialsMirr_inter = trokodialsMirrR.interpolate()
#(trokodials_inter)
#print(trokodialsMirr_inter)
#burada gemiyi ikiye bölüp 2 parça için işlem yapmak istenildi ama başarılı olunamadı
ksi_cukur = np.array(ksi_cukur)
'''A(X) DEĞERLERİ'''
areas = np.array(areas)
equation = []
waterline = np.linspace(h,6*h,6)
ax = []
for i in range(101):
    polifit = np.polyfit(waterline,areas[i],3)
    polifitInter = np.poly1d(polifit)
    equation.append(polifitInter)
    a_x = (equation[i](ksi_cukur[i])) * 1.025
    ax.append(a_x)
#ax = np.ndarray.tolist(ax)
#new_ax = [i[0] for i in ax]
#new_ax[0] = 0
frame_ax = pd.DataFrame(ax)
#axList = []
#for i in range(101):
#    axList.append(ax[i])
displacement_ = []
displacement_.append(0)
for i in range(len(ax)-1):
    displacement_.append((((ax[i] + ax[i + 1]) / 2) + displacement_[i]))
disp_ = []
for i in range(101):
    disp_.append(displacement_[i] * s)
#kaldırma kuvvetleri integre edilip postalar arası mesafe ile çarpılıp deplasmanlar hesaplanmıştır.
#Son postada bulunan deplasman değerinin de geminin deplasman
#değerine eşit olması gerekir bu yüzden de paralel batırma yapıyoruz çünkü asıl deplasman değerimizden büyük çıktı 
# #bu yüzden de formülde delta_h değerinde ekleme yapıyoruz
'''SAKİN SU'''
listeSakinSuAx = []
for i in range(101):
    listeSakinSuAx.append(alanWl4[i] * 1.025)    
#alanWl4_simp = integrate.simps(alanWl4)
#simpson kuralını fonksiyon olarak işleme uydurulamadı
'''
listWl4_simpson = []
for i in range(101):
    if i == 0:
        listWl4_simpson.append(alanWl4[i] * 1)
    elif i%2 == 0:
        listWl4_simpson.append(alanWl4[i] * 4)
    elif i %2 == 1:
        listWl4_simpson.append(alanWl4[i] * 2) 
    elif i == 100:
        listWl4_simpson.append(alanWl4[i] * 1)
'''
#burada simpson kuralı açık olarak yazılmayı denendi ama ileride işlemlerde hata çıkardı
listeSakinSuPx = []
for i in range(101):
    listeSakinSuPx.append(listeSakinSuAx[i]-yukDegerNumpy[i]) 
#yük değerleri ve ax kaldırma kuvvetlerini toplayarak p(x) değeri
listeAxInter = []
for i in range(101):    
    listeAxInter.append(listeSakinSuAx[i] * intervals[i])
lCB = sum(listeAxInter) / sum(listeSakinSuAx)
listeYukInter = []
for i in range(101):
    listeYukInter.append(yukDegerNumpy[i] * intervals[i])
#p(x) kümülatif integre edildikten sonra artık değer çıkmaktadır.Bu da %3 den fazladır.Lineer
#düzeltme yapılamamıştır.Bu yüzden gemi trim yapıyor.Lineer düzeltme yerine Prohaska yönteminde sakin su trim düzeltmesi 
#yapılmaktadır.
lCG = sum(listeYukInter) / sum(yukDegerNumpy)
deltaLCG = lCG - lCB
#LCG VE LCB değerlerini aynı noktaya getirmek için x mesafesi kadarki bi değeri geminin kıçından alıp başına eklendi
x = (displacement * deltaLCG) / (length**2) * (54/7)
cikar_yuk = (-1 * x) / intervals[34] 
listCıkYuk = []
for i in range(34):
    listCıkYuk.append(intervals[i] * cikar_yuk)
listResultTers = listCıkYuk[::-1]
listResultTers = list(listResultTers)
newListResult = [i[0] for i in listResultTers]
listYeniYukDegerA = []
listA = yukDegerNumpy[:34]
listA = list(listA)
listNewA = [i[0] for i in listA]
for i in range(34):
    listYeniYukDegerA.append(listNewA[i]- newListResult[i])
listYeniYukDegerC = []
listC = yukDegerNumpy[67:]
listC = list(listC)
listNewC = [i[0] for i in listC]
for i in range(34):
    listYeniYukDegerC.append(listNewC[i] + listCıkYuk[i])
listYeniYukDegerB = yukDegerNumpy[34:67]
listYeniYukDegerB = list(listYeniYukDegerB)
listYeniYukDegerB = [i[0] for i in listYeniYukDegerB]
listYeniYukDegerC = list(listYeniYukDegerC)
listYeniYukDegerC = [i[0] for i in listYeniYukDegerC]
listYeniYukDegerA.extend(listYeniYukDegerB)
listYeniYukDegerA.extend(listYeniYukDegerC)
#x mesafesini a b kısımları arasındaki mesafelerle orantılı olarak azaltıp c kısmına eklendi.
#daha sonra yeni yük değerleri kullanılarak p(x) hesabına geçildi.
plt.figure()
plt.plot(listYeniYukDegerA, label = "Yeni Yük")
plt.plot(yukDegerNumpy, label= "Eski Yük")
plt.title("Prohaska Yük Düzeltmesi")
plt.xlabel("Posta Numaraları")
plt.ylabel("q(ton / metre")
plt.legend()
plt.grid()
plt.show()
#bu grafikte prohaska yöntemiyle bulduğumuz sakin su trim düzeltmesinin değişimi gösterildi 
listSakinSuYeniPx = []
for i in range(101):
    listSakinSuYeniPx.append(listeSakinSuAx[i] - listYeniYukDegerA[i])
listSakinYeniPx = []
for i in range(len(listSakinSuYeniPx)):
    listSakinYeniPx.append(listSakinSuYeniPx[i] + trok_deger)
listYeniPx = []
listYeniPx.append(0)
for i in range(len(listSakinYeniPx )-1):
    listYeniPx.append(((listSakinYeniPx[i] + listSakinYeniPx[i + 1]) / 2) + listYeniPx[i])
listeLineerPx = []
for i in range(101):
    listeLineerPx.append((intervals[i]/length) * listYeniPx[100])
duzeltmeYeniPx =  []
for i in range(101):
    duzeltmeYeniPx.append(listYeniPx[i] - listeLineerPx[i])  
duzeltmeYeniPx_int = []
duzeltmeYeniPx_int.append(0)
for i in range(len(duzeltmeYeniPx) - 1):
    duzeltmeYeniPx_int.append(((duzeltmeYeniPx[i] + duzeltmeYeniPx[i + 1]) / 2) + duzeltmeYeniPx_int[i])
duzeltmeYeniPxLineer = []
for i in range(101):
    duzeltmeYeniPxLineer.append(((intervals[i]/length) * duzeltmeYeniPx_int[100]))
duzeltmeYeniLineerFark = []
for i in range(101):
    duzeltmeYeniLineerFark.append(duzeltmeYeniPx_int[i] - duzeltmeYeniPxLineer[i])
listKesmeKuvveti = []
for i in range(101):
    listKesmeKuvveti.append(duzeltmeYeniPx[i] * s)
listMoment = []
for i in range(101):
    listMoment.append(duzeltmeYeniLineerFark[i] * (s**2))
#bu bölümde yeni yük değerleriyle birlikte p(x) değerleri bulunduktan sonra p(x) kümülatif integre edilerek 
#∫p(x) e geçiş yapıldı burada son değerde çıkan değer maksimum değerinin %3 den küçük olduğundan dolayı lineer düzeltme
#yapıldı.Tekrar integre edildikten sonra ∫∫p(x) değerinin son değeri de maksimum değerin %6 sından küçük
#olduğunda tekrar lineer düzeltme yapılarak düzeltildi.Kesme kuvveti ve moment değerlerine geçiş
#yapıldı. kesme kuvveti bulunurken ∫p(x) postalar arası mesafe ile çarpılarak moment değerleri de ∫∫p(x) in postalar
#arası mesafenin karesi ile çarpılarak yapıldı. 

'''DALGA ÇUKURU'''
'''hacim oran yük dağılımı '''
#dalga çukuru problemleni çözerken prohaska yöntemiyle sonuçlar olumlu sonuç vermediğinden dolayı hacim oran yöntemi
#kullanılmıştır.
listWl6_simpson = []
for i in range(101):
    if i == 0:
        listWl6_simpson.append(alanWl6[i] * 1)
    elif i%2 == 0:
        listWl6_simpson.append(alanWl6[i] * 4)
    elif i %2 == 1:
        listWl6_simpson.append(alanWl6[i] * 2) 
    elif i == 100:
        listWl6_simpson.append(alanWl6[i] * 1)
hacim = sum(listWl6_simpson) * (1/3) * s
#hacmi bulurken geminin WL6 ya kadar olan alanları simpson yapılarak bulunmuştur.

listHacimOran = []
for i in range(101):
    listHacimOran.append((displacement * alanWl6[i]) / hacim )
#burada da geminin deplasmanının WL6 daki her postadaki alanlarla çarpılıp geminin toplam hacmine bölünerek 
#her postaya denk gelen yük değerleri bulundu.
hacimOranYuk = []
for i in range(101):
    hacimOranYuk.append( ax[i] - listHacimOran[i])
listIntCukur = []
listIntCukur.append(0)
for i in range(len(hacimOranYuk) - 1):
    listIntCukur.append(((hacimOranYuk[i] + hacimOranYuk[i + 1]) / 2) + listIntCukur[i])
#listeFark_cumul = integrate.cumtrapz(listeFark)
#listeFark_cumul = list(listeFark_cumul)
#listeFark_cumul.insert(0,0.0)
#burada oluşturulan listelere kümülatif trapez yapıldı ve  bazı değerleri 0 eklendi ama sonrasında yanlış olduğu farkedilerek 
#kümülatif trapez yöntemi açık şekilde yazılarak listeler işleme alındı
listeLineer = []
for i in range(101):
    listeLineer.append((intervals[i]/length) * listIntCukur[100])
listeLineer[0] = (-1) * listeLineer[0]
listeIntPx = []
for i in range(101):
    listeIntPx.append(listIntCukur[i] - listeLineer[i])
intIntPx_cukur = []
intIntPx_cukur.append(0)
for i in range(len(listeIntPx) - 1):
    intIntPx_cukur.append(((listeIntPx[i] + listeIntPx[i + 1]) / 2) + intIntPx_cukur[i])
duzIntInt = []
for i in range(101):
    duzIntInt.append((intervals[i]/length) * intIntPx_cukur[100])

listeDuzIntInt= []
for i in range(101):
    listeDuzIntInt.append(intIntPx_cukur[i] - duzIntInt[i])
cukurKesme = []
for i in range(101):
    cukurKesme.append(listeIntPx[i] * s)
cukurMoment = []
for i in range(101):
    cukurMoment.append(listeDuzIntInt[i] * (s**2))
#bu kısımda p(x) değeri a(x) - yük değerleri bulunmuştur 
#eksi yapmamızdaki sebep a(x) i pozitif alıp yük değerleri negatif almamızdır. daha sonra sırasıyla p(x) integre
#edilip ∫p(x) in son değeri maksimum değerininin %3 den küçük olduğundan lineer düzeltmme yapılmıştır. Sonra tekrar integre 
#edip ∫∫p(x) inde son değeri maksimum değerin %6 sından küçük olduğundan lineer düzeltme yapılmıştır.kesme kuvveti ve
#moment değerlerini bulurken de kesme kuvveti için ∫p(x) i postalar arası mesafe(s) ile momenti de ∫∫p(x) i postalar
#arası mesafenin karesi(s^2) ile çarpılması sonıucu bulunmuştur.
#listeIntPx_int = integrate.cumtrapz(listeIntPx)
#listeIntPx_int = list(listeIntPx_int)
#listeIntPx_int.insert(0,0.0) 
# kümülatif trapez burada bize yanlış değer verdiği için istediğimiz şekilde yazıldı 
'''DALGA TEPESİ'''
trok_tepe = [0,0.018,0.072,0.16,0.28,0.422,0.578,0.795,0.871,0.966,1,((-1)*(-0.966)),
            ((-1)*(-0.871)),((-1)*(-0.795)),((-1)*(-0.578)),((-1)*(-0.422)),((-1)*(-0.28)),
            ((-1)*(-0.16)),((-1)*(-0.072)),((-1)*(-0.018)),(0*1)]
indexForKisi_tepe = [0,(length/20),(length/10),((3*length)/20),(length/5),(length/4),
                ((3*length)/10),((7*length)/20),((2*length)/5),((9*length)/20),(length/2),
                ((11*length)/20),((12*length)/20),((13*length)/20),((14*length)/20),((15*length)/20),
                ((16*length)/20),((17*length)/20),((18*length)/20),((19*length)/20),length]
trokodialPosta =np.linspace(0,length,101)
delta_h1 = 0.54179
tepe = np.interp(trokodialPosta,indexForKisi_tepe,trok_tepe)
tepe = np.roll(tepe, -1) 
#burada artık değerleri %3 ve %6 değerlerinin altında kalması için birer posta kaydırılmnası yapılmıştır ve aşağıdaki
# yani önce paralel batırma veya yükseltme yaptıktan sonra hala linner düzeltme kuralı uygulanamadı ve sonrasında lineer düzeltme yapılmıştır.
ksi_tepe = ((draught - r) + (H * tepe) - delta_h1)#ξ değerleri ((draught - r) + (H * c) ) hesaplanmıştır.
for i in range(101):
    if ksi_tepe[i] > D : 
        ksi_tepe[i] = D
#kısinin güverteyi geçmemesi için sınırlama yapıldı
trokodials_tepeFrame = pd.DataFrame(trok_tepe,index = indexForKisi_tepe);trokodialsR_tepe = trokodials_tepeFrame.reindex(trokodialPosta)
trokodialsTepe_int = trokodialsR_tepe.interpolate();trokNumpy_tepe = trokodialsTepe_int.to_numpy()
listeKisi_tepe = []
delta_h1 = 0.5
for i in range(101):
    listeKisi_tepe.append((draught-r) + (H * trokNumpy_tepe[i]) - delta_h1)
listeKisi_tepe = np.array(listeKisi_tepe)
for i in range(101):
    if listeKisi_tepe[i] > D:
        listeKisi_tepe[i] = D
equationTepe = []
axTepe = []
for i in range(101):
    polifitTepe = np.polyfit(waterline,areas[i],3)
    polifitInterTepe = np.poly1d(polifitTepe)
    equationTepe.append(polifitInterTepe)
    a_xTepe= (equationTepe[i](ksi_tepe[i])) * 1.025 #ξ bonjean alan eğrileriyle kesiştiği yerdeki alnları hesaplamak için 3.dereceden 
#bir eğri uydurarak her postaya denk gelicek şekilde a(x) değerleri suyun yoğunluğuyla çarpılarak hesaplanmıştır.
    axTepe.append(a_xTepe)#kaldırma kuvveti
for i in range(101):
    if axTepe[i] < 0 :
        axTepe[i] = 0

plt.figure()
plt.plot(axTepe)
plt.show()
#oluşturulan değerlerde bir kısımdan sonra eğriler kesişmediği için eksi değer alınıyordu
#bu eksi değerlerin yerine 0 kabul edildi
displacement_Tepe = []
displacement_Tepe.append(0)
for i in range(len(axTepe)-1):
    displacement_Tepe.append((((axTepe[i] + axTepe[i + 1]) / 2) + displacement_Tepe[i]))
disp_Tepe = []
for i in range(101):
    disp_Tepe.append(displacement_Tepe[i] * s)
pxTepe = [] # px değerleri
for i in range(101):
    pxTepe.append(axTepe[i] - listYeniYukDegerA[i])
pxTepe_int = [] # integre edilmiş px değerleri
pxTepe_int.append(0)
for i in range(len(pxTepe) - 1):
    pxTepe_int.append((((pxTepe[i] + pxTepe[i + 1]) / 2) + pxTepe_int[i]))
listeLineerTepe = [] #lineer değerleri
for i in range(101):
    listeLineerTepe.append((intervals[i]/length) * pxTepe_int[100])
listeLineerTepe[0] = (-1) * listeLineerTepe[0]
listDuzeltmeTepe = [] # lineer düzeltilmiş integre edilen px değerleri 
for i in range(101):
    listDuzeltmeTepe.append(pxTepe_int[i] - listeLineerTepe[i])
intIntPxTepe = [] # çift katlı integre edilmiş px değerleri
intIntPxTepe.append(0)
for i in range(len(listDuzeltmeTepe) - 1):
    intIntPxTepe.append(((listDuzeltmeTepe[i] + listDuzeltmeTepe[i + 1]) / 2) + intIntPxTepe[i])
listeLineerTepe_int = []
for i in range(101):
    listeLineerTepe_int.append((intervals[i]/length) * intIntPxTepe[100])
listeLineerTepe_int[0] = (-1) * listeLineerTepe_int[0]
listDuzeltmeTepe_int = []
for i in range(101):
    listDuzeltmeTepe_int.append(intIntPxTepe[i] - listeLineerTepe_int[i])
kesmeKuvvetiTepe = []#kesme kuvveti için ∫p(x) i postalar arası mesafe(s) ile çarpılır
for i in range(101):
    kesmeKuvvetiTepe.append(listDuzeltmeTepe[i] * s)
momentTepe = [] # momenti de ∫∫p(x) i postalar arası mesafenin karesi(s^2) ile çarpılır.
for i in range(101):
    momentTepe.append(listDuzeltmeTepe_int[i] * (s**2))
def grafik_olusturma(y_deger, title,y_label): # istenilen grafikler için fonksiyon oluşturuldu
    plt.figure()
    plt.plot(number0_100, y_deger)
    plt.title(title, fontweight = 'bold')
    plt.xlabel("Gemi Boyu", fontweight = 'bold')
    plt.ylabel(y_label, fontweight = 'bold')
    plt.grid()
    plt.show()
grafik_olusturma(listKesmeKuvveti,"Sakin Su Kesme Kuvveti", "ton")
grafik_olusturma(listMoment, "Sakin Su Moment","ton.metre")
grafik_olusturma(cukurKesme, "Dalga Çukuru Kesme Kuvveti","ton")
grafik_olusturma(cukurMoment, "Dalga Çukuru Moment","ton.metre")
grafik_olusturma(kesmeKuvvetiTepe, "Dalga Tepesi Kesme Kuvveti","ton")
grafik_olusturma(momentTepe, "Dalga Tepesi Moment","ton.metre")
grafik_olusturma(listHacimOran,"Hacim Oran Yük Dağılımı", "q(ton / metre")
''' ATALET MOMENTLERİ'''
#min midship section modulus
cRs = 1 #for unlimited service range
cRw = 1 # for unlimited service range
k = 1 # for Reh = 235 N / mm2
c0 = (10.75 - (((300- length) / 100) ** (1.5))) * cRw
w_min = k * c0 * (length ** 2) * breadth * (Cb + 0.7) * cRs * (10 ** (-6)) #metreküp
iMastori = 3 * (10 ** -2) * w_min * (length / k)
y_max= iMastori / w_min #tarafsız eksenden geminin güvertesine olan uzaklık
#tarafsız eksen bütün gemi boyunca sabit olarak kabul edilmiştir.
listI_x = []
for i in intervals:
    if i >= 0 and i < length/20:
        listI_x.append(5 * iMastori * (i / length))
    if i >= length/20 and i < ((7*length) / 20):
        listI_x.append((0.25 * iMastori) + (((15 * iMastori)/(6*length))*(i -(length/20))))
    if i >= ((7*length) / 20) and i < ((15 * length) / 20):
        listI_x.append(iMastori)
    if i >= ((15 * length) / 20) and i < ((19* length) / 20):
        listI_x.append(iMastori - ((2.5 *(iMastori/length)*(i - (15 * length) /20))))
    if i >= ((19* length) / 20) and i <= length:
        listI_x.append((0.5 * iMastori) - (((10 * iMastori) / length) * (i - ((19* length) / 20))))
#bu kısımda geminin belli boy aralıklarına göre verilen ampirik atalet momenti formülüne göre hesaplar yapılıp
#bu hesaplar gerilme hesabı yapılırken kullanılmıştır.        
#sakin su, dalga tepesi ve dalga çukuru için bulunan momentler kullanılarak güvertedeki gerilmeler hesaplanmıştır.
listGerilme = []
listGerilme_tepe = []
listGerilme_cukur = []
def gerilmeler(gerilme_adi, moment_adi):
    for i in range(101):
        if listI_x[i] == 0:
            continue
        else:
            gerilme_adi.append((((moment_adi[i] / listI_x[i]) * y_max) * 9.81) / 1000)
    gerilme_adi.append(0.0)
    gerilme_adi.insert(0,0.0) #atalet listesinde ilk ve son değerler sıfır olduğundan NaN değeri çıktısı veriyordu.
    #bu yüzden if döngüsünde atalet listesinde sıfır olan değerler işleme alınmayıp direkt olarak sıfır değerleri atanmıştır.
gerilmeler(listGerilme, listMoment)
gerilmeler(listGerilme_tepe, momentTepe)
gerilmeler(listGerilme_cukur, cukurMoment)
frameDuzIntIntPx = pd.DataFrame(duzeltmeYeniLineerFark)
frameDuzeltmeYeniInt = pd.DataFrame(duzeltmeYeniPx_int);frameYeniPx = pd.DataFrame(listYeniPx);frameDuzeltmeYeniPx = pd.DataFrame(duzeltmeYeniPx)
frameYeniSakinSuPx = pd.DataFrame(listSakinSuYeniPx);frameYeniYukDeger = pd.DataFrame(listYeniYukDegerA);frameSakinSuAx = pd.DataFrame(listeSakinSuAx)
frameSakinSuPx = pd.DataFrame(listeSakinSuPx);frameKesme = pd.DataFrame(listKesmeKuvveti);frameMoment = pd.DataFrame(listMoment);
frameSakinGerilme = pd.DataFrame(listGerilme)
framesTableSakinSu =basamak([framePostNumber,frameIntervals, frameForQrates,frameYeniYukDeger,frameSakinSuAx,frameSakinSuPx,
                            frameYeniSakinSuPx,frameYeniPx,frameDuzeltmeYeniPx,frameDuzeltmeYeniInt,frameDuzIntIntPx,frameKesme,frameMoment,
                            frameSakinGerilme])        
result2_sakinSu = pd.concat(framesTableSakinSu,axis=1)
result3_sakinSu = result2_sakinSu.reindex(number0_100)
columns_sakinSu = ["Post Numbers","Intervals","Yük Degerleri","Yeni Yük Degerleri","SakinSu A(x)","SakinSu P(x)","Yeni SakinSu P(x)",
                   "Yeni Sakin Su IntP(x)","Duzeltilmis YSS IntP(x)","Int Int P(x)","Duzeltilmis IntIntP(x)",
                   "Kesme Kuvveti","Moment","Gerilme"]
result3_sakinSu.columns = columns_sakinSu
result3_sakinSu.to_excel("Sakin Su Tablosu.xlsx")# sakin suda hesaplanan tüm değerleri excel formatında görebilirsiniz 
framePx = pd.DataFrame(hacimOranYuk);framePxCukur = pd.DataFrame(listIntCukur);frameDuzIntInt = pd.DataFrame(listeDuzIntInt)
frameIntIntPx= pd.DataFrame(intIntPx_cukur);frameCukurKesme = pd.DataFrame(cukurKesme);frameCukurMoment = pd.DataFrame(cukurMoment)
frameListeLineer = pd.DataFrame(listeLineer);frameIntDuzPx = pd.DataFrame(listeIntPx);frameYeniYukA = pd.DataFrame(listYeniYukDegerA)
frameDis = pd.DataFrame(disp_);frameCukurGerilme = pd.DataFrame(listGerilme_cukur)
framesTable = basamak([framePostNumber,frameIntervals, frameYeniYukA, frameKisi,frame_ax,frameDis,framePx,
               framePxCukur,frameListeLineer,frameIntDuzPx,frameIntIntPx, frameDuzIntInt,
               frameCukurKesme, frameCukurMoment,frameCukurGerilme])
result2 = pd.concat(framesTable,axis=1)
result3 = result2.reindex(number0_100)
columns = ["Post Numbers","Intervals","Yük Degerleri","Kısi","A(x)","Displacement","P(x)",
           "Integ. P(x)","L.D.","Düzeltilmiş Int.P(x)","IntIntP(x)", "Duzeltilmiş IntIntP(x)",
           "Kesme Kuvveti", "Moment","Gerilme"]
result3.columns = columns
result3.to_excel("Dalga Çukuru Tablosu.xlsx") # dalga çukurunda oluşan tüm değerleri gösteren tablo excel formatında hazırlanmıştır
frameKisi_tepe = pd.DataFrame(ksi_tepe, index = number0_100);frameAxTepe = pd.DataFrame(axTepe);frameDispTepe = pd.DataFrame(disp_Tepe)
framePxTepe = pd.DataFrame(pxTepe);framePxIntTepe = pd.DataFrame(pxTepe_int);frameLd = pd.DataFrame(listeLineerTepe)
frameDuzTepePxInt = pd.DataFrame(listDuzeltmeTepe);frameIntIntPxTepe = pd.DataFrame(intIntPxTepe);frameLD_int = pd.DataFrame(listeLineerTepe_int)
frameDuzIntIntPx = pd.DataFrame(listDuzeltmeTepe_int);frameKesmeTepe = pd.DataFrame(kesmeKuvvetiTepe);frameMomentTepe = pd.DataFrame(momentTepe)
frameTepeGerilme = pd.DataFrame(listGerilme_tepe)
framesTable_tepe = basamak([framePostNumber,frameIntervals, frameYeniYukDeger, frameKisi_tepe,frameAxTepe,frameDispTepe,framePxTepe,
               framePxIntTepe,frameLd,frameDuzTepePxInt,frameIntIntPxTepe, frameLD_int,frameDuzIntIntPx,
               frameKesmeTepe, frameMomentTepe,frameTepeGerilme])
result_tepe = pd.concat(framesTable_tepe,axis=1)
result_tepe2 = result_tepe.reindex(number0_100)
columns_tepe = ["Post Numbers","Intervals","Yük Degerleri","Kısi","A(x)","Displacement","P(x)",
           "Integ. P(x)","L.D.","Düzeltilmiş Int.P(x)","IntIntP(x)","L.D", "Duzeltilmiş IntIntP(x)",
           "Kesme Kuvveti", "Moment","Gerilme"]
result_tepe2.columns = columns_tepe
result_tepe2.to_excel("Dalga Tepesi Tablosu.xlsx") #dalga tepesi için tüm değerlerin gösterildiği excel tablosu hazırlanmıştır
'''
for i in range(101):
    if listI_x[i] == 0:
        continue
    else:
        listGerilme.append(((-1) *((listMoment[i] / listI_x[i]) *  y_max) * 9.81)/1000)
listGerilme.append(0.0)
listGerilme.insert(0,0.0)
listGerilme = basamak(listGerilme)
print(listGerilme)
for i in range(101):
    listGerilme_tepe.append(((-1) *((momentTepe[i] / listI_x[i]) *  y_max) * 9.81)/1000)
    if momentTepe[i] == 0:
        listGerilme_tepe[i] = 0
for i in range(101):
    listGerilme_cukur.append((((cukurMoment[i] / listI_x[i]) * y_max) * 9.81) / 1000)
    if cukurMoment[i] == 0:
        listGerilme_cukur[i] = 0
'''
#burada gerilme hesaplamalarını tek tek hesaplama yapmak istendi ama sonrasında fonksiyon oluşturuldu
def grafik_gerilme(liste_gerilme, title, y_labe): # gerilme grafikleri için fonksiyon oluşturuldu
    plt.figure()
    plt.plot()
    plt.plot(number0_100, liste_gerilme)
    plt.title(title, fontweight = 'bold')
    plt.xlabel("Gemi Boyu", fontweight = 'bold')
    plt.ylabel(y_labe)
    plt.grid()
    plt.show()
grafik_gerilme(listGerilme,"Sakin Su Gerilme","σ(MPa)")
grafik_gerilme(listGerilme_tepe,"Dalga Tepesi Gerilme","σ(MPa)")
grafik_gerilme(listGerilme_cukur,"Dalga Çukuru Gerilme","σ(MPa)")

'''GUVERTENİN 1 METRE ALTI İÇİN BİLEŞKE GERİLMELER'''
'''S_SAKİN'''
b_perde = breadth
h_perde = 1
a_i = b_perde * h_perde
y_i = y_max - 0.5 
s_perde = (a_i * y_i)  #buradaki bölge enine perde olarak kabul edilmiştir
#Perde hesaplanırken o posta dikdörtgen olarak kabul edlilp onun ataleti alınıp  
#dikdörtgen perdenin alanı alınmıştır bunlar aynı şekilde o postanın gerçek alanıyla oranlanıp atalet bulunmuştur.
thickness = ((length * k) ** 0.5) / 1000
i_x_sakin = ((( breadth * ( D ** 3 )) / 12) * alanWl6[82]) / (breadth * D)
maxMoment = listMoment[82] * (-1) #her dalga durumu için kesme kuvvetinin maksimum olduğu yerdeki moment ve kesme kuvvetleri belirlendi. 
sigma_sakin = (((maxMoment / listI_x[82] ) * (y_max - 1)) * 9.81) / 1000 # moment kaynaklı gerilmeler (σ) hesaplanmıştır.
tau_sakin = (((listKesmeKuvveti[82] * s_perde) / (i_x_sakin * thickness) * 9.81) / 1000) #τmax bulurken (kesme kuvveti*S)/(atalet *kalınlık) 
sigma_vonmisses = ((sigma_sakin ** 2) + (3 * (tau_sakin ** 2)))** 0.5
''' S DALGA CUKURU'''
i_x_cukur = ((( breadth * ( D ** 3 )) / 12) * alanWl6[26]) / (breadth * D)
maxMoment_cukur = listMoment[26] * (-1)
sigma_cukur = (((maxMoment_cukur / listI_x[26] ) * (y_max - 1)) * 9.81) / 1000
tau_cukur = (((listKesmeKuvveti[26] * s_perde) / (i_x_cukur * thickness) * 9.81) / 1000)
sigma_vonmisses_cukur = ((sigma_cukur ** 2) + (3 * (tau_cukur ** 2)))** 0.5
''' S DALGA TEPESİ'''
i_x_tepe = ((( breadth * ( D ** 3 )) / 12) * alanWl6[73]) / (breadth * D)
maxMoment_tepe = listMoment[73] * (-1)
sigma_tepe = (((maxMoment_tepe / listI_x[73] ) * (y_max - 1)) * 9.81) / 1000
tau_tepe = (((listKesmeKuvveti[73] * s_perde) / (i_x_tepe * thickness) * 9.81) / 1000)
sigma_vonmisses_tepe = ((sigma_tepe ** 2) + (3 * (tau_tepe ** 2)))** 0.5
#sonuçların hepsi akma sınırının altındadır.
# geminin ömrünün belirlenmesi için σamplitude un belirlenmesi
#gerekir. bunun hesaplanması da dalga tepesindeki maksimum güverte gerilmesi ile dalga çukurundaki güvertedeki 
#maksimum gerilmenin arasındaki farktır
# bunun sonucu gemi inşa çeliğinin akma gerilmesinin yarısından az ise eğer 
#geminin ömrü sonsuz olduğu denilebilir.
with open("GUVERTENİN 1 METRE ALTI İÇİN BİLEŞKE GERİLMELER.txt", "w") as f:
    f.write(" \n")
    f.write("SAKİN SU İÇİN;\n")
    f.write(" \n")
    f.write(f"Sakin Su I(x): {i_x_sakin}\n")
    f.write(f"Maximum Moment Değeri:{maxMoment}\n")
    f.write(f"Sakin Su Sigma Değeri : {sigma_sakin}\n")
    f.write(f"Sakin Su Tau Değeri : {tau_sakin}\n")
    f.write(f"Sakin Su Sigma VonMisses : {sigma_vonmisses}\n")
    f.write(" \n")
    f.write("DALGA TEPESİ İÇİN;\n")
    f.write(" \n")
    f.write(f"Dalga Tepesi I(x): {i_x_tepe}\n")
    f.write(f"Maximum Moment Değeri:{maxMoment_tepe}\n")
    f.write(f"Dalga Tepesi Sigma Değeri : {sigma_tepe}\n")
    f.write(f"Dalga Tepesi Tau Değeri : {tau_tepe}\n")
    f.write(f"Dalga Çukuru Sigma VonMisses : {sigma_vonmisses_tepe}\n")
    f.write(" \n")
    f.write("DALGA ÇUKURU İÇİN;\n")
    f.write(" \n")
    f.write(f"Dalga Çukuru I(x): {i_x_cukur}\n")
    f.write(f"Maximum Moment Değeri:{maxMoment_cukur}\n")
    f.write(f"Dalga Çukuru Sigma Değeri : {sigma_cukur}\n")
    f.write(f"Dalga Çukuru Tau Değeri : {tau_cukur}\n")
    f.write(f"Dalga Çukuru Sigma VonMisses : {sigma_vonmisses_tepe}\n")
#tüm değerler txt formatında yazdırıldı
        
    











    
    








    
