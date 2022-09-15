#DROP DATABASE lab_individual;
#CREATE DATABASE IF NOT EXISTS lab_individual_2;
USE lab_individual_2;

#SELECT @@global.secure_file_priv;
#SHOW VARIABLES LIKE "secure_file_priv";

-- si queremos hacer un SET para cambiar la variable NO nos va a dejar
-- podemos solucionar esto de la siguiente manera
SET SQL_SAFE_UPDATES = 0;

/*Normalizacion de la data*/

# DROP TABLE IF EXISTS `circuito`;
ALTER TABLE circuits CHANGE circuitId  	`IdCircuit`  INT NOT NULL;
ALTER TABLE circuits CHANGE name  		`Name` 	     varchar(250) COLLATE utf8mb4_spanish_ci DEFAULT NULL;
ALTER TABLE circuits CHANGE location    `Location`	 varchar(250) COLLATE utf8mb4_spanish_ci DEFAULT NULL;
ALTER TABLE circuits CHANGE country  	`Country` 	 varchar(250) COLLATE utf8mb4_spanish_ci DEFAULT NULL;
ALTER TABLE circuits CHANGE url    		`URL`        varchar(300) COLLATE utf8mb4_spanish_ci DEFAULT NULL;
#ALTER TABLE circuits CHANGE    `Latitud`    decimal(13,6) NOT NULL DEFAULT 0.000000;
#ALTER TABLE circuits CHANGE	`Longitud`   decimal(13,6) NOT NULL DEFAULT 0.000000;
#ALTER TABLE circuits CHANGE    `Altura`	 INT NOT NULL DEFAULT 0;
#ALTER TABLE circuits CHANGE circuitRef  	`RefCircuit` varchar(250) COLLATE utf8mb4_spanish_ci DEFAULT NULL;
ALTER TABLE circuits DROP `index`; 


# DROP TABLE IF EXISTS `races`;
ALTER TABLE races CHANGE raceId  	`IdRace`    INT NOT NULL;
ALTER TABLE races CHANGE circuitId  `IdCircuit` INT NOT NULL;
ALTER TABLE races CHANGE  `name`	`Name`      varchar(300) COLLATE utf8mb4_spanish_ci DEFAULT NULL;
ALTER TABLE races CHANGE `date` 	`Date` 		DATE;
ALTER TABLE races CHANGE  `url` 	`URL`       varchar(300) COLLATE utf8mb4_spanish_ci DEFAULT NULL;
ALTER TABLE races DROP `index`;
UPDATE races SET time = 0 WHERE time IS NULL OR time = '\\N';
ALTER TABLE races CHANGE `time` `Time` TIME;

# DROP TABLE IF EXISTS `constructor`;
ALTER TABLE  `constructor` CHANGE `constructorId`	`IdConstructor`  INTEGER NOT NULL;
ALTER TABLE  `constructor` CHANGE `constructorRef`	`RefConstructor` varchar(250) COLLATE utf8mb4_spanish_ci DEFAULT NULL;
ALTER TABLE  `constructor` CHANGE `name` 			`Name`			 varchar(250) COLLATE utf8mb4_spanish_ci DEFAULT NULL;
ALTER TABLE  `constructor` CHANGE `nationality`   	`Nationality`	 varchar(250) COLLATE utf8mb4_spanish_ci DEFAULT NULL;
ALTER TABLE  `constructor` CHANGE  `url` 			`URL`        	 varchar(300) COLLATE utf8mb4_spanish_ci DEFAULT NULL;
ALTER TABLE `constructor`  DROP `index`;
				
# DROP TABLE IF EXISTS `drivers`;
ALTER TABLE drivers CHANGE driverId  		`IdDriver`  	INTEGER NOT NULL;
ALTER TABLE drivers CHANGE driverRef		`RefDriver` 	varchar(250) COLLATE utf8mb4_spanish_ci DEFAULT NULL;
ALTER TABLE drivers CHANGE code 			`Code`      	varchar(250) COLLATE utf8mb4_spanish_ci DEFAULT NULL;
ALTER TABLE drivers CHANGE dob  			`Dob`      		date;
ALTER TABLE drivers CHANGE nationality  	`Nationality`	varchar(250) COLLATE utf8mb4_spanish_ci DEFAULT NULL;
ALTER TABLE drivers CHANGE url  `URL`       				varchar(300) COLLATE utf8mb4_spanish_ci DEFAULT NULL;
ALTER TABLE drivers CHANGE `name.forename`  `Forename` 		varchar(250) COLLATE utf8mb4_spanish_ci DEFAULT NULL;
ALTER TABLE drivers CHANGE `name.surname` 	`Surname` 		varchar(250) COLLATE utf8mb4_spanish_ci DEFAULT NULL;
ALTER TABLE `drivers`  DROP `index`;
# ALTER TABLE drivers CHANGE number  `Number`    INTEGER;

