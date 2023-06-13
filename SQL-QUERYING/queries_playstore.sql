--1. Find app with ID of 1880
SELECT *
FROM analytics
WHERE id =1880;
--2. Find ID and app name for all apps last updated on Aug 01, 2018
SELECT id, app_name
FROM analytics
WHERE last_updated = '2018-08-01';
--3.Count number of apps in each category
SELECT category,
    COUNT(*)
FROM analytics
GROUP BY category;
--4. Find top 5 most reviewed apps and number of views each has
SELECT *
FROM analytics
ORDER BY reviews DESC
LIMIT 5:
--5. Find the app with at least a rating of 4.8 or higher
SELECT *
FROM analytics
WHERE rating >= 4.8
ORDER BY reviews DESC
LIMIT 1;
--6.Find average rating in each category ordered by highest to lowest rated
SELECT category,
    AVG(rating)
FROM analytics
GROUP BY category
ORDER BY avg DESC;
--7. Find name, price, and rating of most expensive app with a rating less than 3
SELECT app_name, price, rating
FROM analytics
WHERE rating < 3
ORDER BY price DESC
LIMIT 1;
--8. Find all apps with min install less than or equal to 50 with a rating, and order by highest to lowest rating
SELECT app_name
FROM analytics
WHERE min_installs <=50
AND rating IS NOT NULL
ORDER By rating DESC;
--9. Find all apps with ratings less than 3 and more than or equal to 10000 reviews
SELECT app_name
FROM analytics
WHERE rating < 3 AND reviews >=10000;
--10. Find top 10 most reviewed apps that cost between .10 and 1.00
SELECT app_name
FROM analytics
WHERE price BETWEEN .1 AND 1.00
LIMIT 10;
--11. Find the most out of date app
SELECT *
FROM analytics
ORDER BY last_updated
LIMIT 1;
--12. Find most expensive app
SELECT *
FROM analytics
ORDER BY price 
LIMIT 1;
--13. Count all reviews in Google Play Store
SELECT SUM(reviews) AS "All Reviews"
FROM analytics;
--14.  Find all categories with 300+ apps in them
SELECT category
FROM analytics
GROUP BY category
HAVING COUNT(*) > 300;
--15. Find the app that has the highest proportion of min_installs to reviews, among apps that have been installed at least 100,000 times. Display the name of the app along with the number of reviews, the min_installs, and the proportion.
SELECT app_name, reviews, min_installs, 
    min_installs/reviews AS proportion
FROM analytics
WHERE min_installs >= 100000
ORDER BY proportion DESC
LIMIT 1;