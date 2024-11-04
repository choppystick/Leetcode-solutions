-- MySQL solution for Immediate Food Delivery II

SELECT ROUND(SUM(d1.order_date=d1.customer_pref_delivery_date) * 100 / COUNT(*), 2) immediate_percentage
FROM Delivery d1 INNER JOIN (
    SELECT customer_id, MIN(order_date) AS min_order
    From Delivery
    GROUP BY customer_id
) AS t 
ON d1.customer_id = t.customer_id AND d1.order_date = t.min_order