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