create database secundaria39Demo6;

use secundaria39Demo6; 

create table maestro (
codigo_ma smallint primary key not null, 
nombre_ma varchar (40) not null,
apellidos_ma varchar (40) not null,
contraseña_ma varchar (9) not null
);
select * from maestro;

create table materia (
codigo_mat tinyint primary key not null,
nombre_mat varchar (40) not null,
grado_mat varchar (20) not null
); 
select * from materia; 

create table alumno (
folio_alu int primary key not null, 
nombre_alu varchar (40) not null,
apellidos_alu varchar (40) not null
);
select * from alumno;

create table clases (
codigo_mat tinyint not null,
nombre_mat varchar (40) not null,
codigo_ma smallint not null,
nombre_ma varchar (40) not null,
apellidos_ma varchar (40) not null, 
Hora varchar (8) not null,
Grupo varchar (5) not null,
clave_clase varchar (15) primary key not null,
 constraint fkmateria foreign key (codigo_mat) references materia(codigo_mat),
 constraint fkmaestro foreign key  (codigo_ma) references maestro(codigo_ma)
 ); 
 select * from clases;
 
 insert into maestro 
 values ('101', 'Patricia del Rosario', 'Cuellar Garza', 'prcg12'),
		('102', 'Cesar Augusto','Noriega Morales', 'canm12'),
        ('103', 'Amanda', 'Chávez Paz', 'acp12'),
        ('104', 'Clara', 'Mendoza Rosales', 'cmr12'),
        ('105', 'Hecto Armando', 'Rosales Cun', 'harc12'),
        ('106', 'Gilberto', 'Santos López', 'gsl12'),
        ('107', 'Ingrid', 'Rodriguez Melgar', 'irm12'),
        ('108', 'Luz Maria', 'Guerra Matías', 'lmgm12'),
        ('109', 'Mariano', 'Mox Callejas', 'mmc12'),
        ('110', 'Otto Rene', 'Calí Perez', 'orcp12'),
        ('111', 'Maribel', 'Trujillo López', 'mtl12'),
        ('112', 'Rossana' , 'Herrera Cano', 'rhc12'),
        ('113', 'Ana', 'Ruiz Rivera', 'arr12'),
        ('114', 'Adolfo Danilo', 'Salazar Ortiz', 'adso12'),
        ('115', 'Oscar Manuel', 'Osorio Vela', 'omov12');
select * from maestro;       
 
 insert into materia
 values ('10', 'Español 1', 'Primero'),
		('11', 'Español 2', 'Segundo'),
        ('12', 'Español 3', 'Tercero'),
        ('13', 'Matemáticas 1', 'Primero'),
        ('14', 'Matemáticas 2', 'Segundo'),
        ('15', 'Matemáticas 3', 'Tercero'),
        ('16', 'Biología', 'Primero'),
        ('17', 'Física', 'Segundo'),
        ('18', 'Química', 'Tercero'),
        ('19', 'Geografía', 'Primero'),
        ('20', 'Historia 1', 'Segundo'),
        ('21', 'Historia 2', 'Tercero'),
        ('22', 'Formación Cívica y Etica', 'Segundo'),
        ('23', 'Formacion Cívica y Etica 2', 'Tercero'),
        ('24', 'Tecnología 1', 'Primero'),
        ('25', 'Tecnología 2', 'Segundo'),
        ('26', 'Tecnología 3', 'Tercero'),
        ('27', 'Artes Visuales', 'Primero'),
        ('28', 'Artes Visuales 2', 'Segundo'),
        ('29', 'Música', 'Tercero'),
        ('30', 'Inglés 1', 'Primero'),
        ('31', 'Inglés 2', 'Segundo'),
        ('32', 'Inglés 3', 'Tercero');
select * from materia; 
 
