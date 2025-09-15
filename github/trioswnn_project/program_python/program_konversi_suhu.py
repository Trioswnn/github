def konversi_suhu(nilai, asal, tujuan):
    # Jadikan dalam satuan celcius
    if asal == 1:
        celcius = asal
    elif asal == 2:
        celcius = nilai * 5/4
    elif asal == 3:
        celcius = nilai - 273.15
    elif asal == 4:
        celcius = (nilai - 32) * 5/9
    else:
        return None
    
    # Hitung konversi dengan satuan awal celcius
    if tujuan == 1:
        return celcius
    elif tujuan == 2:
        return celcius * 4/5
    elif tujuan == 3:
        return celcius + 273.15
    elif tujuan == 4:
        return celcius * 9/5 + 32
    else:
        return None

judul = "Program Konversi Suhu"

print("="*len(judul))
print(judul)
print("="*len(judul))

print('''1. Celcius
2. Reamur
3. Kelvin
4. Fahrenheit
      ''')

nilai = float(input("Derajat suhu asal : "))
asal = int(input("Satuan suhu asal (1/2/3/4) : "))
tujuan = int(input("Satuan suhu tujuan (1/2/3/4) : "))

hasil = konversi_suhu(nilai,asal,tujuan)

# Simpan nilai satuan
satuan = {
    1 : "C",
    2 : "R",
    3 : "K",
    4 : "F"
}

if hasil is not None:
    print(f"Hasil konversi dari {nilai} {satuan[asal]} adalah {hasil:.2f} {satuan[tujuan]}")
else:
    print("Masukan opsi dengan benar!!")