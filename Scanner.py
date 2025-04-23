import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import nmap
import json
import csv

# --- Security Header Check ---
SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy"
]

def check_security_headers(url):
    print("[+] Checking security headers...")
    try:
        response = requests.get(url)
        headers = response.headers
        missing = [h for h in SECURITY_HEADERS if h not in headers]
        print(f"Missing headers: {missing}")
        return missing
    except Exception as e:
        print(f"Error: {e}")
        return []

# --- Admin Panel Detection ---
ADMIN_PATHS = ["/admin", "/admin.html", "/login"]

def find_admin_login(base_url):
    print("[+] Scanning for exposed admin/login pages...")
    driver = webdriver.Chrome()
    exposed = []
    for path in ADMIN_PATHS:
        try:
            url = base_url.rstrip("/") + path
            driver.get(url)
            if driver.find_elements(By.XPATH, "//input[@type='password']"):
                exposed.append(url)
        except Exception as e:
            print(f"Error on {url}: {e}")
    driver.quit()
    print(f"Exposed admin/login pages: {exposed}")
    return exposed

# --- Port Scanning ---
def scan_ports(ip):
    print("[+] Running Nmap port scan...")
    scanner = nmap.PortScanner()
    scanner.scan(ip, '1-1000')
    ports = []
    try:
        for proto in scanner[ip].all_protocols():
            ports += list(scanner[ip][proto].keys())
        print(f"Open ports: {ports}")
    except:
        print("[-] No ports found or scan error.")
    return ports

# --- Report Generation ---
def save_report(headers, admin_pages, ports):
    print("[+] Saving scan results...")
    with open("scan_report.json", "w") as jf:
        json.dump({
            "missing_headers": headers,
            "admin_pages": admin_pages,
            "open_ports": ports
        }, jf, indent=4)

    with open("scan_report.csv", "w", newline="") as cf:
        writer = csv.writer(cf)
        writer.writerow(["Type", "Value"])
        for h in headers:
            writer.writerow(["Missing Header", h])
        for a in admin_pages:
            writer.writerow(["Admin Page", a])
        for p in ports:
            writer.writerow(["Open Port", p])
    print("[✓] Reports saved as scan_report.json and scan_report.csv")

# --- Main Execution ---
def main():
    url = input("Enter website URL (e.g., http://localhost:8000): ")
    ip = input("Enter IP address (e.g., 127.0.0.1): ")

    headers = check_security_headers(url)
    admin_pages = find_admin_login(url)
    ports = scan_ports(ip)
    save_report(headers, admin_pages, ports)

if __name__ == "__main__":
    main()
