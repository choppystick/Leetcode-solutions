-- MySQL solution for Percentage of Users Attended a Contest
SELECT contest_id, round((count(DISTINCT user_id) * 100/(SELECT COUNT(*) FROM Users)), 2) percentage
FROM Register 
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC

