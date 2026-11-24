import socket

ports = [21,22,23,25,53,80,110]
ports += [143,443,3306,8080,8443]

t = input("Target: ").strip()
print("\nScanning", t, "...\n")

for p in ports:
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((t, p))
        print(f"[OPEN]   Port {p}")
        s.close()
    except:
        print(f"[closed] Port {p}")

print("\nDone.")
