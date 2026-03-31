# Network Packet Inspector (DPI)
A Python-based network analysis tool for real-time packet sniffing and security monitoring.

## 🚀 Features
- **Real-time Sniffing:** Captures live IP traffic using Scapy.
- **Security Alerts:** Detects and flags unsecured HTTP traffic (Port 80).
- **Deep Packet Inspection (DPI):** Extracts and decodes payload data from unencrypted packets.
- **Automated Logging:** Saves security events with timestamps to `security_log.txt`.
- **Protocol Identification:** Categorizes traffic into TCP, HTTPS, and DNS.

## 🛠 Installation
1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # On Windows
Install requirements:

Bash
pip install scapy
⚠️ Requirements
Must be run with Administrator/Sudo privileges to access raw network sockets.

Python 3.x
