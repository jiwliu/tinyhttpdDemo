DROP DATABASE IF EXISTS `Demo`;
CREATE DATABASE `Demo` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE Demo
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `username` VARCHAR(80) DEFAULT NULL,
  `password` VARCHAR(32) DEFAULT NULL,
  `salt` VARCHAR(32) DEFAULT NULL,
  `head_url` VARCHAR(256) DEFAULT NULL
);
INSERT INTO `user`(username,`password`,salt,head_url) VALUES('user0','aaa','000','http://images.nowcoder.com/head/911m.png');
INSERT INTO `user`(username,`password`,salt,head_url) VALUES('user1','bbb','111','http://images.nowcoder.com/head/11m.png');
INSERT INTO `user`(username,`password`,salt,head_url) VALUES('user2','ccc','222','http://images.nowcoder.com/head/9m.png');
INSERT INTO `user`(username,`password`,salt,head_url) VALUES('user3','ddd','333','http://images.nowcoder.com/head/11m.png');
INSERT INTO `user`(username,`password`,salt,head_url) VALUES('user4','eee','444','http://images.nowcoder.com/head/41m.png');
INSERT INTO `user`(username,`password`,salt,head_url) VALUES('user5','fff','555','http://images.nowcoder.com/head/46m.png');
INSERT INTO `user`(username,`password`,salt,head_url) VALUES('user6','eee','666','http://images.nowcoder.com/head/1m.png');
INSERT INTO `user`(username,`password`,salt,head_url) VALUES('user7','xxx','777','http://images.nowcoder.com/head/91m.png');
INSERT INTO `user`(username,`password`,salt,head_url) VALUES('user8','zzz','888','http://images.nowcoder.com/head/111m.png');
INSERT INTO `user`(username,`password`,salt,head_url) VALUES('user9','www','999','http://images.nowcoder.com/head/56m.png');
INSERT INTO `user`(username,`password`,salt,head_url) VALUES('user10','ggg','123','http://images.nowcoder.com/head/871m.png');