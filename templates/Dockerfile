# Dockerfile
FROM python:3.11-slim

# install wkhtmltopdf dependencies and wkhtmltopdf
RUN apt-get update && apt-get install -y \
    build-essential \
    qt5-default \
    libxrender1 \
    libfontconfig1 \
    libssl-dev \
    wget ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# download wkhtmltopdf (stable)
RUN wget -q https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.buster_amd64.deb \
    && apt-get update && apt-get install -y ./wkhtmltox_0.12.6-1.buster_amd64.deb || true \
    && rm wkhtmltox_0.12.6-1.buster_amd64.deb

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV PYTHONUNBUFFERED=1

CMD ["python", "run_scan.py", "https://example.com", "--pages", "5"]
