/*THESE ARE COMMANDS TO APPLY WHEN WE HAVE THE MICROSOFT SQL SERVER's COMMAND LINE INTERFACE
        WE LIKE TO CREATE A DB, TWO TABLES AND SOME VALUES INTO THEM
*/

\ld
CREATE DATABASE company
use company
create table productos (id INT NOT NULL PRIMARY KEY, nombre VARCHAR(8), precio_gramo DECIMAL(5,1))
\d dbo."productos"
CREATE TABLE inventarios (id INT NOT NULL PRIMARY KEY, id_prod INT NOT NULL, peso_gramo DECIMAL(5,1) NOT NULL)
\lt
INSERT INTO "dbo"."productos" VALUES (1, "Pera", 12.5) , (2, "Durazno", 45.8) , (3, "Manzana", 24.5) , (4, "Cereza", 1.5) , (5, "Papaya", 23.6)
SELECT * FROM "dbo"."productos"

--SENTENCE CREATED WITH "query.py" SCRIPT
INSERT INTO "dbo"."inventarios" VALUES (1,1,23.7),(2,1,24.6),(3,1,66.6),(4,1,77.8),(5,1,88.9),(6,2,11.1),(7,2,22.2),(8,2,33.3),(9,2,44.4),(10,2,55.5),(11,3,26.7),(12,3,14.6),(13,3,86.6),(14,3,97.8),(15,3,8.9),(16,4,1.5),(17,4,23.7),(18,4,84.6),(19,4,76.6),(20,4,47.7),(21,4,98.9),(22,5,23.6),(23,5,23.7),(24,5,24.6),(25,5,66.6),(26,5,77.8),(27,5,88.6)

