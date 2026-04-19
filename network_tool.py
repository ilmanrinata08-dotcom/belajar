import socket
import time

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()
    except:
        pass

def main():
    print("="*30)
    print(" C'OODIEE NETWORK SCANNER ")
    print("="*30)
    target = input("Masukkan IP Target: ")
    print(f"Memulai scanning pada {target}...")
    
    # Scanning ports yang sering dipakai TKJ
    common_ports = [21, 22, 23, 80, 443, 8080, 3306]
    
    for port in common_ports:
        scan_port(target, port)
        time.sleep(0.1)
    
    print("\n[!] Scanning Selesai.")

if __name__ == "__main__":
    main()

