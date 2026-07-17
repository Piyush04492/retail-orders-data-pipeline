SELECT category,
       ROUND(AVG(discount), 2) AS avg_discount,
       ROUND(AVG(profit), 2) AS avg_profit
FROM df_orders
GROUP BY category
ORDER BY avg_discount DESC;
