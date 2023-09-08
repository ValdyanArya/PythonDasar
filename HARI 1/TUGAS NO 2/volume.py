import math  # Import modul math untuk menggunakan pi

# Fungsi untuk menghitung volume tabung
def volume_tabung(jari_jari, tinggi):
    return math.pi * jari_jari**2 * tinggi

# Fungsi untuk menghitung volume balok
def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

# Input data untuk tabung
jari_jari_tabung = float(input("Masukkan jari-jari tabung: "))
tinggi_tabung = float(input("Masukkan tinggi tabung: "))

# Input data untuk balok
panjang_balok = float(input("Masukkan panjang balok: "))
lebar_balok = float(input("Masukkan lebar balok: "))
tinggi_balok = float(input("Masukkan tinggi balok: "))

# Menghitung volume tabung
volume_tabung_result = volume_tabung(jari_jari_tabung, tinggi_tabung)

# Menghitung volume balok
volume_balok_result = volume_balok(panjang_balok, lebar_balok, tinggi_balok)

# Menampilkan hasil
print("Volume Tabung adalah:", volume_tabung_result)
print("Volume Balok adalah:", volume_balok_result)
