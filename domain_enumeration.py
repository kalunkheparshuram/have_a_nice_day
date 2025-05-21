# Tool Name: Domain Enumeration - Subdomain & IP Scanner

import socket
import requests
import csv
import time
import os
from urllib.parse import urljoin
from collections import defaultdict

def get_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.error:
        return "IP Not Found"

def get_status_code(domain):
    urls = [f"http://{domain}", f"https://{domain}"]
    for url in urls:
        try:
            response = requests.get(url, timeout=5, allow_redirects=True)
            return response.status_code
        except requests.RequestException:
            continue
    return "No Response"


def get_subdomains_crtsh(domain, retries=3, delay=5):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=15)
            if response.status_code != 200:
                raise Exception(f"Bad status: {response.status_code}")
            data = response.json()
            subdomains = set()
            for entry in data:
                name = entry.get("name_value")
                if name:
                    for sub in name.split("\n"):
                        sub = sub.strip().lower()
                        if sub.endswith(domain) and "*" not in sub:
                            subdomains.add(sub)
            return sorted(subdomains)
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    return []


def save_results_by_status_csv(results, results_dir="."):
    status_map = defaultdict(list)
    for entry in results:
        status_map[str(entry['status'])].append(entry)

    for status, entries in status_map.items():
        filepath = os.path.join(results_dir, f"{status}.csv")
        with open(filepath, mode="w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["domain", "ip", "status"])
            writer.writeheader()
            writer.writerows(entries)

def save_to_csv(data, filename="results.csv", results_dir="."):
    filepath = os.path.join(results_dir, filename)
    with open(filepath, mode="w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["domain", "ip", "status"])
        writer.writeheader()
        writer.writerows(data)

def log_error(message, results_dir):
    with open(os.path.join(results_dir, "errors.log"), "a") as f:
        f.write(message + "\n")

def main():
    target_domain = input("Enter the main domain (e.g. example.com): ").strip()
    root_dir = target_domain
    results_dir = os.path.join(root_dir, "1. Reconnaissance")
    os.makedirs(results_dir, exist_ok=True)

    subdomains = get_subdomains_crtsh(target_domain)
    domains_to_check = subdomains + [target_domain]

    results = []
    for domain in domains_to_check:
        ip = get_ip(domain)
        if ip == "IP Not Found":
            log_error(f"IP not found for {domain}", results_dir)
        status = get_status_code(domain)
        print(f"{domain} - IP_ADDR: {ip}, STATUS_CODE: {status}")

     
        results.append({
            "domain": domain,
            "ip": ip,
            "status": status,
        })

    save_to_csv(results, filename="results.csv", results_dir=results_dir)
    save_results_by_status_csv(results, results_dir=results_dir)

    print("\n[✓] Results saved.")

if __name__ == "__main__":
    main()
