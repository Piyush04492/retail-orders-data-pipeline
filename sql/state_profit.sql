SELECT state,
       SUM(profit) AS total_profit
FROM df_orders
GROUP BY state
ORDER BY total_profit DESC
LIMIT 5;
