SELECT *
FROM order_history
WHERE order_date >= DATEADD(day, -7, GETDATE());