import socket

words = ["www","mail","api","blog","shop","admin"]
words += ["dev","test","ftp","maps","drive","docs","support"]

t = input("Domain (google.com): ").strip()
print(f"\nFinding subdomains for {t}...\n")

for w in words:
    sub = f"{w}.{t}"
    try:
        ip = socket.gethostbyname(sub)
        print(f"[FOUND] {sub} -> {ip}")
    except:
        print(f"[NO] {sub}")

print("\nDone.")
