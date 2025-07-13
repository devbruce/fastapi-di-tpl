FROM python:3.13-slim-bookworm

LABEL appname="fastapi-di-tpl"

ARG DEBCONF_NOWARNINGS="yes"
ARG DEBIAN_FRONTEND="noninteractive"

ENV PIP_NO_CACHE_DIR="1"
ENV PATH="/root/.local/bin:${PATH}"

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

WORKDIR /app
COPY ./pyproject.toml .
COPY ./uv.lock .
COPY ./src .

RUN uv sync --locked

ENTRYPOINT ["uv", "run"]
CMD ["uvicorn", "main:create_app", "--host=0.0.0.0", "--port=8000", "--factory"]

EXPOSE 8000
