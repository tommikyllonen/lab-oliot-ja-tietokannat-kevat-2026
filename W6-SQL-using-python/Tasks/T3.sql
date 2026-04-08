SELECT city, COUNT(*) AS account_count
FROM Accounts
GROUP BY city
HAVING COUNT(*) >= 5
ORDER BY city ASC; 