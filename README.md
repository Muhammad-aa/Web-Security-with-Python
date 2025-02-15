
# **Web Security with Python**  

This repository contains Python scripts and tools designed for **Web Security with Python eBook**. The tools cover various aspects of **web security**, including **information gathering, gaining access, and vulnerability scanning**.  

Each chapter folder contains the tools discussed, with separate **`requirements.txt`** files. Before running any tool, ensure you install the required dependencies:  

```sh
pip install -r requirements.txt
```  

---

## **Chapter 2: Information Gathering**  

This chapter focuses on reconnaissance techniques to **collect information** about target websites.  

### 🔹 **Admin Panel Finder**  

- [`admin_panel_finder.py`](Chapter-2/Admin-Panel-Finder/admin_panel_finder.py) - Scans for potential admin panel locations on a website.  

### 🔹 **Domain Names**  
- [`dns_enumeration.py`](Chapter-2/Domain-names/dns_enumeration.py) - Enumerates DNS records of a target domain.  
- [`domain_info_extractor.py`](Chapter-2/Domain-names/domain_info_extractor.py) - Extracts domain registration and WHOIS information.  
- [`domain_validator.py`](Chapter-2/Domain-names/domain_validator.py) - Checks if a domain is valid and active.  
- [`domain_whois.py`](Chapter-2/Domain-names/domain_whois.py) - Retrieves WHOIS records of a domain.  
- [`subdomain_scanner.py`](Chapter-2/Domain-names/subdomain_scanner.py) - Scans for subdomains associated with a target domain.  
- [`subdomains.txt`](Chapter-2/Domain-names/subdomains.txt) - A wordlist for subdomain enumeration.  

### 🔹 **Email Extracting**  
- [`email_extractor.py`](Chapter-2/Email-extracting/email_extractor.py) - Extracts email addresses from web pages.  

### 🔹 **Port Scanning**  
- [`fast_port_scanner.py`](Chapter-2/Port-scanning/fast_port_scanner.py) - Quickly scans for open ports on a target.  
- [`nmap_port_scanner.py`](Chapter-2/Port-scanning/nmap_port_scanner.py) - Uses **Nmap** to scan ports and services.  
- [`port_scanner.py`](Chapter-2/Port-scanning/port_scanner.py) - A basic port scanner for identifying open ports.  

### 🔹 **Reverse DNS Lookup**  
- [`reverse_dns_lookup.py`](Chapter-2/Reverse-DNS-Lookup/reverse_dns_lookup.py) - Resolves IP addresses back to domain names.  

### 🔹 **Website Crawler**  
- [`website_crawler.py`](Chapter-2/Website-Crawler/website_crawler.py) - Crawls a website to discover internal links and resources.  

---

## **Chapter 3: Gaining Access and Web Utilities**  

This chapter includes tools for **testing authentication mechanisms** and **proxy configurations**.  

### 🔹 **FTP Brute Force**  
- [`ftp_bruteforce.py`](Chapter-3/FTP-Brute-Force/ftp_bruteforce.py) - Attempts to brute-force FTP credentials.  

### 🔹 **HTTP Proxy**  
- [`http_proxy.py`](Chapter-3/HTTP-Proxy/http_proxy.py) - Implements an HTTP proxy for monitoring and modifying requests.  

### 🔹 **Listing FTP Files**  
- [`list_ftp_files.py`](Chapter-3/Listing-FTP-Files/list_ftp_files.py) - Lists available files on an FTP server.  

### 🔹 **Login Password Guesser**  
- [`login_password_guesser.py`](Chapter-3/Login-Password-Guesser/login_password_guesser.py) - Attempts login guesses against a target system.  

### 🔹 **Rotating Proxies**  
- [`free_proxies.py`](Chapter-3/Rotating-Proxies/free_proxies.py) - Fetches and rotates through free proxies for anonymity.  
- [`tor_proxy.py`](Chapter-3/Rotating-Proxies/tor_proxy.py) - Routes traffic through the **Tor network**.  
 

### 🔹 **SSH Brute Force**  
- [`ssh_bruteforce.py`](Chapter-3/SSH-Brute-Force/ssh_bruteforce.py) - Attempts to brute-force SSH credentials.  

### 🔹 **TCP Proxy**  
- [`tcp_proxy.py`](Chapter-3/TCP-Proxy/tcp-proxy.py) - Implements a TCP proxy to intercept and modify network traffic.  

---

## **Chapter 4: Vulnerability Scanning**  

This chapter focuses on **identifying web application vulnerabilities**.  

### 🔹 **Clickjacking Scanner**  
- [`clickjacking_scanner.py`](Chapter-4/Clickjacking-Scanner/clickjacking_scanner.py) - Detects websites vulnerable to **clickjacking attacks**.  

### 🔹 **Command Injection Vulnerability Scanner**  
- [`command_injection_scanner.py`](Chapter-4/Command-Injection-Vulnerability-Scanner/command_injection_scanner.py) - Checks if a website is vulnerable to **command injection attacks**.  

### 🔹 **SQLi Scanner**  
- [`sql_injection_detector.py`](Chapter-4/SQLi-Scanner/sql_injection_detector.py) - Scans for **SQL Injection (SQLi) vulnerabilities** in web applications.  

### 🔹 **XSS Vulnerability Scanner**  
- [`xss_scanner.py`](Chapter-4/XSS-Vulnerability-Scanner/xss_scanner.py) - Detects **Cross-Site Scripting (XSS) vulnerabilities**.  
- [`xss_scanner_extended.py`](Chapter-4/XSS-Vulnerability-Scanner/xss_scanner_extended.py) - An **advanced XSS scanner** with additional payloads.  

---

### **Disclaimer**  
This repository is **strictly for educational and ethical hacking purposes**. Unauthorized use of these scripts on systems without permission is **illegal**. Use them responsibly!  

**Stay ethical and secure the web!**
