
USE pokedex;


DROP TABLE IF EXISTS `pokemon`;
DROP TABLE IF EXISTS `moves`;
DROP TABLE IF EXISTS `evolutions`;
DROP TABLE IF EXISTS `generations`;
DROP TABLE IF EXISTS `ability`;
DROP TABLE IF EXISTS `level_moves`;

CREATE TABLE `pokemon` (
    `pokedex_number`            int             not null,
    `name`                varchar(40)     not null unique,
    `type_1`              varchar(20)     ,
    `type_2`              varchar(20)     ,
    `base_stat`           int             not null,
    `hp`                  int             not null,
    `attack`              int             not null,
    `special_attack`      int             not null,
    `defence`             int             not null,
    `special_defence`     int             not null,
    `speed`               int             not null,
    `generation`          int             not null,
    `isLegendary`           varchar(20)       
    
);

/*`ability1`            varchar(20)     ,
    `ability2`            varchar(20)     ,
    `generation`          int             ,
    `class`               int   */          

CREATE TABLE `moves` (
    `name`              varchar(20)     not null unique,
    `type`              varchar(20)     not null unique,
    `description`       varchar(500)    ,
    `power`             int             ,
    `accury`            int             ,
    `pp`                int             not null ,
    `tm_number`         int             unique   
);

CREATE TABLE `evolutions`(
    `lower_pokemon_number`      varchar(40)     not null,
    `high_pokemon_number`       varchar(40)     not null,
    `level`                     int                 ,
    `description`               varchar(40)         
);

CREATE TABLE `generations`(
    `number`    int             not null unique,
    `name`      varchar(20)     not null
);

CREATE TABLE `level_moves`(
    `pokemon_number`    int          not null, 
    `move`              char(20)     not null, 
    `level`             int
);


-- LOAD DATA INFILE '/var/lib/mysql-files/pokemondata.csv' INTO TABLE pokemon 
-- FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' ;

-- select * from pokemon;

-- INSERT INTO `pokemon` (pokedex_number, name, base_stat, hp, attack, special_attack, defence, special_defence, speed, generation, isLegendary)
-- VALUES (151, 'mew', 600, 1,1,1,1,1,1,1,'false');

-- INSERT INTO `pokemon` (pokedex_number, name, base_stat, hp, attack, special_attack, defence, special_defence, speed, generation, isLegendary) 
-- VALUES (720,'HoopaHoopa Unbound','Psychic','Dark',680,80,160,60,170,130,80,6,'True');




