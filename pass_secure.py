import string
import random

print("=== CYBER SECURITY: PASS-CHECKER ===")
password = input("Masukkan Password untuk di-test: ")

# Analisis Kekuatan
length = len(password)
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(char in string.punctuation for char in password)

score = sum([length >= 8, has_upper, has_lower, has_digit, has_symbol])

print(f"\nAnalisis Password: {password}")
if score <= 2:
    status = "LEMAH (Bahaya Brute Force!)"
elif score <= 4:
    status = "SEDANG (Bisa Ditingkatkan)"
else:
    status = "SANGAT KUAT (Aman!)"

print(f"Skor Keamanan: {score}/5")
print(f"Status: {status}")

# Fitur Bonus: Generator Password Kuat
print("\n--- Saran Password Kuat Untukmu ---")
karakter = string.ascii_letters + string.digits + string.punctuation
saran = "".join(random.choice(karakter) for i in range(12))
print(f"Rekomendasi: {saran}")

