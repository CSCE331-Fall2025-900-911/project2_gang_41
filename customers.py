# This file generates the customers_data.csv file

import csv
import random
from datetime import datetime
from faker import Faker

# Initialize the Faker generator
fake = Faker()

# --- Configuration ---
num_customers = 300
csv_file_name = "customers_data.csv"
owner_signup_date = datetime(2019, 2, 6)

# --- Generate Customer Data ---

# 1. Generate customer records WITHOUT IDs first
temp_customer_list = []
for _ in range(num_customers):
    # Use Faker to generate a random datetime between the owner's sign-up and now
    sign_up_datetime = fake.date_time_between(start_date=owner_signup_date, end_date='now')

    temp_customer_list.append({
        "customer_name": fake.name(),
        "points": random.randint(0, 1000),
        "sign_up_date": sign_up_datetime
    })

# 2. Sort the list chronologically by the sign-up date
temp_customer_list.sort(key=lambda record: record['sign_up_date'])

# 3. Create the final list, assigning IDs and formatting the date string
customer_data = []
for index, record in enumerate(temp_customer_list):
    customer_data.append({
        "customers_id": index + 1, # Assign ID based on sorted order (starts at 1)
        "customer_name": record['customer_name'],
        "points": record['points'],
        "sign_up_date": record['sign_up_date'].strftime("%Y-%m-%d %H:%M:%S")
    })

# --- Print to Console ---
print("--- Chronological Customer Data ---")
# Optional: print only the first 20 records to keep the output clean
for record in customer_data[:20]:
    print(record)

# --- Write to CSV File ---
if customer_data:
    headers = customer_data[0].keys()
    try:
        with open(csv_file_name, 'w', newline='', encoding='utf-8') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(customer_data)
        print(f"\n✅ Successfully created the file: {csv_file_name}")
    except IOError as e:
        print(f"I/O error: {e}")
else:
    print("No customer data to write to CSV.")