FROM python:3.12.7-slim-bookworm

LABEL appname "fastapi-di-tpl"

ARG DEBCONF_NOWARNINGS="yes"
ARG DEBIAN_FRONTEND="noninteractive"

ENV PIP_NO_CACHE_DIR "1"
ENV PATH "/usr/local/bin:${PATH}"

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/usr/local python -

WORKDIR /app
COPY ./pyproject.toml .
COPY ./poetry.lock .
COPY ./src .

RUN poetry config virtualenvs.create false && poetry install --only main

ENTRYPOINT ["poetry", "run"]
CMD ["uvicorn", "main:create_app", "--host=0.0.0.0", "--port=8000", "--factory"]

EXPOSE 8000
