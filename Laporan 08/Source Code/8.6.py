print("Clear :")
bio = {
    "nama": "Akhmad Qasim",
    "nim": 2211102441237
}
bio.clear()
print(bio)

print("\nCopy :")
bio = {
    "nama": "Akhmad Qasim",
    "nim": 2211102441237
}
a2 = bio.copy()
print(a2)

print("\nFormkeys :")
a3 = ("nama", "nim", "kelas")
b3 = "null"
c3 = dict.fromkeys(a3, b3)
print(c3)

print("\nGet :")
a4 = bio.get("nama")
print(a4)

print("\n Items :")
a5 = bio.items()
print(a5)

print("\n Keys :")
a6 = bio.keys()
print(a6)

print("\nPop :")
print(bio.pop("nim"))
print(bio)

print("\nSetdefault :")
a8 = bio.setdefault("nim", 2211)
print(a8)

print("\nUpdate :")
bio.update({"nim": 2211102441237})
print(bio)

print("\nValues :")
a10 = bio.values()
print(a10)
