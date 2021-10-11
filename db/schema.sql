-- MySQL dump 10.13  Distrib 8.0.26, for macos11.3 (x86_64)
--
-- Host: localhost    Database: dbproject
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `address` (
  `id` int NOT NULL AUTO_INCREMENT,
  `street` varchar(80) NOT NULL,
  `house_number` varchar(5) NOT NULL,
  `city` varchar(80) NOT NULL,
  `postcode` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` VALUES (1,'WvClaan','35A','Maastricht','6226BR'),(2,'Hood','35','Helsinki','00980'),(3,'Maas street','22','Maastricht','6263AB');
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(80) NOT NULL,
  `lastname` varchar(80) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `address_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `address_id` (`address_id`),
  CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`address_id`) REFERENCES `address` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Eric','Banzuzi','0442935840',1),(2,'Tresor','Banzuzi','0502525611',2),(3,'Kanye','West','046271882',3);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delivery`
--

DROP TABLE IF EXISTS `delivery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery` (
  `delivery_person_id` int NOT NULL,
  `order_id` int NOT NULL,
  `estimated_time` datetime NOT NULL,
  PRIMARY KEY (`delivery_person_id`,`order_id`),
  KEY `order_id` (`order_id`),
  CONSTRAINT `delivery_ibfk_1` FOREIGN KEY (`delivery_person_id`) REFERENCES `delivery_person` (`id`),
  CONSTRAINT `delivery_ibfk_2` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery`
--

LOCK TABLES `delivery` WRITE;
/*!40000 ALTER TABLE `delivery` DISABLE KEYS */;
INSERT INTO `delivery` VALUES (5,1,'2021-10-07 11:32:50'),(5,8,'2021-10-08 22:10:56'),(5,9,'2021-10-08 22:19:22'),(5,14,'2021-10-08 22:55:47'),(5,15,'2021-10-08 23:02:49'),(5,16,'2021-10-08 23:07:22'),(5,17,'2021-10-08 23:10:49'),(5,18,'2021-10-08 23:10:49'),(5,23,'2021-10-08 23:51:27'),(5,25,'2021-10-09 00:26:07'),(5,26,'2021-10-09 01:00:32'),(5,28,'2021-10-09 01:34:46'),(5,30,'2021-10-09 15:26:20'),(5,31,'2021-10-09 15:26:20'),(5,33,'2021-10-09 16:01:10'),(5,36,'2021-10-09 16:35:33'),(5,39,'2021-10-12 17:09:51'),(6,10,'2021-10-08 22:35:32'),(6,11,'2021-10-08 22:36:48'),(6,12,'2021-10-08 22:42:36'),(6,13,'2021-10-08 22:48:50'),(6,19,'2021-10-08 23:31:58'),(6,20,'2021-10-08 23:31:58'),(6,21,'2021-10-08 23:31:58'),(6,22,'2021-10-09 00:06:26'),(6,24,'2021-10-09 00:40:37'),(6,27,'2021-10-09 01:14:53'),(6,29,'2021-10-09 01:49:32'),(6,32,'2021-10-09 15:42:48'),(6,34,'2021-10-09 16:16:55'),(6,35,'2021-10-09 16:16:55'),(6,37,'2021-10-09 16:51:09');
/*!40000 ALTER TABLE `delivery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delivery_person`
--

DROP TABLE IF EXISTS `delivery_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery_person` (
  `id` int NOT NULL AUTO_INCREMENT,
  `area_code` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery_person`
--

LOCK TABLES `delivery_person` WRITE;
/*!40000 ALTER TABLE `delivery_person` DISABLE KEYS */;
INSERT INTO `delivery_person` VALUES (1,'60'),(2,'60'),(3,'61'),(4,'61'),(5,'62'),(6,'62'),(7,'63'),(8,'63'),(9,'64'),(10,'64');
/*!40000 ALTER TABLE `delivery_person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `desert`
--

DROP TABLE IF EXISTS `desert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `desert` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `desert`
--

LOCK TABLES `desert` WRITE;
/*!40000 ALTER TABLE `desert` DISABLE KEYS */;
INSERT INTO `desert` VALUES (1,'Cheese cake',3.50),(2,'Ice cream',2.50);
/*!40000 ALTER TABLE `desert` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drink`
--

DROP TABLE IF EXISTS `drink`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drink` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drink`
--

LOCK TABLES `drink` WRITE;
/*!40000 ALTER TABLE `drink` DISABLE KEYS */;
INSERT INTO `drink` VALUES (1,'Coca-Cola',1.99),(2,'Fanta',1.99),(3,'Sprite',1.99),(4,'Iced-Tea',1.99);
/*!40000 ALTER TABLE `drink` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderline`
--

DROP TABLE IF EXISTS `orderline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orderline` (
  `id` int NOT NULL AUTO_INCREMENT,
  `order_id` int DEFAULT NULL,
  `pizza_id` int DEFAULT NULL,
  `drink_id` int DEFAULT NULL,
  `desert_id` int DEFAULT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_id` (`order_id`),
  KEY `pizza_id` (`pizza_id`),
  KEY `drink_id` (`drink_id`),
  KEY `desert_id` (`desert_id`),
  CONSTRAINT `orderline_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`),
  CONSTRAINT `orderline_ibfk_2` FOREIGN KEY (`pizza_id`) REFERENCES `pizza` (`id`),
  CONSTRAINT `orderline_ibfk_3` FOREIGN KEY (`drink_id`) REFERENCES `drink` (`id`),
  CONSTRAINT `orderline_ibfk_4` FOREIGN KEY (`desert_id`) REFERENCES `desert` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderline`
--

LOCK TABLES `orderline` WRITE;
/*!40000 ALTER TABLE `orderline` DISABLE KEYS */;
INSERT INTO `orderline` VALUES (1,1,1,NULL,NULL,1),(2,1,NULL,2,NULL,1),(3,1,NULL,NULL,1,1),(4,2,1,NULL,NULL,2),(5,2,NULL,NULL,1,2),(6,3,1,NULL,NULL,1),(7,4,1,NULL,NULL,2),(8,4,NULL,1,NULL,1),(9,5,1,NULL,NULL,2),(10,5,NULL,1,NULL,1),(11,6,1,NULL,NULL,1),(12,7,1,NULL,NULL,2),(13,8,9,NULL,NULL,1),(14,9,9,NULL,NULL,1),(15,10,9,NULL,NULL,1),(16,11,2,NULL,NULL,1),(17,12,1,NULL,NULL,1),(18,13,1,NULL,NULL,1),(19,14,1,NULL,NULL,2),(20,15,1,NULL,NULL,1),(21,16,2,NULL,NULL,1),(22,17,2,NULL,NULL,1),(23,18,1,NULL,NULL,1),(24,19,9,NULL,NULL,1),(25,20,8,NULL,NULL,1),(26,21,1,NULL,NULL,1),(27,22,1,NULL,NULL,1),(28,23,1,NULL,NULL,1),(29,24,1,NULL,NULL,1),(30,25,1,NULL,NULL,1),(31,26,1,NULL,NULL,1),(32,27,1,NULL,NULL,1),(33,28,1,NULL,NULL,1),(34,29,1,NULL,NULL,1),(35,30,1,NULL,NULL,1),(36,31,1,NULL,NULL,1),(37,31,NULL,4,NULL,1),(38,32,1,NULL,NULL,1),(39,33,1,NULL,NULL,1),(40,34,1,NULL,NULL,1),(41,35,1,NULL,NULL,1),(42,36,1,NULL,NULL,2),(43,37,1,NULL,NULL,1),(44,38,1,NULL,NULL,3),(45,39,1,NULL,NULL,10),(46,39,NULL,2,NULL,1),(47,40,3,NULL,NULL,1);
/*!40000 ALTER TABLE `orderline` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int DEFAULT NULL,
  `datetime` datetime NOT NULL,
  `discount_code` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,1,'2021-10-04 23:13:41',0),(2,1,'2021-10-05 13:06:49',0),(3,1,'2021-10-07 00:43:19',0),(4,1,'2021-10-08 21:40:07',0),(5,1,'2021-10-08 21:42:30',0),(6,1,'2021-10-08 21:45:36',0),(7,1,'2021-10-08 21:51:33',0),(8,1,'2021-10-08 21:55:56',0),(9,1,'2021-10-08 22:04:22',0),(10,1,'2021-10-08 22:20:32',0),(11,1,'2021-10-08 22:21:48',0),(12,1,'2021-10-08 22:27:36',0),(13,1,'2021-10-08 22:33:50',0),(14,1,'2021-10-08 22:40:47',0),(15,1,'2021-10-08 22:47:49',0),(16,1,'2021-10-08 22:52:22',1),(17,1,'2021-10-08 22:55:49',0),(18,1,'2021-10-08 23:07:20',0),(19,1,'2021-10-08 23:16:58',0),(20,1,'2021-10-08 23:18:06',0),(21,1,'2021-10-08 23:19:37',0),(22,1,'2021-10-08 23:24:26',0),(23,1,'2021-10-08 23:36:27',0),(24,1,'2021-10-08 23:42:37',0),(25,1,'2021-10-08 23:46:07',0),(26,1,'2021-10-09 00:05:32',1),(27,1,'2021-10-09 00:10:53',0),(28,1,'2021-10-09 00:11:46',0),(29,1,'2021-10-09 00:18:32',0),(30,1,'2021-10-09 15:11:20',0),(31,1,'2021-10-09 15:14:17',0),(32,1,'2021-10-09 15:27:48',0),(33,1,'2021-10-09 15:33:10',0),(34,1,'2021-10-09 16:01:55',0),(35,1,'2021-10-09 16:04:54',0),(36,1,'2021-10-09 16:12:33',0),(37,1,'2021-10-09 16:14:09',1),(38,2,'2021-10-11 19:26:11',0),(39,3,'2021-10-11 20:52:51',0),(40,1,'2021-10-11 20:54:05',1);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pizza`
--

DROP TABLE IF EXISTS `pizza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pizza` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pizza`
--

LOCK TABLES `pizza` WRITE;
/*!40000 ALTER TABLE `pizza` DISABLE KEYS */;
INSERT INTO `pizza` VALUES (5,'Diavolo'),(4,'Forest'),(2,'Hawaii'),(1,'Margherita'),(10,'Meatlovers'),(7,'Peppel Pizza'),(6,'Pepperoni'),(8,'Romano'),(3,'Veggie'),(9,'Veggie Deluxe');
/*!40000 ALTER TABLE `pizza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pizza_toppings`
--

DROP TABLE IF EXISTS `pizza_toppings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pizza_toppings` (
  `pizza_id` int NOT NULL,
  `topping_id` int NOT NULL,
  PRIMARY KEY (`pizza_id`,`topping_id`),
  KEY `topping_id` (`topping_id`),
  CONSTRAINT `pizza_toppings_ibfk_1` FOREIGN KEY (`pizza_id`) REFERENCES `pizza` (`id`),
  CONSTRAINT `pizza_toppings_ibfk_2` FOREIGN KEY (`topping_id`) REFERENCES `topping` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pizza_toppings`
--

LOCK TABLES `pizza_toppings` WRITE;
/*!40000 ALTER TABLE `pizza_toppings` DISABLE KEYS */;
INSERT INTO `pizza_toppings` VALUES (1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),(9,1),(10,1),(2,2),(4,2),(10,2),(2,3),(3,4),(5,4),(9,4),(10,4),(3,5),(8,5),(9,5),(3,6),(4,6),(9,6),(3,7),(5,7),(7,7),(9,7),(5,8),(8,8),(10,8),(6,9),(7,9),(10,9),(7,10),(10,10),(8,11),(9,12),(1,13),(2,13),(3,13),(4,13),(5,13),(6,13),(7,13),(8,13),(9,13),(1,14),(8,14),(9,14),(1,15);
/*!40000 ALTER TABLE `pizza_toppings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `topping`
--

DROP TABLE IF EXISTS `topping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `topping` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `vegetarian` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `topping`
--

LOCK TABLES `topping` WRITE;
/*!40000 ALTER TABLE `topping` DISABLE KEYS */;
INSERT INTO `topping` VALUES (1,'tomato sauce',0.99,1),(2,'ham',2.49,0),(3,'pineapple',1.20,1),(4,'onion',0.39,1),(5,'tomato',0.49,1),(6,'mushroom',1.00,1),(7,'pepper',1.20,1),(8,'spicy salami',2.99,0),(9,'pepperoni',2.49,0),(10,'chicken',2.49,0),(11,'egg',1.49,1),(12,'eggplant',1.49,1),(13,'mozzarella',1.59,1),(14,'oregano',0.49,1),(15,'garlic oil',0.49,1);
/*!40000 ALTER TABLE `topping` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-11 21:21:00
