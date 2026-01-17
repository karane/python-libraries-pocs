import csv
import random
from faker import Faker
from datetime import datetime
import argparse

def generate_customer(fake):
    """Generate a single fake customer record."""
    gender = random.choice(["Male", "Female"])
    first_name = fake.first_name_male() if gender == "Male" else fake.first_name_female()
    last_name = fake.last_name()
    full_name = f"{first_name} {last_name}"
    
    return {
        "customer_id": fake.uuid4(),
        "full_name": full_name,
        "gender": gender,
        "email": fake.email(),
        "phone": fake.phone_number(),
        "country": fake.country(),
        "city": fake.city(),
        "join_date": fake.date_between(start_date='-5y', end_date='today'),
        "is_active": random.choice([True, False]),
        "total_spent": round(random.uniform(10, 5000), 2)
    }

def generate_customers_csv(filename, num_records, chunk_size=10_000):
    """Generate a large CSV file with fake customer data efficiently."""
    fake = Faker()
    Faker.seed(42)
    random.seed(42)

    start_time = datetime.now()
    print(f"⏳ Generating {num_records:,} customer records...")

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "customer_id", "full_name", "gender", "email", "phone",
            "country", "city", "join_date", "is_active", "total_spent"
        ])
        writer.writeheader()

        for i in range(num_records):
            writer.writerow(generate_customer(fake))
            
            # Log progress every chunk_size
            if (i + 1) % chunk_size == 0:
                print(f"✅ {i + 1:,} rows written...")

    duration = datetime.now() - start_time
    print(f"\n✅ Done! {num_records:,} customers saved to '{filename}' in {duration}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a large CSV of synthetic customer data.")
    parser.add_argument("-n", type=int, default=1_000_000, help="Number of customer rows to generate")
    parser.add_argument("--output", type=str, default="customers.csv", help="Output CSV filename")
    
    args = parser.parse_args()
    
    generate_customers_csv(filename=args.output, num_records=args.n)
