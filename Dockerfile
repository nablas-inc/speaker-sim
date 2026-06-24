FROM python:3.12.4-slim

RUN apt-get update && apt-get install -y \
    cmake \
    build-essential \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENTRYPOINT ["bash", "boot.sh"]
