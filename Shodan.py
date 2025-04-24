import shodan

# Replace with your Shodan API key
SHODAN_API_KEY = "your_shodan_api_key"

def shodan_scan(target):
    api = shodan.Shodan(SHODAN_API_KEY)

    try:
        result = api.host(target)
        print(f"Shodan results for {target}:\n")
        print(f"IP: {result['ip_str']}")
        print(f"Organization: {result.get('org', 'N/A')}")
        print(f"Operating System: {result.get('os', 'N/A')}")
        print("\nOpen Ports:")
        for port in result['ports']:
            print(f"- {port}")

    except shodan.APIError as e:
        print(f"Shodan API error: {e}")

# Example Usage
shodan_scan("8.8.8.8")  # Google's Public DNS Server
