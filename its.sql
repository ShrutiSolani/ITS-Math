-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 01, 2021 at 01:26 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.3.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `its`
--

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

CREATE TABLE `question` (
  `id` int(20) NOT NULL,
  `qid` varchar(20) NOT NULL,
  `chapter` varchar(20) NOT NULL,
  `level` varchar(20) NOT NULL,
  `topic` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `question`
--

INSERT INTO `question` (`id`, `qid`, `chapter`, `level`, `topic`) VALUES
(1, 'FE1', 'Fraction', 'Easy', 'simplest-form'),
(2, 'FE2', 'Fraction', 'Easy', 'division'),
(3, 'FE3', 'Fraction', 'Easy', 'add-fractions'),
(4, 'FE4', 'Fraction', 'Easy', 'multiply-with-whole'),
(5, 'FI1', 'Fraction', 'Intermediate', 'mixed-fraction\r\n'),
(6, 'FI2', 'Fraction', 'Intermediate', '\r\ncompare\r\n'),
(7, 'FI3', 'Fraction', 'Intermediate', '\r\nnormal-form\r\n'),
(8, 'FI4', 'Fraction', 'Intermediate', '\r\ndivide-with-whole\r\n'),
(9, 'FI5', 'Fraction', 'Intermediate', '\r\nunlike-add'),
(10, 'AE1', 'Algebra', 'Easy', 'coefficient'),
(11, 'AE2', 'Algebra', 'Easy', 'value-of-expression'),
(12, 'AE3', 'Algebra', 'Easy', 'monomial'),
(13, 'AE4', 'Algebra', 'Easy', 'like-unlike'),
(14, 'AI1', 'Algebra', 'Intermediate', 'algebra-add'),
(15, 'AI2', 'Algebra', 'Intermediate', 'vertical-sub');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(10000) NOT NULL,
  `dob` date NOT NULL,
  `grade` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `first_name`, `last_name`, `email`, `password`, `dob`, `grade`) VALUES
(8, 'admin', 'malhotra', 'admin@gmail.com', 'pbkdf2:sha256:260000$jkAtIT4usgqFXU6n$9462947114530579098196cfcdf1dd4053a88696befec4b28201996827ce6dba', '2016-03-28', 5);

-- --------------------------------------------------------

--
-- Table structure for table `student_score`
--

CREATE TABLE `student_score` (
  `id` int(20) NOT NULL,
  `sid` int(20) NOT NULL,
  `qid` int(20) NOT NULL,
  `score` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student_score`
--

INSERT INTO `student_score` (`id`, `sid`, `qid`, `score`) VALUES
(1, 8, 1, 100);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `question`
--
ALTER TABLE `question`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `student_score`
--
ALTER TABLE `student_score`
  ADD PRIMARY KEY (`id`),
  ADD KEY `qid` (`qid`),
  ADD KEY `sid` (`sid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `question`
--
ALTER TABLE `question`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `student_score`
--
ALTER TABLE `student_score`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `student_score`
--
ALTER TABLE `student_score`
  ADD CONSTRAINT `constraint` FOREIGN KEY (`sid`) REFERENCES `student` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
