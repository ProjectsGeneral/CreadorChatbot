-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: db
-- Tiempo de generación: 27-06-2024 a las 23:30:57
-- Versión del servidor: 8.4.0
-- Versión de PHP: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `chatbot`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Bots`
--

CREATE TABLE `Bots` (
  `IdBot` int NOT NULL,
  `IdUsuario` int NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Saludo` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `Bots`
--

INSERT INTO `Bots` (`IdBot`, `IdUsuario`, `Nombre`, `Saludo`) VALUES
(11, 7, 'dsadas', 'dsadsa'),
(12, 7, 'fdsfds', 'fdsfds');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `PClaveBot`
--

CREATE TABLE `PClaveBot` (
  `IdPClave` int NOT NULL,
  `IdBot` int NOT NULL,
  `Clave` varchar(50) NOT NULL,
  `Contenido` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `PClaveBot`
--

INSERT INTO `PClaveBot` (`IdPClave`, `IdBot`, `Clave`, `Contenido`) VALUES
(22, 11, 'dsadsa', 'dsdsa'),
(23, 11, 'dsadsa', 'dsad'),
(24, 12, 'fdsfds', 'fdsfds'),
(25, 12, 'fdsfds', 'fdsfds');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Usuario`
--

CREATE TABLE `Usuario` (
  `IdUsuario` int NOT NULL,
  `Nombre` varchar(30) NOT NULL,
  `Apellidos` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Correo` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `NombreEmpresa` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Cargo` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Password` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `Usuario`
--

INSERT INTO `Usuario` (`IdUsuario`, `Nombre`, `Apellidos`, `Correo`, `NombreEmpresa`, `Cargo`, `Password`) VALUES
(7, '1', '2', '1@hotmail.com', '1', 'Analista', '$2b$12$VT1od2PbNS8dTe0bJyZoF.KqQUgmqaePjsPHdb.nvOowOj2ERjPzO'),
(8, 'Josue', 'Chambilla Zuñiga ', 'josue.200297@hotmail.com', 'Universidad Privada de Tacna', 'Analista', '$2b$12$pdBBjDHaV/Q5kFbfiuPMIu6Fb2ByFSUUjiumdUuEK.o4tZmaJqY9m');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Bots`
--
ALTER TABLE `Bots`
  ADD PRIMARY KEY (`IdBot`),
  ADD KEY `IdUsuario` (`IdUsuario`);

--
-- Indices de la tabla `PClaveBot`
--
ALTER TABLE `PClaveBot`
  ADD PRIMARY KEY (`IdPClave`),
  ADD KEY `IdBot` (`IdBot`);

--
-- Indices de la tabla `Usuario`
--
ALTER TABLE `Usuario`
  ADD PRIMARY KEY (`IdUsuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Bots`
--
ALTER TABLE `Bots`
  MODIFY `IdBot` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `PClaveBot`
--
ALTER TABLE `PClaveBot`
  MODIFY `IdPClave` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `Usuario`
--
ALTER TABLE `Usuario`
  MODIFY `IdUsuario` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `Bots`
--
ALTER TABLE `Bots`
  ADD CONSTRAINT `Bots_ibfk_1` FOREIGN KEY (`IdUsuario`) REFERENCES `Usuario` (`IdUsuario`);

--
-- Filtros para la tabla `PClaveBot`
--
ALTER TABLE `PClaveBot`
  ADD CONSTRAINT `PClaveBot_ibfk_1` FOREIGN KEY (`IdBot`) REFERENCES `Bots` (`IdBot`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
