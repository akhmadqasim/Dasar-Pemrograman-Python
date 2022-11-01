dic = {"nama": "Akhmad Qasim", "prodi": "S1 TI", "nim": "2211102441237", "angkatan": "2022"}

nama = dic["nama"]
prodi = dic["prodi"]
nim = dic["nim"]
angkatan = dic["angkatan"]

userInput = "Akhmad Qasim"
nimInput = "2211102441237"

if userInput == dic["nama"] and nimInput == dic["nim"]:
    print("Nama :", nama)
    print("\nProdi :", prodi)
    print("\nNIM :", nim)
    print("\nAngkatan :", angkatan)
else:
    print("Anda belum terdaftar")
