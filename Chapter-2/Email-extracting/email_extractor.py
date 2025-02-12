import re  # Import regular expression module for pattern matching
import requests  # Import library for making HTTP requests
from bs4 import BeautifulSoup  # Import library for parsing HTML content
from urllib.parse import urljoin, urlparse  # Import URL manipulation functions
import logging  # Import logging module for error tracking and logging

# Configure logging with timestamp, log level, and message format
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_emails_from_text(text):
    """Extract emails from a given text using regex."""
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'  # Regex pattern for email validation
    return re.findall(email_pattern, text)  # Find and return all matching email addresses

def extract_emails_from_url(url, scanned_urls, scan_entire_site):
    """Extract emails from a given URL. Optionally, scan the entire site."""
    emails = set()  # Create a set to store unique email addresses
    try:
        logging.info(f"Scanning URL: {url}")  # Log the URL being scanned
        response = requests.get(url, timeout=10)  # Send GET request with timeout
        response.raise_for_status()  # Raise exception for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')  # Parse HTML content

        # Extract emails from the current page's text
        emails.update(extract_emails_from_text(response.text))

        if scan_entire_site:
            # Find and scan all links on the page if entire site scanning is enabled
            base_url = "{}://{}".format(urlparse(url).scheme, urlparse(url).netloc)  # Construct base URL
            for link in soup.find_all('a', href=True):  # Find all hyperlinks
                absolute_link = urljoin(base_url, link['href'])  # Convert relative to absolute URL
                if absolute_link not in scanned_urls and base_url in absolute_link:
                    scanned_urls.add(absolute_link)  # Mark URL as scanned
                    # Recursively scan links and update email set
                    emails.update(extract_emails_from_url(absolute_link, scanned_urls, scan_entire_site))

    except requests.Timeout:
        logging.error(f"Timeout occurred while trying to access {url}")  # Log timeout error
    except requests.ConnectionError:
        logging.error(f"Connection error while trying to access {url}")  # Log connection error
    except requests.RequestException as e:
        logging.error(f"Error accessing {url}: {e}")  # Log general request errors
    except Exception as e:
        logging.error(f"An unexpected error occurred while scanning {url}: {e}")  # Log unexpected errors

    return emails  # Return set of unique email addresses

def main():
    print("Email Extractor")  # Print script title
    try:
        url = input("Enter the URL to scan: ").strip()  # Prompt for URL input
        if not url.startswith(("http://", "https://")):
            raise ValueError("Invalid URL. Make sure it starts with http:// or https://.")  # Validate URL format
        
        scan_choice = input("Scan one page or the entire website? (page/site): ").strip().lower()  # Prompt for scanning scope
        output_choice = input("Output to console or save to file? (console/file): ").strip().lower()  # Prompt for output method

        scan_entire_site = scan_choice == 'site'  # Determine if entire site should be scanned
        scanned_urls = set()  # Create set to track scanned URLs
        scanned_urls.add(url)  # Add initial URL to scanned URLs

        print("Scanning... This may take a while for larger websites.")
        emails = extract_emails_from_url(url, scanned_urls, scan_entire_site)  # Extract emails

        if output_choice == 'file':
            if emails:
                file_name = input("Enter the filename to save emails (e.g., emails.txt): ").strip()  # Prompt for filename
                try:
                    with open(file_name, 'w') as file:
                        file.write("\n".join(emails))  # Write emails to file
                    print(f"Emails saved to {file_name}")
                except IOError:
                    logging.error("Failed to write to file. Please check the filename and try again.")  # Log file writing error
            else:
                print("No emails found. File not created.")
        else:
            print("\nExtracted Emails:")
            print("\n".join(emails))  # Print emails to console

    except ValueError as ve:
        logging.error(f"Input error: {ve}")  # Log input validation errors
    except Exception as e:
        logging.error(f"An unexpected error occurred in the main function: {e}")  # Log unexpected main function errors

if __name__ == "__main__":  # Entry point of the script
    main()  # Call main function


