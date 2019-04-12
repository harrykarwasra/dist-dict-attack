-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 13, 2019 at 12:39 AM
-- Server version: 10.1.32-MariaDB
-- PHP Version: 7.2.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pass_dict`
--

-- --------------------------------------------------------

--
-- Table structure for table `passwords`
--

CREATE TABLE `passwords` (
  `id` int(11) NOT NULL,
  `pass` varchar(64) NOT NULL,
  `used` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `passwords`
--

INSERT INTO `passwords` (`id`, `pass`, `used`) VALUES
(1, '123456', 0),
(2, 'password', 0),
(3, '12345678', 0),
(4, 'crypto', 0),
(5, 'qwerty', 0),
(6, '12345', 0),
(7, '123456789', 0),
(8, 'letmein', 0),
(9, '1234567', 0),
(10, 'football', 0),
(11, 'iloveyou', 0),
(12, 'admin', 0),
(13, 'welcome', 0),
(14, 'monkey', 0),
(15, 'login', 0),
(16, 'abc123', 0),
(17, 'starwars', 0),
(18, '123123', 0),
(19, 'dragon', 0),
(20, 'passw0rd', 0),
(21, 'master', 0),
(22, 'hello', 0),
(23, 'freedom', 0),
(24, 'whatever', 0),
(25, 'qazwsx', 0),
(26, 'trustno1', 0),
(27, '654321', 0),
(28, 'jordan23', 0),
(29, 'harley', 0),
(30, 'password01', 0),
(31, '1234', 0),
(32, 'robert', 0),
(33, 'matthew', 0),
(34, 'jordan', 0),
(35, 'asshole', 0),
(36, 'daniel', 0),
(37, 'andrew', 0),
(38, 'lakers', 0),
(39, 'andrea', 0),
(40, 'buster', 0),
(41, 'johsua', 0),
(42, '1qaz2wsx', 0),
(43, '12341234', 0),
(44, 'ferrari', 0),
(45, 'cheese', 0),
(46, 'computer', 0),
(47, 'corvette', 0),
(48, 'blahblah', 0),
(49, 'george', 0),
(50, 'mercedes', 0),
(51, '121212', 0),
(52, 'maverick', 0),
(53, 'fuckyou', 0),
(54, 'nicole', 0),
(55, 'hunter', 0),
(56, 'sunshine', 0),
(57, 'tigger', 0),
(58, '1989', 0),
(59, 'merlin', 0),
(60, 'ranger', 0),
(61, 'solo', 0),
(62, 'banana', 0),
(63, 'chelsea', 0),
(64, 'summer', 0),
(65, '1990', 0),
(66, '1991', 0),
(67, 'phoenix', 0),
(68, 'amanda', 0),
(69, 'cookie', 0),
(70, 'ashley', 0),
(71, 'bandit', 0),
(72, 'killer', 0),
(73, 'aaaaa', 0),
(74, 'pepper', 0),
(75, 'jessica', 0),
(76, 'zaq1zaq1', 0),
(77, 'jennifer', 0),
(78, 'test', 0),
(79, 'hockey', 0),
(80, 'dallas', 0),
(81, 'passwor', 0),
(82, 'michelle', 0),
(83, 'admin123', 0),
(84, 'pussy', 0),
(85, 'pass', 0),
(86, 'asdf', 0),
(87, 'william', 0),
(88, 'soccer', 0),
(89, 'london', 0),
(90, '1q2w3e', 0),
(91, '1992', 0),
(92, 'biteme', 0),
(93, 'maggie', 0),
(94, 'querty', 0),
(95, 'rangers', 0),
(96, 'charlie', 0),
(97, 'martin', 0),
(98, 'ginger', 0),
(99, 'golfer', 0),
(100, 'yankees', 0),
(101, 'thunder', 0);

-- --------------------------------------------------------

--
-- Table structure for table `sessions`
--

CREATE TABLE `sessions` (
  `id` varchar(64) NOT NULL,
  `host` varchar(100) NOT NULL,
  `username` varchar(64) NOT NULL,
  `found` tinyint(1) NOT NULL DEFAULT '0',
  `password` varchar(128) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sessions`
--

INSERT INTO `sessions` (`id`, `host`, `username`, `found`, `password`) VALUES
('cc67847b', '10.12.2.93', 'crypto', 1, 'crypto');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `passwords`
--
ALTER TABLE `passwords`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sessions`
--
ALTER TABLE `sessions`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `passwords`
--
ALTER TABLE `passwords`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
