print('\nPerintah Del')
daftar_buku = ["Bulughul Maram", "Syarah Akidah Alusunnah Wal Jamaah", "Riyadus Sholihin", "Sirah Nabawiyah"]
del daftar_buku[2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan List Comprehension')
daftar_buku = ["Bulughul Maram", "Syarah Akidah Alusunnah Wal Jamaah", "Riyadus Sholihin", "Sirah Nabawiyah"]
del daftar_buku[0:12] #START:END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan List Comprehension start')
daftar_buku = ["Bulughul Maram", "Syarah Akidah Alusunnah Wal Jamaah", "Riyadus Sholihin", "Sirah Nabawiyah"]
del daftar_buku[0::2] #START:END:STEP
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat List Baru')
daftar_buku = ["Bulughul Maram", "Syarah Akidah Alusunnah Wal Jamaah", "Riyadus Sholihin", "Sirah Nabawiyah"]
daftar_buku_baru = daftar_buku[:]
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat List Baru')
daftar_buku = ["Bulughul Maram", "Syarah Akidah Alusunnah Wal Jamaah", "Riyadus Sholihin", "Sirah Nabawiyah"]
daftar_buku_baru = daftar_buku[:]
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat List Baru Dengan Comprehension Ganjil')
daftar_buku = ["1. Bulughul Maram", "2. Syarah Akidah Alusunnah Wal Jamaah", "3. Riyadus Sholihin", "4. Sirah Nabawiyah"]
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat List Baru Dengan Comprehension Genap')
daftar_buku = ["1. Bulughul Maram", "2. Syarah Akidah Alusunnah Wal Jamaah", "3. Riyadus Sholihin", "4. Sirah Nabawiyah"]
daftar_buku_baru = daftar_buku[1::2] #START STOP STEP
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat List Baru Dengan Comprehension urutan genap')
daftar_buku = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
daftar_buku_baru = daftar_buku[1:-1:2] #START STOP STEP
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])