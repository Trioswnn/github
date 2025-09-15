
while True:
    judul = "Program konversi Panjang"

    print("\n","="*len(judul),sep="")
    print(judul)
    print("="*len(judul),"\n")

    satuan = {
        "1": ("Kilometer (km)", 1000),
        "2": ("Hektometer (hm)", 100),
        "3": ("Dekameter (dam)", 10),
        "4": ("Meter (m)", 1),
        "5": ("Desimeter (dm)", 0.1),
        "6": ("Centimeter (cm)", 0.01),
        "7": ("Milimeter (mm)", 0.001)
    }

    for key, values in satuan.items():
        print(f"{key}. {values[0]}")

    nilai = float(input("\nMasukan angka yang ingin dikonversi : "))
    asal = input("Satuan asal (1-7): ")
    tujuan = input("Satuan tujuan (1-7): ")

    if asal not in satuan or tujuan not in satuan:
        print("\nMasukan input yang valid!!!")
        continue

    faktor_asal = satuan[asal][1]
    faktor_tujuan = satuan[tujuan][1]

    konversi = nilai * faktor_asal / faktor_tujuan
    print(f"\nHasil konversi satuan panjang dari {nilai} {satuan[asal][0]} ke {satuan[tujuan][0]} adalah {konversi:.2f} {satuan[tujuan][0]}\n")

    nos = input("Apakah kamu masih ingin lanjut ? (y/n) : ")

    if nos == "y":
        continue
    elif nos == "n":
        break

print("Program telah berakhir, terimakasiiih...")

while True:
    rate = input("\nSeberapa kamu menyukai program ini ? (1-5): ")

    if rate in ["1","2","3","4"]:
        print("Hanya menerima rate 5 wkwk")
        continue
    elif rate == "5":
        print("Terimakasiih atas rate tanpa paksaan ini")
        break
    else:
        print("Yang bener masukin rate nya woii!!\n")
        continue