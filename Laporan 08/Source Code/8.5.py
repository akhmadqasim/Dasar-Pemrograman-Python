bio = {
    "nama": "Akhmad Qasim",
    "nim": 2211102441237
}

print("Perulangan pada Index :")
for x in bio:
    print(x)

print("\nAkses Value pada Perulangan :")
for x in bio:
    print(bio[x])

print("\nPerulangan pada Value :")
for x in bio.values():
    print(x)

print("\nPerulangan pada Item/Elemen :")
for x, y in bio.items():
    print(x, y)
