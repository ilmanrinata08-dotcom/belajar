import random

angka_rahasia = random.randint(1, 10)
print("=== GAME TEBAK ANGKA ===")

tebakan = 0
while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka (1-10): "))
    
    if tebakan < angka_rahasia:
        print("Terlalu KECIL! Coba lagi.")
    elif tebakan > angka_rahasia:
        print("Terlalu BESAR! Coba lagi.")
    else:
        print("YAY HORE! Tebakanmu BENAR BENAR TEPAT.")

