import subprocess
from datetime import datetime
print("Lesson 8 - Using curl inside Python...")
file = open("report8.txt", "w")
with open("sites.txt") as f:
    sites = f.read().splitlines()
for site in sites:
    if not site.startswith("http"):
        site = "https://" + site
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        result = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-L", "--max-time", "10", site], capture_output=True, text=True, timeout=15)
        code = result.stdout.strip()
        if code.startswith("2") or code.startswith("3"):
            print(site, "ONLINE!", code, "at", now)
            file.write(now + " | " + site + " ONLINE " + code + "\n")
        else:
            print(site, "OFFLINE code", code, "at", now)
            file.write(now + " | " + site + " OFFLINE " + code + "\n")
    except Exception as e:
        print(site, "OFFLINE -", e)
        file.write(now + " | " + site + " OFFLINE\n")
print("Done! Check report8.txt")
file.close()
