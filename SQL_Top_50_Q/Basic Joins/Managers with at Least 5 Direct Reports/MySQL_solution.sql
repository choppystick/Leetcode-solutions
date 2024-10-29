-- MySQL solution for Managers with at Least 5 Direct Reports

select E1.name FROM Employee E1 
INNER JOIN (
    select managerId FROM Employee
    GROUP BY managerId
    having count(*) >= 5
) as F on E1.id = F.managerId
