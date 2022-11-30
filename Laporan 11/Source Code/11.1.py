# Membuat cetak biru pekerja
class Pekerja:
    # Membuat properti pkTotal bernilai 0
    pkTotal = 0

    # Membuat konstruktor
    # __init__ fungsi khusus yang akan dipanggil saat objek dibuat
    # Parameter self adalah referensi ke objek saat ini
    def __init__(self, nama, gaji):
        # Membuat properti nama dan menerima nilai dari parameter nama
        self.nama = nama
        # Membuat properti gaji dan menerima nilai dari parameter gaji
        self.gaji = gaji
        # Membuat properti pkTotal bertambah 1
        Pekerja.pkTotal += 1

    # Membuat fungsi yang menampilkan jumlah pekerja
    def displayTotal(self):
        print("Total Pekerja %d" % Pekerja.pkTotal)

    # Membuat fungsi yang menampilkan nama dan gaji pekerja
    def displayPekerja(self):
        print("Nama : ", self.nama, ", Gaji : ", self.gaji)
