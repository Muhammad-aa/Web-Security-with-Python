import argparse
import requests
from urllib.parse import urljoin
import signal
import sys

# Default admin panel paths
DEFAULT_PATHS = [
    "admin", "administrator", "admin/login", "adminpanel",
    "backend", "dashboard", "cpanel", "controlpanel",
    "login", "system", "manage"
]

# Handle Ctrl+C gracefully
def handle_interrupt(signal, frame):
    print("\n[!] Exiting... Goodbye!")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

def find_admin_panels(base_url, paths):
    found_panels = []
    print(f"\n[+] Scanning for admin panels on {base_url}...\n")
    for path in paths:
        url = urljoin(base_url, path)
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"[+] Found: {url}")
                found_panels.append(url)
            else:
                print(f"[-] Not Found: {url}")
        except requests.RequestException as e:
            print(f"[!] Error: Unable to access {url} - {e}")
    return found_panels

def save_results(results, output_file):
    try:
        with open(output_file, "w") as f:
            for url in results:
                f.write(url + "\n")
        print(f"\n[+] Results saved to {output_file}")
    except Exception as e:
        print(f"[!] Error saving results: {e}")

def main():
    parser = argparse.ArgumentParser(description="Admin Panel Finder Tool")
    parser.add_argument(
        "url", help="The base URL of the website to scan (e.g., https://example.com)"
    )
    parser.add_argument(
        "-w",
        "--wordlist",
        help="Path to a custom wordlist file (optional). If not provided, a default wordlist is used.",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="File to save the results (optional).",
    )
    args = parser.parse_args()

    # Load custom wordlist or use default paths
    if args.wordlist:
        try:
            with open(args.wordlist, "r") as f:
                paths = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"[!] Error: Wordlist file {args.wordlist} not found.")
            sys.exit(1)
    else:
        paths = DEFAULT_PATHS

    # Run the admin panel finder
    results = find_admin_panels(args.url, paths)

    if results:
        print("\n[+] Admin panels found:")
        for panel in results:
            print(f"  - {panel}")
        # Save results if an output file is specified
        if args.output:
            save_results(results, args.output)
    else:
        print("\n[-] No admin panels were found.")

if __name__ == "__main__":
    main()
