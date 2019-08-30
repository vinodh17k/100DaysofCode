/* SQL stands for Structured Query Language
 Rows = Records
 Columns are represented by fields

• Most Important SQL Commands
---------------------------------------
 SELECT - extracts data from a database
 UPDATE - updates data in a database
 DELETE - deletes data from a database
 INSERT INTO - inserts new data into a database
 CREATE DATABASE - creates a new database
 ALTER DATABASE - modifies a database
 CREATE TABLE - creates a new table
 ALTER TABLE - modifies a table
 DROP TABLE - deletes a table
 CREATE INDEX - creates an index (search key)
 DROP INDEX - deletes an index


Tables represented below are taken from "https://campus.datacamp.com/courses/intro-to-sql-for-data-science/"

 Here the tables are 
 • Table1:"people" and Fields: id(default), name, birthdate, deathdate
 • Table2:"films" and Fields: id(default), title, release_year, country, duration, language, certification, gross, budget
 • Table3:"roles" and Fields: id(default), film_id, person_id, role
 • Table4:"reviews" and Fields: id(default), film_id, num_user, num_critic, imdb_score, num_votes, facebook_likes
*/


/* Selecting name field FROM table people gives output of a single column relating to field 'name'.*/
SELECT name
FROM people;


/* Below query gives output of a data in fields of 'name', 'birthdate' of table 'people'.*/
SELECT name, birthdate
FROM people;


/* Below query gives output of all data from table 'people'.*/
SELECT *
FROM people;


/* Below query gives only distinct data in field 'certification' from table 'films'.*/
/* The catch is here that 'null' data will also be included in the categorization of distinct data values */
SELECT DISTINCT certification
FROM films;


/* Below query gives only the number of distinct values in data in field 'certification' from table 'films'.*/
/* Here 'null' data is excluded in COUNT from distinct data values */
SELECT COUNT(DISTINCT certification)
FROM films;
/* But, the above code doesn't work with Microsoft Access DBs. So, the work-around for that is below */
SELECT Count(*) AS DistinctCertifications
FROM (SELECT DISTINCT certification FROM films);
/* Indirect approach is used as workaround for Microsoft Access DBs */


/* Below query outputs no.of records/rows in table 'people' */
SELECT COUNT(*)
FROM people;


/* Below query shows a output of 'SQL is like salt'. Simple, right? */
/* That's all AS result does. It prints out what the previous statement asks for. */
SELECT 'SQL is like salt'
AS result;
