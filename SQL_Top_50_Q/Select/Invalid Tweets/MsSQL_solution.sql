-- MsSQL solution for Invalid Tweets

SELECT tweet_id 
FROM Tweets
WHERE LEN(content) > 15;