insert into alumno 
values ('1000001', 'Nancy Sarahi', 'Arroyo Reyes'),
		('1000002', 'Paloma Montserrat', 'Banda Izquierdo'),
        ('1000003', 'Britanny Paola', 'De la Rosa Moreno'),
        ('1000004', 'Hanna Morena', 'Diaz Almazan'),
        ('1000005', 'Reyna Sugey', 'Elizondo Rodriguez'),
        ('1000006', 'Valeria Monserrat', 'Escobar Perez'),
        ('1000007', 'Angelica Yissel', 'Garcia Perez'),
        ('1000008', 'Yuremi Natali', 'Garza Diaz'),
        ('1000009', 'Azul Azeneth', 'Gonzalez Alvarado'),
        ('1000010', 'Ximena Alejandra', 'Gonzalez Hernandez'),
        ('1000011', 'Yessica Guadalupe', 'Gonzalez Ibarra'),
        ('1000012', 'Delia Guadalupe', 'Gonzalez Requena'),
        ('1000013', 'Martha Mayle', 'Granados Martinez'),
        ('1000014', 'Yeimi Yamileth', 'Guardado Rodriguez'),
        ('1000015', 'Airam Aracely', 'Guillen Ceniceros'),
        ('1000016', 'Nadia Susana', 'Herminio Galindo'),
        ('1000017', 'Betsililiana', 'Hernandez Rodriguez'),
        ('1000018', 'Britany Guadalupe', 'Herrera Garcia'),
        ('1000019', 'Natali', 'Mendoza Islas'),
        ('1000020', 'Luisa Victoria', 'Lopez Barco'),
        ('1000021', 'Ximena Yazmin', 'Lopez Gonzalez'),
        ('1000022', 'Kimberly Yamileth', 'Loredo Espinosa'),
        ('1000023', 'Yaretsi Alejandra', 'Luevano Torres'),
        ('1000024', 'Jennyfer Maite', 'Luna Gutierrez'),
        ('1000025', 'Liliana Mayte', 'Maya Reyes'),
        ('1000026', 'Isarely Yaretssy', 'Montoya Jaimes'),
        ('1000027', 'Daniela Fernanda', 'Mora Delgado'),
        ('1000028', 'Aleida Sarahi', 'Quintero Arredondo'),
        ('1000029', 'Angela Sofia', 'Quintero Chavez'),
        ('1000030', 'Luz Valentina', 'Quintero Gonzalez'),
        ('1000031', 'Jovana', 'Reyes Rojas'),
        ('1000032', 'Angeline', 'Sanchez Lucio'),
        ('1000033', 'Mariana Berenice', 'Ortiz Perales'),
        ('1000034', 'Clara Estefania', 'Muñoz Torres'),
        ('1000035', 'Fabiola', 'Villarreal Ramirez'),
        ('1000036', 'Mauricio', 'Alvizo Leyva'),
        ('1000037', 'Jorge', 'Arellano Morrugales'),
        ('1000038', 'Carlos Humberto', 'Arista Hurtado'),
        ('1000039', 'Dylan Eduardo', 'Diaz Ruiz'),
        ('1000040', 'Oscar Antonio', 'Botello Casas'),
        ('1000041', 'Jovan Adriel', 'Bustos Garcia'),
        ('1000042', 'Diego Daniel', 'Camacho Gallardo'),
        ('1000043', 'Danny Sebastian', 'Cruz Antonio'),
        ('1000044', 'Luis Angel', 'Cuevas Martinez'),
        ('1000045', 'Fernando', 'Fernandez Ramos '),
        ('1000046', 'Alexis', 'Gaytan Razo'),
        ('1000047', 'Joseph Alejandro', 'Gonzalez Rojas'),
        ('1000048', 'Daniel Esau', 'Marquez Lucio'),
        ('1000049', 'Juan Rodrigo', 'Mata Anguiano'),
        ('1000050', 'Angel Hernan', 'Moreno Garcia'),
        ('1000051', 'Aldo Gael', 'Olvera Corpus'),
        ('1000052', 'Osvaldo Daniel', 'Ovalle Gonzalez'),
        ('1000053', 'Jose Damian', 'Palacios Espinoza'),
        ('1000054', 'Jorge Luis', 'Perez Lopez'),
        ('1000055', 'Josue Roberto', 'Ramirez Silva'),
        ('1000056', 'Marcos Tadeo', 'Refugio Caballero'),
        ('1000057', 'Victor Tadeo', 'Reyes Blanco'),
        ('1000058', 'Luis Fernando', 'Reyes Triana'),
        ('1000059', 'Jose Manuel', 'Reza Velazquez'),
        ('1000060', 'Irvin Daniel', 'Rodriguez Segura'),
        ('1000061', 'Jesus Alfredo', 'Sarmiento Villalpando'),
        ('1000062', 'Samuel', 'Sotero Cruz'),
        ('1000063', 'Gabriel Alejandro', 'Tovar Nuñez'),
        ('1000064', 'Joshua Guadalupe', 'Treviño Hernandez'),
        ('1000065', 'Alejandro', 'Velazquez Amaya'),
        ('1000066', 'Amanda Vanessa', 'Carrizales Carrizales'),
        ('1000067', 'Sofia Michelle', 'Castillo Moreno'),
        ('1000068', 'Ana Naomy', 'Cisneros Martinez'),
        ('1000069', 'Donaji Guadalupe', 'De la Rosa Morales'),
        ('1000070', 'Belen Sarahi', 'Espinoza Garrido'),
        ('1000071', 'Constanza', 'Garcia Treviño'),
        ('1000072', 'Allison Monserrat', 'Gomez Salazar'),
        ('1000073', 'Abril Guadalupe', 'Gonzalez Alfaro'),
        ('1000074', 'Dulce Maria', 'Guevara Guzman'),
        ('1000075', 'Dulce Amairani', 'Hernandez Benito'),
        ('1000076', 'Jenifer Aimee', 'Lopez Villanueva'),
        ('1000077', 'Christiane Renata', 'Muñoz Rodriguez'),
        ('1000078', 'Diana Paola', 'Nicolas Vazquez'),
        ('1000079', 'Karla Marina', 'Nicolas Vazquez'),
        ('1000080', 'Roberta Noemi', 'Perez Martinez'),
        ('1000081', 'Briseidy Mayeli', 'Presas Rivera'),
        ('1000082', 'Deimy Janeth', 'Rico Castillo'),
        ('1000083', 'Pamela Denisse', 'Rocha Martinez'),
        ('1000084', 'Ximena Montserrat', 'Rodriguez Moreno'),
        ('1000085', 'Yameli Aide', 'Rasales de Leon'),
        ('1000086', 'Brisa Sarai', 'Ruiz Lopez'),
        ('1000087', 'Lina Coral', 'Salas Castillo'),
        ('1000088', 'Paola Alejandra', 'Salas Perez'),
        ('1000089', 'Paula Cristina', 'Saldaña Arevalo'),
        ('1000090', 'Grecia Monserrat', 'Salinas Colin'),
        ('1000091', 'Debanhi Jocelyn', 'Santamaria Duron'),
        ('1000092', 'Belinda Paola', 'Silva Solis'),
        ('1000093', 'Danna Paola', 'Torres Nuñez'),
        ('1000094', 'Fernanda Ailed', 'Treviño Lugo'),
        ('1000095', 'Devany Stefania', 'Ulloa Tienda'),
        ('1000096', 'Abril Isaac', 'Vela Marroquin'),
        ('1000097', 'Ximena Carolina', 'Victorino Moreno'),
        ('1000098', 'Valeria Patricia', 'Villela Lizcano'),
        ('1000099', 'Valeria', 'Puente Cardenas');
