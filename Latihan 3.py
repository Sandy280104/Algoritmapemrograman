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

# Penentuan grade matakuliah
if b_ind <= 60:
    g_ind = "D"
elif b_ind <= 70:
    g_ind = "C"
elif b_ind <= 80:
    g_ind = "B"
elif b_ind <= 85:
    g_ind = "AB"
elif b_ind <= 95:
    g_ind = "A"
else:
    g_ind = "Grade Anda tidak ditemukan!"

if b_ing <= 60:
    g_ing = "D"
elif b_ing <= 70:
    g_ing = "C"
elif b_ing <= 80:
    g_ing = "B"
elif b_ing <= 85:
    g_ing = "AB"
elif b_ing <= 95:
    g_ing = "A"
else:
    g_ing = "Grade Anda tidak ditemukan!"

if pd <= 60:
    g_pd = "D"
elif pd <= 70:
    g_pd = "C"
elif pd <= 80:
    g_pd = "B"
elif pd <= 85:
    g_pd = "AB"
elif pd <= 95:
    g_pd = "A"
else:
    g_pd = "Grade Anda tidak ditemukan!"

if mtk <= 60:
    g_mtk = "D"
elif mtk <= 70:
    g_mtk = "C"
elif mtk <= 80:
    g_mtk = "B"
elif mtk <= 85:
    g_mtk = "AB"
elif mtk <= 95:
    g_mtk = "A"
else:
    g_mtk = "Grade Anda tidak ditemukan!"

if kal1 <= 60:
    g_kal1 = "D"
elif kal1 <= 70:
    g_kal1 = "C"
elif kal1 <= 80:
    g_kal1 = "B"
elif kal1 <= 85:
    g_kal1 = "AB"
elif kal1 <= 95:
    g_kal1 = "A"
else:
    g_kal1 = "Grade Anda tidak ditemukan!"

# Penentuan grade rata-rata
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
print("Nama Matkul\tnilai\nilai matakuliah\tGrade")
print("----------")
print("1. Bahasa Indonesia\t", b_ind, "\t", g_ind)
print("2. Bahasa Inggris\t", b_ing, "\t", g_ing)
print("3. Pemrograman Dasar\t", pd, "\t", g_pd)
print("4. Matematika\t\t", mtk, "\t", g_mtk)
print("5. Kalkulus\t\t", kal1, "\t", g_kal1)
print("----------")
print("Rata-rata\t", rata, "\t", grade_rata)
