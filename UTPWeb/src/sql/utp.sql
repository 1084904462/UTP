/*
Navicat MySQL Data Transfer

Source Server         : weige
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : utp

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2018-01-30 12:22:01
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `content`
-- ----------------------------
DROP TABLE IF EXISTS `content`;
CREATE TABLE `content` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `keyword_id` bigint(20) NOT NULL,
  `content` varchar(500) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`) USING BTREE,
  KEY `keyword_id` (`keyword_id`),
  CONSTRAINT `content_ibfk_1` FOREIGN KEY (`keyword_id`) REFERENCES `keyword` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of content
-- ----------------------------

-- ----------------------------
-- Table structure for `doc`
-- ----------------------------
DROP TABLE IF EXISTS `doc`;
CREATE TABLE `doc` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `link` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`) USING BTREE,
  UNIQUE KEY `link` (`link`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of doc
-- ----------------------------

-- ----------------------------
-- Table structure for `doc_content_conn`
-- ----------------------------
DROP TABLE IF EXISTS `doc_content_conn`;
CREATE TABLE `doc_content_conn` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `doc_id` bigint(20) NOT NULL,
  `content_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`) USING BTREE,
  KEY `doc_id` (`doc_id`),
  KEY `content_id` (`content_id`),
  CONSTRAINT `doc_content_conn_ibfk_1` FOREIGN KEY (`doc_id`) REFERENCES `doc` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `doc_content_conn_ibfk_2` FOREIGN KEY (`content_id`) REFERENCES `content` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of doc_content_conn
-- ----------------------------

-- ----------------------------
-- Table structure for `doc_tag_conn`
-- ----------------------------
DROP TABLE IF EXISTS `doc_tag_conn`;
CREATE TABLE `doc_tag_conn` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `doc_id` bigint(20) NOT NULL,
  `tag_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`) USING BTREE,
  KEY `doc_id` (`doc_id`),
  KEY `tag_id` (`tag_id`),
  CONSTRAINT `doc_tag_conn_ibfk_1` FOREIGN KEY (`doc_id`) REFERENCES `doc` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `doc_tag_conn_ibfk_2` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of doc_tag_conn
-- ----------------------------

-- ----------------------------
-- Table structure for `keyword`
-- ----------------------------
DROP TABLE IF EXISTS `keyword`;
CREATE TABLE `keyword` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `keyword` varchar(20) NOT NULL,
  `sign` int(20) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of keyword
-- ----------------------------

-- ----------------------------
-- Table structure for `keyword_conn`
-- ----------------------------
DROP TABLE IF EXISTS `keyword_conn`;
CREATE TABLE `keyword_conn` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `keyword_id1` bigint(20) NOT NULL,
  `keyword_id2` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`) USING BTREE,
  KEY `keyword_id1` (`keyword_id1`),
  KEY `keyword_id2` (`keyword_id2`),
  CONSTRAINT `keyword_conn_ibfk_1` FOREIGN KEY (`keyword_id1`) REFERENCES `keyword` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `keyword_conn_ibfk_2` FOREIGN KEY (`keyword_id2`) REFERENCES `keyword` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of keyword_conn
-- ----------------------------

-- ----------------------------
-- Table structure for `spider_url`
-- ----------------------------
DROP TABLE IF EXISTS `spider_url`;
CREATE TABLE `spider_url` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `web_url` varchar(100) NOT NULL,
  `last_url` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`) USING BTREE,
  UNIQUE KEY `web_url` (`web_url`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of spider_url
-- ----------------------------
INSERT INTO `spider_url` VALUES ('1', 'http://www.ccgp-jiangsu.gov.cn/cgxx/cjgg/', 'http://www.ccgp-jiangsu.gov.cn/cgxx/cjgg/zhenjiang/tnull_287343.html');

-- ----------------------------
-- Table structure for `tag`
-- ----------------------------
DROP TABLE IF EXISTS `tag`;
CREATE TABLE `tag` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `tag` varchar(20) NOT NULL,
  `sign` int(20) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tag
-- ----------------------------

-- ----------------------------
-- Table structure for `tag_conn`
-- ----------------------------
DROP TABLE IF EXISTS `tag_conn`;
CREATE TABLE `tag_conn` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `tag_id1` bigint(20) NOT NULL,
  `tag_id2` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`) USING BTREE,
  KEY `tag_id1` (`tag_id1`),
  KEY `tag_id2` (`tag_id2`),
  CONSTRAINT `tag_conn_ibfk_1` FOREIGN KEY (`tag_id1`) REFERENCES `tag` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tag_conn_ibfk_2` FOREIGN KEY (`tag_id2`) REFERENCES `tag` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tag_conn
-- ----------------------------
