import PySimpleGUI as sg

layout = [[sg.Button('Klik Saya')]]

window = sg.Window("Contoh Program PySimpleGUI", layout)

while True:
    event, values = window.read()
    if event == "Klik Saya":
        print("Tombol Diklik")

window.close()