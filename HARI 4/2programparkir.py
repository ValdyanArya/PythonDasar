import tkinter as tk
from datetime import datetime, timedelta

# Database sederhana untuk menyimpan data nomor plat kendaraan
database = {
    "ABC123": {
        "nama_kendaraan": "Honda Civic",
        "waktu_masuk": None,
        "waktu_keluar": None,
        "biaya_per_jam": 10,  # Biaya parkir per jam
        "pelanggaran": [],
    },
    "XYZ789": {
        "nama_kendaraan": "Toyota Corolla",
        "waktu_masuk": None,
        "waktu_keluar": None,
        "biaya_per_jam": 10,  # Biaya parkir per jam
        "pelanggaran": [],
    },
    # Tambahkan lebih banyak data sesuai kebutuhan
}

def cari_nomor_plat():
    nomor_plat = nomor_plat_entry.get()
    if nomor_plat in database:
        kendaraan = database[nomor_plat]
        nama_kendaraan = kendaraan["nama_kendaraan"]
        if kendaraan["waktu_masuk"] is not None and kendaraan["waktu_keluar"] is not None:
            durasi_parkir = kendaraan["waktu_keluar"] - kendaraan["waktu_masuk"]
            biaya_per_jam = kendaraan["biaya_per_jam"]
            biaya_parkir = (durasi_parkir.seconds // 3600) * biaya_per_jam
            hasil_label.config(text=f"Nomor Plat: {nomor_plat}\nNama Kendaraan: {nama_kendaraan}\nWaktu Masuk: {kendaraan['waktu_masuk']}\nWaktu Keluar: {kendaraan['waktu_keluar']}\nBiaya Per Jam: {biaya_per_jam} IDR\nBiaya Parkir: {biaya_parkir} IDR\nPelanggaran: {', '.join(kendaraan['pelanggaran'])}")
        else:
            hasil_label.config(text=f"Nomor Plat: {nomor_plat}\nNama Kendaraan: {nama_kendaraan}\nWaktu Masuk: Belum Dicatat\nWaktu Keluar: Belum Dicatat")
    else:
        hasil_label.config(text="Nomor Plat tidak ditemukan.")

def catat_waktu_masuk():
    nomor_plat = nomor_plat_entry.get()
    if nomor_plat in database:
        database[nomor_plat]["waktu_masuk"] = datetime.now()
        hasil_label.config(text="Waktu Masuk berhasil dicatat.")
    else:
        hasil_label.config(text="Nomor Plat tidak ditemukan.")

def catat_waktu_keluar():
    nomor_plat = nomor_plat_entry.get()
    if nomor_plat in database:
        database[nomor_plat]["waktu_keluar"] = datetime.now()
        hasil_label.config(text="Waktu Keluar berhasil dicatat.")
    else:
        hasil_label.config(text="Nomor Plat tidak ditemukan.")

def tambah_pelanggaran():
    nomor_plat = nomor_plat_entry.get()
    pelanggaran = pelanggaran_entry.get()
    if nomor_plat in database:
        database[nomor_plat]["pelanggaran"].append(pelanggaran)
        hasil_label.config(text="Pelanggaran berhasil dicatat.")
    else:
        hasil_label.config(text="Nomor Plat tidak ditemukan.")

app = tk.Tk()
app.title("Aplikasi Parkir")
app.attributes('-fullscreen', True)  # Menampilkan aplikasi dalam mode fullscreen

nomor_plat_label = tk.Label(app, text="Masukkan Nomor Plat:")
nomor_plat_label.pack()

nomor_plat_entry = tk.Entry(app)
nomor_plat_entry.pack()

cari_button = tk.Button(app, text="Cari", command=cari_nomor_plat)
cari_button.pack()

waktu_masuk_button = tk.Button(app, text="Catat Waktu Masuk", command=catat_waktu_masuk)
waktu_masuk_button.pack()

waktu_keluar_button = tk.Button(app, text="Catat Waktu Keluar", command=catat_waktu_keluar)
waktu_keluar_button.pack()

biaya_per_jam_label = tk.Label(app, text="Biaya Per Jam: 10 IDR")  # Ganti 10 dengan biaya per jam yang sesuai
biaya_per_jam_label.pack()

pelanggaran_label = tk.Label(app, text="Catat Pelanggaran:")
pelanggaran_label.pack()

pelanggaran_entry = tk.Entry(app)
pelanggaran_entry.pack()

tambah_pelanggaran_button = tk.Button(app, text="Tambah Pelanggaran", command=tambah_pelanggaran)
tambah_pelanggaran_button.pack()

hasil_label = tk.Label(app, text="")
hasil_label.pack()

app.mainloop()

