import tkinter as tk

def hitung_total():
    harga_per_unit = float(harga_per_unit_entry.get())
    kuantitas = int(kuantitas_entry.get())
    total = harga_per_unit * kuantitas
    total_label.config(text=f"Total: {total}")

app = tk.Tk()
app.title("Kalkulator Harga")

harga_label = tk.Label(app, text="Harga:")
harga_label.pack()

harga_per_unit_entry = tk.Entry(app)
harga_per_unit_entry.pack()

kuantitas_label = tk.Label(app, text="Kuantitas:")
kuantitas_label.pack()

kuantitas_entry = tk.Entry(app)
kuantitas_entry.pack()

hitung_button = tk.Button(app, text="Hitung Total", command=hitung_total)
hitung_button.pack()

total_label = tk.Label(app, text="")
total_label.pack()

app.mainloop()
