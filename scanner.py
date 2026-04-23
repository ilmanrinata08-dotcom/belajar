import socket

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()
    except:
        pass

target_ip = "google.com" # "github.com"
print(f"Memulai scanning pada: {target_ip}")

# tambahan daftar scan port standart + 8080 dan 8291 (winbox) 
ports = [21, 22, 23, 53, 80, 443, 3306, 8080, 8291]
for port in ports:
    scan_port(target_ip, port)

print("Scan selesai.")

