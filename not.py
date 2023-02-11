# Üniversite not ortalaması
vize = int(input("Vize Notunuzu Giriniz:"))
final = int(input("Final Notunuzu Giriniz:"))
ortalama = (vize*0.4)+(final*0.6)

if ortalama > 90:
    print("Notunuz:{} Mükemmel AA ile geçtiniz.".format(ortalama))
    
elif ortalama > 80:
    print("Notunuz:{} Pekiyi BA ile geçtiniz.".format(ortalama))

elif ortalama > 70:
    print("Notunuz:{} İyi BB ile geçtiniz.".format(ortalama))

elif ortalama > 60:
    print("Notunuz:{} Orta CB ile geçtiniz.".format(ortalama))

elif ortalama > 55:
    print("Notunuz:{} Geçer CC ile geçtiniz.".format(ortalama))

elif ortalama > 50:
    print("Notunuz:{} Koşullu Geçer DC ile geçtiniz.".format(ortalama))

elif ortalama < 50:
    print("Notunuz:{} Kaldınız FF ile geçtiniz.".format(ortalama))