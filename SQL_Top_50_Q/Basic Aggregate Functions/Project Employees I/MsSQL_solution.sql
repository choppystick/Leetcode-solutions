-- MsSQL solution for Project Employees I

SELECT project_id, 
    ROUND(AVG(CAST(e.experience_years AS DECIMAL)), 2) AS average_years 
FROM Project p LEFT JOIN Employee e
ON p.employee_id = e.employee_id
GROUP BY p.project_id;