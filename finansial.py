print("=== KALKULATOR TARGET FINANSIAL ===")

target = float(input("Masukkan target uang yang ingin dicapai: "))
tabungan_bulan = float(input("Berapa yang bisa kamu tabung per bulan? "))

bulan = 0
total_tabungan = 0

while total_tabungan < target:
    bulan += 1
    total_tabungan += tabungan_bulan
    print(f"Bulan ke-{bulan}: Tabungan terkumpul Rp {total_tabungan}")

print("-" * 30)
print(f"Selesai! Kamu butuh {bulan} bulan untuk mencapai target.")

