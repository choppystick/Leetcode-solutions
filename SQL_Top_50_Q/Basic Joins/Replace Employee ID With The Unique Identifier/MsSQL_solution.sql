-- MsSQL solution for Replace Employee ID With The Unique Identifier

SELECT 
    uni.unique_id, 
    emp.name
FROM Employees emp 
LEFT JOIN EmployeeUNI uni ON emp.id = uni.id;
