FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml README_PYPI.md ./
COPY src ./src

RUN pip install --no-cache-dir .

LABEL org.opencontainers.image.source="https://github.com/pepkio/pepkio-ddct-clarity"

ENTRYPOINT ["pepkio-ddct-clarity"]