select * from alumno;

insert into clases
values ('10', 'Español 1', '103', 'Amanda', 'Chávez Paz', 'M1', '1A', 'acpesp111a'),
		('13', 'Matemáticas 1', '101', 'Patricia del Rosario', 'Cuellar Garza', 'M2', '1A', 'pcgmat121a'),
        ('16', 'Biología', '109', 'Mariano', 'Mox Callejas', 'M3', '1A', 'mmcbio31a'),
        ('19', 'Geografía', '115', 'Oscar Manuel', 'Osorio Vela', 'M5', '1A', 'oovgeo41a'),
        ('24', 'Tecnología 1','106', 'Gilberto', 'Santos López', 'M6', '1A', 'gsltec141a'),
        ('27', 'Artes Visuales', '104', 'Clara', 'Mendoza Rosales', 'V1', '1A', 'cmrartv61a'),
        ('30', 'Inglés 1', '105', 'Hecto Armando', 'Rosales Cun', 'V2', '1A', 'hrcing1v21a'),
        ('19', 'Geografía', '102', 'Cesar Augusto','Noriega Morales', 'M1', '1B', 'cnmgeo11b'),
        ('10', 'Español 1', '103', 'Amanda', 'Chávez Paz', 'M2', '1B', 'acpesp121b'),
        ('13', 'Matemáticas 1', '101', 'Patricia del Rosario', 'Cuellar Garza', 'M3', '1B', 'pcgmat131b'),
        ('16', 'Biología', '110', 'Otto Rene', 'Calí Perez', 'M5', '1B', 'ocpbio51b'),
        ('24', 'Tecnología 1', '108', 'Luz Maria', 'Guerra Matías', 'M6', '1B', 'lgmtec161b'),
        ('30', 'Inglés 1', '105', 'Hecto Armando', 'Rosales Cun', 'V1', '1B', 'hrcing1v11b'),
        ('27', 'Artes Visuales', '113', 'Ana', 'Ruiz Rivera', 'V2', '1B', 'arrartvv21b'),
        ('13', 'Matemáticas 1', '101', 'Patricia del Rosario', 'Cuellar Garza', 'M1', '1C', 'pcgmat111c'),
        ('24', 'Tecnología 1','106', 'Gilberto', 'Santos López', 'M2', '1C', 'gsltec121c');
select * from clases; 

