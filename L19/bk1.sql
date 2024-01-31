-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: sbi_4jan23
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `sbi_4jan23`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `sbi_4jan23` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `sbi_4jan23`;

--
-- Table structure for table `sa`
--

DROP TABLE IF EXISTS `sa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sa` (
  `ano` bigint unsigned NOT NULL,
  `name` varchar(50) NOT NULL,
  `balance` double unsigned NOT NULL,
  PRIMARY KEY (`ano`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sa`
--

LOCK TABLES `sa` WRITE;
/*!40000 ALTER TABLE `sa` DISABLE KEYS */;
INSERT INTO `sa` VALUES (100,'kamal',10000),(200,'vedant',3500);
/*!40000 ALTER TABLE `sa` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `t1` BEFORE INSERT ON `sa` FOR EACH ROW begin
	if (new.ano is null)  or (new.ano < 1) then
		signal SQLSTATE '12345' set message_text = "invalid account number";
	end if;

	if (new.name is null) or (length(trim(new.name)) = 0 ) or 
		(length(trim(new.name)) < 2) or (not new.name regexp "^[A-Za-z ]+$") then
		signal SQLSTATE '23456' set message_text = "invalid name";
	end if;
	
	if (new.balance is null) or (new.balance < 3000) then
		signal SQLSTATE '34567' set message_text = "balance shoud be minimum 3000";
	end if;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `t2` BEFORE UPDATE ON `sa` FOR EACH ROW begin
	if (new.ano is null)  or (new.ano < 1) then
		signal SQLSTATE '12345' set message_text = "invalid account number";
	end if;

	if (new.name is null) or (length(trim(new.name)) = 0 ) or 
		(length(trim(new.name)) < 2) or (not new.name regexp "^[A-Za-z ]+$") then
		signal SQLSTATE '23456' set message_text = "invalid name";
	end if;
	
	if (new.balance is null) or (new.balance < 3000) then
		signal SQLSTATE '34567' set message_text = "balance shoud be minimum 3000";
	end if;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `sa_bbkuop`
--

DROP TABLE IF EXISTS `sa_bbkuop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sa_bbkuop` (
  `ano` bigint unsigned NOT NULL,
  `name` varchar(50) NOT NULL,
  `balance` double unsigned NOT NULL,
  PRIMARY KEY (`ano`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sa_bbkuop`
--

LOCK TABLES `sa_bbkuop` WRITE;
/*!40000 ALTER TABLE `sa_bbkuop` DISABLE KEYS */;
/*!40000 ALTER TABLE `sa_bbkuop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sa_bkup`
--

DROP TABLE IF EXISTS `sa_bkup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sa_bkup` (
  `ano` bigint unsigned NOT NULL,
  `name` varchar(50) NOT NULL,
  `balance` double unsigned NOT NULL,
  PRIMARY KEY (`ano`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sa_bkup`
--

LOCK TABLES `sa_bkup` WRITE;
/*!40000 ALTER TABLE `sa_bkup` DISABLE KEYS */;
INSERT INTO `sa_bkup` VALUES (100,'kamal',10000),(200,'vedant',3500);
/*!40000 ALTER TABLE `sa_bkup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'sbi_4jan23'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-04 20:07:45
