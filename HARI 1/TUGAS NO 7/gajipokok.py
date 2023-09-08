nama = input("Masukkan nama karyawan: ")
GajiPokok = float(input("Masukkan Gaji Pokok: "))

tunjangan = 0.20 * GajiPokok
pajak = 0.15 * (GajiPokok + tunjangan)
GajiBersih = GajiPokok + tunjangan - pajak

print(nama)
print("Gaji Pokok:", GajiPokok)
print("Gaji Bersih:", GajiBersih)