create table trimestre1 (
clave_clase varchar (15) not null,
folio_alu int not null,
no_lista smallint not null,
nombre_alumno varchar (90) not null,
act_1 float,
act_2 float,
act_3 float,
act_4 float,
act_5 float,
act_6 float,
act_7 float,
act_8 float,
act_9 float,
act_10 float,
Examen float,
Promedio float,
constraint fkclases foreign key  (clave_clase) references clases(clave_clase),
constraint fkalumno foreign key  (folio_alu) references alumno(folio_alu)
);
select * from trimestre1;

create table trimestre2 (
clave_clase varchar (15) not null,
folio_alu int not null,
no_lista smallint not null,
nombre_alumno varchar (90) not null,
act_1 float,
act_2 float,
act_3 float,
act_4 float,
act_5 float,
act_6 float,
act_7 float,
act_8 float,
act_9 float,
act_10 float,
Examen float,
Promedio float,
constraint fkclases1 foreign key  (clave_clase) references clases(clave_clase),
constraint fkalumno1 foreign key  (folio_alu) references alumno(folio_alu)
);
select * from trimestre2;

create table trimestre3 (
clave_clase varchar (15) not null,
folio_alu int not null,
no_lista smallint not null,
nombre_alumno varchar (90) not null,
act_1 float,
act_2 float,
act_3 float,
act_4 float,
act_5 float,
act_6 float,
act_7 float,
act_8 float,
act_9 float,
act_10 float,
Examen float,
Promedio float,
constraint fkclases2 foreign key  (clave_clase) references clases(clave_clase),
constraint fkalumno2 foreign key  (folio_alu) references alumno(folio_alu)
);
select * from trimestre3;

