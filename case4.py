punya_wifi = False
punya_kuota = True

bisa_menghubungi = punya_wifi or punya_kuota

if bisa_menghubungi:
    print("Bisa menghubungi teman")
else:
    print("Tidak bisa menghubungi teman")