nilai = float(input("Berapa tinggi badan anda? "))
if nilai < 154 :
    print("terlalu pendek")
elif nilai >= 154 and nilai <= 165 :
    print("cukup ideal")
elif nilai >= 166 and nilai <= 170 :
    print("Ideal")
elif nilai >= 171 and nilai <= 176 :
    print("cukup tinggi")
else :
    print("Abnormal/Berlebih")