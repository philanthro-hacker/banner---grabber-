import subprocess
from datetime import datetime
import time

print("Lesson 10 - DOWN Alert System Started!")
print("I will ALERT you if any site goes DOWN. Press CTRL+C to stop")

# Remember last status: start with everything ONLINE
last_status = {}

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
            is_online = code.startswith("2") or code.startswith("3")
        except:
            is_online = False
            code = "000"

        # Check if it CHANGED
        if site in last_status:
            was_online = last_status[site]
            if was_online and not is_online:
                # IT JUST WENT DOWN! ALERT!
                alert = f"🚨 ALERT! {site} WENT DOWN at {datetime.now()} code {code}"
                print(alert)
                print("\a")  # Beep sound
                with open("alerts.txt", "a") as alert_file:
                    alert_file.write(alert + "\n")
            elif not was_online and is_online:
                print(f"✅ {site} is BACK ONLINE! {code}")
            else:
                print(site, "ONLINE!" if is_online else "OFFLINE", code)
        else:
            print(site, "ONLINE!" if is_online else "OFFLINE", code)

        last_status[site] = is_online

    round = round + 1
    print("Sleeping 10 seconds...")
    time.sleep(10)
