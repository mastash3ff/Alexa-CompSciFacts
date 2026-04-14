# Comp Sci Facts

![Deploy](https://github.com/mastash3ff/Alexa-CompSciFacts/actions/workflows/deploy.yml/badge.svg)

An Alexa skill that delivers random computer science facts covering data structures, algorithms, and sorting complexities.

## Usage

**Invocation:** `comp sci facts`

| Say... | Response |
|--------|----------|
| "Alexa, open comp sci facts" | Speaks a random fact and closes |
| "Tell me a comp sci fact" | Delivers another fact |
| "Help" | Lists available commands |
| "Stop" / "Exit" | Ends the skill |

## Development

**Stack:** Python 3.12 · ASK SDK v2 · AWS Lambda (us-east-1)

```bash
# Install dependencies
pip install -r src/requirements.txt

# Run tests
PYTHONPATH=src pytest tests/ -v

# Deploy — automatic on push to master via GitHub Actions
```

## Project structure

```
src/lambda_function.py      Intent handlers and fact bank (23 facts)
src/requirements.txt        ask-sdk-core dependency
tests/test_skill.py         Unit tests
.github/workflows/          CI/CD — tests gate deployment to Lambda
```
