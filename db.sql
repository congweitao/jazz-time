-- execute the command to create related tables
--- mysql -uroot -p123456 -e "source db.sql"
DROP DATABASE IF EXISTS `wanghong`;
CREATE DATABASE `wanghong` DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_general_ci;
USE `wanghong`;
set names utf8mb4;

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
    `id` INT UNSIGNED,
    `name` VARCHAR(100),
    `order` INT UNSIGNED,
    PRIMARY KEY (`id`)
);

--DROP TABLE IF EXISTS `Tbl_Huajiao_Live`;
CREATE TABLE `Tbl_Huajiao_Live` (
    `FLiveId` INT UNSIGNED NOT NULL,
    `FUserId` INT UNSIGNED NOT NULL,
    `FWatches` INT UNSIGNED NOT NULL DEFAULT 0  COMMENT '观看人数',
    `FPraises` INT UNSIGNED NOT NULL DEFAULT 0  COMMENT '赞数',
    `FReposts` INT UNSIGNED NOT NULL DEFAULT 0  COMMENT 'unknown',
    `FReplies` INT UNSIGNED NOT NULL DEFAULT 0  COMMENT 'unknown',
    `FPublishTimestamp` INT UNSIGNED NOT NULL COMMENT '发布日期',
    `FTitle` VARCHAR(100) NOT NULL DEFAULT '' COMMENT '直播名称',
    `FImage` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '直播封面',
    `FLocation` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '地点',
    `FScrapedTime` timestamp NOT NULL COMMENT '爬虫更新时间',
    PRIMARY KEY (`FLiveId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--DROP TABLE IF EXISTS `Tbl_Huajiao_User`;
CREATE TABLE `Tbl_Huajiao_User` (
    `FUserId` INT UNSIGNED NOT NULL,
    `FUserName` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '昵称',
    `FLevel` INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '等级',
    `FFollow` INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '关注数',
    `FFollowed` INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '粉丝数',
    `FSupported` INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '赞数',
    `FExperience` INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '经验值',
    `FAvatar` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '头像地址',
    `FScrapedTime` timestamp NOT NULL COMMENT '爬虫时间',
    PRIMARY KEY (`FUserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 主播汇总表
-- DROP TABLE IF EXISTS `Tbl_Actor`;
CREATE TABLE `Tbl_Actor` (
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `uid` VARCHAR(30) NOT NULL DEFAULT '' COMMENT '唯一标识用户',
    `nickname` VARCHAR(100) NOT NULL DEFAULT '' COMMENT '昵称',
    `follow` INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '关注数',
    `followed` INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '粉丝数',
    `praised` INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '被赞数',
    `avatar` VARCHAR(200) NOT NULL DEFAULT '' COMMENT '头像',
    `pid` TINYINT UNSIGNED NOT NULL DEFAULT 0 COMMENT '平台id, 1-花椒，2-一下',
    `scraped_time` timestamp NOT NULL COMMENT '爬虫更新时间',
    PRIMARY KEY (`id`),
    UNIQUE INDEX `INDEX_uid_pid` (`uid`, `pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
