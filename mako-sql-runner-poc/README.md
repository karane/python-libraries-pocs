# Mako SQL Runner - POC

## How to Run
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# run and check output
python render.py \
  --template query.sql.mako \
  --vars '{"roles": ["admin", "editor"], "ages": [20, 25, 30], "limit": 100}'
```