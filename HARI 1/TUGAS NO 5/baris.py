# Meminta jumlah baris dari pengguna
jumlah_baris = int(input("Masukkan jumlah baris: "))

# Loop untuk mencetak tumpukan segitiga
for i in range(1, jumlah_baris + 1):
    print("*" * i)