<h1 align="center">
    FastAPI with Dependency Injector
</h1>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python" />
    <img src="https://img.shields.io/badge/FastAPI-0.115-brightgreen?style=flat&logo=fastapi" />
    <img src="https://github.com/devbruce/fastapi-di-tpl/actions/workflows/test.yaml/badge.svg?branch=main" />
</p>

> [!NOTE]  
> This repository is a template of [FastAPI](https://fastapi.tiangolo.com/) with [Dependency Injector](https://python-dependency-injector.ets-labs.org/)

## 📖 How to Set Local Environment

### 🛠️ Prerequisites

- [pyenv](https://github.com/pyenv/pyenv)
- [Poetry](https://python-poetry.org/)
- [direnv](https://direnv.net/)

<br>

### ✔️ Set Environment Variables

Copy  [`.envrc.tpl`](./.envrc.tpl) to `.envrc` for setting environment variables with [direnv](https://direnv.net/)

```bash
cp .envrc.tpl .envrc
```

```bash
direnv allow
```

<br>

### ✔️ Create Virtual Environment with [Poetry](https://python-poetry.org/)

Install python with [pyenv](https://github.com/pyenv/pyenv)

```bash
pyenv install ${PYTHON_VERSION}
```

Set poetry config

```bash
poetry config virtualenvs.in-project true
```

Create virtualenv(`.venv`) with poetry

```bash
poetry env use $(pyenv root)/versions/${PYTHON_VERSION}/bin/python
```

Install python dependencies with poetry([`poetry.lock`](./poetry.lock))

```bash
poetry install
```

Activate virtualenv(`.venv`) with poetry

```bash
poetry shell
```

<br>

### ✔️ Install pre-commit Hooks(`.git/hooks`)

> pre-commit: [Link](https://pre-commit.com/)

```bash
pre-commit install -t pre-commit
```

```bash
pre-commit install -t pre-push
```

<br>

<details>
  <summary>🖱️ Run Manually</summary>

```bash
pre-commit run
```

</details>

<br>

<details>
  <summary>🖱️ How to Skip Hooks</summary>

After installing the hooks, you can use the `--no-verify` option to skip it.

```bash
git commit --no-verify
```

```bash
git push --no-verify
```

</details>

<br><br>

> [!TIP]  
> For details on the make commands, refer to the [`Makefile`](./Makefile).


## 🚀 Run Server on Local

```bash
make run
```

<br>

## 💯 Test

```bash
make test
```

<br>

## ✅ Lint & Format

Check lint & format only

```bash
make check
```

Format

```bash
make format
```

<br><br>

## 👤 Authors

- Maintainer: @devbruce
