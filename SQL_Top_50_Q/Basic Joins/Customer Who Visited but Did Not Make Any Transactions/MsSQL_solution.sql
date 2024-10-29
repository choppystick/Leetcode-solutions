-- MsSQL solution for Customer Who Visited but Did Not Make Any Transactions

-- Left Join version
SELECT 
    v.customer_id, 
    COUNT(*) AS count_no_trans 
FROM Visits v 
LEFT JOIN Transactions t 
    ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY v.customer_id;

-- Subquery version
SELECT 
    customer_id, 
    COUNT(*) AS count_no_trans 
FROM Visits v 
WHERE (
    SELECT COUNT(*) 
    FROM Transactions t 
    WHERE t.visit_id = v.visit_id
) = 0 
GROUP BY customer_id;
