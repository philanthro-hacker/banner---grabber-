# Uptime Monitor - Built on Termux

A Python website monitor that checks if websites are ONLINE/OFFLINE every 10 seconds and sends an ALERT when a site goes DOWN.

Built on a phone in Douala, Cameroon using Termux + Python + curl.

## Features
- Checks multiple sites from sites.txt
- Uses curl for real HTTP status codes
- Loops forever with time.sleep()
- Remembers last status
- ALERT when site goes DOWN
- BACK ONLINE message when it recovers
- Saves alerts to alerts.txt

## How to run
python lesson10.py

## Files
- lesson10.py - Main monitor with alerts
- lesson9.py - Auto monitor
- lesson8.py - One-time monitor
- sites.txt - List of websites to check
- alerts.txt - Saved alerts

## Example Output
https://google.com ONLINE! 200
🚨 ALERT! https://facebook.com WENT DOWN
✅ https://facebook.com is BACK ONLINE! 200
