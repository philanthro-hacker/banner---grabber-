import math, getpass, hashlib

common = ["password","123456","123456789","qwerty","password123","letmein","admin","12345","iloveyou","12345678"]

p = getpass.getpass("Enter password to test (won't show): ")
print(f"\nLength: {len(p)}")

# charset size
size = 0
if any(c.islower() for c in p): size += 26
if any(c.isupper() for c in p): size += 26
if any(c.isdigit() for c in p): size += 10
if any(not c.isalnum() for c in p): size += 32

entropy = len(p) * math.log2(size) if size else 0
print(f"Entropy: {entropy:.1f} bits")

# 10 billion guesses/sec = fast GPU
guesses = 2 ** entropy
seconds = guesses / 10_000_000_000
if seconds < 60:
    time_str = f"{seconds:.2f} seconds"
elif seconds < 3600:
    time_str = f"{seconds/60:.1f} minutes"
elif seconds < 86400:
    time_str = f"{seconds/3600:.1f} hours"
elif seconds < 31536000:
    time_str = f"{seconds/86400:.1f} days"
else:
    time_str = f"{seconds/31536000:.1f} years"

print(f"Time to crack (10B/sec): {time_str}")

if p.lower() in common:
    print("\n[CRITICAL] This is in the TOP 10 most common passwords. Cracked instantly.")
elif entropy < 40:
    print("\n[WEAK] Would fall to a wordlist attack.")
elif entropy < 60:
    print("\n[OK] Decent, but could be stronger.")
else:
    print("\n[STRONG] Good passphrase.")

print(f"\nSHA256: {hashlib.sha256(p.encode()).hexdigest()[:16]}...")
