-- MsSQL solution for Queries Quality and Percentage

SELECT 
    query_name,
    ROUND(SUM(CAST(rating AS FLOAT)/position) / COUNT(*), 2) AS quality,
    ROUND(
        (COUNT(CASE WHEN rating < 3 THEN 1 END) * 100.0 / COUNT(*)), 
        2
    ) AS poor_query_percentage
FROM 
    Queries
WHERE 
    query_name IS NOT NULL 
GROUP BY 
    query_name;