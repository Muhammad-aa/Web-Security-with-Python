import argparse         # For parsing command-line arguments
import requests         # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML content
from urllib.parse import urljoin, urlparse  # For URL manipulation
import sys             # For system-related operations
import signal          # For handling interrupt signals


class WebsiteCrawler:
    def __init__(self, base_url, max_depth, output_file=None):
        self.base_url = base_url
        self.max_depth = max_depth
        self.visited_urls = set()
        self.output_file = output_file

        if self.output_file:
            with open(self.output_file, "w") as f:
                f.write("Crawled URLs:\n")

    def crawl(self, url, depth=0):
        if depth > self.max_depth:
            return

        # Ensure we don't visit the same URL twice
        if url in self.visited_urls:
            return

        self.visited_urls.add(url)
        print(f"[+] [Depth {depth}] Crawling: {url}")

        # Save the URL to the output file if specified
        if self.output_file:
            with open(self.output_file, "a") as f:
                f.write(url + "\n")

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"[-] Error accessing {url}: {e}")
            return

        soup = BeautifulSoup(response.text, "html.parser")

        # Find all links on the page
        for link in soup.find_all("a", href=True):
            href = link["href"]
            full_url = urljoin(url, href)

            # Ensure the link stays within the base domain
            if self.is_same_domain(full_url):
                self.crawl(full_url, depth + 1)

    def is_same_domain(self, url):
        base_domain = urlparse(self.base_url).netloc
        target_domain = urlparse(url).netloc
        return base_domain == target_domain


def signal_handler(sig, frame):
    print("\n[!] Program interrupted by user. Exiting...")
    sys.exit(0)


def main():
    # Handle Ctrl+C gracefully
    signal.signal(signal.SIGINT, signal_handler)

    parser = argparse.ArgumentParser(description="Website Crawler")
    parser.add_argument("url", help="The base URL to start crawling from")
    parser.add_argument(
        "-d", "--depth", type=int, default=2, help="Maximum depth to crawl (default: 2)"
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Path to a file where crawled URLs will be saved (optional)",
    )
    args = parser.parse_args()

    # Validate the URL
    try:
        requests.get(args.url, timeout=10).raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"[-] Error: Invalid URL {args.url}: {e}")
        sys.exit(1)

    print(f"[!] Starting crawl at {args.url} with a max depth of {args.depth}")
    if args.output:
        print(f"[!] Crawled URLs will be saved to {args.output}")

    crawler = WebsiteCrawler(args.url, args.depth, args.output)
    crawler.crawl(args.url)


if __name__ == "__main__":
    main()
