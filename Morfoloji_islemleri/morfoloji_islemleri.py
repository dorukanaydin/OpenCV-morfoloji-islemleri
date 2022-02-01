import cv2
import numpy as np
#Resimlere morfoloji işlemlerinin uygulanması
cekirdek = np.ones((7,7),np.uint8)
resim = cv2.imread(r"opencv\video_ve_resimler\j.png")
gri_resim = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
resim2 = cv2.imread(r"opencv\video_ve_resimler\acma.JPG",0)
resim3 = cv2.imread(r"opencv\video_ve_resimler\kapama.JPG",0)


#Aşındırma(erozyon) işleminin yapılması, beyaz noktalar azalır.

# iteration : tekrarlama, yapılacak aşındırma işlemi sayısı
asındırma = cv2.erode(resim,cekirdek,iterations=1)

#Yayma işleminin yapılması, beyaz noktalar artar.
yayma = cv2.dilate(gri_resim,cekirdek,iterations=1)

#Gradyan işleminin yapılması, yayma ve aşındırmanın farkı(görüntünün iskeletini bulur.)
gradyan = cv2.morphologyEx(gri_resim,cv2.MORPH_GRADIENT,cekirdek)

#Açma ve kapama işlemlerinin yapılması
acma = cv2.morphologyEx(resim2,cv2.MORPH_OPEN,cekirdek)
kapama = cv2.morphologyEx(resim3,cv2.MORPH_CLOSE,cekirdek)

#Top-hat ve black-hat işlemlerinin yapılması , 
#top-hat:açma işleminden orjinali çıkarmak(beyaz fazla kalır) , black-hat: kapatma işleminden orjinali çıkarmak(beyaz az kalır)
top_hat = cv2.morphologyEx(gri_resim,cv2.MORPH_TOPHAT,cekirdek)
black_hat = cv2.morphologyEx(gri_resim,cv2.MORPH_BLACKHAT,cekirdek)

while True:
    print("1-Asindirma\n2-Yayma\n3-Gradyan\n4-Acma ve Kapama\n5-Top Hat ve Black Hat\n6-Cikis")
    secim = input("Yapmak istediginiz islemi seciniz:")
    
    if secim == '1':
        cv2.imshow("Orjinal",resim)
        cv2.imshow("Erozyon",asındırma)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
    
    if secim == '2':
        cv2.imshow("Orjinal",resim)
        cv2.imshow("Yayma",yayma)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
    
    if secim == '3':
        cv2.imshow("Orjinal",resim)
        cv2.imshow("Gradyan",gradyan)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
    
    if secim == '4':
        cv2.imshow("Orjinal Acma",resim2)
        cv2.imshow("Orjinal Kapama",resim3)
        cv2.imshow("Acma",acma)
        cv2.imshow("Kapama",kapama)
        cv2.waitKey(7000)
        cv2.destroyAllWindows()
    
    if secim == '5':
        cv2.imshow("Orjinal",resim)
        cv2.imshow("Top Hat",top_hat)
        cv2.imshow("Black Hat",black_hat)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
    
    if secim == '6':
        break
        
