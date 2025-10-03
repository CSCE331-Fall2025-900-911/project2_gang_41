import csv
import random
from faker import Faker
from datetime import date

# Initialize the Faker generator
fake = Faker()

# --- Job and Pay Definitions ---
job_pay_scales = {
    "Staff Member": {"min": 15.00, "max": 16.50},
    "Cashier":      {"min": 16.00, "max": 17.50},
    "Manager":      {"min": 22.00, "max": 25.00},
    "Store Owner":  {"min": 35.00, "max": 40.00}
}

# --- Structured Data Generation ---

# 1. Generate all employee records WITHOUT assigning final IDs yet
temp_employee_list = []

# Generate the Store Owner with the earliest date
owner_hire_date = date(2019, 2, 6)
owner_rate = round(random.uniform(job_pay_scales["Store Owner"]["min"], job_pay_scales["Store Owner"]["max"]), 2)
temp_employee_list.append({
    "employee_name": fake.name(), # <-- ADDED
    "job_title": "Store Owner",
    "hourly_rate": owner_rate,
    "date_hired": owner_hire_date
})

# Define hire date ranges for other roles
manager_start_date = date(2019, 3, 1)
manager_end_date = date(2020, 12, 31)
staff_start_date = date(2021, 1, 1)
staff_end_date = date.today()

# Create and shuffle the list of remaining jobs
remaining_jobs = (
    ["Manager"] * 2 +
    ["Cashier"] * 5 +
    ["Staff Member"] * 12
)
random.shuffle(remaining_jobs)

# Generate the remaining 19 employees
for job_title in remaining_jobs:
    pay_range = job_pay_scales[job_title]
    hourly_rate = round(random.uniform(pay_range["min"], pay_range["max"]), 2)

    if job_title == "Manager":
        hire_date = fake.date_between(start_date=manager_start_date, end_date=manager_end_date)
    else: # For Cashiers and Staff Members
        hire_date = fake.date_between(start_date=staff_start_date, end_date=staff_end_date)
    
    temp_employee_list.append({
        "employee_name": fake.name(), # <-- ADDED
        "job_title": job_title,
        "hourly_rate": hourly_rate,
        "date_hired": hire_date,
    })

# 2. Sort the entire list by the date hired
temp_employee_list.sort(key=lambda record: record['date_hired'])

# 3. Now, create the final list by iterating through the sorted list and assigning the IDs
employee_data = []
for index, record in enumerate(temp_employee_list):
    employee_data.append({
        "employee_id": index, # Assign ID based on the sorted order
        "employee_name": record['employee_name'], # <-- ADDED
        "job_title": record['job_title'],
        "hourly_rate": record['hourly_rate'],
        "date_hired": record['date_hired']
    })

# --- Print and Write to CSV ---

csv_file_name = "employee_data.csv"
headers = employee_data[0].keys()

print("--- Final Chronological Employee Data ---")
for record in employee_data:
    print(record)

try:
    with open(csv_file_name, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(employee_data)

    print(f"\n✅ Successfully created the file: {csv_file_name}")

except IOError:
    print("I/O error")