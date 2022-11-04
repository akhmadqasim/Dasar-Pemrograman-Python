formatData = ["nama", "prodi", "nim", "angkatan"]
data = ["Akhmad Qasim", "S1 Teknik Informatika", 2211102441237, 2022]
dic = {}

for x, y in zip(formatData, data):
    dic[x] = y

nama = dic["nama"]
prodi = dic["prodi"]
nim = dic["nim"]
angkatan = dic["angkatan"]

userInput = "Akhmad Qasim"
nimInput = 2211102441237

if userInput == nama and nimInput == nim:
    print("Nama :", nama)
    print("\nProdi :", prodi)
    print("\nNIM :", nim)
    print("\nAngkatan :", angkatan)
else:
    print("Anda belum terdaftar")
