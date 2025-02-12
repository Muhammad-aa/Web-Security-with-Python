import requests
import sys
from colorama import init, Fore

def check_clickjacking_protection(url):
    """
    Check if a website is vulnerable to clickjacking by examining security headers.
    Returns a tuple of (is_vulnerable, details)
    """
    try:
        # Add scheme if not present
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url

        # Make the request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, allow_redirects=True)
        
        # Get the headers we care about
        x_frame_options = response.headers.get('X-Frame-Options', '').upper()
        csp = response.headers.get('Content-Security-Policy', '')
        
        # Check X-Frame-Options header
        xfo_protected = x_frame_options in ['DENY', 'SAMEORIGIN']
        
        # Check CSP frame-ancestors directive
        csp_protected = False
        if 'frame-ancestors' in csp:
            csp_protected = True
        
        # Site is vulnerable if neither protection is in place
        is_vulnerable = not (xfo_protected or csp_protected)
        
        details = {
            'url': url,
            'status_code': response.status_code,
            'x_frame_options': x_frame_options if x_frame_options else 'Not Set',
            'csp_frame_ancestors': 'Present' if csp_protected else 'Not Set',
            'is_vulnerable': is_vulnerable
        }
        
        return is_vulnerable, details
    
    except requests.exceptions.RequestException as e:
        return True, {
            'url': url,
            'error': str(e),
            'is_vulnerable': True
        }

def print_results(details):
    """Pretty print the scan results"""
    print("\n[!] Clickjacking Vulnerability Scan Results")
    print("=" * 50)
    print(f"URL: {details['url']}")
    
    if 'error' in details:
        print(f"\nError: {details['error']}")
        return
    
    print(f"[!] Status Code: {details['status_code']}")
    print("\n[!] Security Headers:")
    print(f"[!] - X-Frame-Options: {details['x_frame_options']}")
    print(f"[!] - CSP frame-ancestors: {details['csp_frame_ancestors']}")
    
    if details['is_vulnerable']:
        print(f"\n{Fore.RED}[-] VULNERABLE: This site may be vulnerable to clickjacking!")
        print(f"\n{Fore.WHITE}[!] Missing both X-Frame-Options and CSP frame-ancestors protections.")
    else:
        print(f"\n[+] {Fore.GREEN}PROTECTED: This site has clickjacking protections in place.")
    
    print(f"{Fore.WHITE}\nRecommendations:")
    if details['x_frame_options'] == 'Not Set':
        print("[!] - Add X-Frame-Options header with DENY or SAMEORIGIN value")
    if details['csp_frame_ancestors'] == 'Not Set':
        print("[!] - Add Content-Security-Policy header with frame-ancestors directive")

def main():
    init()  # Initialize colorama
    
    if len(sys.argv) != 2:
        print("Usage: python clickjacking_scanner.py <url>")
        print("Example: python clickjacking_scanner.py example.com")
        sys.exit(1)
    
    url = sys.argv[1]
    is_vulnerable, details = check_clickjacking_protection(url)
    print_results(details)

if __name__ == "__main__":
    main()