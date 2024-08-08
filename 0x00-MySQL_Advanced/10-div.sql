-- A SQL script that creates a function SafeDiv that divides


DELIMITER //

DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
NO SQL
BEGIN
    DECLARE res FLOAT;
    
    IF b = 0 THEN
        SET res = 0;
    ELSE
        SET res = a / b;
    END IF;
    
    RETURN res;
END//

DELIMITER ;