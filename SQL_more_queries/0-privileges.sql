-- Create users if they do not exist (for setup purposes)
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant privileges to users (for setup purposes)
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT SELECT, INSERT ON *.* TO 'user_0d_2'@'localhost';

-- Reload privileges to ensure they are applied
FLUSH PRIVILEGES;

-- Show the grants for each user
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
