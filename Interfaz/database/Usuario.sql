-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Generation Time: May 22, 2024 at 04:32 PM
-- Server version: 8.4.0
-- PHP Version: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `chatbot`
--

-- --------------------------------------------------------

--
-- Table structure for table `Usuario`
--

CREATE TABLE `Usuario` (
  `IdUsuario` int NOT NULL,
  `Nombre` varchar(30) NOT NULL,
  `Apellidos` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Correo` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `NombreEmpresa` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Cargo` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Password` char(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `RepeatPassword` char(102) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Usuario`
--

INSERT INTO `Usuario` (`IdUsuario`, `Nombre`, `Apellidos`, `Correo`, `NombreEmpresa`, `Cargo`, `Password`, `RepeatPassword`) VALUES
(1, 'Josue', 'Chambilla Zuñiga', 'jc2020067575@virtual.upt.pe', 'UPT', 'Supervisor', 'scrypt:32768:8:1$iYNKwLNmIwhXxcHT$9ced5a7115eb934474109db163ed4cd25c235ec861aa0d5f1f06c95d8021db5e502bb7d717bd92fece4bb947f51572f11d7e003b9d2a956662ce211c493fb135', '123456');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Usuario`
--
ALTER TABLE `Usuario`
  ADD PRIMARY KEY (`IdUsuario`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Usuario`
--
ALTER TABLE `Usuario`
  MODIFY `IdUsuario` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
