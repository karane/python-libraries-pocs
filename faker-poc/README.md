# Faker POC

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Generate 500,000 customers in custom file
python generate_customers_large.py -n 500000 --output my_customers.csv

# Default: 1 million rows, 'customers.csv'
python generate_customers_large.py
```