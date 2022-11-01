nama = {"Akhmad", "Qasim", 2211102441237}
nama.add('Teknik Informatika')
print(nama)

nama = {"Akhmad", "Qasim", 2211102441237}
nama.clear()
print(nama)

nama = {"Akhmad", "Qasim", 2211102441237}
nama_baru = nama.copy()
print(nama_baru)

nama = {"Akhmad", "Qasim", 2211102441237}
nama_2 = {"Akhmad", "Qasim", 2211102441239}
print(nama.difference(nama_2))

nama = {"Akhmad", "Qasim", 2211102441237}
nama.discard("Qasim")
print(nama)

nama = {"Akhmad", "Qasim", 2211102441237}
nama_2 = {"Akhmad", "Qasim",  2211102441212}
print(nama.intersection(nama_2))

nama = {"Akhmad", "Qasim", 2211102441237}
nama_2 = {"Akhmad", "Qasim", 2211102441212}
nama.intersection_update(nama_2)
print(nama)

nama = {"Akhmad", "Qasim", 2211102441237}
nama_2 = {"Akhmad", "Qasim", 2211102441212}
print(nama.isdisjoint(nama_2))

nama = {"Akhmad", "Qasim", 2211102441237}
nama_2 = {"Akhmad", "Qasim", 2211102441212}
print(nama.issuperset(nama_2))

nama = {"Akhmad", "Qasim", 2211102441237}
print(nama.pop())
print(nama)

nama = {"Akhmad", "Qasim", 2211102441237}
nama.remove("Akhmad")
print(nama)

nama = {"Akhmad", "Qasim", 2211102441237}
nama_2 = {"Akhmad", "Qasim", 2211102441212}
print(nama.symmetric_difference(nama_2))

nama = {"Akhmad", "Qasim", 2211102441237}
nama_2 = {"Akhmad", "Qasim", 2211102441212}
nama.symmetric_difference_update(nama_2)
print(nama)

nama = {"Akhmad", "Qasim", 2211102441237}
nama_2 = {"Akhmad", "Qasim", 2211102441212}
print(nama.union(nama_2))

nama = {"Akhmad", "Qasim", 2211102441237}
nama_2 = {"Akhmad", "Qasim", 2211102441212}
nama.update(nama_2)
print(nama)
