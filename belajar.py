nama = input("Nama kamu: ")
umur = int(input("Umur kamu: "))
kota = input("Kota kamu: ")

print("Halo,", nama + "!")
print("umur kamu", umur, "tahun.")
print("Saya", nama + ",", "umur", umur, "tahun,", "dan saya tinggal di", kota + ".")

if umur >= 18:
    print("kamu sudah dewasa.")
else:
    print("kamu masih di bawah umur.")