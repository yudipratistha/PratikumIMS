/*
SQLyog Ultimate v12.4.3 (64 bit)
MySQL - 10.1.28-MariaDB : Database - db_bank
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_bank` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `db_bank`;

/*Table structure for table `tb_transaksi_toko` */

DROP TABLE IF EXISTS `tb_transaksi_toko`;

CREATE TABLE `tb_transaksi_toko` (
  `id_transaksi_toko` int(5) NOT NULL AUTO_INCREMENT,
  `nama_member` varchar(50) DEFAULT NULL,
  `no_transaksi` char(12) DEFAULT NULL,
  `status_transaksi` enum('pending','lunas','belum lunas') DEFAULT 'pending',
  `tanggal_transaksi` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_transaksi_toko`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `tb_transaksi_toko` */

insert  into `tb_transaksi_toko`(`id_transaksi_toko`,`nama_member`,`no_transaksi`,`status_transaksi`,`tanggal_transaksi`,`updated_at`) values 
(1,'Yudi Pratistha','213454222','pending','2018-05-07 11:46:29','2018-05-07 11:54:13'),
(5,'Satria','11156wwe5','pending','2018-05-07 13:08:43','2018-05-07 13:08:43'),
(6,'Evan','F23341322','pending','2018-05-07 13:16:37','2018-05-07 13:16:37'),
(9,'Arab','27131942','pending','2018-05-07 13:30:21','2018-05-07 13:30:21');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