# DROP TABLE IF EXISTS `pit_stops`;
ALTER TABLE pit_stops CHANGE raceId  		`IdRace`   INT NOT NULL;
ALTER TABLE pit_stops CHANGE driverId 		`IdDriver` INTEGER;
ALTER TABLE pit_stops CHANGE stop   		`Stop`     INT NOT NULL DEFAULT 0;
ALTER TABLE pit_stops CHANGE lap   			`Lap`      INT NOT NULL DEFAULT 0;
ALTER TABLE pit_stops CHANGE time 			`Time`     time;
ALTER TABLE pit_stops CHANGE duration    	`Duration` decimal(13,4) NOT NULL DEFAULT 0.0000;
ALTER TABLE pit_stops CHANGE milliseconds   `Milliseconds` INT NOT NULL DEFAULT 0;


#DROP TABLE IF EXISTS `results`;
ALTER TABLE results CHANGE resultId   		`IdResults`    	INT NOT NULL;
ALTER TABLE results CHANGE raceId  			`IdRace`      	INT;
ALTER TABLE results CHANGE driverId    		`IdDriver`     	INT;
ALTER TABLE results CHANGE constructorId    `IdConstructor` INT;
#ALTER TABLE results CHANGE number   		`Number`		INT;
ALTER TABLE results CHANGE grid    			`Grid`          INT NOT NULL DEFAULT 0;
# ALTER TABLE results CHANGE position   	`Position`		INT NOT NULL DEFAULT 0;
ALTER TABLE results CHANGE positionText    `PositionText`   varchar(50) COLLATE utf8mb4_spanish_ci DEFAULT NULL;
ALTER TABLE results CHANGE positionOrder 	`PositionOrder` INT NOT NULL DEFAULT 0;
ALTER TABLE results CHANGE points   		`Points`        INT NOT NULL DEFAULT 0;
ALTER TABLE results CHANGE laps				`Laps`          INT NOT NULL DEFAULT 0;
ALTER TABLE results CHANGE fastestLapTime  `FastestLapTime` time;
ALTER TABLE results CHANGE  statusId  `IdStatus`       		INT;
ALTER TABLE results DROP `index`;

SET SQL_SAFE_UPDATES = 0;
UPDATE results SET milliseconds = 0 WHERE milliseconds IS NULL OR milliseconds= '';
ALTER TABLE results CHANGE milliseconds   `Milliseconds` INT NOT NULL DEFAULT 0;
UPDATE results SET fastestLapSpeed = 0.0 WHERE fastestLapSpeed IS NULL OR milliseconds= '0';
#ALTER TABLE results CHANGE fastestLapSpeed   `FastestLapSpeed` decimal(13,4) NOT NULL DEFAULT 0.0000;
# ALTER TABLE results CHANGE fastestLap    `FastestLap`     INT NOT NULL DEFAULT 0;
# ALTER TABLE results CHANGE `rank`    `Rank`           INT NOT NULL DEFAULT 0;


#DROP TABLE IF EXISTS `Qualifying`;
ALTER TABLE qualifying CHANGE qualifyId 	`Idqualify`      INT NOT NULL;
ALTER TABLE qualifying CHANGE raceId  		`IdRace`      	 INT;
ALTER TABLE qualifying CHANGE driverId    	`IdDriver`     	 INT;
ALTER TABLE qualifying CHANGE constructorId	`IdConstructor`  INT;
ALTER TABLE qualifying CHANGE q1    `q1`					 time;
ALTER TABLE qualifying CHANGE q2    `q2`					 time;
ALTER TABLE qualifying CHANGE q3    `q3`					 time;
ALTER TABLE qualifying DROP `index`;
#ALTER TABLE qualifying CHANGE number    `Number`         INT NOT NULL DEFAULT 0,
#ALTER TABLE qualifying CHANGE    `Position`		 INT NOT NULL DEFAULT 0,

/*Creamos indices de las tablas determinando claves primarias y foraneas*/
/*Creamos las relaciones entre las tablas, y con ellas las restricciones*/

ALTER TABLE circuits ADD PRIMARY KEY(IdCircuit);
ALTER TABLE constructor ADD PRIMARY KEY(IdConstructor);
ALTER TABLE drivers ADD PRIMARY KEY(IdDriver);
ALTER TABLE qualifying ADD PRIMARY KEY(Idqualify);
ALTER TABLE races ADD PRIMARY KEY(IdRace);
ALTER TABLE results ADD PRIMARY KEY(IdResults);


ALTER TABLE qualifying ADD CONSTRAINT `qualifying_fk_races` FOREIGN KEY (IdRace) REFERENCES races(IdRace) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE qualifying ADD CONSTRAINT `qualifying_fk_drivers` FOREIGN KEY (IdDriver) REFERENCES drivers(IdDriver) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE qualifying ADD CONSTRAINT `qualifying_fk_constructor` FOREIGN KEY (IdConstructor) REFERENCES constructor(IdConstructor) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE races ADD CONSTRAINT `races_fk_circuits` FOREIGN KEY (IdCircuit) REFERENCES circuits (IdCircuit) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE results ADD CONSTRAINT `results_fk_races` FOREIGN KEY (IdRace) REFERENCES races(IdRace) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE results ADD CONSTRAINT `results_fk_drivers` FOREIGN KEY (IdDriver) REFERENCES drivers(IdDriver) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE results ADD CONSTRAINT `results_fk_constructor` FOREIGN KEY (IdConstructor) REFERENCES constructor(IdConstructor) ON DELETE RESTRICT ON UPDATE RESTRICT;
