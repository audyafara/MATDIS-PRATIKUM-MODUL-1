sudah_mandi = True
sudah_sarapan = True
membawa_tas = True

pergi_kuliah = sudah_mandi and sudah_sarapan and membawa_tas

if pergi_kuliah:
    print("Bisa pergi kuliah")
else:
    print("Belum bisa pergi kuliah")