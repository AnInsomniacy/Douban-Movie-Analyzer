SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS `movie_info`;
CREATE TABLE `movie_info`
(
    `id`            int(10) NOT NULL AUTO_INCREMENT,
    `url`           varchar(255) DEFAULT NULL,
    `filmname`      varchar(255) DEFAULT NULL,
    `score`         double       DEFAULT NULL,
    `mins`          int(255)     DEFAULT NULL,
    `comments`      int(255)     DEFAULT NULL,
    `showtime`      int(255)     DEFAULT NULL,
    `genres`        varchar(255) DEFAULT NULL,
    `areas`         varchar(255) DEFAULT NULL,
    `actors`        varchar(255) DEFAULT NULL,
    `directors`     varchar(255) DEFAULT NULL,
    `scriptwriters` varchar(255) DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 2187
  DEFAULT CHARSET = utf8;