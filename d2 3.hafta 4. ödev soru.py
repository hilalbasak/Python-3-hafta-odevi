while True:
    print("1-Carpma")
    print("2-Bölme")
    secim=input("Bir işlem seçin:")
    
    if secim== "1" or secim=="2":
        sayi1=float(input("Birinci sayiyi girin:"))
        sayi2=float(input("ikinci sayiyi girin:"))
    
        if secim=="1":
            sonuc=sayi1*sayi2
            print("sonuç:",sonuc)
            
        elif secim=="2":
            if sayi2==0:
                print("0'a bölme yapılamaz.")
            else:
                sonuc=sayi1/sayi2
                print("sonuç:",sonuc)
                break
    else:
        print("Gecersiz secim.")       
        
    
"""
Merhaba hocam,
4.ödev sorusu "Menüye çarpma/bölme ekle;bölmede 0 kontrolü yap." idi.
Tavsiyeniz üzere kullanıcı gibi de düşünerek yazdığım bu kodda eğer kullanıcı 1 veya 2 
dışında bir secim yaparsa programın hata vermemesi için önce seçim kontrolü yapıp daha
sonra sayıları istedim. Programın hatalı girişte kapanmaması için while döngüsü ekledim.
Teşekkür ederim.
"""