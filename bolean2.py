#setting variable
n1  = input("masukkan nim")
n2  = input("masukkan nama lengkap")
n3  = input("masukkan kelas")
n4  = input("masukkan nama prodi")

#setting variable nilai
b_ind  = int(input("Nilai Bahasa indonesia  :"))
b_ing  = int(input("Nilai Bahasa Inggris    :"))
pd     = int(input("Nilai Pemrograman Dasar"))
mtk    = int(input("Nilai "))
kal1   = int(input("Nilai"))

#perhitungan
rata = (bhs_indo+bhs_ing+pd+mtk+kall/5)

if(rata>0 and rata <=60)
grade_rata = ("c")
elif(rata >60 and rata <=75)
grade_rata = ("b")
elif(rata >75 and rata <=85)
grade_rata = ("ab")
elif(rata >85 and rata <=95)
grade_rata = ("a")
else: grade_rata =("grade anda tidak ditemukan! ")

#menampilkan
print("----------")
print(" kartu hasil studi ")
print(" nim :",nim)
print(" nama :",nama)
print(" kelas :",kelas)
print(" program studi :",prodi)
print("----------")
print("no nama matkul   nilai  grade")
print("----------")
print("1.  bhs indo",bhs_ind)
print("2.  bhs ing",bhs_ing)
print("3.  pemrograman",pd)
print("4.  matematika",mtk)
print("5.  kalkulus",kall)
print("----------")
print("rata-rata  ",rata," ",grade_rata)
print
