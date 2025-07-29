-- MYSQL advanced project
-- script that creates a metal_bands table with attributes origin and fans_number
SELECT origin, SUM(fans)
AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
