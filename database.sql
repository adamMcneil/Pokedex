
USE pokedex;


DROP TABLE IF EXISTS `pokemon`;
DROP TABLE IF EXISTS `level_moves`;
DROP TABLE IF EXISTS `moves`;
DROP TABLE IF EXISTS `evolutions`;
DROP TABLE IF EXISTS `generations`;
DROP TABLE IF EXISTS `ability`;


CREATE TABLE `generations`(
    `number`    int             not null unique,
    `name`      varchar(20)     not null,
    Primary Key (number)
);

CREATE TABLE `pokemon` (
    `pokedex_number`      int             not null,
    `name`                varchar(40)     not null unique,
    `type_1`              varchar(20)     not null,
    `type_2`              varchar(20)     ,
    `base_stat`           int             not null,
    `hp`                  int             not null,
    `attack`              int             not null,
    `special_attack`      int             not null,
    `defence`             int             not null,
    `special_defence`     int             not null,
    `speed`               int             not null,
    `generation`          int             not null,
    `isLegendary`         varchar(20)     not null,
    Primary Key (name),
    foreign key (generation) references generations(number)   
    
);

-- Name,Type,Category,Effect,Power,Acc,PP,TM,Prob.(%),Gen
CREATE TABLE `moves` (
    `name`              varchar(40)     not null unique,
    `type`              varchar(20)     not null,
    `category`          varchar(20)     not null,
    `description`       varchar(500)    ,
    `power`             int             ,
    `accury`            int             ,
    `pp`                int             ,
    `tm_number`         int             ,
    `probability`       int             ,
    `generation`        int             not null,
    Primary Key (name)
);

CREATE TABLE `level_moves`(
    `pokemon_number`    int          not null, 
    `move`              char(20)     not null, 
    `level`             int
);

CREATE TABLE `evolutions`(
    `lower_pokemon_number`      varchar(40)     not null,
    `high_pokemon_number`       varchar(40)     not null,
    `level`                     int                 ,
    `description`               varchar(40)         
);




-- LOAD DATA INFILE '/var/lib/mysql-files/pokemondata.csv' INTO TABLE pokemon 
-- FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' ;

-- select * from pokemon;

-- INSERT INTO `pokemon` (pokedex_number, name, base_stat, hp, attack, special_attack, defence, special_defence, speed, generation, isLegendary)
-- VALUES (151, 'mew', 600, 1,1,1,1,1,1,1,'false');

-- INSERT INTO `moves` (name, type, category, description, power, accury, pp, tm_number, probability, generation) 
-- VALUES ('Absorb','Grass','Special','User recovers half the HP inflicted on opponent.',20,100,25,NULL,NULL,1);




