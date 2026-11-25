def sapa(nama):
    return "Halo, " + nama

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def total_harga(jumlah, harga=3500):
    return jumlah * harga

print(sapa("Rahma"))
print("Luas:", luas_persegi_panjang(6, 4))
print("Total harga:", total_harga(9))
print("Total harga promo:", total_harga(9, 3000))
