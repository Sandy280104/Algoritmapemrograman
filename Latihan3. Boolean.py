# Input
n1 = input("Masukkan nim: ")
n2 = input("Masukkan nama lengkap: ")
n3 = input("Masukkan kelas: ")
n4 = input("Masukkan nama prodi: ")

# Input nilai
b_ind = int(input("Nilai Bahasa Indonesia: "))
b_ing = int(input("Nilai Bahasa Inggris: "))
pd = int(input("Nilai Pemrograman Dasar: "))
mtk = int(input("Nilai Matematika: "))
kal1 = int(input("Nilai Kalkulus: "))

# Perhitungan rata-rata
rata = (b_ind + b_ing + pd + mtk + kal1) / 5

# Penentuan grade
if rata <= 60:
    grade_rata = "C"
elif rata <= 75:
    grade_rata = "B"
elif rata <= 85:
    grade_rata = "AB"
elif rata <= 95:
    grade_rata = "A"
else:
    grade_rata = "Grade Anda tidak ditemukan!"

# Menampilkan hasil
print("----------")
print("Kartu Hasil Studi")
print("NIM:", n1)
print("Nama:", n2)
print("Kelas:", n3)
print("Program Studi:", n4)
print("----------")
print("Nama Matkul\tNilai\tGrade")
print("----------")
print("1. Bahasa Indonesia\t", b_ind)
print("2. Bahasa Inggris\t", b_ing)
print("3. Pemrograman Dasar\t", pd)
print("4. Matematika\t\t", mtk)
print("5. Kalkulus\t\t", kal1)
print("----------")
print("Rata-rata\t", rata, "\t", grade_rata)
