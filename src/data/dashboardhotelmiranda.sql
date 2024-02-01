CREATE DATABASE  IF NOT EXISTS `dashboardhotelmiranda`;
USE `dashboardhotelmiranda`;

DROP TABLE IF EXISTS `rooms`;
CREATE TABLE `rooms` (
  `id` int NOT NULL AUTO_INCREMENT,
  `number` int NOT NULL,
  `photo` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `bed` varchar(255) NOT NULL,
  `amenities` json DEFAULT NULL,
  `description` varchar(255) NOT NULL,
  `rate` int NOT NULL,
  `price` int NOT NULL,
  `discount` int NOT NULL,
  `available` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `bookings`;
CREATE TABLE `bookings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `photo` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `orderDate` date NOT NULL,
  `orderTime` time NOT NULL,
  `checkinDate` date NOT NULL,
  `checkinTime` time NOT NULL,
  `checkout` date NOT NULL,
  `checkoutTime` time NOT NULL,
  `notes` text NOT NULL,
  `roomId` int NOT NULL,
  `status` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roomId` (`roomId`),
  CONSTRAINT `bookings_ibfk_1` FOREIGN KEY (`roomId`) REFERENCES `rooms` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `photo` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(9) NOT NULL,
  `description` text NOT NULL,
  `status` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `contacts`;
CREATE TABLE `contacts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `photo` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(9) NOT NULL,
  `comment` text NOT NULL,
  `date` date NOT NULL,
  `dateTime` time NOT NULL,
  `archived` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


LOCK TABLES `rooms` WRITE;
INSERT INTO `rooms` VALUES (29,16,'https://picsum.photos/seed/OHBAyDbO/640/480','Suite','Medium','[\"Room service\"]','j',0,75,54,1),(31,271,'https://picsum.photos/seed/Clg5jB/640/480','Single Bed','Medium','[\"Room service\"]','F',2,133,85,0),(32,159,'https://picsum.photos/seed/TggWV/640/480','Suite','Small','[\"Sea\"]','x',1,184,21,1),(33,77,'https://picsum.photos/seed/xsbQQ/640/480','Double Bed','Big','[\"Sea\"]','m',1,183,59,1),(34,36,'https://picsum.photos/seed/1aptfK6/640/480','Suite','Medium','[\"Room service\"]','w',4,92,44,0),(35,98,'https://picsum.photos/seed/ZL2cq2j/640/480','Double Bed','Medium','[\"Room service\"]','G',2,142,17,1),(36,292,'https://picsum.photos/seed/NAFdu07b/640/480','Suite','Big','[\"TV\"]','S',3,20,86,1),(37,185,'https://picsum.photos/seed/lYGhCnDd/640/480','Suite','Small','[\"Room service\"]','D',5,96,91,1),(38,72,'https://picsum.photos/seed/J6nsaf/640/480','Single Bed','Small','[\"Sea\"]','P',2,93,19,1),(39,294,'https://picsum.photos/seed/dX4B0ybt/640/480','Single Bed','Medium','[\"Sea\"]','w',3,109,39,1),(40,273,'https://picsum.photos/seed/a5kfrZpr/640/480','Double Bed','Big','[\"Sea\"]','j',1,274,98,1),(41,16,'https://picsum.photos/seed/DHwGg/640/480','Suite','Medium','[\"Room service\"]','Y',3,31,45,0),(42,227,'https://picsum.photos/seed/t3LNoA/640/480','Single Bed','Medium','[\"Sea\"]','U',3,81,18,1),(43,87,'https://picsum.photos/seed/B19rc/640/480','Single Bed','Medium','[\"Room service\"]','e',5,10,45,0),(44,182,'https://picsum.photos/seed/LlmWCS/640/480','Double Bed','Small','[\"Sea\"]','w',4,260,41,0),(45,226,'https://picsum.photos/seed/C8zKUX2XT/640/480','Suite','Medium','[\"TV\"]','description of room with id 6 and number 226',0,259,85,1);
UNLOCK TABLES;

LOCK TABLES `bookings` WRITE;
INSERT INTO `bookings` VALUES (26,'https://picsum.photos/seed/NoZQBE3dg/640/480','Mrs. Judy Stamm-Macejkovic III','2023-12-25','01:44:00','2024-01-19','11:44:00','2024-08-10','06:28:00','Alter sodalitas magnam centum casus adduco ea.',29,'booked'),(27,'https://picsum.photos/seed/cN8Tti/640/480','Anthony Sanford','2023-06-17','11:01:00','2024-01-19','01:44:00','2024-07-13','11:34:00','Confugo censura tamen tempus.',29,'refund'),(28,'https://picsum.photos/seed/wP1pXz8xUF/640/480','Nina Bartoletti','2023-11-20','02:21:00','2024-01-20','21:51:00','2024-12-14','14:41:00','Ultra deorsum ex canonicus a ciminatio nulla tripudio.',29,'refund'),(29,'https://picsum.photos/seed/QIx4L/640/480','Lana Stokes','2023-02-18','22:46:00','2024-01-19','03:34:00','2024-04-19','23:52:00','Alias caecus trans pel defero quis decipio votum.',29,'pending'),(30,'https://picsum.photos/seed/16jQm51K/640/480','test','2023-02-15','13:16:00','2024-01-19','10:05:00','2024-03-30','06:53:00','test',29,'pending'),(31,'https://picsum.photos/seed/T5gJmRMc/640/480','Dennis Crist V','2023-12-23','23:30:00','2024-01-19','10:40:00','2024-02-21','20:42:00','Demonstro repellat deserunt tempus defendo umerus tricesimus trado creator.',29,'refund'),(32,'https://picsum.photos/seed/sPr8vF/640/480','David Rodriguez II','2023-12-29','01:06:00','2024-01-19','11:23:00','2025-01-08','07:42:00','Aqua vesica talio communis thesaurus aranea virtus tripudio defessus ara.',34,'booked'),(33,'https://picsum.photos/seed/tTSxt0i6/640/480','Shelly Schneider DVM','2023-05-06','03:51:00','2024-01-19','00:42:00','2024-09-07','16:58:00','Deserunt traho vado amitto placeat asperiores utpote vomica venio arca.',31,'pending'),(34,'https://picsum.photos/seed/gdD6TR2/640/480','Kelvin Mayer','2023-04-16','07:45:00','2024-01-19','20:38:00','2024-04-05','05:39:00','Apparatus conservo complectus tempus.',29,'booked'),(35,'https://picsum.photos/seed/Gm1lir5/640/480','Kristin Reinger','2023-02-22','09:42:00','2024-01-19','09:36:00','2024-09-28','01:49:00','Addo tremo tergiversatio libero.',34,'pending'),(36,'https://picsum.photos/seed/IOVOm7ym/640/480','Wallace Weissnat','2023-11-19','15:18:00','2024-01-20','17:55:00','2024-07-11','21:53:00','Aro sto sollers beatae demitto tepidus.',35,'booked'),(37,'https://picsum.photos/seed/knUBdYXFxs/640/480','Miss Jessica Metz','2023-04-27','23:48:00','2024-01-20','22:35:00','2024-09-28','10:40:00','Absque quaerat acies defluo.',33,'refund'),(38,'https://picsum.photos/seed/O7Af5b/640/480','Spencer Homenick','2023-07-29','12:18:00','2024-01-19','06:41:00','2024-12-28','09:46:00','Pauper adulatio compello cohaero celo apparatus ventus depromo.',37,'refund'),(39,'https://picsum.photos/seed/f8VPhK46s/640/480','Eleanor Fay-Carroll','2023-07-02','15:21:00','2024-01-20','04:28:00','2024-06-11','00:30:00','Bestia theatrum verus aliquid adipiscor capitulus possimus vox.',32,'booked'),(40,'https://picsum.photos/seed/wHPJFNt/640/480','Josefina Bradtke','2023-04-11','08:55:00','2024-01-20','11:13:00','2025-01-02','04:29:00','Sponte spectaculum theologus adiuvo molestias artificiose comparo commodi caecus.',33,'booked');
UNLOCK TABLES;

LOCK TABLES `contacts` WRITE;
INSERT INTO `contacts` VALUES (25,'https://picsum.photos/seed/kdZIAydVQ/640/480','Beatrice Cartwright','Jo.Orn@gmail.com','639834434','Deleo angelus atrocitas verbum suus et curiositas. Bestia libero auctor avarus quod thymum amicitia esse. Illo corpus arguo chirographum tamquam solium pectus.','2024-01-18','05:26:00',1),(26,'https://picsum.photos/seed/UuycPQlCEG/640/480','April Lang','Mavis77@gmail.com','695943197','Crur video stillicidium sollers porro cupiditate sono crux cupio. Ustilo thorax sum chirographum. Denego triumphus celo taedium.','2024-01-18','00:35:00',0),(27,'https://picsum.photos/seed/AckF4nm/640/480','Blanche Kassulke','Shawn_Farrell38@gmail.com','682662207','Iusto corrumpo administratio. Demitto atque tabernus. Aeger communis varius tutamen ducimus tyrannus speciosus spes valens thymbra.','2024-01-18','16:42:00',0),(28,'https://picsum.photos/seed/Fwl5J63B/640/480','Winston Koepp','Ludwig10@yahoo.com','684907025','Astrum virgo ulciscor minima ulterius vilis nobis cilicium. Adhaero illo vix omnis demitto. Cohors ulciscor sulum coniecto dens.','2024-01-19','09:57:00',0),(29,'https://picsum.photos/seed/Qd51qklGa/640/480','Jackie Orn PhD','Armando.Funk92@hotmail.com','642670573','Quis acies turba cado iste adduco iusto eaque sodalitas. Ancilla thorax illum. Cursim appono doloribus arma patruus thesis possimus curo adsum doloremque.','2024-01-18','14:56:00',1),(30,'https://picsum.photos/seed/qqzkg4/640/480','test','test@test.com','675038080','Terror caecus tamen comparo harum. Tres cum creo solium crastinus audax amoveo denique cohors appositus. Stipes celer aegrus dignissimos.','2024-01-18','11:57:00',1),(31,'https://picsum.photos/seed/FbPnDjSUg/640/480','Marion Bernier','Taurean66@hotmail.com','658307130','Arceo custodia exercitationem adulatio stillicidium confero. Crux usque taceo ara expedita talus ademptio odit. Subvenio blanditiis accendo laudantium.','2024-01-18','09:51:00',1),(32,'https://picsum.photos/seed/6HoTcymT/640/480','Ruth Anderson','Anita.Kuhlman81@hotmail.com','628419521','Vigilo cometes caritas cribro ascisco. Cometes nihil absens brevis terebro dolorum titulus tabella suggero. Adduco taedium vulariter vero recusandae capillus armarium sub anser.','2024-01-19','04:13:00',0),(33,'https://picsum.photos/seed/HgWN2RD/640/480','Erma Quitzon','Cordia19@hotmail.com','682797671','Comes suadeo abscido. Aeneus quisquam tergeo caelum pecus solio harum pecus. Centum vere centum dedico itaque vestrum tres.','2024-01-18','20:18:00',0),(34,'https://picsum.photos/seed/GUyV907g0f/640/480','Blanche Grimes','Stephanie_Wunsch@yahoo.com','665471658','Verecundia adiuvo depereo avaritia. Porro vallum aveho delicate centum stella talus vociferor. Cupiditas asporto cotidie compello.','2024-01-19','02:34:00',1),(35,'https://picsum.photos/seed/649zB/640/480','Whitney Hartmann','Chase_Labadie@hotmail.com','682590497','Comminor necessitatibus virgo vesper tamquam asper arguo. Nobis sto defessus angelus. Conduco atavus utilis toties.','2024-01-18','23:29:00',0),(36,'https://picsum.photos/seed/qXCdP/640/480','Caroline Feest Sr.','Vidal.Morissette11@yahoo.com','652647259','Aestus delicate crux aranea ciminatio. Abduco usitas vir ocer theologus. Esse cavus delego animus tondeo comitatus subito decet trucido videlicet.','2024-01-19','14:26:00',0),(37,'https://picsum.photos/seed/aEdgQfLE/640/480','Delores VonRueden','Pat_Conn@gmail.com','685180395','Alter tenetur commodo tergiversatio acerbitas verumtamen quisquam alioqui. Auxilium appono delego creta nisi autem certe vox degenero. Thesis varius avaritia doloremque atavus tibi cito sponte cribro.','2024-01-18','22:22:00',0),(38,'https://picsum.photos/seed/XYTnsCgX/640/480','Wilbur Kris','Marcos.Koelpin@hotmail.com','685598931','Laudantium minus amoveo texo cohibeo. Similique alius laboriosam conspergo abduco civitas at depromo depopulo. Admoneo ter terreo ex beneficium testimonium vicinus ventus vulgo.','2024-01-18','03:35:00',1),(39,'https://picsum.photos/seed/dO1Wsof8y/640/480','Bryan Yost-Kreiger','Yasmin.Renner45@hotmail.com','686835701','Magnam alter decipio caelum capillus cuius tandem. Voluptatibus temeritas culpa alias ut laborum claudeo umerus argentum somnus. Solum coruscus vorax.','2024-01-18','13:38:00',1),(40,'https://picsum.photos/seed/iAfyqmPrz/640/480','Austin Kohler','Ali50@yahoo.com','632034401','Ustilo umquam adhaero natus adduco aiunt repellat. Communis caelestis acerbitas vobis subito acerbitas. Aspicio summopere magni.','2024-01-18','13:06:00',1);
UNLOCK TABLES;

LOCK TABLES `users` WRITE;
INSERT INTO `users` VALUES (25,'https://picsum.photos/seed/uJSmFKv/640/480','Miss Amber Bogisich Sr.','1989-07-23','Lamont.Bergstrom@gmail.com','643427347','i','INACTIVE'),(26,'https://picsum.photos/seed/qYZEZ/640/480','Muriel Powlowski III','2002-07-19','Cathryn1@hotmail.com','625261074','A','INACTIVE'),(27,'https://picsum.photos/seed/ETcJ6nA/640/480','Hugh Schneider','1994-01-17','Anabel.Harvey@gmail.com','635186594','r','INACTIVE'),(28,'https://picsum.photos/seed/k3QEtGs/640/480','Alberto Kuphal','1989-12-30','Lenna48@hotmail.com','682367118','W','ACTIVE'),(29,'https://picsum.photos/seed/RvS4EusaB/640/480','Dr. Ben Predovic','1962-03-13','Trisha_Kertzmann@gmail.com','679397017','q','ACTIVE'),(30,'https://picsum.photos/seed/vF8SX8/640/480','Allen Murray','1985-11-07','Willie_Hansen21@hotmail.com','679994680','y','ACTIVE'),(31,'https://picsum.photos/seed/SfyS8u/640/480','Dr. Danielle Stroman','1973-10-30','Gabriel_Nikolaus96@yahoo.com','634534871','q','INACTIVE'),(32,'https://picsum.photos/seed/z3vItcSz/640/480','Tomas Hintz V','1966-03-16','Arlene_OConner39@hotmail.com','681156580','U','ACTIVE'),(33,'https://picsum.photos/seed/o0gWpA5r/640/480','test','1954-10-17','test@test.com','679743418','m','INACTIVE'),(34,'https://picsum.photos/seed/dXnjKas/640/480','Carrie Hyatt','2000-05-01','Eloise86@gmail.com','650841489','z','ACTIVE'),(35,'https://picsum.photos/seed/DS1Sizn/640/480','Michelle Reichert IV','1984-02-28','Stacey.Gleichner34@gmail.com','660059385','V','INACTIVE'),(36,'https://picsum.photos/seed/eXbr1z2hQ/640/480','Dr. Ellen O´Connell PhD','1979-11-06','Maryjane97@hotmail.com','671344389','J','ACTIVE'),(37,'https://picsum.photos/seed/RChPTZwVPb/640/480','Edgar Ferry','1959-05-07','Nathanael_OKon-Dach56@hotmail.com','695638901','p','ACTIVE'),(38,'https://picsum.photos/seed/7fzuhUa/640/480','Claire Heaney','1952-01-27','Minerva59@gmail.com','616096284','I','INACTIVE'),(39,'https://picsum.photos/seed/16mlJDhbLn/640/480','Harry Cole','1954-04-23','Adeline.Streich32@hotmail.com','675245532','T','INACTIVE'),(40,'https://picsum.photos/seed/GrxtdkHfnV/640/480','Dr. Joel Wolf','1950-07-22','Celine57@gmail.com','660299168','E','INACTIVE'),(41,'https://picsum.photos/seed/SxXbYufG9/640/480','Nadine Mosciski V','1999-02-10','Kiara.McGlynn73@gmail.com','635556546','i','INACTIVE'),(43,'photoprueba','name','2002-10-22','prueba@prueba.com','123456789','description of user','ACTIVE');
UNLOCK TABLES;