insert into trimestre1
values ('pcgmat121a', '1000001', '1', 'Nancy Sarahi Arroyo Reyes', '85','90','91','88', '70', '83', '89', '79', '92', '87', '82', null),
		('pcgmat121a', '1000002', '2', 'Paloma Montserrat Banda Izquierdo', '70','77','80','88', '79', '90', '99', '100', '82', '87', '75', null),
		('pcgmat121a', '1000003', '3', 'Britanny Paola De la Rosa Moreno', '70','100','90','88', '77', '100', '95', '100', '82', '80', '85', null),
		('pcgmat121a', '1000004', '4', 'Hanna Morena Diaz Almazan', '100','100','95','90', '89', '100', '94', '85', '82', '87', '95', null),
		('pcgmat121a', '1000005', '5', 'Reyna Sugey Elizondo Rodriguez', '100','97','100','88', '99', '90', '92', '89', '85', '87', '89', null),
        ('pcgmat121a', '1000006', '6', 'Valeria Monserrat Escobar Perez', '80','85','88','98', '100', '100', '100', '83', '86', '89', '88', null),
        ('pcgmat121a', '1000007', '7', 'Angelica Yissel Garcia Perez', '100','100','88','91', '100', '100', '95', '93', '85', '89', '90', null),
        ('pcgmat121a', '1000008', '8', 'Yuremi Natali Garza Diaz', '50','72','74','80', '75', '100', '63', '82', '84', '79', '66', null),
        ('pcgmat121a', '1000009', '9', 'Azul Azeneth Gonzalez Alvarado', '70','60','54','40', '75', '100', '73', '69', '84', '80', '42', null),
        ('pcgmat121a', '1000010', '10', 'Ximena Alejandra Gonzalez Hernandez', '45','62','70','50', '55', '79', '70', '50', '74', '93', '38', null),
        ('pcgmat121a', '1000011', '11', 'Yessica Guadalupe Gonzalez Ibarra', '70','78','79','80', '85', '89', '63', '82', '84', '79', '66', null),
		('pcgmat121a', '1000012', '12', 'Delia Guadalupe Gonzalez Requena', '90','92','89','85', '95', '99', '100', '80', '82', '88', '84', null),
		('pcgmat121a', '1000013', '13', 'Martha Mayle Granados Martinez', '42','68','59','71', '75', '31', '43', '62', '84', '59', '50', null),
		('pcgmat121a', '1000014', '14', 'Yeimi Yamileth Guardado Rodriguez', '85','88','89','90', '95', '100', '93', '92', '100', '100', '90', null),
		('pcgmat121a', '1000015', '15', 'Airam Aracely Guillen Ceniceros', '77','68','79','80', '55', '69', '76', '82', '84', '79', '60', null),
		('pcgmat121a', '1000016', '16', 'Nadia Susana Herminio Galindo', '90','95','89','100', '81', '88', '82', '86', '94', '92', '84', null),
        ('pcgmat121a', '1000017', '17', 'Betsililiana Hernandez Rodriguez', '94','95','100','100', '100', '98', '92', '86', '90', '85', '87', null),
        ('pcgmat121a', '1000018', '18', 'Britany Guadalupe Herrera Garcia', '100','100','100','100', '100', '100', '99', '100', '100', '100', '100', null),
        ('pcgmat121a', '1000019', '19', 'Natali Mendoza Islas', '100','100','89','92', '94', '98', '92', '100', '95', '90', '89', null),
        ('pcgmat121a', '1000020', '20', 'Luisa Victoria Lopez Barco', '60','65','79','85', '81', '76', '72', '66', '84', '52', '64', null),
        ('pcgmat121a', '1000021', '21', 'Ximena Yazmin Lopez Gonzalez', '90','81','89','100', '88', '88', '77', '76', '100', '70', '80', null),
        ('pcgmat121a', '1000022', '22', 'Kimberly Yamileth Loredo Espinosa', '96','100','100','100', '77', '79', '81', '80', '90', '82', '80', null),
        ('pcgmat121a', '1000023', '23', 'Yaretsi Alejandra Luevano Torres', '66','100','100','59', '67', '61', '51', '60', '72', '74', '70', null),
        ('pcgmat121a', '1000024', '24', 'Jennyfer Maite Luna Gutierrez', '50','50','57','80', '87', '77', '41', '62', '60', '66', '45', null),
        ('pcgmat121a', '1000025', '25', 'Liliana Mayte Maya Reyes', '66','100','100','50', '57', '80', '61', '50', '33', '80', '20', null),
        ('pcgmat121a', '1000026', '26', 'Isarely Yaretssy Montoya Jaimes', '30','40','55','45', '77', '69', '88', '80', '66', '75', '61', null),
        ('pcgmat121a', '1000027', '27', 'Daniela Fernanda Mora Delgado', '70','65','69','50', '57', '77', '100', '100', '74', '72', '59', null),
        ('pcgmat121a', '1000028', '28', 'Aleida Sarahi Quintero Arredondo', '70','70','62','100', '77', '79', '81', '88', '70', '63', '60', null),
        ('pcgmat121a', '1000029', '29', 'Angela Sofia Quintero Chavez', '80','100','100','63', '70', '71', '75', '63', '60', '73', '64', null),
        ('pcgmat121a', '1000030', '30', 'Luz Valentina Quintero Gonzalez', '100','100','70','75', '77', '64', '61', '60', '81', '62', '56', null),
        ('pcgmat121a', '1000031', '31', 'Jovana Reyes Rojas', '40','40','50','53', '57', '79', '81', '60', '55', '42', '41', null),
        ('pcgmat121a', '1000032', '32', 'Angeline Sanchez Lucio', '50','100','70','50', '67', '69', '59', '55', '63', '60', '59', null),
        ('pcgmat121a', '1000033', '33', 'Mariana Berenice Ortiz Perales', '0','0','0','0', '7', '0', '0', '0', '0', '0', '0', null),
        ('pcgmat121a', '1000034', '34', 'Clara Estefania Muñoz Torres', '0','0','0','0', '0', '0', '0', '0', '0', '0', '0', null),
        ('pcgmat121a', '1000035', '35', 'Fabiola Villarreal Ramirez', '0','0','20','0', '15', '0', '0', '0', '0', '0', '0', null);
        
select clave_clase, folio_alu, no_lista, nombre_alumno, act_1, act_2, act_3, act_4, act_5 act_6, act_7, act_8, act_9, act_10, Examen,
 round(avg(act_1+act_2+act_3+act_4+act_5+act_6+act_7+act_8+act_9+act_10+Examen)/11, 2) Promedio from trimestre1
group by clave_clase, folio_alu, no_lista, nombre_alumno;
select * from trimestre1 group by clave_clase, folio_alu, no_lista, nombre_alumno;
UPDATE trimestre1 SET Promedio= (Select round(avg(act_1+act_2+act_3+act_4+act_5+act_6+act_7+act_8+act_9+act_10+Examen)/11, 2)) WHERE folio_alu=1000035 and clave_clase like 'pcgmat121a';


