-- poista kaikki hedelmät, jotka sisältävät Folaatti (foolihappo) vitamiinia, eli esim kaikki omenat jos
--yhdelläkin omena rivillä on foliaatti happoa

SELECT name, vitamin, value
FROM Fruit
WHERE name NOT IN (
    SELECT name
    FROM Fruit
    WHERE vitamin = 'Folate (folic acid)'
) ORDER BY name DESC, vitamin ASC;