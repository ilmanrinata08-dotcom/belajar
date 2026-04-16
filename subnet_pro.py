print("="*45)
print("   ADVANCED SUBNET CALCULATOR (CIDR)   ")
print("="*45)

ip_input = input("Masukkan IP (ex: 192.168.10.1): ")
cidr = int(input("Masukkan Prefix/CIDR (ex: 24, 26, 30): "))

# 1. Menghitung Jumlah Bit Host dan Mask
host_bits = 32 - cidr
jumlah_host = (2**host_bits) - 2

# 2. Logika Mask Sederhana (Hanya untuk CIDR /24 sampai /32)
# Ini adalah bagian yang paling sering keluar di ujian TKJ
last_oktet_mask = 256 - (2**host_bits) if cidr >= 24 else 0
full_mask = f"255.255.255.{last_oktet_mask}"

# 3. Menghitung Network & Broadcast (Sederhana untuk blok /24 ke atas)
oktet = ip_input.split('.')
ip_terakhir = int(oktet[3])
blok = 2**host_bits
network_last = (ip_terakhir // blok) * blok
broadcast_last = network_last + blok - 1

# 4. Output Hasil Analisis ala Cisco Packet Tracer
print("\n" + "RESULT ANALYSIS".center(30, "-"))
print(f"IP Address    : {ip_input}/{cidr}")
print(f"Subnet Mask   : {full_mask}")
print(f"Total Usable  : {jumlah_host if jumlah_host > 0 else 0} Host")

print("-" * 30)
print(f"Network ID    : {oktet[0]}.{oktet[1]}.{oktet[2]}.{network_last}")
print(f"IP Pertama    : {oktet[0]}.{oktet[1]}.{oktet[2]}.{network_last + 1}")
print(f"IP Terakhir   : {oktet[0]}.{oktet[1]}.{oktet[2]}.{broadcast_last - 1}")
print(f"Broadcast ID  : {oktet[0]}.{oktet[1]}.{oktet[2]}.{broadcast_last}")
print("-" * 30)

print("\n[INFO] VLSM Note: Gunakan Network ID ini")
print("sebagai dasar pembagian subnet selanjutnya.")

