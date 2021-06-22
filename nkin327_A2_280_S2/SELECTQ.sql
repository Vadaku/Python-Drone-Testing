SELECT *
FROM `Operator`
WHERE First_Name = "Bob" AND Family_Name = "Marley"
LIMIT 0 , 30

SELECT *
FROM `Operator`
ORDER BY Family_Name, First_Name ASC

SELECT *
FROM `drones`
WHERE Operator_ID IS null

SELECT * 
FROM `drones`
WHERE Operator_ID IS NOT null
