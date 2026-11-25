import socket

ports = [21,22,23,25,80,110,143]
ports += [443,3306,8080,8443,9929]
t = input("Target: ").strip()
print("\nRecon on", t, "...\n")

for p in ports:
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((t, p))
        if p in [80,443,8080,8443,9929]:
            s.send(b"HEAD / HTTP/1.0\r\n\r\n")
        else:
            s.send(b"HELLO\r\n")
        try:
            data = s.recv(1024)
        except:
            data = b""
        s.close()
        if data:
            print(f"[OPEN] {p}")
            print(data.decode(errors="ignore")[:200])
            print("-" * 30)
        else:
            print(f"[FAKE] {p}")
    except:
        print(f"[closed] {p}")
print("\nRecon done.")
