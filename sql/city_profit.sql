SELECT city,
       SUM(profit) AS total_profit
FROM df_orders
GROUP BY city
ORDER BY total_profit DESC
LIMIT 10;
