import urllib.request, urllib.error

words = ["admin","login","robots.txt",".env","backup"]
words += ["config","test","api","dashboard","wp-admin"]

t = input("Target (example.com): ").strip()
if not t.startswith("http"):
    t = "http://" + t
print("\nBusting", t, "...\n")

for w in words:
    url = t + "/" + w
    try:
        r = urllib.request.urlopen(url, timeout=3)
        print(f"[FOUND] {r.status} /{w}")
    except urllib.error.HTTPError as e:
        if e.code != 404:
            print(f"[FOUND] {e.code} /{w}")
        else:
            print(f"[404] /{w}")
    except Exception as e:
        print(f"[ERR] /{w} {e}")
print("\nDone.")
