SELECT category,
       SUM(quantity) AS total_quantity
FROM df_orders
GROUP BY category
ORDER BY total_quantity DESC;
