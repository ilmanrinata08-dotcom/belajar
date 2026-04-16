print("=== KALKULATOR PEMBURU TARGET ===")

target = float(input("Target uang (contoh 100000000): "))
nabung = float(input("Sanggup nabung per bulan: "))
uang = 0
bulan = 0

# Selama uang belum mencapai target, lari terus!
while uang < target:
    uang += nabung
    bulan += 1

tahun = bulan // 12
sisa_bulan = bulan % 12

print("-" * 30)
print(f"Target Rp {target:,.0f} tercapai dalam:")
print(f"{bulan} bulan")
print(f"Atau: {tahun} tahun {sisa_bulan} bulan")

