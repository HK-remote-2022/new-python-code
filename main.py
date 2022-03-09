"""
Ini adalah demo projek pertama dengan Python
Semua sinteaksi dasar pemrograman terdiri dari
1. Sekuensial : Langkah berurutan
2. Percabangan : Langkah melompat jika kondisi terpenuhi
3. Pengulangan : mengulang langkah yang sama berkali kali selama/sampai kondisi terpenuhi
"""

# Sekuensial
print("hello world")
print("My Name is Hendra")
print('Ibu Berkata,"pulang jangan malam malam ya jangan lebih dari jam 9 malam"')
print('hendra menjawab,"oke bu, Hendra pulang pagi ya"')
print('ibu berkata, "bagus, mendingan ga usah pulang aja ya!!"')
print('hendra menjawab,"iya deh bu, liat nanti aja ya"')

#Percabangan

jam_pulang_main = 8

if jam_pulang_main < 9:
    print("Hendra cek jam berapa sekarang, ternyata masih bisa pulang sebelum jam 9")
    print("Hendra pulang kerumah ")
else:
    print("Hendra liat jam ternyata sudah lewat jam 9 malam")
    print("Hendra tidak jadi pulang dan nginep dirumah teman sampai pagi")


