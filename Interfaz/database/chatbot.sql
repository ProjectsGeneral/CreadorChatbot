-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: db
-- Tiempo de generación: 25-06-2024 a las 17:19:38
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
(1, 8, 'Josue2', '1234'),
(2, 8, 'testeo', 'saludo de testeo'),
(3, 8, '2do testeo', 'testeo2'),
(4, 8, '1', '1'),
(5, 8, 'abc', 'dfg');

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
(1, 1, 'telefono', 'test 982531296'),
(2, 2, 'telefono', 'test 982531296'),
(3, 2, 'direccion', 'av industrial'),
(4, 2, 'ciudad', 'Tacna - Tacna'),
(5, 3, 'palabra clave 1', 'contenido 1'),
(6, 3, 'palabra clave 2', 'contenido 2'),
(7, 4, '1', '1'),
(8, 4, '2', '2'),
(9, 5, '123', '123'),
(10, 5, '123', '123'),
(11, 5, '123', '123');

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
  MODIFY `IdBot` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `PClaveBot`
--
ALTER TABLE `PClaveBot`
  MODIFY `IdPClave` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

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
