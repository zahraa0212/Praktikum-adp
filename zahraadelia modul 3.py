operasi = True
while operasi :
    angka_pertama = int(input("masukkan angka pertama : "))
    angka_kedua = int(input("masukkan angka kedua : "))
    pilihan_operasi = int(input("pilih operasi : "))
    print("1. penjumlahan")
    print("2. pengurangan")
    print("3. perkalian")
    print("4. pembagian")
    print("5. keluar")
    if pilihan_operasi == 1 :
        hasil = angka_pertama + angka_kedua
        print(f"hasil = {hasil}")
    elif pilihan_operasi == 2 :
        hasil = angka_pertama - angka_kedua
        print(f"hasil = {hasil}")
    elif pilihan_operasi == 3 :
        hasil = angka_pertama * angka_kedua
        print(f"hasil = {hasil}")
    elif pilihan_operasi == 4 :
        if angka_kedua == 0 :
            print("tidak valid")
        else :
            hasil = angka_pertama / angka_kedua
            print(f"hasil = {hasil}")
    else :
        print("pilihan operasi tidak valid = keluar")
    perulangan = input("pilih (yes/no) : ")
    if perulangan == "yes" :
        print("lakukan ulang operasi")
    else :
        break