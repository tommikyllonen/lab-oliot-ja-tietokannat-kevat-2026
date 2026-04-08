-- Second letter of the fruit is "a"
SELECT DISTINCT fruit FROM Fruits WHERE SUBSTR(fruit, 2, 1) = 'a';