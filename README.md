<h1 align="center">
    FastAPI with Dependency Injector
</h1>

<p align="center">
    <img src="https://github.com/devbruce/fastapi-di-tpl/actions/workflows/test.yml/badge.svg?branch=main" alt="github-action" />
    <img src="https://img.shields.io/github/release/devbruce/fastapi-di-tpl.svg" alt="release" />
    <br>
    <img src="https://img.shields.io/badge/Python-3.14-blue?style=flat&logo=python" alt="python" />
    <img src="https://img.shields.io/badge/FastAPI-0.128-brightgreen?style=flat&logo=fastapi" alt="fastapi" />
    <img src="https://img.shields.io/badge/Dependency Injector-4.48-skyblue?style=flat" alt="dependency-injector" />
</p>

> [!NOTE]  
> This repository is a template of [FastAPI](https://fastapi.tiangolo.com/) with [Dependency Injector](https://python-dependency-injector.ets-labs.org/)

## 📖 How to Set Local Environment

### 🛠️ Prerequisites

- [uv](https://github.com/astral-sh/uv)
- [direnv](https://direnv.net/)

<br>

### ✔️ Set Environment Variables

Copy  [`.envrc.example`](./.envrc.example) to `.envrc` for setting environment variables with [direnv](https://direnv.net/)

```bash
cp .envrc.example .envrc
```

```bash
direnv allow
```

<br>

### ✔️ Create Virtual Environment with [uv](https://github.com/astral-sh/uv)

```bash
uv sync
```

- Activate virtualenv(`.venv`)

```bash
source .venv/bin/activate
```

<br>

### ✔️ Install prek Hooks(`.git/hooks`)

> prek: [Link](https://prek.j178.dev/)

```bash
prek install -t pre-commit
```

```bash
prek install -t pre-push
```

<br>

<details>
  <summary>🖱️ Run Manually</summary>

```bash
prek run
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
> For details on the make commands, refer to the [`Makefile`](./Makefile)

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
