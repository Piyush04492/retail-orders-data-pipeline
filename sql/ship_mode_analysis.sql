SELECT ship_mode,
       COUNT(order_id) AS total_orders,
       SUM(sale_price) AS total_sales,
       SUM(profit) AS total_profit
FROM df_orders
GROUP BY ship_mode
ORDER BY total_sales DESC;
