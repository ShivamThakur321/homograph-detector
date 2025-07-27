
import idna
import difflib
import sys
import re

# Your list of trusted domains
TRUSTED_DOMAINS = [
    "google.com",
    "facebook.com",
    "youtube.com",
    "twitter.com",
    "amazon.com",
    "apple.com","instagram.com","snapchat.com","gmail.com","microsoft.com","whatsapp.com","x.com","wikipedia.org",
    "yahoo.com","reddit.com","linkden.com","netflix.com"
]

def is_similar(domain, trusted_domain):
    return difflib.SequenceMatcher(None, domain, trusted_domain).ratio() > 0.8

def check_domain(domain):
    try:
        ascii_domain = idna.encode(domain).decode('ascii')
    except idna.IDNAError as e:
        return f"[!] IDNA Error: {e}"

    print(f"→ ASCII-encoded domain: {ascii_domain}")

    for trusted in TRUSTED_DOMAINS:
        if is_similar(domain, trusted) and is_similar(ascii_domain, trusted):
            return "Domain is safe to search"
    return f" Warning: Domain '{domain}' is highly risky"


def main():
    print("🔍 Homograph Guard - Detect Homograph Attacks")
    domain = input("Enter the domain name: ").strip()
    result = check_domain(domain)
    print(result)

if __name__ == "__main__":
    main()
