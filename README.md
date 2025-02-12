
# **Ethical Website Hacking with Python**  

This repository contains Python scripts and tools designed for **ethical website hacking and security testing**. The tools cover various aspects of **web security**, including **information gathering, gaining access, and vulnerability scanning**.  

Each chapter folder contains the tools discussed, with separate **`requirements.txt`** files. Before running any tool, ensure you install the required dependencies:  

```sh
pip install -r requirements.txt
```  

---

## 📌 **Chapter 2: Information Gathering**  

This chapter focuses on reconnaissance techniques to **collect information** about target websites.  

### 🔹 **Admin Panel Finder**  
- [`admin_panel_finder.py`](admin_panel_finder.py) - Scans for potential admin panel locations on a website.  

### 🔹 **Domain Names**  
- [`dns_enumeration.py`](dns_enumeration.py) - Enumerates DNS records of a target domain.  
- [`domain_info_extractor.py`](domain_info_extractor.py) - Extracts domain registration and WHOIS information.  
- [`domain_validator.py`](domain_validator.py) - Checks if a domain is valid and active.  
- [`domain_whois.py`](domain_whois.py) - Retrieves WHOIS records of a domain.  
- [`subdomain_scanner.py`](subdomain_scanner.py) - Scans for subdomains associated with a target domain.  
- [`subdomains.txt`](subdomains.txt) - A wordlist for subdomain enumeration.  

### 🔹 **Email Extracting**  
- [`email_extractor.py`](email_extractor.py) - Extracts email addresses from web pages.  

### 🔹 **Port Scanning**  
- [`fast_port_scanner.py`](fast_port_scanner.py) - Quickly scans for open ports on a target.  
- [`nmap_port_scanner.py`](nmap_port_scanner.py) - Uses **Nmap** to scan ports and services.  
- [`port_scanner.py`](port_scanner.py) - A basic port scanner for identifying open ports.  

### 🔹 **Reverse DNS Lookup**  
- [`reverse_dns_lookup.py`](reverse_dns_lookup.py) - Resolves IP addresses back to domain names.  

### 🔹 **Website Crawler**  
- [`website_crawler.py`](website_crawler.py) - Crawls a website to discover internal links and resources.  

---

## 🔓 **Chapter 3: Gaining Access**  

This chapter includes tools for **testing authentication mechanisms** and **proxy configurations**.  

### 🔹 **FTP Brute Force**  
- [`ftp_bruteforce.py`](ftp_bruteforce.py) - Attempts to brute-force FTP credentials.  

### 🔹 **HTTP Proxy**  
- [`http_proxy.py`](http_proxy.py) - Implements an HTTP proxy for monitoring and modifying requests.  

### 🔹 **Listing FTP Files**  
- [`list_ftp_files.py`](list_ftp_files.py) - Lists available files on an FTP server.  

### 🔹 **Login Password Guesser**  
- [`login_password_guesser.py`](login_password_guesser.py) - Attempts login guesses against a target system.  

### 🔹 **Rotating Proxies**  
- [`free_proxies.py`](free_proxies.py) - Fetches and rotates through free proxies for anonymity.  
- [`tor_proxy.py`](tor_proxy.py) - Routes traffic through the **Tor network**.  
- [`using_crawlera.py`](using_crawlera.py) - Uses a **web crawling proxy setup**.  

### 🔹 **SSH Brute Force**  
- [`ssh_bruteforce.py`](ssh_bruteforce.py) - Attempts to brute-force SSH credentials.  

### 🔹 **TCP Proxy**  
- [`tcp_proxy.py`](tcp_proxy.py) - Implements a TCP proxy to intercept and modify network traffic.  

---

## 🛡️ **Chapter 4: Vulnerability Scanning**  

This chapter focuses on **identifying web application vulnerabilities**.  

### 🔹 **Clickjacking Scanner**  
- [`clickjacking_scanner.py`](clickjacking_scanner.py) - Detects websites vulnerable to **clickjacking attacks**.  

### 🔹 **Command Injection Vulnerability Scanner**  
- [`command_injection_scanner.py`](command_injection_scanner.py) - Checks if a website is vulnerable to **command injection attacks**.  

### 🔹 **SQLi Scanner**  
- [`sql_injection_detector.py`](sql_injection_detector.py) - Scans for **SQL Injection (SQLi) vulnerabilities** in web applications.  

### 🔹 **XSS Vulnerability Scanner**  
- [`xss_scanner.py`](xss_scanner.py) - Detects **Cross-Site Scripting (XSS) vulnerabilities**.  
- [`xss_scanner_extended.py`](xss_scanner_extended.py) - An **advanced XSS scanner** with additional payloads.  

---

### ⚠️ **Disclaimer**  
This repository is **strictly for educational and ethical hacking purposes**. Unauthorized use of these scripts on systems without permission is **illegal**. Use them responsibly!  

🚀 **Stay ethical and secure the web!**
