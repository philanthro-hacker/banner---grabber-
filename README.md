# Banner Grabber + Recon Toolkit

Tools built in Termux on Android.
Built to work even on networks that fake open ports.

## Tools
- banner.py - Grab banner from one host/port
- scanner.py - Basic port scanner (naive)
- scanner2.py - Verified scanner, filters FAKE ports
- recon.py - Combined scanner + banner grabber
- dir-buster.py - Find hidden paths (/admin, /login, /robots.txt)
- subdomain-finder.py - Find subdomains via DNS (mail, api, maps)

## Workflow
1. subdomain-finder.py -> find the doors
2. recon.py -> check which ports are open
3. dir-buster.py -> find hidden pages

## Tested On
- scanme.nmap.org: found 22, 80, 9929
- google.com: found 10 subdomains, robots.txt

## Disclaimer
For learning and authorized testing only.
