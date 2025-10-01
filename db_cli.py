import psycopg2
import getpass

# connection details
host = "csce-315-db.engr.tamu.edu"
db   = "gang_41_db"
user = "gang_41"

# choose your password method lol
password = "gang_41"
# password = getpass.getpass("Password: ")

conn = psycopg2.connect(host=host, dbname=db, user=user, password=password)
cur = conn.cursor()

def print_rows():
    """ print column headers and all the rows in the query"""
    try:
        # Get column names from the cursor description
        if cur.description:
            column_names = [desc[0] for desc in cur.description]
            print("\n--- " + " | ".join(column_names) + " ---")
        
        rows = cur.fetchall()
        
        if not rows:
            print("(no rows to display)")
            return

        for row in rows:
            # To make the output cleaner, convert each item in the row to a string
            print(" | ".join(map(str, row)))

    except psycopg2.ProgrammingError:
        print("(no rows) :(  (PM forces us to work for no money)")

while True:
    print("\nChoose a query:")
    print("0. Exit The Program")
    print("1. Weekly Sales History")
    print("2. Realistic Sales History (by hour)")
    print("3. Peak Sales Day (top 10)")
    print("4. Profit per Drink")
    print("5. Ingredients Almost Out of Stock")
    print("6. Menu Item Inventory (Special Query 4)")
    print("7. Items by Popularity")
    print("8. Most Used Payment Methods")
    print("9. Top 10 Customers by Spend")
    print("10. Total Revenue (SUM totalprice)")
    print("11. Count customers")
    print("12. Count employee_data")
    print("13. Count Total Ingredients")
    print("14. Count inventory")
    print("15. Count menuitems")

    choice = input("Enter choice: ").strip()

    if choice == "0":
        break
    
    # try specific choice made
    try:
        if choice == "1":
            print("Query used:\n")
            print("""SELECT EXTRACT(WEEK FROM orderdate) AS week_number,
                       COUNT(DISTINCT orderid) AS number_of_orders
                FROM order_history
                GROUP BY week_number
                ORDER BY week_number;\n""")
            cur.execute("""
                SELECT EXTRACT(WEEK FROM orderdate) AS week_number,
                       COUNT(DISTINCT orderid) AS number_of_orders
                FROM order_history
                GROUP BY week_number
                ORDER BY week_number;
            """)
            print_rows()

        elif choice == "2":
            print("Query used:\n")
            print("""
                SELECT EXTRACT(HOUR FROM orderdate) AS hour_of_day,
                       COUNT(DISTINCT orderid) AS number_of_orders,
                       SUM(totalprice) AS total_revenue
                FROM order_history
                GROUP BY hour_of_day
                ORDER BY hour_of_day;\n
            """)
            cur.execute("""
                SELECT EXTRACT(HOUR FROM orderdate) AS hour_of_day,
                       COUNT(DISTINCT orderid) AS number_of_orders,
                       SUM(totalprice) AS total_revenue
                FROM order_history
                GROUP BY hour_of_day
                ORDER BY hour_of_day;
            """)
            print_rows()

        elif choice == "3":
            print("Query used:\n")
            print("""SELECT DATE_TRUNC('day', orderdate)::DATE AS sales_day,
                       SUM(totalprice) AS total_revenue
                FROM order_history
                GROUP BY sales_day
                ORDER BY total_revenue DESC
                LIMIT 10;\n""")
            cur.execute("""
                SELECT DATE_TRUNC('day', orderdate)::DATE AS sales_day,
                       SUM(totalprice) AS total_revenue
                FROM order_history
                GROUP BY sales_day
                ORDER BY total_revenue DESC
                LIMIT 10;
            """)
            print_rows()

        elif choice == "4":
            print("Query used:\n")
            print("""SELECT m.item_name, m.cost AS sale_price,
                       SUM(inv.cost * r.quantity) AS ingredient_cost,
                       (m.cost - SUM(inv.cost * r.quantity)) AS profit_per_drink
                FROM MenuItems m
                JOIN DrinkJoinTable r ON m.item_id = r.drink_id
                JOIN Inventory inv ON r.inventory_id = inv.item_id
                GROUP BY m.item_name, m.cost
                ORDER BY profit_per_drink DESC;\n""")
            cur.execute("""
                SELECT m.item_name, m.cost AS sale_price,
                       SUM(inv.cost * r.quantity) AS ingredient_cost,
                       (m.cost - SUM(inv.cost * r.quantity)) AS profit_per_drink
                FROM MenuItems m
                JOIN DrinkJoinTable r ON m.item_id = r.drink_id
                JOIN Inventory inv ON r.inventory_id = inv.item_id
                GROUP BY m.item_name, m.cost
                ORDER BY profit_per_drink DESC;
            """)
            print_rows()

        elif choice == "5":
            print("Query used:\n")
            print("""SELECT item_name, supply, unit
                FROM Inventory
                WHERE supply < 150
                  AND item_name NOT LIKE '%Water & Ice%'
                ORDER BY supply ASC;\n""")
            cur.execute("""
                SELECT item_name, supply, unit
                FROM Inventory
                WHERE supply < 150
                  AND item_name NOT LIKE '%Water & Ice%'
                ORDER BY supply ASC;
            """)
            print_rows()

        elif choice == "6":
            print("Query used:\n")
            print("""SELECT m.item_name,
                       COUNT(r.inventory_id) AS ingredient_count
                FROM MenuItems m
                JOIN DrinkJoinTable r ON m.item_id = r.drink_id
                GROUP BY m.item_name
                ORDER BY m.item_name ASC;\n""")
            cur.execute("""
                SELECT m.item_name,
                       COUNT(r.inventory_id) AS ingredient_count
                FROM MenuItems m
                JOIN DrinkJoinTable r ON m.item_id = r.drink_id
                GROUP BY m.item_name
                ORDER BY m.item_name ASC;
            """)
            print_rows()

        elif choice == "7":
            print("Query used:\n")
            print("""SELECT MenuItemID, SUM(Quantity) AS TotalSold
                FROM order_history
                GROUP BY MenuItemID
                ORDER BY TotalSold DESC;\n""")
            cur.execute("""
                SELECT MenuItemID, SUM(Quantity) AS TotalSold
                FROM order_history
                GROUP BY MenuItemID
                ORDER BY TotalSold DESC;
            """)
            print_rows()

        elif choice == "8":
            print("Query used:\n")
            print("""SELECT paymentmethod, SUM(Quantity) AS usage
                FROM order_history
                GROUP BY paymentmethod
                ORDER BY usage DESC;\n""")
            cur.execute("""
                SELECT paymentmethod, SUM(Quantity) AS usage
                FROM order_history
                GROUP BY paymentmethod
                ORDER BY usage DESC;
            """)
            print_rows()

        elif choice == "9":
            print("Query used:\n")
            print("""SELECT CustomerID, SUM(TotalPrice) AS TotalSpent
                FROM order_history
                GROUP BY CustomerID
                ORDER BY TotalSpent DESC
                LIMIT 10;\n""")
            cur.execute("""
                SELECT CustomerID, SUM(TotalPrice) AS TotalSpent
                FROM order_history
                GROUP BY CustomerID
                ORDER BY TotalSpent DESC
                LIMIT 10;
            """)
            print_rows()

        elif choice == "10":
            print("Query used:\n")
            print("""SELECT SUM(totalprice) FROM order_history;\n""")
            cur.execute("SELECT SUM(totalprice) FROM order_history;")
            print_rows()

        elif choice == "11":
            print("Query used:\n")
            print("""SELECT COUNT(*) FROM customers;\n""")
            cur.execute("SELECT COUNT(*) FROM customers;")
            print_rows()

        elif choice == "12":
            print("Query used:\n")
            print("""SELECT COUNT(*) FROM employee_data;\n""")
            cur.execute("SELECT COUNT(*) FROM employee_data;")
            print_rows()

        elif choice == "13":
            print("Query used:\n")
            print("""SELECT COUNT(*) FROM drinkjointable;\n""")
            cur.execute("SELECT COUNT(*) FROM drinkjointable;")
            print_rows()

        elif choice == "14":
            print("Query used:\n")
            print("""SELECT COUNT(*) FROM inventory;\n""")
            cur.execute("SELECT COUNT(*) FROM inventory;")
            print_rows()

        elif choice == "15":
            print("Query used:\n")
            print("""SELECT COUNT(*) FROM menuitems;\n""")
            cur.execute("SELECT COUNT(*) FROM menuitems;")
            print_rows()

        else:
            print("Invalid choice. PM's fault ")

    except Exception as e:
        print("Error running query:", e)
        print("This error is caused by PM William ")
        break

cur.close()
conn.close()
