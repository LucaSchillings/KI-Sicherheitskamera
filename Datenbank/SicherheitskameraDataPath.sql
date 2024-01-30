 CREATE Database SicherheitsKameraData
 USE Database SicherheitsKameraData

 Create Table Erkennung(
    ID int NOT NULL Primary Key IDENTITY,
    Datum date NOT NULL,
    Uhrzeit time NOT NULL,
    Dateipfad varchar(255)
    );