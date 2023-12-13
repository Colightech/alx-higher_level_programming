-- Write a script that converts hbtn_0c_0 database
-- to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

SET NAMES utf8mb4;
SET CHARACTER SET utf8mb4;

USE hbtn_0c_0;

ALTER TABLE first_table
  CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
  MODIFY name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
