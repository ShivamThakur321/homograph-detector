# 🛡️ Homograph Detector

A simple Python-based tool to detect **homograph attacks** — where malicious domains use lookalike Unicode characters to impersonate legitimate websites.

---

## 🚀 Features

- Detects non-ASCII characters in domain names
- Converts Unicode domains to ASCII (IDNA/Punycode)
- Compares input domain with trusted domains using fuzzy matching
- CLI-based, lightweight, cross-platform (Kali Linux, Linux, Windows)

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/homograph-detector.git
   cd homograph-detector
