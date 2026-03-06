# Security Log Analyzer

A lightweight Python tool for analyzing authentication logs and detecting suspicious login activity such as potential brute force attacks.

## Features

- Detects repeated failed login attempts
- Identifies suspicious IP addresses
- Detects possible brute force attacks
- Generates a security report

## Example

Example log:

Failed login from 192.168.1.10  
Failed login from 192.168.1.10  
Successful login from 10.0.0.5  

Example output:

192.168.1.10 -> 4 failed attempts  
Possible brute force detected

## Usage

Run the script:

python log_analyzer.py

Enter the log file when prompted:

sample_log.txt

## Technologies Used

- Python 3
- Log parsing
- Basic intrusion detection techniques

## Purpose

This project was created to practice analyzing authentication logs and detecting suspicious activity such as brute force attacks.

## Author

Even Torkildsrud  
Bachelor in Information Technology – Cybersecurity