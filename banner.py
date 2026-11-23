import socket

target = input("Target: ").strip()
if target.startswith("http"):
    target = target.replace("https://", "").replace("http://", "").split("/")[0]

print(f"\nKnocking on {target} port 80...\n")

try:
    s = socket.socket()
    s.settimeout(5)
    s.connect((target, 80))
    s.sendall(f"HEAD / HTTP/1.0\r\nHost: {target}\r\n\r\n".encode())
    data = s.recv(2048).decode(errors="ignore")
    s.close()
    print("--- Server replied: ---")
    print(data)
    print("-----------------------")
    for line in data.splitlines():
        if "Server:" in line or "server:" in line:
            print(f"\n🎯 FOUND IT: {line.strip()}")
            break
    else:
        print("\nNo Server header, but we got a real reply - so it's really there.")
except Exception as e:
    print(f"Failed: {e}")
