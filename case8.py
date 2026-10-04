motor = True
mobil = False

transportasi = motor ^ mobil

if transportasi:
    print("Pilihan transportasi valid")
else:
    print("Pilihan transportasi tidak valid")