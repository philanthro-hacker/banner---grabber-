import socket

ports = [21,22,23,25,80,110,143,443]
t = input("Target: ").strip()
print("\nScanning", t, "with verification...\n")

for p in ports:
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((t, p))
        try:
            s.send(b"HELLO\r\n")
            data = s.recv(1024)
        except:
            data = b""
        s.close()
        if data:
            print(f"[OPEN] Port {p} -> {data[:60]}")
        else:
            print(f"[FAKE] Port {p} - no reply")
    except:
        print(f"[closed] Port {p}")
print("\nDone.")
