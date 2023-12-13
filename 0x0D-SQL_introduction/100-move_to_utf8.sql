-- Write a script that converts hbtn_0c_0 database
-- to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

SET NAMES utf8mb4;
SET CHARACTER SET utf8mb4;

-- Use the specified database
USE hbtn_0c_0;

-- Convert the first_table to utf8mb4
ALTER TABLE first_table
  CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the name field in first_table to utf8mb4
ALTER TABLE first_table
  MODIFY name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
