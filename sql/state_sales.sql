SELECT state,
       SUM(sale_price) AS total_sales
FROM df_orders
GROUP BY state
ORDER BY total_sales DESC
LIMIT 10;
