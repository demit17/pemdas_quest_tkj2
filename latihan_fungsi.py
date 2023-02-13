'''Fungsi pada python didefinisikan dengan def'''

'''def nama_fungsi():'''

def salam():
    print("Assalamu'alaikum !! Akhi Ukhty")

salam()
salam()
salam()

'''Buatlah sebuah fungsi versi kalian'''

def jawab():
    print("wa'alaikumsalam")

jawab()
jawab()
jawab()

'''Fungsi dengan parameter'''
'''def nama_fungsi(p1, p2)'''

def say_hi(nama):
    print("Halo perkenalkan nama saya", nama)

say_hi("Jawir")
say_hi("Reog")

'''Buatlah fungsi dengan 3 Parameter'''

def hy(nama, umur, kelas):

    print("halo nama saya:",nama)
    print("umur:",umur)
    print("kelas:",kelas)

hy("dhafin","16","10")
hy("dayat","17","10")
hy("sadam","17","10")

'''buatlah program menghitung luas bangun datar menggunakan fungsi. Gunakan parameter
- segitga
-persegi panjang
'''

def segitga(alas,tinggi):
    luas = alas*tinggi/2
    print("luas segitiga adalah:%i cm"%luas)
segitga(15,20)

def persegi_panjang(panjang,lebar):
    luas = panjang*lebar
    print("luas persegi panjang adalah:%i"%luas)

persegi_panjang(10,20)