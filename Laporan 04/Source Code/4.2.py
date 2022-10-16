kelas = input("Kelas berapa anda sekarang? ")
kelas = int(kelas)
if kelas <= 1 and kelas <= 6 :
    print("Anda masih SD")
elif kelas <= 7 and kelas <= 9:
    print("Anda sudah SMP")
elif kelas >= 10 and kelas <= 12 :
    print("Anda SMA/SMK")
elif kelas >= 13:
    print("Anda sudah lulus sekolah")