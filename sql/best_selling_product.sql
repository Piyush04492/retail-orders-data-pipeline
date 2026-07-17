WITH ranked_products AS (
    SELECT
        category,
        product_id,
        SUM(sale_price) AS total_sales,
        ROW_NUMBER() OVER(
            PARTITION BY category
            ORDER BY SUM(sale_price) DESC
        ) AS rn
    FROM df_orders
    GROUP BY category, product_id
)
SELECT category,
       product_id,
       total_sales
FROM ranked_products
WHERE rn = 1;
