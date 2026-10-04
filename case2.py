punya_uang = True
makanan_tersedia = True
toko_buka = True

beli_makanan = punya_uang and makanan_tersedia and toko_buka

if beli_makanan:
    print("Bisa membeli makanan")
else:
    print("Tidak bisa membeli makanan")