-- MySQL solution for Department Top Three Salaries


SELECT d.name Department, E1.name Employee, E1.salary Salary
FROM Employee E1 LEFT JOIN Department d ON E1.departmentId = d.id
WHERE (
SELECT COUNT(DISTINCT E2.salary)
FROM Employee E2
WHERE E1.departmentId = E2.departmentId AND E1.salary <= E2.salary 
) <= 3