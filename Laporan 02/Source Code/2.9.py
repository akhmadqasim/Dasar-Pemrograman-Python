nama = "Akhmad Qasim"  # Variable yang berisi string.
nim = 2211102441237  # Variable yang berisi interger.
tb = 165.5  # Variable yang berisi float.
a = 100  # Assign nilai untuk var a.
b = 50  # Assign nilai untuk var b.
c = 8  # Assign nilai untuk var c.
d = 2  # Assign nilai untuk var d.


print("__________Aritmatika__________")  # Aritmatika
a1 = a + b + c  # Operasi penambahan.
a2 = a - b - c  # Operasi pengurangan.
a3 = a * c  # Operasi perkalian.
a4 = a / b  # Operasi pembagian.
a5 = a % c  # Operasi modulo / sisa bagi.
a6 = a ** c  # Operasi perpangkatan.
a7 = a // b  # Operasi pembagian bulat.

print("a =", a, " | b =", b, " | c =", c)  # Menampilkan nilai dari setiap variable.
print("a + b + c =", a1)  # Menampilkan hasil operasi di variable a1.
print("a - b - c =", a2)  # Menampilkan hasil operasi di variable a2.
print("a * c =", a3)  # Menampilkan hasil operasi di variable a3.
print("a / b =", a4)  # Menampilkan hasil operasi di variable a4.
print("a % c =", a5)  # Menampilkan hasil operasi di variable a5.
print("a ** c =", a6)  # Menampilkan hasil operasi di variable a6.
print("a // b =", a7)  # Menampilkan hasil operasi di variable a7.


print("\n_____Operator Assignment_____")  # Operator Assignment
b1 = a  # Melakukan assign nilai dari variable a.
print("b1 =", b1)  # Menampilkan hasil operasi b1 menggunakan assignment.

b1 += 100  # Melakukan operasi pertambahan dengan metode assignment.
print("b1 += 100 =", b1)  # Menampilkan hasil operasi b1 menggunakan assignment.

b1 -= 50  # Melakukan operasi pengurangan dengan metode assignment.
print("b1 -= 50 =", b1)  # Menampilkan hasil operasi b1 menggunakan assignment.

b1 *= 2  # Melakukan operasi perkalian dengan metode assignment.
print("b1 *= 2 =", b1)  # Menampilkan hasil operasi b1 menggunakan assignment.

b1 /= 2  # Melakukan operasi pembagian dengan metode assignment.
print("b1 /= 2 =", b1)  # Menampilkan hasil operasi b1 menggunakan assignment.

b1 %= 40  # Melakukan operasi modulo dengan metode assignment.
print("b1 %= 40 =", b1)  # Menampilkan hasil operasi b1 menggunakan assignment.

b1 //= 3  # Melakukan operasi pembagian bulat/kebawah dengan metode assignment.
print("b1 //= 3 =", b1)  # Menampilkan hasil operasi b1 menggunakan assignment.

b1 **= 2  # Melakukan operasi perpangkatan dengan metode assignment.
print("b1 **= 2 =", b1)  # Menampilkan hasil operasi b1 menggunakan assignment.


print("\n____Operator Perbandingan____")  # Operator Perbandingan
c1 = b == a  # Membandingkan nilai yang sama.
c2 = b == c  # Membandingkan nilai yang sama.
c3 = b != a  # Membandingkan nilai yang tidak sama.
c4 = b != c  # Membandingkan nilai yang tidak sama.
c5 = b > a  # Membandingkan nilai yang lebih besar.
c6 = b > c  # Membandingkan nilai yang lebih besar.
c7 = b < a  # Membandingkan nilai yang lebih kecil.
c8 = b < c  # Membandingkan nilai yang lebih kecil.
c9 = b >= a  # Membandingkan nilai yang lebih besar sama dengan.
c10 = b >= c  # Membandingkan nilai yang lebih besar sama dengan.
c11 = b <= a  # Membandingkan nilai yang lebih kecil sama dengan.
c12 = b <= c  # Membandingkan nilai yang lebih kecil sama dengan.

