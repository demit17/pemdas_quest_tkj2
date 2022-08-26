input("masukan nama depan anda= ")
input("masukan nama belakang anda= ")

print (",persegi panjang")

panjang = int(input("masukan nilai panjang= "))
lebar = int(input("masukan nilai lebar= "))
luas_pp = panjang * lebar
print("masukan nilai" , luas_pp)

print (",segitiga")

alas = int(input("masukan nilai alas= "))
tinggi = int(input("masukan nilai tinggi= "))
luas_segitiga = 1/2 * alas * tinggi
print("masukan nilai" , luas_segitiga)

print (",jajar genjang")

alas = int(input("masukan nilai alas= "))
tinggi = int(input("masukan nilai tinggi= "))
luas_jj = alas * tinggi
print("masukan nilai" , luas_jj)

print (",lingkaran")

r = int(input("masukan nilai jari jari= "))
luas_l = r * r * 3.14
print("masukan nilai" , luas_l)