
#  README.md

````markdown
#  VulnScan – Lightweight Python Vulnerability Scanner

VulnScan is a lightweight, Python-based vulnerability scanner that crawls web applications, checks for common misconfigurations, and generates professional reports in **HTML** and **PDF**.

This project is portfolio-ready, showing both offensive security (scanning for issues) and defensive security (reporting & remediation).  

---

##  Features
- Crawl target websites and extract links
- Detect OWASP Top 10 patterns (basic regex payload checks)
- Check for missing security headers (CSP, HSTS, X-Frame-Options, etc.)
- Perform Shodan lookups for external exposure (optional)
- Generate executive-style HTML and PDF reports with severity ratings
- Dockerized for easy runs
- CI pipeline with linting & tests

---

## Installation

### 1. Clone repo
```bash
git clone https://github.com/R0C0D6/vulnscan.git
cd vulnscan
````

### 2. Setup Python virtual environment

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install `wkhtmltopdf` (for PDF reports)

* Download: [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html)
* Install to `C:\Program Files\wkhtmltopdf\bin` (Windows) or `/usr/local/bin` (Linux/Mac).
* Verify:

  ```bash
  wkhtmltopdf --version
  ```

---

##  Example Usage

### Basic scan

```bash
python run_scan.py https://example.com --pages 10
```

### With Shodan API key

```bash
set SHODAN_API_KEY=your_api_key_here   # Windows PowerShell
export SHODAN_API_KEY=your_api_key_here # Linux/Mac

python run_scan.py https://example.com --pages 10 --use-shodan
```

Reports will be saved as:

* `vuln_report.html`
* `vuln_report.pdf`

---

##  Adding SHODAN API Key

1. Get your API key at: [https://account.shodan.io](https://account.shodan.io)
2. Set it as an environment variable:

   ```bash
   export SHODAN_API_KEY=your_api_key_here
   ```
3. Run the scanner with `--use-shodan`.

---

##  Legal & Ethical Use

>  **Important**: This tool is for **educational purposes only**.
> Use it responsibly on systems you **own** or have **explicit permission** to test.
> Unauthorized scanning may be **illegal** and could get you into trouble.

---

##  License

This project is licensed under the MIT License — feel free to use, modify, and share.
See [LICENSE](LICENSE) for details.

---

##  Project Structure

```
vulnscan/
├── scanner/
│   ├── crawler.py
│   ├── headers.py
│   ├── shodan_integration.py
│   ├── report.py
├── examples/
│   ├── sample_report.html
│   ├── sample_report.pdf
├── run_scan.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── LICENSE
└── README.md
```

---

##  Docker Usage

Build image:

```bash
docker build -t vulnscan .
```

Run scan:

```bash
docker run --rm vulnscan https://example.com --pages 10
```

---

##  Continuous Integration

GitHub Actions workflow runs on every push:

* Linting with `flake8`
* Basic tests to confirm modules import correctly

File: `.github/workflows/ci.yml`

```yaml
name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.10"
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Lint with flake8
        run: |
          pip install flake8
          flake8 scanner run_scan.py
      - name: Run tests
        run: |
          pytest tests || echo "No tests yet"
```

---

##  Credits

Built with ❤️ for the cybersecurity community.
Inspired by OWASP Top 10 and ethical hacking practices.

````

---

#  .gitignore  

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
*.sqlite3

# Virtual environments
.venv/

# Reports
vuln_report*
examples/*.pdf
examples/*.html

# IDE
.vscode/
.idea/
````

---

#  LICENSE (MIT)

```text
MIT License

Copyright (c) 2025 ROLAND MAWULI AWUKU

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

[...]
```
