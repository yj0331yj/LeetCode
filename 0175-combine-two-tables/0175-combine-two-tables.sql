# Write your MySQL query statement below
SELECT 
    P.firstName, 
    P.lastName, 
    CASE 
        WHEN A.city = '' THEN 'Null'
        ELSE A.city END AS city,
        A.state
FROM Person AS P
LEFT JOIN Address AS A ON P.personId = A.personId;
