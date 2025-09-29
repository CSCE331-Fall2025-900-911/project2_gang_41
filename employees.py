from faker import Faker
fake = Faker()

employee_data = [{
    "employee_id": i,
    "hourly_rate": fake.pyfloat(min_value=12.0, max_value=20.0, right_digits=2),
    "date_hired": fake.date_this_decade(),
    "food_handling_document": f"{fake.name()}_food_handling.pdf",
    "work_documents": ""
    } for i in range(0, 20)]
print(employee_data)