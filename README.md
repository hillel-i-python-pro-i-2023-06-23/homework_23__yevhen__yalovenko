# Django homework-23. REST API

---
[![Main workflow](https://github.com/hillel-i-python-pro-i-2023-06-23/Django_base_project_YY/actions/workflows/main-workflow.yml/badge.svg)](https://github.com/hillel-i-python-pro-i-2023-06-23/Django_base_project_YY/actions/workflows/main-workflow.yml)
## 🏠 Django project

Base project

### ▶️ Run

Make all actions needed for run homework from zero. Including configuration.

```shell
make d-homework-i-run
```

### 🚮 Purge

Make all actions needed for run homework from zero.

```shell
make d-homework-i-purge
```

---

## 🛠️ Dev

### Initialize dev

Install dependencies and register pre-commit.

```shell
make init-dev
```

### ⚙️ Configure

Configure homework.

```shell
make init-configs
```

Make migrations

```shell
make migrations
```

Migrate

```shell
make migrate
```

Create Admin

```shell
make create-admin
```
---

## 🐳 Docker

Use services in dockers.

### ▶️ Run

Just run

```shell
make d-run
```

### ⏹️Stop

Stop services

```shell
make d-stop
```

### 🚮 Purge

Purge all data related with services

```shell
make d-purge
```
