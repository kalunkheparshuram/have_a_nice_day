```
# 🛡️ Have a Nice Day – Cybersecurity Automation Toolkit

Welcome to **Have a Nice Day**, a personal toolkit designed to automate essential cybersecurity operations for reconnaissance, enumeration, and penetration testing workflows.

---

## 📁 Project Structure

This repository will grow to include modular tools for each step in the cybersecurity process. Each script lives in its own directory and follows a structured output format.

root/
├── domain-enumerator/
│   ├── domain_enum.py
│   └── README.md
├── future-tools/
│   ├── port-scanner/
│   ├── brute-forcer/
│   └── ...
└── results/


---

## 📌 Tool #1: Domain Enumerator – Subdomain & IP Scanner

**Description:**  
This script performs passive domain enumeration using public Certificate Transparency logs (`crt.sh`) to discover subdomains, resolve them to IP addresses, and check their HTTP/HTTPS availability.

### 🔧 Features

- 🔍 Subdomain enumeration via `crt.sh`
- 🌐 IP resolution of each domain
- 📡 HTTP/HTTPS status code checking
- 📁 CSV output organized by status codes
- 📂 Clean directory structure for result storage

---

## 🚀 How to Use

### 1. Clone the Repository
```
git clone https://github.com/your-username/have-a-nice-day.git
cd have-a-nice-day/domain-enumerator
````

### 2. Install Requirements
 ⚙️ **Dependencies:** This script relies on standard Python libraries, but you should install external packages using `requirements.txt`.

```
pip install -r requirements.txt
```

### 3. Run the Script

```
python3 domain_enum.py
```

### 4. Example Output

When prompted, enter a domain:

```
Enter the main domain (e.g. example.com): example.com
```

Your results will be saved in:

```
example.com/
└── 1. Reconnaissance/
    ├── results.csv
    ├── 200.csv
    ├── 403.csv
    ├── No Response.csv
```

---

## 📦 Output Format

Each CSV includes:

| Domain                                    | IP Address    | HTTP Status |
| ----------------------------------------- | ------------- | ----------- |
| [www.example.com](http://www.example.com) | 93.184.216.34 | 200         |
| mail.example.com                          | IP Not Found  | No Response |

---

## 🛠 Planned Tools

* [x] Subdomain Enumerator (✔ done)
* [ ] Port Scanner (next up)
* [ ] SSH Brute-force Tester
* [ ] Web Vulnerability Checker
* [ ] Screenshot Grabber
* [ ] Directory Brute Forcer

---

## 🧠 Notes

* This tool is for **educational and authorized security testing** only.
* Please ensure you have permission before scanning any domains.

---

## ☕ Author

**Parshuram Kalunkhe**
*“Have a nice day, while making the internet a safer place.”*

---

## 📄 License

This project is licensed under the GNU General Public License (GPL).
You are free to use, modify, and distribute this code under the terms of the GPL.
