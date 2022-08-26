print ("balok")

panjang = int(input("masukan nilai panjang= "))
lebar = int(input("masukan nilai lebar= "))
tinggi = int(input("masukan nilai tinggi= "))
volume_b = panjang * lebar * tinggi
print ("volume balok adalah= " , volume_b)

print ("limas")

luas_alas_persegi = int(input("masukan nilai luas alas persegi= "))
tinggi = int(input("masukan nilai tinggi= "))
volume_ling = (1/3 * luas_alas_persegi) * tinggi

print("nilai volume limas adalah" , volume_ling)

print ("tabung")

luas_alas_lingkaran = int(input("masukan nilai luas alas lingkaran= "))
tinggi = int(input("masukan nilai tinggi= "))

volume_ling = luas_alas_lingkaran * tinggi
print("nilai volume tabung adalah" , volume_ling)

print ("program konversi nilai mata uang")

kursDolar = 14591
rupiah = float(input("masukan nilai mata uang rupiah= "))
rupToDol = rupiah / kursDolar
dolDecimal = round(rupToDol, 2)
print("Rp.",rupiah, "==> Dolar", dolDecimal)