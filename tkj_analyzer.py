import os

# Tampilan Header biar keren
print("="*40)
print("   IP SUBNET ANALYZER - TKJ EDITION   ")
print("="*40)

ip_input = input("Masukkan IP Address (ex: 192.168.10.1): ")

# 1. Proses Pemecahan IP
oktet = ip_input.split('.')
first = int(oktet[0])

# 2. Proses Konversi Biner Lengkap (4 Oktet)
biner_list = [bin(int(x)).replace("0b", "").zfill(8) for x in oktet]
biner_full = ".".join(biner_list)

# 3. Logika Penentu Kelas & Subnet (Sesuai Tabelmu)
if 1 <= first <= 126:
    kelas, mask, n = "A", "255.0.0.0", 24
elif 128 <= first <= 191:
    kelas, mask, n = "B", "255.255.0.0", 16
elif 192 <= first <= 223:
    kelas, mask, n = "C", "255.255.255.0", 8
elif 224 <= first <= 239:
    kelas, mask, n = "D (Multicast)", "N/A", 0
elif 240 <= first <= 255:
    kelas, mask, n = "E (Eksperimen)", "N/A", 0
else:
    kelas, mask, n = "Unknown/Loopback", "N/A", 0

# 4. Hitung Host dengan Rumus 2^n - 2
jml_host = (2**n) - 2 if n > 0 else 0

# 5. Output Hasil Analisis
print("\n" + "-"*30)
print(f"IP ADDRESS    : {ip_input}")
print(f"BINER (8-bit) : {biner_full}")
print(f"CLASS         : Class {kelas}")
print(f"DEFAULT MASK  : {mask}")
print("-"*30)

if n > 0:
    print(f"Bit Host (n)  : {n} bit")
    print(f"Rumus Host    : 2^{n} - 2")
    print(f"Total Usable  : {jml_host:,} Host")
else:
    print("Keterangan    : IP Khusus (Tidak untuk Host)")
print("-" * 30)

