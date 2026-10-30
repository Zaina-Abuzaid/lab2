FROM python:3.13-slim-trixie AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

RUN python -m pip install --no-cache-dir --prefix=/install --upgrade --force-reinstall "setuptools>=78.1.1" "msgpack>=1.2.3" "urllib3>=2.8.0"

FROM python:3.13-slim-trixie AS runtime

RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=builder /install /usr/local

RUN python -m pip install --no-cache-dir --upgrade --force-reinstall "setuptools>=78.1.1" "msgpack>=1.2.3" "urllib3>=2.8.0"

COPY src/ ./src/

COPY model.joblib ./model.joblib

RUN useradd --create-home appuser

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]