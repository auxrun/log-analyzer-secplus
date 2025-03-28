import sys
from collections import defaultdict

if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} <log_file>")
    sys.exit(1)

log_file = sys.argv[1]
failed_logins = defaultdict(int)

with open(log_file, "r") as file:
    content = file.read()

# Split into blocks per event
events = content.split("Event ID")

for event in events:
    if "4625" in event:
        account_candidates = []

        for line in event.splitlines():
            if "Account Name:" in line:
                parts = line.strip().split(":", 1)
                if len(parts) > 1:
                    name = parts[1].strip()
                    if (
                        name
                        and name != "-"
                        and name.upper() != "SYSTEM"
                        and not name.endswith("$")
                    ):
                        account_candidates.append(name)

        if account_candidates:
            final_account = account_candidates[-1]  # Get last valid username
            failed_logins[final_account] += 1

# Output
print("🔐 Failed Login Attempts by Account:")
for account, count in failed_logins.items():
    print(f"{account}: {count} attempt(s)")

print("\n🚨 Accounts with Multiple Failures:")
for account, count in failed_logins.items():
    if count > 1:
        print(f"⚠️  {account} - {count} times")
