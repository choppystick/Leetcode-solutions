-- MySQL solution for Employee Bonus

SELECT E.name, B.bonus
FROM Employee E LEFT JOIN Bonus B
ON E.empId = B.empId
where B.bonus < 1000 OR B.bonus IS NULL
