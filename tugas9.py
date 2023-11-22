def profil(nama, alamat, gender, umur, hobi):
    print("nama saya adalah", nama)
    print("alamat saya di", alamat)
    print("gender saya adalah", gender)
    print("umur saya adalah", umur)
    print("hobi saya adalah", hobi)
profil("fadhil", "bogor", "lakilaki", "18", "olahraga")

print()
def cek_kelulusan(nilai):
    if nilai < 60:
        print("Gagal")
    elif 61 <= nilai <= 70:
        print("Baik")
    elif 71 <= nilai <= 80:
        print("Sangat Baik")
    elif 81 <= nilai <= 100:
        print("Istimewa")
    
    else:
        print("Tidak Lulus")
cek_kelulusan(60)
print()
def ganjil(angka):
    for i in range(1, angka + 1, 2):
        print(i)
ganjil(100)