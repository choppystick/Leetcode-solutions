-- MySQL solution for Rising Temperature

select today.id
FROM Weather yesterday
CROSS JOIN Weather today
where DATEDIFF(today.recordDate, yesterday.RecordDate) = 1 and today.temperature > yesterday.temperature 

