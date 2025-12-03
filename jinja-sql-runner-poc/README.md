# Jinja2 Rendered POC

## How to Run
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# run and check output
python runner.py --template templates/query.sql.j2 --vars vars.yaml
```