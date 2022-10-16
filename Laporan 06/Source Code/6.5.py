nama = ["Akhmad", "Qasim"]
nim = [22, 11, 10, 24, 41, 23, 7]

print(nama)
print(nim)

print("\n>>> nim.append(11)")
nim.append(11)
print("nim :", nim)

print("\n>>> nama.clear()")
nama.clear()
print("nama :", nama)

print("\n>>> nama = nim.copy()")
nama = nim.copy()
print("nama :", nama)

print("\n>>> nim.count(11)")
print("nim :", nim.count(11))

print("\n>>> nama.extend(nim)")
nama.extend(nim)
print("nama :", nama)

print("\n>>> nama.index(41)")
print("nama :", nama.index(41))

print("\n>>> nama.insert(0, 32)")
nama.insert(0, 32)
print("nama :", nama)

print("\n>>> nama.pop")
print(nama.pop())
print("nama :", nama)

print("\n>>> nama.remove(41)")
nama.remove(41)
print("nama :", nama)

print("\n>>> nama.reverse()")
nama.reverse()
print("nama :", nama)

print("\n>>> nama.sort()")
nama.sort()
print("nama :", nama)
