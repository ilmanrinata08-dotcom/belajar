print("=== TABUNGAN + BUNGA 5% ===")
nabung = float(input("setoran bulanan: "))
tahun = int(input("jangka waktu(tahun): "))
total_bulan = tahun * 12
uang = 0
bunga_tahunan = 0.05  # ini artinya 5%
print(f"\nproyeksi hasil tahun {tahun} tahun:")
for bulan in range(1, total_bulan + 1):
    uang += nabung
    # cek apakah sudah lewat 12 bulan (1 tahun)
    if bulan % 12 == 0:
        # hitung bunga dari uang yang ada
        bonus =  uang * bunga_tahunan
        uang += bonus
        ke = bulan // 12
        print(f"tahun {ke}: Rp{uang:,.0f} (+bunga) ")
print("-" * 25)
print(f"total akhir: Rp{uang:,.0f}")
