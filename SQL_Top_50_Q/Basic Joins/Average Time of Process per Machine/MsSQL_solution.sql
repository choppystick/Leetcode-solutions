-- MsSQL solution for Average Time of Process per Machine

SELECT 
    s.machine_id, 
    ROUND(AVG(CAST(e.timestamp - s.timestamp AS FLOAT)), 3) AS processing_time
FROM Activity s 
JOIN Activity e
    ON s.machine_id = e.machine_id 
    AND s.process_id = e.process_id 
    AND s.activity_type = 'start'
    AND e.activity_type = 'end'
GROUP BY s.machine_id;