insert into trimestre2
values  ('pcgmat121a', '1000001', '1', 'Nancy Sarahi Arroyo Reyes', '90','100','91','88', '95', '93', '87', '89', '92', '97', '92', null),
		('pcgmat121a', '1000002', '2', 'Paloma Montserrat Banda Izquierdo', '100','77','60','54', '51', '40', '45', '61', '66', '50', '65', null),
		('pcgmat121a', '1000003', '3', 'Britanny Paola De la Rosa Moreno', '70','100','90','88', '77', '100', '95', '100', '82', '80', '85', null),
		('pcgmat121a', '1000004', '4', 'Hanna Morena Diaz Almazan', '60','65','100','40', '39', '45', '54', '55', '60', '57', '50', null),
		('pcgmat121a', '1000005', '5', 'Reyna Sugey Elizondo Rodriguez', '40','47','33','60', '69', '70', '62', '42', '45', '47', '35', null),
        ('pcgmat121a', '1000006', '6', 'Valeria Monserrat Escobar Perez', '50','45','58','82', '100', '51', '15', '73', '60', '52', '41', null),
        ('pcgmat121a', '1000007', '7', 'Angelica Yissel Garcia Perez', '100','100','100','99', '100', '100', '100', '100', '100', '100', '100', null),
        ('pcgmat121a', '1000008', '8', 'Yuremi Natali Garza Diaz', '50','69','74','60', '66', '52', '53', '40', '34', '72', '40', null),
        ('pcgmat121a', '1000009', '9', 'Azul Azeneth Gonzalez Alvarado', '90','100','85','70', '85', '88', '93', '79', '82', '85', '80', null),
        ('pcgmat121a', '1000010', '10', 'Ximena Alejandra Gonzalez Hernandez', '50','52','60','58', '68', '70', '55', '50', '44', '30', '52', null),
        ('pcgmat121a', '1000011', '11', 'Yessica Guadalupe Gonzalez Ibarra', '70','78','79','80', '85', '89', '63', '82', '84', '79', '66', null),
		('pcgmat121a', '1000012', '12', 'Delia Guadalupe Gonzalez Requena', '35','24','75','75', '100', '63', '66', '42', '80', '70', '64', null),
		('pcgmat121a', '1000013', '13', 'Martha Mayle Granados Martinez', '20','38','49','81', '85', '79', '73', '65', '44', '54', '60', null),
		('pcgmat121a', '1000014', '14', 'Yeimi Yamileth Guardado Rodriguez', '100','100','100','100', '100', '100', '100', '100', '100', '100', '99', null),
		('pcgmat121a', '1000015', '15', 'Airam Aracely Guillen Ceniceros', '57','68','40','40', '89', '79', '63', '72', '55', '72', '59',null),
		('pcgmat121a', '1000016', '16', 'Nadia Susana Herminio Galindo', '80','90','89','100', '100', '78', '72', '76', '94', '92', '80', null),
        ('pcgmat121a', '1000017', '17', 'Betsililiana Hernandez Rodriguez', '94','95','100','100', '100', '98', '92', '86', '90', '85', '87', null),
        ('pcgmat121a', '1000018', '18', 'Britany Guadalupe Herrera Garcia', '100','100','66','70', '77', '85', '89', '71', '67', '66', '74', null),
        ('pcgmat121a', '1000019', '19', 'Natali Mendoza Islas', '90','95','80','72', '64', '60', '72', '100', '71', '70', '70', null),
        ('pcgmat121a', '1000020', '20', 'Luisa Victoria Lopez Barco', '70','70','70','85', '92', '96', '100', '100', '100', '70', '65', null),
        ('pcgmat121a', '1000021', '21', 'Ximena Yazmin Lopez Gonzalez', '60','61','49','50', '58', '84', '74', '100', '100', '59', '60', null),
        ('pcgmat121a', '1000022', '22', 'Kimberly Yamileth Loredo Espinosa', '100','100','100','82', '97', '99', '88', '85', '94', '92', '95', null),
        ('pcgmat121a', '1000023', '23', 'Yaretsi Alejandra Luevano Torres', '51','56','100','49', '37', '55', '70', '70', '77', '20', '50', null),
        ('pcgmat121a', '1000024', '24', 'Jennyfer Maite Luna Gutierrez', '60','60','75','80', '87', '84', '66', '54', '50', '68', '60', null),
        ('pcgmat121a', '1000025', '25', 'Liliana Mayte Maya Reyes', '100','100','85','70', '75', '50', '41', '33', '48', '40', '53', null),
        ('pcgmat121a', '1000026', '26', 'Isarely Yaretssy Montoya Jaimes', '15','30','71','45', '77', '100', '40', '70', '76', '75', '59', null),
        ('pcgmat121a', '1000027', '27', 'Daniela Fernanda Mora Delgado', '100','75','86','50', '77', '100', '100', '94', '82', '81', '70', null),
        ('pcgmat121a', '1000028', '28', 'Aleida Sarahi Quintero Arredondo', '52','27','60','41', '72', '89', '70', '66', '70', '50', '67', null),
        ('pcgmat121a', '1000029', '29', 'Angela Sofia Quintero Chavez', '70','90','90','63', '70', '71', '75', '63', '60', '90', '81', null),
        ('pcgmat121a', '1000030', '30', 'Luz Valentina Quintero Gonzalez', '60','70','86','85', '99', '54', '43', '77', '85', '62', '37', null),
        ('pcgmat121a', '1000031', '31', 'Jovana Reyes Rojas', '30','35','50','55', '70', '62', '54', '50', '55', '30', '22', null),
        ('pcgmat121a', '1000032', '32', 'Angeline Sanchez Lucio', '24','50','77','60', '51', '59', '32', '45', '83', '80', '50', null),
        ('pcgmat121a', '1000033', '33', 'Mariana Berenice Ortiz Perales', '50','55','30','41', '47', '66', '70', '72', '0', '0', '42', null),
        ('pcgmat121a', '1000034', '34', 'Clara Estefania Muñoz Torres', '20','15','50','55', '70', '0', '40', '44', '61', '63', '40', null),
        ('pcgmat121a', '1000035', '35', 'Fabiola Villarreal Ramirez', '70','60','50','0', '0', '41', '44', '56', '30', '40', '39', null);
        
