umur = int(input("Masukkan Umur: "))

if umur <= 10:
    print("Anak-Anak")
elif umur <= 18:
    print("Remaja")
elif umur <= 35:
    print("Dewasa")
elif umur <= 65:
    print("Tua")
else:
    print("Parubaya")