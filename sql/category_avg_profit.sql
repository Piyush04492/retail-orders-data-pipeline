SELECT category,
       ROUND(AVG(profit), 2) AS avg_profit
FROM df_orders
GROUP BY category
ORDER BY avg_profit DESC;
