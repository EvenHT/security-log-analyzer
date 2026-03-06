from collections import defaultdict

def analyze_log(file_path):

    failed_attempts = defaultdict(int)
    successful_logins = 0

    with open(file_path, "r") as file:
        for line in file:

            if "Failed login from" in line:
                ip = line.split()[-1]
                failed_attempts[ip] += 1

            if "Successful login from" in line:
                successful_logins += 1

    report = []
    report.append("\n--- Security Log Analysis ---\n")

    report.append(f"Successful logins: {successful_logins}\n")

    report.append("Failed login attempts by IP:\n")

    for ip, count in failed_attempts.items():
        report.append(f"{ip} -> {count} failed attempts")

    report.append("\nSuspicious IPs (possible brute force):\n")

    for ip, count in failed_attempts.items():
        if count > 3:
            report.append(f"{ip} - possible brute force attack")

    # Print report
    for line in report:
        print(line)

    # Save report
    with open("security_report.txt", "w") as file:
        for line in report:
            file.write(line + "\n")

    print("\nReport saved to security_report.txt")


if __name__ == "__main__":

    log_file = input("Enter log file path: ")

    analyze_log(log_file)