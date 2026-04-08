SELECT id AS "opiskelija tunnus", name AS "nimi", group_id AS "ryhma", ects AS "ECTS"
FROM Students AS s
WHERE ects = (
	SELECT MAX(ects)
	FROM Students
	WHERE group_id = s.group_id
)
ORDER BY group_id ASC;