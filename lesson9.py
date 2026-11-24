import subprocess
from datetime import datetime
import time

print("Lesson 9 - Auto Monitor Started! Press CTRL+C to stop")
print("Checking every 10 seconds...")

round = 1
while True:
    print("\n--- ROUND", round, "at", datetime.now().strftime("%H:%M:%S"), "---")
    with open("sites.txt") as f:
        sites = f.read().splitlines()

    for site in sites:
        if not site.startswith("http"):
            site = "https://" + site
        try:
            result = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-L", "--max-time", "10", site], capture_output=True, text=True, timeout=15)
            code = result.stdout.strip()
            if code.startswith("2") or code.startswith("3"):
                print(site, "ONLINE!", code)
            else:
                print(site, "OFFLINE code", code)
        except Exception as e:
            print(site, "OFFLINE -", e)

    round = round + 1
    print("Sleeping 10 seconds...")
    time.sleep(10)
