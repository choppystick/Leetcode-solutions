--  MsSQL solution for Immediate Food Delivery II

SELECT ROUND(SUM(CASE WHEN d1.order_date = d1.customer_pref_delivery_date THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS immediate_percentage
FROM Delivery d1 INNER JOIN (
    SELECT customer_id, MIN(order_date) AS min_order
    FROM Delivery
    GROUP BY customer_id
) AS t 
ON d1.customer_id = t.customer_id AND d1.order_date = t.min_order