select clave_clase, folio_alu, no_lista, nombre_alumno, act_1, act_2, act_3, act_4, act_5 act_6, act_7, act_8, act_9, act_10, Examen,
 avg(act_1+act_2+act_3+act_4+act_5+act_6+act_7+act_8+act_9+act_10+Examen)/11 Promedio from trimestre2
group by clave_clase, folio_alu, no_lista, nombre_alumno;

insert into trimestre3
values  ('pcgmat121a', '1000001', '1', 'Nancy Sarahi Arroyo Reyes', '90','100','91','88', '95', '93', '87', '89', '92', '97', '92', null),
		('pcgmat121a', '1000002', '2', 'Paloma Montserrat Banda Izquierdo', '100','100','100','94', '85', '80', '77', '86', '92', '90', '82', null),
		('pcgmat121a', '1000003', '3', 'Britanny Paola De la Rosa Moreno', '50','55','70','72', '80', '82', '83', '100', '100', '70', '64', null),
		('pcgmat121a', '1000004', '4', 'Hanna Morena Diaz Almazan', '70','65','100','100', '98', '70', '7', '81', '67', '51', '43', null),
		('pcgmat121a', '1000005', '5', 'Reyna Sugey Elizondo Rodriguez', '30','20','50','55', '70', '69', '45', '49', '66', '67', '20', null),
        ('pcgmat121a', '1000006', '6', 'Valeria Monserrat Escobar Perez', '90','100','80','70', '60', '50', '55', '52', '40', '30', '38', null),
        ('pcgmat121a', '1000007', '7', 'Angelica Yissel Garcia Perez', '100','100','100','100', '100', '100', '100', '100', '100', '100', '100', null),
        ('pcgmat121a', '1000008', '8', 'Yuremi Natali Garza Diaz', '63','69','100','90', '86', '62', '54', '40', '20', '20', '40', null),
        ('pcgmat121a', '1000009', '9', 'Azul Azeneth Gonzalez Alvarado', '80','70','85','62', '100', '100', '40', '55', '44', '95', '60', null),
        ('pcgmat121a', '1000010', '10', 'Ximena Alejandra Gonzalez Hernandez', '20','32','51','58', '77', '62', '42', '90', '94', '50', '43', null),
        ('pcgmat121a', '1000011', '11', 'Yessica Guadalupe Gonzalez Ibarra', '100','88','100','100', '70', '77', '51', '82', '38', '80', '60', null),
		('pcgmat121a', '1000012', '12', 'Delia Guadalupe Gonzalez Requena', '20','0','0','40', '82', '83', '55', '52', '91', '0', '29', null),
		('pcgmat121a', '1000013', '13', 'Martha Mayle Granados Martinez', '0','0','30','71', '75', '36', '33', '70', '74', '66', '30', null),
		('pcgmat121a', '1000014', '14', 'Yeimi Yamileth Guardado Rodriguez', '100','100','100','100', '100', '100', '100', '100', '100', '100', '99', null),
		('pcgmat121a', '1000015', '15', 'Airam Aracely Guillen Ceniceros', '42','46','58','50', '0', '62', '60', '77', '78', '60', '64', null),
		('pcgmat121a', '1000016', '16', 'Nadia Susana Herminio Galindo', '88','100','100','100', '90', '88', '70', '76', '84', '88', '64', null),
        ('pcgmat121a', '1000017', '17', 'Betsililiana Hernandez Rodriguez', '100','100','100','100', '100', '80', '88', '90', '91', '90', '82', null),
        ('pcgmat121a', '1000018', '18', 'Britany Guadalupe Herrera Garcia', '100','100','100','80', '65', '85', '90', '94', '92', '71', '70', null),
        ('pcgmat121a', '1000019', '19', 'Natali Mendoza Islas', '100','100','100','100', '100', '100', '100', '100', '100', '100', '100', null),
        ('pcgmat121a', '1000020', '20', 'Luisa Victoria Lopez Barco', '90','65','34','55', '86', '90', '100', '63', '79', '70', '75', null),
        ('pcgmat121a', '1000021', '21', 'Ximena Yazmin Lopez Gonzalez', '70','77','20','30', '33', '64', '82', '100', '93', '95', '80', null),
        ('pcgmat121a', '1000022', '22', 'Kimberly Yamileth Loredo Espinosa', '100','100','92','100', '85', '90', '100', '74', '84', '95', '80', null),
        ('pcgmat121a', '1000023', '23', 'Yaretsi Alejandra Luevano Torres', '20','36','75','65', '45', '90', '90', '99', '100', '100', '83', null),
        ('pcgmat121a', '1000024', '24', 'Jennyfer Maite Luna Gutierrez', '75','70','77','34', '77', '80', '88', '64', '100', '60', '30', null),
        ('pcgmat121a', '1000025', '25', 'Liliana Mayte Maya Reyes', '90','94','100','70', '100', '60', '66', '59', '72', '70', '50', null),
        ('pcgmat121a', '1000026', '26', 'Isarely Yaretssy Montoya Jaimes', '0','0','35','35', '50', '52', '60', '72', '66', '68', '50', null),
        ('pcgmat121a', '1000027', '27', 'Daniela Fernanda Mora Delgado', '100','100','90','100', '79', '82', '86', '91', '85', '60', '77', null),
        ('pcgmat121a', '1000028', '28', 'Aleida Sarahi Quintero Arredondo', '100','100','90','100', '80', '83', '79', '84', '78', '93', '70', null),
        ('pcgmat121a', '1000029', '29', 'Angela Sofia Quintero Chavez', '100','72','80','77', '88', '80', '85', '90', '96', '100', '80', null),
        ('pcgmat121a', '1000030', '30', 'Luz Valentina Quintero Gonzalez', '50','55','64','75', '100', '64', '100', '80', '61', '50', '34', null),
        ('pcgmat121a', '1000031', '31', 'Jovana Reyes Rojas', '0','0','10','40', '49', '53', '55', '65', '42', '0', '43', null),
        ('pcgmat121a', '1000032', '32', 'Angeline Sanchez Lucio', '34','40','50','70', '77', '88', '65', '49', '88', '0', '70', null),
        ('pcgmat121a', '1000033', '33', 'Mariana Berenice Ortiz Perales', '30','50','30','39', '47', '50', '77', '69', '90', '40', '64', null),
        ('pcgmat121a', '1000034', '34', 'Clara Estefania Muñoz Torres', '50','50','40','36', '77', '70', '60', '66', '84', '30', '49', null),
        ('pcgmat121a', '1000035', '35', 'Fabiola Villarreal Ramirez', '80','70','75','36', '40', '64', '44', '60', '78', '50', '56', null);

