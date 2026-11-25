# Banner Grabber + Recon Toolkit

Tools built in Termux on Android.
Built to work even on networks that fake open ports.

## Tools
- banner.py - Grab banner from one host/port
- scanner.py - Basic port scanner (naive)
- scanner2.py - Verified scanner, filters FAKE ports
- recon.py - Combined scanner + banner grabber

## Usage
python recon.py
Target: scanme.nmap.org

## Features
- Detects FAKE open ports from carrier proxies
- Verifies with real banner
- Tested on scanme.nmap.org: found 22, 80, 9929

## Disclaimer
For learning and authorized testing only.
