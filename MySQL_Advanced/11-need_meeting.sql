-- MySQL Advanced project
-- script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month
CREATE VIEW need_meeting AS
SELECT name FROM students 
WHERE score < 80 
AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH)); 
