from PIL import Image, ImageDraw

# Membuat gambar kosong dengan ukuran tertentu
width, height = 400, 400
img = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(img)

# Menggambar persegi panjang (merah)
draw.rectangle([50, 50, 200, 150], fill='red')

# Menggambar segitiga (kuning)
draw.polygon([(250, 50), (350, 50), (300, 150)], fill='yellow')

# Menggambar trapesium (hijau)
draw.polygon([(50, 200), (100, 200), (150, 250), (30, 250)], fill='green')

# Menggambar jajaran genjang (biru)
draw.polygon([(200, 200), (300, 200), (250, 300), (150, 300)], fill='blue')

# Menggambar segilima (ungu)
draw.polygon([(300, 200), (375, 250), (325, 325), (250, 350), (175, 325)], fill='purple')

# Menyimpan gambar sebagai file
img.save('bangun_datar.png')

# Menampilkan gambar (opsional)
img.show()
