## 3. The terms

| Term | What it is | Analogy |
|---|---|---|
| `backend/` | The folder for server-side code: the data, the logic, and the API that apps call. "Frontend" is what users see (web or iOS). | The kitchen, not the dining room |
| `uv` | Installs Python versions and libraries, and creates a private environment (`.venv`) per project. `uv.lock` records exact versions so every machine installs the same thing. | App Store + receipt for your project |
| lint / `ruff` | A linter reads code without running it and flags likely bugs, unused imports and style problems. `ruff` is the linter (and formatter) we use. | Spell-check plus grammar-check |
| `mypy` | A type checker. It checks that you pass the right kind of data, e.g. a number where a number is expected, using hints like `def main() -> None`. | Checking the plug fits before switching on |
| `pytest` | Runs tests: small functions that call your code and assert the result. See `backend/tests/test_smoke.py`. | A checklist the robot re-runs forever |
| `.toml` | A simple config file format (`key = "value"` under `[sections]`). `pyproject.toml` holds the project's name, dependencies and settings for ruff, mypy and pytest in one place. | The project's settings page |
