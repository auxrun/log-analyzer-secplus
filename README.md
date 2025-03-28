# 🔐 Log File Analyzer (Security+ Project)

A simple Python script that scans Linux-style authentication logs (`auth.log`) to identify any failed login attempts while simultaneously flagging suspicious IP addresses.

This project is part of my hands-on preparation for the **CompTIA Security+ certification**, focusing on log analysis and basic threat detection techniques.

---

## 📌 Key Features

- Parses authentication logs (e.g., `auth.log`)
- Identifies failed login attempts
- Tracks and counts attempts by IP address
- Highlights IPs with repeated failures
- Easy to customize or extend

---

## 🧠 Why It Matters (Security+ Tie-In)

This tool reinforces concepts from **Security+ Domain 2 (Technologies and Tools)**, specifically:

- Log analysis
- Detection of potential brute-force attempts
- Security monitoring fundamentals

---

## 🚀 How to Use

### 1. Prepare a Log File

If you're using a simulated log file, run:

```bash
nano sample_auth.log
```
Then paste the following example log contents:

```bash
Mar 27 10:15:43 localhost sshd[1001]: Failed password for invalid user root from 192.168.1.100 port 22 ssh2
Mar 27 10:16:10 localhost sshd[1001]: Failed password for user admin from 192.168.1.101 port 22 ssh2
Mar 27 10:16:45 localhost sshd[1001]: Accepted password for user alex from 192.168.1.102 port 22 ssh2
Mar 27 10:17:12 localhost sshd[1001]: Failed password for root from 192.168.1.100 port 22 ssh2
Mar 27 10:18:03 localhost sshd[1001]: Failed password for root from 192.168.1.103 port 22 ssh2
```
Save and exit the file: CTRL+O, Enter, CTRL+X

---

## ▶️ How to Run the Script

1. Make sure you have **Python 3 installed**:
   ```bash
   python3 --version
   ```
   
2. Run Script with sample log file:
   ```bash
   python3 log_analyzer.py
   ```

3. Output is a breakdown of the failed login attempts by IP with repeated failed being flagged
  ```yaml
  🔐 Failed Login Attempts by IP:
  192.168.1.100: 2 attempt(s)
  192.168.1.101: 1 attempt(s)
  192.168.1.103: 1 attempt(s)
  
  🚨 Suspicious IPs (multiple failures):
  ⚠️  192.168.1.100 - 2 times
  ```

---

## 🪟 Windows Log Analyzer (Event ID 4625)

This script scans exported Windows Security logs for **failed login attempts** based on **Event ID 4625**.

It intelligently filters out system/service accounts (like `SYSTEM` or machine names ending in `$`) and identifies the actual username involved in failed login events.

---

### ▶️ How to Use (Windows)

1. In **Windows Event Viewer**, go to:
   - **Windows Logs > Security**
   - Click **Filter Current Log**
   - Enter **Event ID: 4625**
   - Click **OK**

2. Export the filtered results as a `.txt` file (e.g. `eventlog.txt`)

3. Move the log into WSL:
   ```bash
   cp /mnt/c/Users/<YourUsername>/Downloads/eventlog.txt ~/real_logs.txt```
4. Run the script:
   ```bash
   python3 log_analyzer_windows.py real_logs.txt```

SAMPLE OUTPUT
   ```csharp
   🔐 Failed Login Attempts by Account:
      some+email@gmail.com: 1 attempt(s)

   🚨 Accounts with Multiple Failures:```
      
---

### 3. Save & Exit:
```yaml
   - `CTRL + O`, then `Enter` to save
   - `CTRL + X` to exit```



