create database Prueba;
Use Prueba;

create table Profesor(
Id_profesor tinyint not null primary key,
Nombre_p varchar(30) not null,
contraseña varchar (18) not null
);

insert into Profesor Values(1,"Fernando","estudio"); 
select * from profesor;

SELECT contraseña FROM Profesor WHERE Nombre_p;