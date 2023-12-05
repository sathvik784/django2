-- create new table countries
CREATE TABLE countries (
    country_code VARCHAR(50) PRIMARY KEY,
    country_name VARCHAR(50)
);

-- insert row into new table
INSERT INTO countries VALUES ("USA", "United States of America");

-- If you try to do this again, it should throw an error (duplicate key)
INSERT INTO countries VALUES ("USA", "United States of America");

INSERT INTO countries VALUES ("UK", "United Kingdom");

-- Basic Join
select * from Customers, Countries where Customers.country = Countries.country_code;
