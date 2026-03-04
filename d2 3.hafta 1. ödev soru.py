sayi=77
while True:
    try:
        tahmin= int(input("1 ile  100 arasında bir sayi tahmin ediniz:"))
        if tahmin<1 or tahmin>100:
            print("1 ile 100 arasında bir sayi giriniz.")
            continue
        if tahmin<sayi:
            print("Daha büyük bir sayi deneyiniz.")
        elif tahmin>sayi:
            print("Daha küçük bir sayi deneyiniz.")
        else:
            print("Tebrikler dogru tahmin!") 
            break
    except:
        print("Hatalı giriş, yalnızca sayı giriniz.")
        
        
"""
Merhaba hocam, 
1.Ödev sorusu "Sayı tahmin oyunu:1-100 arası;"daha büyük/küçük"ipucu ver."idi.
Yalnızca geliştirici olarak değil kullanıcı gözünden de bakarak programı yazmamız 
gerektiği tavsiyenizi göz önüne alarak ödev sorusunu while döngüsüne aldım ki yanlış tahmin
sonrası program kapanmasın. Ayrıca hocamızın 5.ödev sorusu yani try-except'i de sorulara ekleyin
isteği üzerine bu soruya entegre ettim ki sayı yerine metin girilirse program hata vermesin.
Teşekkür ederim.
"""