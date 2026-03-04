while True:
    try:
        vize=float(input("Vize notunu giriniz:"))
        final=float(input("Final notunu giriniz:"))
    
        if vize>=0 and vize<=100 and final>=0 and final<=100:
            ortalama= float(vize*0.4 + final*0.6)
            print(f"ortalama={ortalama:.2f}'dir.")
            if ortalama<=60 and ortalama>=0:
                print("Dersi şartlı geçtiniz.")
            elif ortalama<=70 and ortalama>60:
                print("Dersi cc geçtiniz.")
            elif ortalama<=80 and ortalama>70:
                print("Dersi bc geçtiniz.")
            elif ortalama<=90 and ortalama>80:
                print("Dersi ab geçtiniz.")
            elif ortalama<=100 and ortalama>90:
                print("Dersi aa geçtiniz.")
        else:
            print("Sınırların dışında değer tanımlandı. Lütfen 0<=not<=100 aralığında değer giriniz.")
            continue
    except:
         print("Hatalı giriş, yalnızca sayı giriniz.")     

""" 
Merhaba hocam,
3.Ödev sorusu "Not sistemi: 0-100 validasyon+harf notu(A-F)." idi.
Soruyu yalnızca not değerine göre değil, vize ve final ortalaması hesaplaması sonrası
harf notunu hesaplayan bu programı yazdım. Birinci soruda olduğu gibi bu soruda da 
try-except ekledim ki kullanıcı sayı yerine metin (örneğin "Ahmet") girerse program çökmesin.
Programın hatalı girişte kapanmaması için while döngüsü ekledim.
Teşekkür ederim.   
"""