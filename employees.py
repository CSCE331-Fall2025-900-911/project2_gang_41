from faker import Faker
import psycopg2
fake = Faker()

#  pip install psycopg2-binary

employee_data = [{
    "employee_id": i,
    "hourly_rate": fake.pyfloat(min_value=12.0, max_value=20.0, right_digits=2),
    "date_hired": fake.date_this_decade(),
    "food_handling_document": f"{fake.name()}_food_handling.pdf",
    "work_documents": ""
    } for i in range(0, 20)]
print(employee_data)

try:
    conn = psycopg2.connect(
        dbname="your_database_name",
        user="your_username",
        password="your_password",
        host="your_host",  # e.g., "localhost"
        port="your_port"    # e.g., 5432
    )
    print("Connected to PostgreSQL successfully!")
except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL: {e}")

cursor = conn.cursor()

for employee in employee_data:
    sql = f"INSERT INTO employees VALUES ({employee.id}, {employee.hourly_rate}, {employee.date_hired}, {employee.food_handling_document}, {employee.work_documents});"
    cursor.execute(sql)
    conn.commit()