-- MsSQL solution for Rising Temperature

SELECT today.id 
FROM Weather yesterday 
CROSS JOIN Weather today 
WHERE DATEDIFF(day, yesterday.recordDate, today.recordDate) = 1 
    AND today.temperature > yesterday.temperature;