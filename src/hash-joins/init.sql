create database playground;

use playground;

CREATE TABLE `t1` (
    `id` int(11) NOT NULL AUTO_INCREMENT ,
    `c1` int(11) NOT NULL DEFAULT '0',
    `c2` int(11) NOT NULL DEFAULT '0',
    PRIMARY KEY (`id`),
    KEY `idx_c1` (`c1`)
    ) ENGINE=InnoDB;

 CREATE TABLE `t2` (
    `id` int(11) NOT NULL AUTO_INCREMENT ,
    `c1` int(11) NOT NULL DEFAULT '0',
    `c2` int(11) NOT NULL DEFAULT '0',
    PRIMARY KEY (`id`),
    KEY `idx_c1` (`c1`)
    ) ENGINE=InnoDB;

CREATE TABLE `t1_idx` (
    `id` int(11) NOT NULL AUTO_INCREMENT ,
    `c1` int(11) NOT NULL DEFAULT '0',
    `c2` int(11) NOT NULL DEFAULT '0',
    PRIMARY KEY (`id`),
    KEY `idx_c1` (`c1`),
    KEY `idx_c2` (`c2`)
    ) ENGINE=InnoDB;

 CREATE TABLE `t2_idx` (
    `id` int(11) NOT NULL AUTO_INCREMENT ,
    `c1` int(11) NOT NULL DEFAULT '0',
    `c2` int(11) NOT NULL DEFAULT '0',
    PRIMARY KEY (`id`),
    KEY `idx_c1` (`c1`),
    KEY `idx_c2` (`c2`)
    ) ENGINE=InnoDB;
