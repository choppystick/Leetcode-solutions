-- MySQL solution for Replace Employee ID With The Unique Identifier

select uni.unique_id, emp.name
from Employees emp LEFT JOIN EmployeeUNI uni
on emp.id = uni.id
