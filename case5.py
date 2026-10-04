uang_tunai = False
saldo_ewallet = True

bisa_bayar = uang_tunai or saldo_ewallet

if bisa_bayar:
    print("Bisa membayar belanja")
else:
    print("Tidak bisa membayar belanja")