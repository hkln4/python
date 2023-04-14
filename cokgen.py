def kare(a):
    print(f"Karenin alanı: {a*a}")
def dikdortgen(a,b):
    print(f"Dikdörtgenin alanı: {a*b}")
def daire(r):
    pi = 3.14
    print(f"Dairenin alanı: {pi*(r**2):.2f}")
def ucgen(t,h):
    print(f"Üçgenin alanı: {t*h/2}")
def yamuk(a_t,u_t,h):
    print(f"Karenin alanı: {((a_t + u_t)* h)/ 2:.2f}")
def paralelkenar(a, h):
    print(f"Paralel kenarın alanı: {a * h}")
def eskenardortgen(a_k, y_k):
    print(f"Eşkenar dörtgenin alanı: {((a_k * y_k) / 2):.2f}")
secim = input("""Alanını bulmak istediğiniz geometrik şekli giriniz.
(kare,dikdortgen,daire,ucgen,yamuk,paralelkenar,eskenar dortgen)
""")
if secim == 'kare':
    a = int(input("Karenin bir kenarini giriniz."))
    kare(a)
elif secim == 'dikdortgen':
    a = int(input("Dikdortgenin kisa kenarini giriniz."))
    b = int(input("Dikdortgenin uzun kenarini giriniz."))
    dikdortgen(a,b)
elif secim == 'daire':
    r = int(input("Dairenin yari capini giriniz."))
    daire(r)
elif secim == 'ucgen':
    t = int(input("Ucgenin taban uzunlugunu giriniz."))
    h = int(input("Ucgenin yuksekligini giriniz."))
    ucgen(t,h)
elif secim == 'yamuk':
    a_t = int(input("Yamugun alt taban uzunlugunu giriniz."))
    u_t = int(input("Yamugun üst taban uzunlugunu giriniz."))
    h = int(input("Yamugun yuksekligini giriniz."))
    yamuk(a_t,u_t,h)
elif secim == 'paralelkenar':
    a = int(input("Paralelkenarin alt kenar uzunlugunu giriniz."))
    h = int(input("Paralelkenarin yuksekligini giriniz."))
    paralelkenar(a,h)
elif secim == 'eskenar dortgen':
    a_k = int(input("Eskenar dortgenin alt kenar uzunlugunu giriniz."))
    y_k = int(input("Eskenar dortgenin yan kenar uzunlugunu giriniz."))
    eskenardortgen(a_k, y_k)
else:
    print("Hatali secim yaptiniz. Tekrar Deneyiniz.")