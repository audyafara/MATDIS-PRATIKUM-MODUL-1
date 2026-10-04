kendaraan_pribadi = False
kendaraan_umum = True

bisa_ke_kampus = kendaraan_pribadi or kendaraan_umum

if bisa_ke_kampus:
    print("Bisa pergi ke kampus")
else:
    print("Tidak bisa pergi ke kampus")