```
  ____   ___  ____ _____   ____   ____    _    _   _ _   _ _____ ____  
 |  _ \ / _ \|  _ \_   _| / ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
 | |_) | | | | |_) || |   \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
 |  __/| |_| |  _ < | |    ___) | |___ / ___ \| |\  | |\  | |___|  _ < 
 |_|    \___/|_| \_\|_|   |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\
```
# PortScanner

A Python-based interactive command-line interface for **Nmap**. This tool simplifies the process of performing various network scans including service detection, OS fingerprinting, and comprehensive analysis through an easy-to-use menu.

## Features

* **Fast Scan:** Quick port analysis using default Nmap parameters.
* **Service Scan:** Detects versions of services running on open ports (`-sS -sV`).
* **OS Detection:** Identifies the target's operating system using TCP/IP stack fingerprinting (`-O`).
* **Full Scan:** Combined scan for services, versions, and OS information in one go.
* **Visual Interface:** Utilizes `figlet` for a stylized ASCII banner.

## Prerequisites

Before running the tool, ensure you have the following installed:

* **Python 3.x**
* **Nmap** (The script calls `nmap` via system commands)
* **Figlet** (The script attempts to install this automatically via `apt`)

## Installation

1. Clone the repository:
   git clone [https://github.com/Tde99/PortScanner.git](https://github.com/Tde99/PortScanner.git)
2. Navigate to the project directory:
   cd PortScanner
3. Make the script executable:
   chmod +x PortScanner.py


## Usage
Run the script with root privileges (required for certain Nmap scans like OS detection):

sudo python3 PortScanner.py


Menu Options:
Fast Scan: Basic port scanning.
Service Scan: Identify running services and their versions.
Operating System Info: Fingerprint the target OS.
All Of Them: Perform all of the above scans simultaneously.

Type q or press Ctrl+C to exit.
