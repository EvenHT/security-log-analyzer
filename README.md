# Security Log Analyzer

Python tool for analyzing authentication logs and detecting suspicious login activity such as brute force attempts.

## Features

- Detects repeated failed login attempts
- Identifies suspicious IP addresses
- Detects possible brute force attacks
- Generates a security report

## Example log

Failed login from 192.168.1.10  
Failed login from 192.168.1.10  
Successful login from 10.0.0.5  

## Usage

Run the script:

python log_analyzer.py

Then enter the log file:

sample_log.txt

## Example output

--- Security Log Analysis ---

Successful logins: 2

Failed login attempts by IP:

192.168.1.10 -> 4 failed attempts

Suspicious IPs (possible brute force):

192.168.1.10 - possible brute force attack

Report saved to security_report.txt

## Author

Even Hynden Torkildsrud  
Bachelor in Information Technology – Cybersecurity