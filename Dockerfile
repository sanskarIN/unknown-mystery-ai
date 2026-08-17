FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN useradd --create-home --uid 10001 appuser

COPY pyproject.toml README.md LICENSE NOTICE ./
COPY src ./src

RUN python -m pip install --no-cache-dir .

USER appuser

CMD ["python", "-c", "import umai; print('UMAI companion', umai.__version__); print('Official store: https://ramsandesh.gumroad.com')"]
