"""
Program Perulangan Membaca Buku Dengan While Sampai Paham
"""
jumlah_buku = 10
print('Ibu Berkata "baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca = 0
print(f"jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}")

while jumlah_buku_yang_sudah_dibaca < jumlah_buku:
    jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1
    print(f'buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca')

print(f'jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

print("total buku yang ada =", jumlah_buku)