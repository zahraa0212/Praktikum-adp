def tampilkan_menu():
    print("menu")
    print("1. tabel perkalian modulo n")
    print("2. mencari nilai sigma x")
    print("3. mencari nilai n!")
    print("4. total dan rata-rata suatu data")
    print("5. keluar")

def tabel_perkalian_modulo():
    n = int(input("masukkan nilai n (1-10): "))
    while n <= 0 or n > 10:
        print("nilai tidak valid, harus antara 1 dan 10")
        n = int(input("masukkan lagi nilai n (1-10): "))

    print("tabel perkalian modulo", n)
    print("    ", end="")
    for i in range(n):
        print(f"{i:3}", end="")
    print()
    for i in range(n):
        print(f"{i:2} |", end="")
        for j in range(n):
            print(f"{(i * j) % n:3}", end="")
        print()

def sigma_x():
    batas_bawah = int(input("batas bawah: "))
    batas_atas = int(input("batas atas: "))
    while batas_atas < batas_bawah:
        print("batas atas harus lebih besar atau sama dengan batas bawah.")
        batas_bawah = int(input("batas bawah: "))
        batas_atas = int(input("batas atas: "))

    total = 0
    for x in range(batas_bawah, batas_atas + 1):
        total += x
    print("jumlah sigma x dari", batas_bawah, "sampai", batas_atas, "adalah", total)

def faktorial():
    n = int(input("masukkan nilai n (>= 0): "))
    while n < 0:
        print("n harus lebih besar atau sama dengan 0")
        n = int(input("masukkan nilai n (>= 0): "))

    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    print(f"{n}! =", hasil)

def total_rata_rata():
    jumlah = int(input("masukkan banyak data: "))
    while jumlah <= 0:
        print("Jumlah data harus lebih dari 0.")
        jumlah = int(input("masukkan banyak data: "))

    data = []
    for i in range(jumlah):
        nilai = int(input(f"Data ke-{i+1}: "))
        data.append(nilai)

    total = 0
    for x in data:
        total += x

    rata_rata= total / jumlah
    print("total semua data =", total)
    print("rata-rata =", rata_rata)

def menu():
    pilihan = 0
    while pilihan != 5:
        tampilkan_menu()
        pilihan = int(input("pilih menu (1-5): "))
        if pilihan == 1:
            tabel_perkalian_modulo()
        elif pilihan == 2:
            sigma_x()
        elif pilihan == 3:
            faktorial()
        elif pilihan == 4:
            total_rata_rata()
        elif pilihan == 5:
            print("terima kasih, program selesai")
        else:
            print("pilihan tidak valid, silakan pilih angka 1 sampai 5")
menu()