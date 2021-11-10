-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: sql6.freesqldatabase.com
-- Generation Time: Nov 10, 2021 at 10:12 AM
-- Server version: 5.5.62-0ubuntu0.14.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sql6449635`
--

-- --------------------------------------------------------

--
-- Table structure for table `log`
--

CREATE TABLE `log` (
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `entry` longtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `log`
--

INSERT INTO `log` (`timestamp`, `entry`) VALUES
('2021-11-08 13:20:19', '{\"userid\": 8, \"message\": \"Logged In\"}'),
('2021-11-08 13:20:21', '{\"userid\": 8, \"message\": \"Home Page\"}'),
('2021-11-08 13:20:32', '{\"userid\": 8, \"qid\": \"FI2\", \"qcount\": 1}'),
('2021-11-08 13:20:50', '{\"userid\": 8, \"qid\": \"FI2\", \"qcount\": \"1\", \"startTime\": \"2021-11-08 13:45:28.762883\", \"endTime\": \"2021-11-08 13:46:54.162730\", \"levelofdifficulty\": \"Intermediate\", \"chapter\": \"Fraction\", \"hintCount\": \"0\", \"h1time\": 0, \"h2time\": 0, \"diffh1\": 0, \"diffh2\": 0, \"wrongCount\": \"1\", \"wronghintcount\": \"0\", \"score\": \"25\"}'),
('2021-11-08 13:20:52', '{\"userid\": 8, \"qid\": \"FI2\", \"qcount\": 2}'),
('2021-11-08 13:21:12', '{\"userid\": 8, \"qid\": \"FI2\", \"qcount\": \"2\", \"startTime\": \"2021-11-08 13:45:28.762883\", \"endTime\": \"2021-11-08 13:47:16.504870\", \"levelofdifficulty\": \"Intermediate\", \"chapter\": \"Fraction\", \"hintCount\": \"0\", \"h1time\": 0, \"h2time\": 0, \"diffh1\": 0, \"diffh2\": 0, \"wrongCount\": \"0\", \"wronghintcount\": \"0\", \"score\": \"25\"}'),
('2021-11-08 13:21:15', '{\"userid\": 8, \"qid\": \"FI2\", \"qcount\": 3}'),
('2021-11-08 13:21:38', '{\"userid\": 8, \"qid\": \"FI2\", \"qcount\": \"3\", \"startTime\": \"2021-11-08 13:45:28.748743\", \"endTime\": \"2021-11-08 13:47:42.154956\", \"levelofdifficulty\": \"Intermediate\", \"chapter\": \"Fraction\", \"hintCount\": \"1\", \"h1time\": \"2021-11-08 13:47:22.124000\", \"h2time\": 0, \"diffh1\": \"0:00:20.030956\", \"diffh2\": 0, \"wrongCount\": \"1\", \"wronghintcount\": \"0\", \"score\": \"20\"}'),
('2021-11-08 13:21:40', '{\"userid\": 8, \"qid\": \"FI2\", \"qcount\": 4}'),
('2021-11-08 13:22:04', '{\"userid\": 8, \"qid\": \"FI2\", \"qcount\": \"4\", \"startTime\": \"2021-11-08 13:45:28.762883\", \"endTime\": \"2021-11-08 13:48:08.175420\", \"levelofdifficulty\": \"Intermediate\", \"chapter\": \"Fraction\", \"hintCount\": \"0\", \"h1time\": 0, \"h2time\": 0, \"diffh1\": 0, \"diffh2\": 0, \"wrongCount\": \"1\", \"wronghintcount\": \"0\", \"score\": \"25\"}'),
('2021-11-08 13:22:06', '{\"userid\": 8, \"qid\": \"FI2\", \"q1\": \"25\", \"q2\": \"25\", \"q3\": \"20\", \"q4\": \"25\", \"total\": 95}'),
('2021-11-08 13:22:09', '{\"userid\": 8, \"message\": \"Home Page\"}'),
('2021-11-08 13:50:22', '{\"userid\": 9, \"message\": \"Logged In\"}'),
('2021-11-08 13:50:24', '{\"userid\": 9, \"message\": \"Home Page\"}'),
('2021-11-08 13:50:31', '{\"userid\": 9, \"message\": \"Profile Page\"}'),
('2021-11-08 13:51:17', '{\"userid\": 9, \"message\": \"Profile Page\"}'),
('2021-11-08 13:52:17', '{\"userid\": 9, \"message\": \"Home Page\"}'),
('2021-11-08 13:52:26', '{\"userid\": 9, \"message\": \"Logged out\"}'),
('2021-11-09 13:19:21', '{\"userid\": 8, \"message\": \"Logged In\"}'),
('2021-11-09 13:19:23', '{\"userid\": 8, \"message\": \"Logged In\"}'),
('2021-11-09 13:19:25', '{\"userid\": 8, \"message\": \"Home Page\"}'),
('2021-11-09 13:19:26', '{\"userid\": 8, \"message\": \"Logged In\"}'),
('2021-11-09 13:19:28', '{\"userid\": 8, \"message\": \"Home Page\"}'),
('2021-11-09 13:21:14', '{\"userid\": 8, \"message\": \"Logged In\"}'),
('2021-11-09 13:21:15', '{\"userid\": 8, \"message\": \"Home Page\"}'),
('2021-11-09 13:21:23', '{\"userid\": 8, \"message\": \"Home Page\"}'),
('2021-11-09 13:21:25', '{\"userid\": 8, \"message\": \"Profile Page\"}'),
('2021-11-09 13:21:35', '{\"userid\": 8, \"message\": \"Logged out\"}'),
('2021-11-09 13:41:45', '{\"userid\": 8, \"message\": \"Logged In\"}'),
('2021-11-09 13:41:46', '{\"userid\": 8, \"message\": \"Home Page\"}'),
('2021-11-09 13:41:49', '{\"userid\": 8, \"message\": \"Logged out\"}'),
('2021-11-10 04:43:37', '{\"userid\": 8, \"message\": \"Logged In\"}'),
('2021-11-10 04:43:38', '{\"userid\": 8, \"message\": \"Home Page\"}');

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
  `grade` int(20) NOT NULL,
  `school` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `first_name`, `last_name`, `email`, `password`, `dob`, `grade`, `school`) VALUES
(8, 'admin', 'malhotra', 'admin@gmail.com', 'pbkdf2:sha256:260000$jkAtIT4usgqFXU6n$9462947114530579098196cfcdf1dd4053a88696befec4b28201996827ce6dba', '2016-03-28', 5, 'D.J Sanghvi'),
(9, 'Raj', 'Shah', 'rshah@gmail.com', 'pbkdf2:sha256:260000$Dmb3UfEqHGkezLwu$90d9f23a6ad0a39efaf50dab64ceac8ce9f8e150ec67b70ecb3a2d4f0a129027', '2006-02-02', 7, 'St. Xavier High School');

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
(1, 8, 1, 100),
(2, 8, 1, 100),
(3, 8, 10, 100),
(4, 8, 12, 100),
(5, 8, 14, 85),
(6, 8, 7, 90),
(7, 8, 1, 100),
(8, 8, 6, 90),
(9, 8, 6, 95);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `log`
--
ALTER TABLE `log`
  ADD UNIQUE KEY `timestamp` (`timestamp`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `student_score`
--
ALTER TABLE `student_score`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
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
