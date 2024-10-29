-- MySQL solution for Confirmation Rate

SELECT sig.user_id, round(coalesce(avg(action = 'confirmed'), 0) , 2) confirmation_rate
FROM Signups sig LEFT JOIN Confirmations con
on sig.user_id = con.user_id
GROUP BY sig.user_id
