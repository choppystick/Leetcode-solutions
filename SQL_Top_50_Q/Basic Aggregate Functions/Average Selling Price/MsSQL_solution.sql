-- MsSQL solution for Average Selling Price

SELECT 
    p.product_id, 
    COALESCE(ROUND(CAST(SUM(p.price * u.units) AS FLOAT) / CAST(SUM(u.units) AS FLOAT), 2), 0) AS average_price
FROM Prices p 
LEFT JOIN UnitsSold u ON p.product_id = u.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;