from collections import defaultdict

log_file = "sample_auth.log"
failed_logins = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            # Extract the IP address
            parts = line.strip().split()
            ip_index = parts.index("from") + 1
            ip = parts[ip_index]
            failed_logins[ip] += 1

# Print a summary
print("🔐 Failed Login Attempts by IP:")
for ip, count in failed_logins.items():
    print(f"{ip}: {count} attempt(s)")

# Flag IPs with more than 1 failure
print("\n🚨 Suspicious IPs (multiple failures):")
for ip, count in failed_logins.items():
    if count > 1:
        print(f"⚠️  {ip} - {count} times")
