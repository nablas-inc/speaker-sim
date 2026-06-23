FROM jrottenberg/ffmpeg:6-ubuntu

RUN apt-get update && apt-get install -y \
    cmake \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN uv venv /opt/venv --python 3.12.4
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
COPY requirements.txt .
RUN uv pip install resemblyzer
RUN uv pip install -r requirements.txt
COPY . .

ENTRYPOINT ["bash", "boot.sh"]
