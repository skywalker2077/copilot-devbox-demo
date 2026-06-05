# copilot-devbox-demo

Dev Box + GitHub Copilot art-of-the-possible demo.

## Overview

A minimal Python Flask REST API used to demonstrate the **intent → agent → PR → governed delivery** workflow using Microsoft Dev Box and GitHub Copilot.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Returns API info |

> **Note:** A `/health` endpoint is intentionally missing — it will be added live by GitHub Copilot during the demo (Issue #1).

## Setup

```bash
pip install -r requirements.txt
python app.py
```

API runs at `http://localhost:5000`.

## Run tests

```bash
pytest test_app.py -v
```

## Architecture

```
Developer (Intent: GitHub Issue)
   ↓
GitHub Copilot Agent
   ↓
Branch → Pull Request → CI (GitHub Actions + CodeQL)
   ↓
Merge → Issue closes automatically
```

## Adapting for WDC

| Item | Personal demo | WDC client demo |
|------|--------------|-----------------|
| `runs-on` | `ubuntu-latest` | `wdc-ubuntu-latest` |
| Repo owner | `skywalker2077` | `WDC-TEST-PLAYORG` |
| PR approvals | 0 | 1 |

---

*Walker Gomes Viana — Accenture / Avanade*
