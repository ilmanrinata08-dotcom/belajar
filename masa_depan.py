print("=== PROYEKSI TABUNGAN ===")

# 1. Bagian Input (Rata Kiri)
nabung = float(input("Nabung per bulan: "))
tahun = int(input("Berapa tahun: "))

# 2. Perhitungan Dasar (Rata Kiri)
total_bln = tahun * 12
uang = 0

print(f"\nHasil untuk {tahun} tahun:")

# 3. Bagian Perulangan (Hati-hati Spasi!)
for bln in range(1, total_bln + 1):
    uang += nabung  # Menjorok 4 spasi
    if bln % 12 == 0:  # Menjorok 4 spasi
        ke = bln // 12  # Menjorok 8 spasi
        print(f"Thn {ke}: Rp {uang:,.0f}")  # Menjorok 8 spasi

# 4. Penutup (Rata Kiri Kembali)
print("-" * 25)
print(f"Total Akhir: Rp {uang:,.0f}")


