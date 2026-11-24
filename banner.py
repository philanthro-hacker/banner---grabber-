import socket

def grab_banner(target, port):
    print(f"\nKnocking on {target} port {port}...")
    try:
        s = socket.socket()
        s.settimeout(5)
        s.connect((target, port))
        s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
        data = s.recv(4096).decode(errors="ignore")
        s.close()

        print("\n--- Server replied: ---")
        print(data)
        print("-----------------------")

        for line in data.splitlines():
            if "Server:" in line:
                print(f"FOUND IT: {line.strip()}")
                return
        print("No Server header found - site is hiding it.")

    except Exception as e:
        print(f"Could not connect: {e}")

print("=== Banner Grabber V2 ===")
target = input("Target (or type 'all' to use sites.txt): ").strip()
port = int(input("Port (try 80): ").strip() or 80)

if target.lower() == "all":
    with open("sites.txt") as f:
        for site in f:
            site = site.strip()
            if site:
                grab_banner(site, port)
else:
    grab_banner(target, port)