print("a =", a, " | b =", b, " | c =", c)  # Menampilkan nilai dari setiap variable.
print("b == a =", c1)  # Menampilkan output dari hasil perbandingan variable c1.
print("b == c =", c2)  # Menampilkan output dari hasil perbandingan variable c2.
print("b != a =", c3)  # Menampilkan output dari hasil perbandingan variable c3.
print("b != c =", c4)  # Menampilkan output dari hasil perbandingan variable c4.
print("b > a =", c5)  # Menampilkan output dari hasil perbandingan variable c5.
print("b > c =", c6)  # Menampilkan output dari hasil perbandingan variable c6.
print("b < a =", c7)  # Menampilkan output dari hasil perbandingan variable c7.
print("b < c =", c8)  # Menampilkan output dari hasil perbandingan variable c8.
print("b >= a =", c9)  # Menampilkan output dari hasil perbandingan variable c9.
print("b >= c =", c10)  # Menampilkan output dari hasil perbandingan variable c10.
print("b <= a =", c11)  # Menampilkan output dari hasil perbandingan variable c11.
print("b <= c =", c12)  # Menampilkan output dari hasil perbandingan variable c12.


print("\n_______Operator Logika_______")  # Operator Logika
print("a =", a)  # Menampilkan nilai dari variable a.
d1 = a < 10 and a < 160  # Bernilai true apabila kedua nilai bernilai true dan bernilai false apabila salah satunya bernilai false.
d2 = a > 10 and a > 80  # Bernilai true apabila kedua nilai bernilai true dan bernilai false apabila salah satunya bernilai false.
d3 = a < 10 or a < 170  # Bernilai true apabila salah satu nilai bernilai true dan bernilai false apabila keduanya bernilai false.
d4 = a < 10 or a < 100  # Bernilai true apabila salah satu nilai bernilai true dan bernilai false apabila keduanya bernilai false.

print("a < 10 and a < 160 =", d1)  # Menampilkan output dari variable d1.
print("a > 10 and a > 80 =", d2)  # Menampilkan output dari variable d2.
print("a < 10 or a < 170 =", d3)  # Menampilkan output dari variable d3.
print("a < 10 or a < 100 =", d4)  # Menampilkan output dari variable d4.


print("\n_____Operator Identitas_____")  # Operator Identitas
e1 = a is b  # Melakukan operasi identitas dengan mengecek nilai yang sama.
e2 = a is not b  # Melakukan operasi identitas dengan mengecek nilai yang tidak sama.

print("a is b =", e1)  # Menampilkan output dari variable e1.
print("a is not b =", e2)  # Menampilkan output dari variable e2.


print("\n____Operator Keanggotaan____")  # Operator Keanggotaan
f1 = "a" in nama  # Mengecek apakah ada huruf a di dalam variable ${nama}.
f2 = "a" not in nama  # Mengecek apakah tidak ada huruf a di dalam variable ${nama}.

print("\"a\" in nama =", f1)  # Menampilkan output dari variable f1.
print("\"a\" not in nama =", f2)  # Menampilkan output dari variable f2.


print("\n______Operator Bitwise______")  # Operator Bitwise
g1 = c & d  # Operator AND “&” digunakan untuk membandingkan biner, bernilai true apabila dua-duanya bernilai 1 (true) dan bernilai false apabila salah satu bernilai 0 (false).
g2 = c | d  # Operator OR “|” digunakan untuk membandingkan biner, bernilai true apabila salah-satu bernilai 1 (true), atau keduanya bernilai 1 (true) dan false apabila keduanya bernilai 0 (false).
g3 = c ^ d  # Operator XOR “^” digunakan untuk membandingkan biner, bernilai true apabila salah satu bernilai 1 (true), dan false apabila keduanya 1 (true) ataupun 0 (false).
g4 = c << d  # Operator SHIFT LEFT “<<” digunakan untuk m-enggeser nilai biner ke kiri.
g5 = c >> d  # Operator SHIFT RIGHT “>>” digunakan untuk menggeser nilai biner ke kanan.

print("c & d =", g1)  # Menampilkan hasil dari operasi bitwise pada variable g1
print("c | d =", g2)  # Menampilkan hasil dari operasi bitwise pada variable g2
print("c ^ d =", g3)  # Menampilkan hasil dari operasi bitwise pada variable g3
print("c << d =", g4)  # Menampilkan hasil dari operasi bitwise pada variable g4
print("c >> d =", g5)  # Menampilkan hasil dari operasi bitwise pada variable g5