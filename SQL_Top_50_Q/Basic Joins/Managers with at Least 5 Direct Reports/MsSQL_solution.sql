-- MsSQL solution for Managers with at Least 5 Direct Reports

SELECT E1.name 
FROM Employee E1 
INNER JOIN (
    SELECT managerId 
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) >= 5
) AS F ON E1.id = F.managerId;
