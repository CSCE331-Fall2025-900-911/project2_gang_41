import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# we have these
menu_items = pd.read_csv("menu_items.csv")
customers = pd.read_csv("customers_data.csv")
employees = pd.read_csv("employee_data.csv")

data = []
num_orders = 160000 # change me for more orders

end_date = datetime.today()
start_date = end_date - timedelta(weeks=52)
order_dates = [fake.date_time_between(start_date=start_date, end_date=end_date) for _ in range(num_orders)]
order_dates.sort()

order_id = 1

for order_date in order_dates:
    customer = customers.sample(1).iloc[0]
    payment_method = random.choice(["cash", "card", "bitcoin", "Turkish Lira", "Japanese Yen", "TSLA stock", "10-year US Series EE Savings Bonds Non-Marketable", "Klarna", "stole it"])

    # weight so most ppl o
    num_items = random.choices([1, 2, 3], weights=[90, 5, 5], k=1)[0]
    chosen_items = menu_items.sample(num_items)

    for _, menu_item in chosen_items.iterrows():
        # weight so most ppl order 1 drink
        quantity = random.choices([1, 2], weights=[90, 10], k=1)[0]
        price = float(menu_item["COST"])
        total = round(price * quantity, 2)
        random_number = random.randint(1, 20)

        data.append({
            "OrderID": order_id,
            "CustomerID": customer["customers_id"],
            "OrderDate": order_date.strftime("%Y-%m-%d %H:%M:%S"),
            "EmployeeAtCheckout": random_number,
            "PaymentMethod": payment_method,
            "MenuItemID": menu_item["ITEM_ID"],
            "ItemName": menu_item["ITEM_NAME"],
            "Quantity": quantity,
            "UnitPrice": price,
            "TotalPrice": total
        })

        # order_item_id += 1

    order_id += 1

# Save CSV
df = pd.DataFrame(data)
df.to_csv("order_final.csv", index=False)

print("order_final.csv in files left sidebar")