select clave_clase, folio_alu, no_lista, nombre_alumno, act_1, act_2, act_3, act_4, act_5 act_6, act_7, act_8, act_9, act_10, Examen,
 avg(act_1+act_2+act_3+act_4+act_5+act_6+act_7+act_8+act_9+act_10+Examen)/11 Promedio from trimestre3
group by clave_clase, folio_alu, no_lista, nombre_alumno;

select b.folio_alu, b.no_lista,b.nombre_alumno,b.Promedio Trimestre_1, c.Promedio Trimestre_2, d.Promedio Trimestre_3, round(avg(b.Promedio+c.Promedio+d.Promedio)/3,0) Final from Trimestre1 as b, Trimestre2 as c, Trimestre3 as d
where (((b.folio_alu = c.folio_alu) and (c.folio_alu = d.folio_alu)))and (b.clave_clase like 'pcgmat121a'and ((b.clave_clase=c.clave_clase)and(c.clave_clase=d.clave_clase)))
group by b.folio_alu, b.clave_clase; 
/*(b.folio_alu = 1000035 and ((b.folio_alu = c.folio_alu) and (c.folio_alu = d.folio_alu))) and (b.clave_clase like 'pcgmat121a' and ((b.clave_clase=c.clave_clase)and(c.clave_clase=d.clave_clase))) 
group by b.folio_alu, b.clave_clase; 
inner join b on a.folio_alu = b.folio_alu
inner join c on a.folio_alu = c.folio_alu
inner join d on a.folio_alu = d.folio_alu*/
