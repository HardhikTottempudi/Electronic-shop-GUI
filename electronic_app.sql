-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: 12b_hardhik
-- ------------------------------------------------------
-- Server version	5.5.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill` (
  `Item_type` varchar(20) DEFAULT NULL,
  `Item_name` varchar(50) DEFAULT NULL,
  `Price` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES ('MOBILE','Iphone 13 mini',3000),('MOBILE','Iphone 13 pro',4000);
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bill_final`
--

DROP TABLE IF EXISTS `bill_final`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill_final` (
  `sl_no` int(11) DEFAULT NULL,
  `Item_type` varchar(20) DEFAULT NULL,
  `Item_name` varchar(50) DEFAULT NULL,
  `Price` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill_final`
--

LOCK TABLES `bill_final` WRITE;
/*!40000 ALTER TABLE `bill_final` DISABLE KEYS */;
INSERT INTO `bill_final` VALUES (0,'MOBILE','Iphone 13 mini',3000),(1,'MOBILE','Iphone 13 pro',4000);
/*!40000 ALTER TABLE `bill_final` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `laptops`
--

DROP TABLE IF EXISTS `laptops`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `laptops` (
  `item_name` varchar(20) DEFAULT NULL,
  `brand_name` varchar(50) DEFAULT NULL,
  `Price` int(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `laptops`
--

LOCK TABLES `laptops` WRITE;
/*!40000 ALTER TABLE `laptops` DISABLE KEYS */;
INSERT INTO `laptops` VALUES ('LAPTOPS','Asus TUF',2149),('LAPTOPS','VivoBook',1999),('LAPTOPS','MacBook',8000),('LAPTOPS','Chromebook',4000),('LAPTOPS','Lenovo yoga slim',3299),('LAPTOPS','HP',2099),('LAPTOPS','Dell vosto',1299),('LAPTOPS','Surface go miscrosoft',1899);
/*!40000 ALTER TABLE `laptops` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_data`
--

DROP TABLE IF EXISTS `login_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login_data` (
  `Username` varchar(11) DEFAULT NULL,
  `password` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_data`
--

LOCK TABLES `login_data` WRITE;
/*!40000 ALTER TABLE `login_data` DISABLE KEYS */;
INSERT INTO `login_data` VALUES ('Harsh','password@123'),('Hardhik','projectrender'),('Hrishikesh','1234'),('Smitha','smitha'),('hi1','hello');
/*!40000 ALTER TABLE `login_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `music`
--

DROP TABLE IF EXISTS `music`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `music` (
  `Sno` int(11) DEFAULT NULL,
  `Music` varchar(50) DEFAULT NULL,
  `Artist` varchar(50) DEFAULT NULL,
  `Date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `music`
--

LOCK TABLES `music` WRITE;
/*!40000 ALTER TABLE `music` DISABLE KEYS */;
INSERT INTO `music` VALUES (1,'Strawberries & cigarettes','Troy sivon','2022-06-10'),(2,'Enchanted','Taylor swift','2022-06-15'),(3,'Rockstar','Post malone','2010-05-21'),(3,'Heartless','Kanye west','2022-05-21'),(4,'Goosebumps','Travis Scott','2023-05-21');
/*!40000 ALTER TABLE `music` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop`
--

DROP TABLE IF EXISTS `shop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop` (
  `No` int(11) DEFAULT NULL,
  `shop_name` varchar(20) DEFAULT NULL,
  `sale` int(11) DEFAULT NULL,
  `Area` varchar(20) DEFAULT NULL,
  `Cust_percent` decimal(4,2) DEFAULT NULL,
  `Rating` char(5) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop`
--

LOCK TABLES `shop` WRITE;
/*!40000 ALTER TABLE `shop` DISABLE KEYS */;
INSERT INTO `shop` VALUES (1,'West side',250000,'West',68.60,'C','Delhi');
/*!40000 ALTER TABLE `shop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `smartphones`
--

DROP TABLE IF EXISTS `smartphones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `smartphones` (
  `item_name` varchar(20) DEFAULT NULL,
  `brand_name` varchar(50) DEFAULT NULL,
  `Price` int(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smartphones`
--

LOCK TABLES `smartphones` WRITE;
/*!40000 ALTER TABLE `smartphones` DISABLE KEYS */;
INSERT INTO `smartphones` VALUES ('MOBILE','Iphone 13 mini',3000),('MOBILE','Iphone 13 pro',4000),('MOBILE','Samsung Galaxy Z',4249),('MOBILE','Oneplus-nord',799),('MOBILE','Oppo Reno5',1049);
/*!40000 ALTER TABLE `smartphones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tvaudio`
--

DROP TABLE IF EXISTS `tvaudio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tvaudio` (
  `item_name` varchar(20) DEFAULT NULL,
  `brand_name` varchar(50) DEFAULT NULL,
  `Price` int(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tvaudio`
--

LOCK TABLES `tvaudio` WRITE;
/*!40000 ALTER TABLE `tvaudio` DISABLE KEYS */;
INSERT INTO `tvaudio` VALUES ('TV&AUDIO','Sony bravia 65\'',3239),('TV&AUDIO','Samsung 55\'',1546),('TV&AUDIO','Star trach 40\'',360),('TV&AUDIO','Samsung AU7000',2799),('TV&AUDIO','TLC',800),('TV&AUDIO','JBL home studio',500),('TV&AUDIO','KEF MUO wireless',549),('TV&AUDIO','RedDragon Gs520',60),('TV&AUDIO','KEF Prosche Design',1599),('TV&AUDIO','Sony SRS',1051);
/*!40000 ALTER TABLE `tvaudio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `videogames`
--

DROP TABLE IF EXISTS `videogames`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `videogames` (
  `item_name` varchar(20) DEFAULT NULL,
  `brand_name` varchar(50) DEFAULT NULL,
  `Price` int(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `videogames`
--

LOCK TABLES `videogames` WRITE;
/*!40000 ALTER TABLE `videogames` DISABLE KEYS */;
INSERT INTO `videogames` VALUES ('VIDEO GAMES','Red dead redemption 1',200),('VIDEO GAMES','Super mario bros',175),('VIDEO GAMES','Legends of Zelda',175),('VIDEO GAMES','Assasins creed ',85),('VIDEO GAMES','FIFA 22',50);
/*!40000 ALTER TABLE `videogames` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-16  0:23:20
