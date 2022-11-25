# Membuat fungsi rekursif
def rekursif(angka):
    # Jika angka lebih besar dari -5
    if angka > -5:
        # Maka cetak variable angka
        print(angka)
        # Angka dikurangi 1
        angka = angka - 1
        # Panggil fungsi rekursif dengan parameter angka
        rekursif(angka)
    # Jika angka lebih kecil dari -5
    else:
        # Cetak angka
        print(angka)


# Masukkan angka dan diubah menjadi integer
masukkan = int(input("masukkan angka: "))
# Panggil fungsi rekursif dengan parameter masukkan
rekursif(masukkan)
