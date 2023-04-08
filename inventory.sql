-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.7.33 - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for inventory
CREATE DATABASE IF NOT EXISTS `inventory` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `inventory`;

-- Dumping structure for table inventory.barang
CREATE TABLE IF NOT EXISTS `barang` (
  `id_barang` varchar(50) NOT NULL,
  `nama_barang` varchar(100) DEFAULT NULL,
  `stok` int(11) DEFAULT NULL,
  `keterangan` text,
  `id_jenis` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_barang`),
  KEY `id_jenis` (`id_jenis`),
  CONSTRAINT `barang_ibfk_1` FOREIGN KEY (`id_jenis`) REFERENCES `jenis_barang` (`id_jenis`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table inventory.barang: ~17 rows (approximately)
DELETE FROM `barang`;
/*!40000 ALTER TABLE `barang` DISABLE KEYS */;
INSERT INTO `barang` (`id_barang`, `nama_barang`, `stok`, `keterangan`, `id_jenis`) VALUES
	('1111', 'Kerudung Segitiga', 100, 'tersedia warna pink,abu abu,broken white,hijau,baby blue,merah', 7),
	('1112', 'Bergo Hamdalah', 80, 'tersedia warna dark blue,soft blue,black,snow black,snow blue,white', 7),
	('1113', 'Paris Premium Segi Empat', 60, 'tersedia warna pink,abu abu,broken white,hijau,baby blue,merah,cream,coklat', 7),
	('1114', 'Bella Square', 40, 'tersedia warna pink,abu abu,broken white,hijau,baby blue,merah', 7),
	('1115', 'Hijab Khimar Jumbo', 67, 'tersedia warna hitam,merah,biru,coklat,cream,pink', 7),
	('1233', 'Baju Tidur Ghan', 60, 'tersedia warna merah,hijau,kuning', 11),
	('1234', 'Baju Tidur Marsha', 186, 'Warna Pink', 11),
	('1235', 'Sweater Domba', 70, '31', 15),
	('2167', 'Blouse balon', 39, 'warna hijau', 2),
	('2314', 'Baju Tidur Upin Ipin', 12, 'warna kuning dan biru', 11),
	('2333', 'Kaos Jajem Shirt', 110, 'warna hitam dan putih', 12),
	('2334', 'Shirt Aniversary Jajem', 51, 'Warna Hitam', 12),
	('2335', 'Jaket Keren ', 63, 'tersedia warna pink,abu abu,broken white,hijau,baby blue,merah', 16),
	('2345', 'Kostum Kebaya', 137, 'warna merah', 6),
	('2444', 'Klambi Kandel', 70, 'warna hitam dan putih', 13),
	('4536', 'Kemeja Wanita', 100, 'tersedia warna pink,abu abu,broken white,hijau,baby blue,merah', 3),
	('7676', 'Celana Reggae', 116, 'tersedia warna hijau, kuning, merah', 10),
	('9843', 'Cullote Highwaist', 60, 'warna hitam dan putih', 4),
	('9865', 'Celana Panjang Denim', 38, 'tersedia warna dark blue,soft blue,black,snow black,snow blue,white', 1),
	('B1', 'Pulpen', 15, 'masih', 1);
/*!40000 ALTER TABLE `barang` ENABLE KEYS */;

-- Dumping structure for table inventory.jenis_barang
CREATE TABLE IF NOT EXISTS `jenis_barang` (
  `id_jenis` int(11) NOT NULL AUTO_INCREMENT,
  `jenis_barang` varchar(100) DEFAULT NULL,
  `bahan` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_jenis`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

-- Dumping data for table inventory.jenis_barang: ~15 rows (approximately)
DELETE FROM `jenis_barang`;
/*!40000 ALTER TABLE `jenis_barang` DISABLE KEYS */;
INSERT INTO `jenis_barang` (`id_jenis`, `jenis_barang`, `bahan`) VALUES
	(1, 'Celana Panjang', 'Denim'),
	(2, 'Baju', 'katun'),
	(3, 'Kemeja', 'Linen'),
	(4, 'Celana Culotte', 'Drill'),
	(5, 'Blouse', 'Viscouse'),
	(6, 'Kebaya', 'Tile'),
	(7, 'Kerudung', 'Katun'),
	(8, 'Rok Panjang', 'Denim'),
	(9, 'Kebaya', 'Brokat'),
	(10, 'Celana Pendek', 'Plisket'),
	(11, 'Baju Tidur', 'Sifon'),
	(12, 'Kaos Lengan Pendek', 'Cotton Combed 24S'),
	(13, 'Kaos Lengan Panjang', 'Cotton Combed 20S'),
	(14, 'Dress', 'Satin'),
	(15, 'Sweater Rajut', 'Wool'),
	(16, 'Jaket', 'Denim');
/*!40000 ALTER TABLE `jenis_barang` ENABLE KEYS */;

-- Dumping structure for table inventory.jenis_karyawan
CREATE TABLE IF NOT EXISTS `jenis_karyawan` (
  `id_jenis_karyawan` int(11) NOT NULL AUTO_INCREMENT,
  `jeniskaryawan` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_jenis_karyawan`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

-- Dumping data for table inventory.jenis_karyawan: ~6 rows (approximately)
DELETE FROM `jenis_karyawan`;
/*!40000 ALTER TABLE `jenis_karyawan` DISABLE KEYS */;
INSERT INTO `jenis_karyawan` (`id_jenis_karyawan`, `jeniskaryawan`) VALUES
	(2, 'Magang'),
	(3, 'Tetap'),
	(4, 'Kasir 2'),
	(5, 'Kasir 1'),
	(6, 'Staff Gudang'),
	(7, 'Admin');
/*!40000 ALTER TABLE `jenis_karyawan` ENABLE KEYS */;

-- Dumping structure for table inventory.karyawan
CREATE TABLE IF NOT EXISTS `karyawan` (
  `id_karyawan` varchar(100) NOT NULL,
  `nama_karyawan` varchar(100) DEFAULT NULL,
  `id_jenis_karyawan` int(11) DEFAULT NULL,
  `alamat` varchar(100) DEFAULT NULL,
  `no_telp` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_karyawan`),
  KEY `id_jenis_karyawan` (`id_jenis_karyawan`),
  CONSTRAINT `karyawan_ibfk_1` FOREIGN KEY (`id_jenis_karyawan`) REFERENCES `jenis_karyawan` (`id_jenis_karyawan`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table inventory.karyawan: ~5 rows (approximately)
DELETE FROM `karyawan`;
/*!40000 ALTER TABLE `karyawan` DISABLE KEYS */;
INSERT INTO `karyawan` (`id_karyawan`, `nama_karyawan`, `id_jenis_karyawan`, `alamat`, `no_telp`, `email`) VALUES
	('001', 'Amalia', 5, 'Salem Brebes', '08532368787', 'amalia@gmail.com'),
	('002', 'Budi', 6, 'Purwosari', '085836363789', 'budi@gmail.com'),
	('003', 'Siti', 4, 'Purwanegara', '085676768831', 'sisiti@gmail.com'),
	('004', 'Andi', 7, 'Grendeng', '08908988098', 'andilaw@gmail.com'),
	('K1', 'AGIL', 2, 'pbg\r\n', '089665881651', 'agil@agil.com');
/*!40000 ALTER TABLE `karyawan` ENABLE KEYS */;

-- Dumping structure for table inventory.pembukuan
CREATE TABLE IF NOT EXISTS `pembukuan` (
  `id_pembukuan` int(11) NOT NULL AUTO_INCREMENT,
  `id_barang` varchar(50) DEFAULT NULL,
  `barang_terjual` int(11) DEFAULT NULL,
  `harga_jual` int(11) DEFAULT NULL,
  `harga_beli` int(11) DEFAULT NULL,
  `laba` int(11) DEFAULT NULL,
  `tanggal_update` date DEFAULT NULL,
  PRIMARY KEY (`id_pembukuan`),
  KEY `FK_pembukuan_barang` (`id_barang`),
  CONSTRAINT `FK_pembukuan_barang` FOREIGN KEY (`id_barang`) REFERENCES `barang` (`id_barang`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

-- Dumping data for table inventory.pembukuan: ~12 rows (approximately)
DELETE FROM `pembukuan`;
/*!40000 ALTER TABLE `pembukuan` DISABLE KEYS */;
INSERT INTO `pembukuan` (`id_pembukuan`, `id_barang`, `barang_terjual`, `harga_jual`, `harga_beli`, `laba`, `tanggal_update`) VALUES
	(1, 'B1', 5, 5000, 2000, 3000, '2022-12-02'),
	(2, '1112', 10, 23000, 15000, 8000, '2022-12-11'),
	(3, '1113', 20, 28000, 20000, 8000, '2022-12-11'),
	(4, '1114', 30, 15000, 10000, 5000, '2022-12-11'),
	(5, '1115', 13, 25000, 18000, 7000, '2022-12-11'),
	(6, '1234', 14, 120000, 110000, 10000, '2022-12-08'),
	(7, '2167', 30, 75000, 60000, 15000, '2022-12-08'),
	(8, '9843', 56, 130000, 110000, 20000, '2022-12-08'),
	(10, '9865', 14, 170000, 135000, 35000, '2022-12-08'),
	(11, '2335', 7, 150000, 123000, 27000, '2022-12-08'),
	(12, '2314', 48, 76000, 56000, 20000, '2022-12-08'),
	(13, '7676', 14, 35000, 15000, 20000, '2022-12-08'),
	(14, '2334', 89, 80000, 70000, 10000, '2022-12-08'),
	(15, '4536', 76, 89000, 76000, 13000, '2022-12-08');
/*!40000 ALTER TABLE `pembukuan` ENABLE KEYS */;

-- Dumping structure for table inventory.penerimaan
CREATE TABLE IF NOT EXISTS `penerimaan` (
  `id_terima` int(11) NOT NULL AUTO_INCREMENT,
  `id_supplier` varchar(100) DEFAULT NULL,
  `tgl_terima` date DEFAULT NULL,
  `id_barang` varchar(50) DEFAULT NULL,
  `jumlah_terima` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_terima`),
  KEY `id_supplier` (`id_supplier`),
  KEY `id_barang` (`id_barang`),
  CONSTRAINT `penerimaan_ibfk_1` FOREIGN KEY (`id_supplier`) REFERENCES `supplier` (`id_supplier`),
  CONSTRAINT `penerimaan_ibfk_2` FOREIGN KEY (`id_barang`) REFERENCES `barang` (`id_barang`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

-- Dumping data for table inventory.penerimaan: ~18 rows (approximately)
DELETE FROM `penerimaan`;
/*!40000 ALTER TABLE `penerimaan` DISABLE KEYS */;
INSERT INTO `penerimaan` (`id_terima`, `id_supplier`, `tgl_terima`, `id_barang`, `jumlah_terima`) VALUES
	(1, 'S1', '2022-12-02', 'B1', 11),
	(3, '185', '2022-12-07', '1234', 100),
	(4, '185', '2022-12-07', '1233', 30),
	(5, '185', '2022-12-07', '1235', 40),
	(6, '185', '2022-12-07', '2167', 35),
	(7, '185', '2022-12-07', '2314', 30),
	(8, '185', '2022-12-07', '9843', 60),
	(9, '528', '2022-12-05', '7676', 65),
	(10, '528', '2022-12-03', '9865', 35),
	(11, '528', '2022-12-05', '2345', 70),
	(12, '528', '2022-12-05', '2444', 40),
	(13, 'S1', '2022-12-05', '2333', 60),
	(14, 'S1', '2022-12-02', '2334', 100),
	(15, 'S1', '2022-12-05', '4536', 90),
	(16, 'S1', '2022-12-05', '2335', 40),
	(17, '112', '2022-12-01', '1111', 50),
	(18, '112', '2022-12-01', '1112', 50),
	(19, '112', '2022-12-01', '1113', 50),
	(20, '112', '2022-12-01', '1114', 50),
	(21, '112', '2022-12-01', '1115', 50);
/*!40000 ALTER TABLE `penerimaan` ENABLE KEYS */;

-- Dumping structure for table inventory.supplier
CREATE TABLE IF NOT EXISTS `supplier` (
  `id_supplier` varchar(100) NOT NULL,
  `nama_supplier` varchar(100) DEFAULT NULL,
  `alamat` varchar(100) DEFAULT NULL,
  `no_telp` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_supplier`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table inventory.supplier: ~3 rows (approximately)
DELETE FROM `supplier`;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` (`id_supplier`, `nama_supplier`, `alamat`, `no_telp`, `email`) VALUES
	('112', 'Adia', 'Meikarta', '087898978789', 'adia@gmail.com'),
	('185', 'Aida', 'Purbalingga', '08538238478', 'aai@gmail.com'),
	('528', 'Syifa', 'Cilongok', '087878799878', 'oii@gmail.com'),
	('S1', 'Agil', 'pbg', '08966588161', 'a@gmail.com');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;

-- Dumping structure for table inventory.users
CREATE TABLE IF NOT EXISTS `users` (
  `id_users` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `token` varchar(255) DEFAULT NULL,
  `level` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_users`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- Dumping data for table inventory.users: ~1 rows (approximately)
DELETE FROM `users`;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`id_users`, `name`, `email`, `password`, `token`, `level`) VALUES
	(2, 'admin', 'admin@gmail.com', '$2b$12$Yh8dZKXan6gOE7mV4n7H/OxHASMhsn34ZkuaWm6fpoBWHGDIic/Nu', NULL, 'Admin'),
	(3, 'Agil', 'kiravelnote@gmail.com', '$2b$12$hrFY937XRuDc5.edYZjn7u4SOcMJ4CH59nPvMPw5Bde3kWQu5n3tu', 'e29e2639-b0a7-41d9-8780-a164cceb1b32', 'Petugas'),
	(4, 'yuhu', 'yuhu@gmail.com', '$2b$12$ohiklzyMkgNyEBZpGR6BgebfVXTD5pfGGvUtsjpZfIvrimVTlvFei', NULL, 'Admin');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

-- Dumping structure for trigger inventory.pembukuan_after_insert
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `pembukuan_after_insert` AFTER INSERT ON `pembukuan` FOR EACH ROW BEGIN
	UPDATE barang SET stok = stok - NEW.barang_terjual
	WHERE id_barang = NEW.id_barang;
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

-- Dumping structure for trigger inventory.pembukuan_after_update
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `pembukuan_after_update` AFTER UPDATE ON `pembukuan` FOR EACH ROW BEGIN
	UPDATE barang SET stok = (stok + old.barang_terjual) - NEW.barang_terjual
	WHERE id_barang = NEW.id_barang;
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

-- Dumping structure for trigger inventory.penerimaan_after_insert
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `penerimaan_after_insert` AFTER INSERT ON `penerimaan` FOR EACH ROW BEGIN
	UPDATE barang SET stok = stok + NEW.jumlah_terima
	WHERE id_barang = NEW.id_barang;
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

-- Dumping structure for trigger inventory.penerimaan_after_update
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `penerimaan_after_update` AFTER UPDATE ON `penerimaan` FOR EACH ROW BEGIN
	UPDATE barang SET stok = (stok - OLD.jumlah_terima) + NEW.jumlah_terima
	WHERE id_barang = NEW.id_barang;
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
