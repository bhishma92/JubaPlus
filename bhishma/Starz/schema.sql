-- MySQL dump 10.13  Distrib 5.5.47, for Linux (x86_64)
--
-- Host: localhost    Database: starz
-- ------------------------------------------------------
-- Server version	5.5.47-cll

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `data`
--

DROP TABLE IF EXISTS `data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data` (
  `TransactionStart` varchar(32) DEFAULT NULL,
  `TransactionEnd` varchar(32) DEFAULT NULL,
  `AccountID` varchar(50) DEFAULT NULL,
  `ClientID` varchar(50) DEFAULT NULL,
  `SessionID` bigint(20) DEFAULT NULL,
  `DeviceID` varchar(50) DEFAULT NULL,
  `Affiliate` varchar(50) DEFAULT NULL,
  `Service` varchar(50) DEFAULT NULL,
  `ISP` varchar(50) DEFAULT NULL,
  `ASN` int(11) DEFAULT NULL,
  `Country` varchar(50) DEFAULT NULL,
  `State` varchar(8) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  `OS` varchar(32) DEFAULT NULL,
  `DeviceType` varchar(16) DEFAULT NULL,
  `DeviceModel` varchar(32) DEFAULT NULL,
  `ConnectionType` varchar(16) DEFAULT NULL,
  `AssetName` varchar(255) DEFAULT NULL,
  `Title` varchar(255) DEFAULT NULL,
  `seriesName` varchar(255) DEFAULT NULL,
  `episodeName` varchar(255) DEFAULT NULL,
  `season` smallint(3) DEFAULT NULL,
  `ContentID` int(8) DEFAULT NULL,
  `ContentType` varchar(16) DEFAULT NULL,
  `Rating` varchar(8) DEFAULT NULL,
  `AccessType` varchar(32) DEFAULT NULL,
  `CompleteView25Pct` tinyint(1) DEFAULT NULL,
  `CompleteView50Pct` tinyint(1) DEFAULT NULL,
  `CompleteView75Pct` tinyint(1) DEFAULT NULL,
  `CompleteView90Pct` tinyint(1) DEFAULT NULL,
  `Minute0To2` tinyint(1) DEFAULT NULL,
  `Minute2To5` tinyint(1) DEFAULT NULL,
  `Minute5To10` tinyint(1) DEFAULT NULL,
  `Minute10To20` tinyint(1) DEFAULT NULL,
  `Minute20To40` tinyint(1) DEFAULT NULL,
  `Minute40To60` tinyint(1) DEFAULT NULL,
  `Minute60To90` tinyint(1) DEFAULT NULL,
  `Minute90To120` tinyint(1) DEFAULT NULL,
  `Minute120To150` tinyint(1) DEFAULT NULL,
  `Minute150To180` tinyint(1) DEFAULT NULL,
  `MinuteGT180` tinyint(1) DEFAULT NULL,
  `TotalPlayTimeSec` float(9,3) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-04-20 17:24:02
