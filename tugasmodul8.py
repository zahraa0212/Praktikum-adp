praktikan = {"241001": ["Tazkia", 88, 70, 89],
            "242001": ["Siti", 90, 75, 95], 
            "243001": ["Keca", 95, 80, 85],
            "244001": ["Avris", 90, 88, 95],
            "245001": ["Kia", 87, 98, 75],
            "241002": ["Naura", 75, 90,88],
            "242002": ["Lalisa", 87, 90,85],
            "243002": ["Sepia", 85, 90, 78],
            "244002": ["Ruby", 88, 95, 78],
            "245002": ["Quen", 77, 90, 86]}
def hitung_nilai_akhir(pretest, posttest, tugas):
    return (0.35 * pretest) + (0.35 * posttest) + (0.30 * tugas)
nilai_akhir = {}
for nim in praktikan:
    nama = praktikan[nim][0]
    pretest = praktikan[nim][1]
    posttest = praktikan[nim][2]
    tugas = praktikan[nim][3]
    total = hitung_nilai_akhir(pretest, posttest, tugas)
    nilai_akhir[nim] = [nama, total]
file = open("data_nilai_akhir.txt", "w")
for nim in nilai_akhir:
    nama = nilai_akhir[nim][0]
    total_nilai = nilai_akhir[nim][1]
    file.write(f"{nim}, {nama}, {total_nilai}")
file.close()
jumlah = 0
total_semua = 0
for nim in nilai_akhir:
    total_semua += nilai_akhir[nim][1]
    jumlah += 1
rata_rata = total_semua / jumlah
nim_tertinggi = None
nilai_tertinggi = -1 
nim_terendah = None
nilai_terendah = 101 
for nim_praktikan, data_nilai_akhir_praktikan in nilai_akhir.items(): 
    nama_praktikan = data_nilai_akhir_praktikan[0]
    nilai_total_praktikan = data_nilai_akhir_praktikan[1]
    if nilai_tertinggi == -1 or nilai_total_praktikan > nilai_tertinggi:
        nilai_tertinggi = nilai_total_praktikan
        nim_tertinggi = nim_praktikan
    if nilai_terendah == 101 or nilai_total_praktikan < nilai_terendah:
        nilai_terendah = nilai_total_praktikan
        nim_terendah = nim_praktikan
bawah_rata_rata = 0
for nim in nilai_akhir:
    if nilai_akhir[nim][1] < rata_rata:
        bawah_rata_rata += 1
print("Rata-rata nilai akhir:", rata_rata)
print("Nilai tertinggi:", nilai_tertinggi, "(", nilai_akhir[nim_tertinggi][0], ")")
print("Nilai terendah:", nilai_terendah, "(", nilai_akhir[nim_terendah][0], ")")
print("Jumlah praktikan yang nilainya di bawah rata-rata:", bawah_rata_rata)