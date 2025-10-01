-- Step 1: Truncate all tables to clear existing data
\echo '--- Truncating all tables... ---'
TRUNCATE TABLE
    customers,
    drinkjointable,
    employee_data,
    inventory,
    menuitems,
    order_history
RESTART IDENTITY CASCADE;
\echo '--- All tables have been cleared. ---'

-- Step 2: Repopulate tables from CSV files
\echo '--- Starting data population... ---'
\copy employee_data FROM 'C:\Users\willi\Downloads\employee_data.csv' CSV HEADER;
\copy customers FROM 'C:\Users\willi\Downloads\customers_data.csv' CSV HEADER;
\copy menuitems FROM 'C:\Users\willi\Downloads\MenuItems.csv' CSV HEADER;
\copy inventory FROM 'C:\Users\willi\Downloads\Inventory.csv' CSV HEADER;
\copy order_history FROM 'C:\Users\willi\Downloads\order_final.csv' CSV HEADER;
\copy drinkjointable FROM 'C:\Users\willi\Downloads\DrinkJoinTable.csv' CSV HEADER;
\echo '--- ✅ Data population complete. ---'