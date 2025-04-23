# Term-Project-Final-Presentation
"Automated Security Misconfiguration Scanner"

Project Overview
  This project is an automated tool designed to detect common security misconfigurations in web applications and networked services. Misconfigurations such as missing security headers, exposed admin panels, and default credentials are common vulnerabilities. Our scanner integrates web scraping, network port scanning, and public intelligence APIs to identify and report these issues.

Features:
- Detect missing HTTP security headers
- Identify exposed admin login panels
- Scan open ports using Nmap
- Gather service data using the Shodan API
- Generate structured reports (JSON and CSV formats)

Technologies Used:
- Python
- Selenium
- BeautifulSoup
- Requests
- Nmap (via python-nmap)
- Shodan API
- Pandas (for report generation)

Setup Instructions:

  1).Clone the repository
    https://github.com/yourusername/security-misconfig-scanner.git
cd security-misconfig-scanner

  2).Install dependencies
    pip install -r requirements.txt
    
  3).Add your Shodan API key
    Create a file named config.py and include:
SHODAN_API_KEY = "your_shodan_api_key_here"

  4).Run the scanner
    python scanner.py

Project Structure:

security-misconfig-scanner/
│
├── scanner.py              # Main entry point
├── web_scanner.py          # Handles web scraping and header analysis
├── network_scanner.py      # Nmap and Shodan integration
├── report_generator.py     # Exports results
├── config.py               # API keys and settings
└── requirements.txt        # Python dependencies

Usage:
You will be prompted to enter a URL and IP address to scan. After the scan, results will be saved to scan_report.json and scan_report.csv.

Testing Targets:
OWASP Juice Shop
Damn Vulnerable Web Application (DVWA)

Authors:
Gabriella Cedillos-Dixon
Taha Soil

License:
This project is for educational use only.
