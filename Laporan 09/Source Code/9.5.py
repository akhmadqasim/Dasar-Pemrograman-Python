# Fungsi lambda untuk menggandakan angka dengan dikali 2
gandakan_angka = lambda angka: (angka * 2)
# Fungsi lambda untuk melakukan pemangkatan angka dengan pangkat 2
pangkatkan_angka = lambda angka: (angka ** 2)
# Fungsi lambda untuk mengecek apakah angka lebih kecil sama dengan 5
# Nilai balikkan berupa boolean
cek_bilangan_genap = lambda angka: angka <= 5
# Fungsi lambda untuk mengembalikan nilai berupa string "Akhmad Qasim"
hello = lambda: "Akhmad Qasim"
# Mengeluarkan output dari fungsi lambda hello()
print(hello())
# Mengeluarkan output dari fungsi lambda gandakan_angka()
print(gandakan_angka(5))
# Mengeluarkan output dari fungsi lambda pangkatkan_angka()
print(cek_bilangan_genap(7))
# Membuat list baru dengan nama angka_ajaib
angka_ajaib = [1, 2, 3, 4, 5, 6, 7, 8]
# Membuat list baru dan menggandakan setiap angka pada list angka_ajaib
print(list(map(lambda angka: (angka * 2), angka_ajaib)))
# Membuat list baru dan memangkatkan setiap angka pada list angka_ajaib
print(list(map(lambda angka: (angka ** 2), angka_ajaib)))
# Membuat list baru dan menyaring angka yang lebih kecil sama dengan 5
print(list(filter(lambda angka: angka <= 5, angka_ajaib)))
