-- script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO second_table (id, name, score) VALUES (3, "Bob", 14);
INSERT INTO second_table (id, name, score) VALUES (1, "John", 10);
INSERT INTO second_table (id, name, score) VALUES (4, "George", 8);
INSERT INTO second_table (id, name, score) VALUES (2, "Alex", 3);

