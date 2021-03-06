"""
List
"""
daftar_buku = ["Bulughul Maram", "Syarah Akidah Alusunnah Wal Jamaah", "Riyadus Sholihin", "Sirah Nabawiyah"]
print('tampilkan variable daftar buku')
print(daftar_buku)

print("\nproses semua dengan for in")
for buku in daftar_buku:
    print(buku)

print("\ntampilkan isi daftar_buku pada indeks tertentu")
print (daftar_buku[0])
print (daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [72, "doraemon", 17.5, -36]
print('\nTampilkan dengan for in range dimana tipe data tiap element berbeda beda')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nkembalikan nilai awal daftar_buku")
daftar_buku = ["Bulughul Maram", "Syarah Akidah Alusunnah Wal Jamaah", "Riyadus Sholihin", "Sirah Nabawiyah"]
print('\ntambah 1 buku baru')
daftar_buku.append("buku tembus kerja remot")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear List')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti element pertama')
daftar_buku = ["Bulughul Maram", "Syarah Akidah Alusunnah Wal Jamaah", "Riyadus Sholihin", "Sirah Nabawiyah"]
daftar_buku [0] = 'Bulughul Maram Jilid 2'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil element Kedua')
buku = daftar_buku.pop(0)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\nPop')
daftar_buku = ["Bulughul Maram", "Syarah Akidah Alusunnah Wal Jamaah", "Riyadus Sholihin", "Sirah Nabawiyah"]
daftar_buku.pop(2)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

