/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : books

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2020-07-26 20:23:19
*/
#补充mysql安装
#https://www.cnblogs.com/zhangkanghui/p/9613844.html
#库生成
#create database book;
-- CREATE DATABASE IF NOT EXISTS book
--     -> DEFAULT CHARACTER SET utf8
--     -> DEFAULT COLLATE utf8_chinese_ci;

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_login
-- ----------------------------
DROP TABLE IF EXISTS `t_login`;
CREATE TABLE `t_login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `case_desc` varchar(100) NOT NULL COMMENT '用例描述',
  `loginName` varchar(11) NOT NULL COMMENT '用户名',
  `password` varchar(100) NOT NULL COMMENT '密码',
  `status_code` int(10) NOT NULL DEFAULT '0' COMMENT '响应状态码',
  `returnCode` varchar(11) NOT NULL COMMENT '业务状态码',
  `returnMsg` varchar(100) NOT NULL COMMENT '业务状态消息',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='iHousekeeping参数化';

-- ----------------------------
-- Records of t_login
-- ----------------------------
INSERT INTO `t_login` VALUES ('1', 'case01登录成功', '13500000000', 'e52f073160e5604f72b24a7d6df0d526b5c0b0e2fa7ecac31ca45223ebe9a0d1', '200',  '0000', 'Success');
INSERT INTO `t_login` VALUES ('2', 'case02密码错误', '13500000000', '1e52f073160e5604f72b24a7d6df0d526b5c0b0e2fa7ecac31ca45223ebe9a0d1', '200',  'IHKER04', '账号或密码有误，请重新输入。提示：账号或密码输入错误超过5次，系统将锁定30分钟');
INSERT INTO `t_login` VALUES ('3', 'case03账号不存在', '13500000999', 'e52f073160e5604f72b24a7d6df0d526b5c0b0e2fa7ecac31ca45223ebe9a0d1', '200',  'IHK14', '用户不存在');
