class Pekerja:
    pkTotal = 0

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Pekerja.pkTotal += 1

    def displayTotal(self):
        print("Total Pekerja %d" % Pekerja.pkTotal)

    def displayPekerja(self):
        print("Nama : ", self.nama, ", Gaji : ", self.gaji)


worker1 = Pekerja("Andi Akbar Soleh", 2_000_000)
worker1.displayPekerja()
