CREATE TABLE `curso_python`.`apostantes` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL,
  `Saldo` INT NULL,
  PRIMARY KEY (`ID`));

CREATE TABLE `curso_python`.`gran_premio` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL,
  `Distancia` INT NULL,
  `Num_Carreras` INT NULL,
  PRIMARY KEY (`ID`));

CREATE TABLE `curso_python`.`caballos` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL,
  `Fecha_nacimiento` DATETIME NULL,
  `Velocidad` INT NULL,
  `Experiencia` INT NULL,
  `Valor_apuesta` INT NULL,
  `ID_gran_premio` INT NULL,
  PRIMARY KEY (`ID`),
  INDEX `ID_gran_premio_idx` (`ID_gran_premio` ASC) VISIBLE,
  CONSTRAINT `ID_gran_premio`
    FOREIGN KEY (`ID_gran_premio`)
    REFERENCES `curso_python`.`gran_premio` (`ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);