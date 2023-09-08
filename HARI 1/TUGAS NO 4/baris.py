jumlah_baris = int(input("Masukkan jumlah baris: "))

for i in range(1, jumlah_baris + 1):
    for j in range(jumlah_baris - i):
        print(" ", end="")
    
    for k in range(2 * i - 1):
        print("*", end="")
    print()