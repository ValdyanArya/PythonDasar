import PySimpleGUI as sg

def simpan_data(values):
    nama_lengkap = values['nama_lengkap']
    tanggal_lahir = values['tanggal_lahir']
    asal_sekolah = values['asal_sekolah']
    nisn = values['nisn']
    nama_ayah = values['nama_ayah']
    nama_ibu = values['nama_ibu']
    nomor_telepon = values['nomor_telepon']
    alamat = values['alamat']

    window['hasil'].update("Data siswa telah disimpan!")

sg.theme('LightGray1')  

layout = [
    [sg.Text('Data Siswa Baru', font=('Helvetica', 24))],  # Judul dengan ukuran besar
    [sg.Text('Nama Lengkap :', font=('Helvetica', 16)), sg.InputText(key='nama_lengkap', font=('Helvetica', 16))],
    [sg.Text('Tanggal Lahir   :', font=('Helvetica', 16)), sg.InputText(key='tanggal_lahir', font=('Helvetica', 16))],
    [sg.Text('Asal Sekolah    :', font=('Helvetica', 16)), sg.InputText(key='asal_sekolah', font=('Helvetica', 16))],
    [sg.Text('NISN                :', font=('Helvetica', 16)), sg.InputText(key='nisn', font=('Helvetica', 16))],
    [sg.Text('Nama Ayah      :', font=('Helvetica', 16)), sg.InputText(key='nama_ayah', font=('Helvetica', 16))],
    [sg.Text('Nama Ibu         :', font=('Helvetica', 16)), sg.InputText(key='nama_ibu', font=('Helvetica', 16))],
    [sg.Text('Nomor Telepon:', font=('Helvetica', 16)), sg.InputText(key='nomor_telepon', font=('Helvetica', 16))],
    [sg.Text('Alamat             :', font=('Helvetica', 16)), sg.InputText(key='alamat', font=('Helvetica', 16))],
    [sg.Button('Simpan Data', font=('Helvetica', 16))],
    [sg.Text('', size=(40, 1), font=('Helvetica', 18), key='hasil')],
]

window = sg.Window('Form Data Siswa Baru', layout, resizable=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == 'Simpan Data':
        simpan_data(values)

window.close()
