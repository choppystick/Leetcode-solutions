-- MsSQL solution for Percentage of Users Attended a Contest

SELECT 
    contest_id,
    CAST(
        ROUND(
            (COUNT(DISTINCT user_id) * 100.0 / 
            (SELECT COUNT(*) FROM Users)), 
            2
        ) AS DECIMAL(10,2)
    ) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;