import argparse         # Import library for parsing command-line arguments
import requests         # Import library for making HTTP requests
from bs4 import BeautifulSoup  # Import library for parsing HTML content
from urllib.parse import urljoin, urlparse  # Import URL manipulation functions
import sys             # Import system-specific parameters and functions
import signal          # Import library for handling interrupt signals


class WebsiteCrawler:
    def __init__(self, base_url, max_depth, output_file=None):  # Initialize crawler with base parameters
        self.base_url = base_url  # Store the starting URL
        self.max_depth = max_depth  # Set maximum crawling depth
        self.visited_urls = set()  # Create a set to track visited URLs
        self.output_file = output_file  # Optional output file for saving crawled URLs

        if self.output_file:  # If output file is specified
            with open(self.output_file, "w") as f:  # Open file in write mode
                f.write("Crawled URLs:\n")  # Write header to file

    def crawl(self, url, depth=0):  # Recursive crawling method
        if depth > self.max_depth:  # Stop if max depth is reached
            return

        if url in self.visited_urls:  # Skip already visited URLs
            return

        self.visited_urls.add(url)  # Mark URL as visited
        print(f"[+] [Depth {depth}] Crawling: {url}")  # Print current crawling status

        if self.output_file:  # If output file is specified
            with open(self.output_file, "a") as f:  # Open file in append mode
                f.write(url + "\n")  # Write URL to file

        try:
            response = requests.get(url, timeout=10)  # Send GET request with timeout
            response.raise_for_status()  # Raise exception for bad status codes
        except requests.exceptions.RequestException as e:  # Catch request errors
            print(f"[-] Error accessing {url}: {e}")  # Print error message
            return

        soup = BeautifulSoup(response.text, "html.parser")  # Parse HTML content

        for link in soup.find_all("a", href=True):  # Find all hyperlinks
            href = link["href"]  # Extract href attribute
            full_url = urljoin(url, href)  # Convert relative to absolute URL

            if self.is_same_domain(full_url):  # Check if URL is in same domain
                self.crawl(full_url, depth + 1)  # Recursively crawl with increased depth

    def is_same_domain(self, url):  # Check if URL is in same domain
        base_domain = urlparse(self.base_url).netloc  # Extract base domain
        target_domain = urlparse(url).netloc  # Extract target domain
        return base_domain == target_domain  # Compare domains


def signal_handler(sig, frame):  # Handle keyboard interrupt
    print("\n[!] Program interrupted by user. Exiting...")  # Print exit message
    sys.exit(0)  # Exit program


def main():
    signal.signal(signal.SIGINT, signal_handler)  # Register signal handler for Ctrl+C

    parser = argparse.ArgumentParser(description="Website Crawler")  # Create argument parser
    parser.add_argument("url", help="The base URL to start crawling from")  # URL argument
    parser.add_argument(
        "-d", "--depth", type=int, default=2, help="Maximum depth to crawl (default: 2)"  # Depth argument
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Path to a file where crawled URLs will be saved (optional)"  # Output file argument
    )
    args = parser.parse_args()  # Parse command-line arguments

    try:
        requests.get(args.url, timeout=10).raise_for_status()  # Validate URL
    except requests.exceptions.RequestException as e:  # Catch URL validation errors
        print(f"[-] Error: Invalid URL {args.url}: {e}")  # Print error message
        sys.exit(1)  # Exit with error status

    print(f"[!] Starting crawl at {args.url} with a max depth of {args.depth}")  # Print start message
    if args.output:
        print(f"[!] Crawled URLs will be saved to {args.output}")  # Print output file message

    crawler = WebsiteCrawler(args.url, args.depth, args.output)  # Create crawler instance
    crawler.crawl(args.url)  # Start crawling


if __name__ == "__main__":  # Entry point of the script
    main()  # Call main function


