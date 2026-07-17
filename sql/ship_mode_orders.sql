SELECT ship_mode,
       COUNT(order_id) AS total_orders
FROM df_orders
GROUP BY ship_mode
ORDER BY total_orders DESC;
