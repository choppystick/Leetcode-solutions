-- MySQL solution for Customer Who Visited but Did Not Make Any Transactions

-- Left Join version:
SELECT V.customer_id, count(*) AS count_no_trans
FROM Visits V LEFT JOIN Transactions T
ON V.visit_id = T.visit_id
WHERE T.transaction_id IS NULL
GROUP BY V.customer_id

-- Subquery version:
SELECT customer_id, COUNT(*) as count_no_trans
FROM Visits v
WHERE (
    SELECT COUNT(*) 
    FROM Transactions t 
    WHERE t.visit_id = v.visit_id
) = 0
GROUP BY customer_id;
