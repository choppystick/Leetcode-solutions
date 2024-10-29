-- MsSQL solution for Confirmation Rate

SELECT 
    sig.user_id, 
    ROUND(COALESCE(AVG(CASE WHEN action = 'confirmed' THEN 1.0 ELSE 0.0 END), 0), 2) AS confirmation_rate
FROM Signups sig 
LEFT JOIN Confirmations con ON sig.user_id = con.user_id
GROUP BY sig.user_id;
