-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 14, 2019 at 12:27 PM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kbp_questions`
--
CREATE DATABASE IF NOT EXISTS `kbp_questions` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `kbp_questions`;

-- --------------------------------------------------------

--
-- Table structure for table `a`
--

CREATE TABLE `a` (
  `ID` int(11) DEFAULT NULL,
  `Question` varchar(200) DEFAULT NULL,
  `A` varchar(200) DEFAULT NULL,
  `B` varchar(200) DEFAULT NULL,
  `C` varchar(200) DEFAULT NULL,
  `D` varchar(200) DEFAULT NULL,
  `Correct` varchar(200) DEFAULT NULL,
  `Score` int(11) DEFAULT NULL,
  `Topic` varchar(120) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `a`
--

INSERT INTO `a` (`ID`, `Question`, `A`, `B`, `C`, `D`, `Correct`, `Score`, `Topic`) VALUES
(2, 'Ultraviolet light lies in the range of', '10 – 300 nm', '10 – 400 nm', '100 – 300 n', '100 – 400 nm', '10 – 400 nm', 10, 'Modern Physics'),
(3, 'Einstein got Nobel prize for', 'Photoelectric effect', 'Brownian Motion', 'Theory of relativity', 'Bose-Einstein statistics', 'Photoelectric effect', 10, 'Scientist'),
(4, 'Who is known to break the atom first?', 'Rutherford', 'Neils Bohr', 'J J Thomson', 'Schrodinger', 'J J Thomson', 10, 'Scientist'),
(5, 'In an elastic collision', 'Both kinetic energy and momentum are conserved', 'Only momentum is conserved', 'Only kinetic energy is conserved', 'None of them is conserved', 'Both kinetic energy and momentum are conserved', 25, 'Classical Mechanics'),
(6, 'If the Earth\'s mass increases by 100 %, the weight of an object on its surface would be', 'Halved', 'Quadrapled', 'Doubled', 'No change', 'Doubled', 25, 'General');

-- --------------------------------------------------------

--
-- Table structure for table `b`
--

CREATE TABLE `b` (
  `ID` int(11) DEFAULT NULL,
  `Question` varchar(200) DEFAULT NULL,
  `A` varchar(200) DEFAULT NULL,
  `B` varchar(200) DEFAULT NULL,
  `C` varchar(200) DEFAULT NULL,
  `D` varchar(200) DEFAULT NULL,
  `Correct` varchar(200) DEFAULT NULL,
  `Score` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `b`
--

INSERT INTO `b` (`ID`, `Question`, `A`, `B`, `C`, `D`, `Correct`, `Score`) VALUES
(2, 'Raman effect is based on __________ of light.', 'Polarisation', 'Scattering', 'Diffraction', 'Absorption', 'Scattering', 5),
(3, 'Atomic spectra is an example of', 'Continuous spectra', 'Band spectra', 'Line spectra', 'Both a and b', 'Line spectra', 10),
(4, 'Who had formulated theory of relativity prior to Einstein?', 'Archimedes', 'Kepler', 'Galileo', 'Aristotle', 'Galileo', 15),
(5, 'As per Newtons law of gravitation, the gravitational force between two bodies is proportional to ___ power of mass of each body and ___ power of the distance between them.', '1, -2', '1, 2', '2, 1', '2, -1', '1, -2', 10),
(6, 'In quantum mechanics, |psi| squared represents which of these?', 'negative density', 'eigen energy', 'probability density', 'wave-function', 'probability density', 25),
(7, 'Which concept did Einstein banish from physics?', 'Photoelectric effect', 'The ether', 'Black body radiation', 'Electromagnetic induction', 'The ether', 30),
(8, 'Which material has magnetic susceptibility equal to -1?', 'Metallic', 'Paramagnetic', 'Superconductor', 'Semiconductor', 'Superconductor', 35),
(9, 'Planck\'s constant has the dimensions of', 'Energy', 'Force', 'Angular Momentum', 'Momentumn', 'Angular Momentum', 40),
(10, 'The solution of the differential equation  (dy/dx)-y=0 is', 'y = x', 'y = e^x', 'y = -x', 'y = e^(-x)', 'y = e^x', 45),
(11, 'It is impossible for waves to diffract when', 'The slit width is less than the wavelength', 'The slit width is greater than the wavelength', 'The slit width is equal the wavelength', 'The waves are longitudinal regardless of the slit width', 'The slit width is less than the wavelength', 50);

-- --------------------------------------------------------

--
-- Table structure for table `c`
--

CREATE TABLE `c` (
  `ID` int(11) DEFAULT NULL,
  `Question` varchar(200) DEFAULT NULL,
  `A` varchar(200) DEFAULT NULL,
  `B` varchar(200) DEFAULT NULL,
  `C` varchar(200) DEFAULT NULL,
  `D` varchar(200) DEFAULT NULL,
  `Correct` varchar(200) DEFAULT NULL,
  `Score` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `c`
--

INSERT INTO `c` (`ID`, `Question`, `A`, `B`, `C`, `D`, `Correct`, `Score`) VALUES
(2, 'Who among these physicists have received the Nobel prize in Physics?', 'Homi Bhabha', 'G.N. Ramchandran', 'S.N. Bose', 'S. Chandrashekar', 'S. Chandrashekar', 5),
(3, 'With increasing quantum number the energy difference between adjacent levels in atoms', 'Decreases', 'Increases', 'Remain constant', 'Becomes zero', 'Decreases', 10),
(4, 'Einstein was awarded Nobel prize for his work in', 'Special theory of relativity', 'General theory of relativity', 'Photoelectric effect', 'Brownian motion', 'Photoelectric effect', 15),
(5, 'Which of these is an ideal engine?', 'Otto engine', 'Diesel engine', 'Steam engine', 'Carnot engine', 'Carnot engine', 20),
(6, 'How many Bravais lattices exist in three dimensions?', '7', '16', '10', '14', '14', 25),
(7, 'A monkey of mass 18 kg on earth is sent in a spaceship moving with a velocity 0.8c wrt earth. Its mass wrt an earth observer is', '18 kg', '30 kg', '10.8 kg', '6.48 kg', '30 kg', 30),
(8, 'The effective number of lattice points', '1', '4', '2', '8', '2', 35),
(9, 'The average binding energy per nucleon for a nucleus is', '8 KeV', '8 MeV', '80 KeV', '80 MeV', '8 MeV', 5),
(10, 'A boy travels 6 m towards east and turns north and travels distance 8 m. What is a distance of boy from starting point.', '14 m', '2 m', '48 m', '10 m', '10 m', 45),
(11, 'Which of the wave behavior is not possible for longitudinal waves?', 'Reflection', 'Polarisation', 'Diffraction', 'Refraction', 'Polarisation', 50);

-- --------------------------------------------------------

--
-- Table structure for table `d`
--

CREATE TABLE `d` (
  `ID` int(11) DEFAULT NULL,
  `Question` varchar(200) DEFAULT NULL,
  `A` varchar(200) DEFAULT NULL,
  `B` varchar(200) DEFAULT NULL,
  `C` varchar(200) DEFAULT NULL,
  `D` varchar(200) DEFAULT NULL,
  `Correct` varchar(200) DEFAULT NULL,
  `Score` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `d`
--

INSERT INTO `d` (`ID`, `Question`, `A`, `B`, `C`, `D`, `Correct`, `Score`) VALUES
(2, 'The concept of atom was put forward by', 'Kanada', 'Bhaskaracharya', 'Chanakya', 'Aryabhatta', 'Kanada', 5),
(3, 'An electron can never be found inside a nucleus this statement is according to', 'Bernoulli\'s equation', 'Bohr’s model of atom', 'Heisenberg uncertainty principle ', 'Both A and C', 'Heisenberg uncertainty principle', 10),
(4, 'When Einstein worked on his great papers in 1905, his profession was', 'Engineer', 'Doctor', 'Patent Officer', 'Professor', 'Patent Officer', 15),
(5, 'Young\'s modulus of elasticity Y is given by longitudinal stress/longitudinal strain within elastic limits. If the force exerted to stretch a steel bar is doubled, the value of Y', 'Increases', 'Cannot be determined', 'Decreases', 'Remains constant', 'Remains constant', 20),
(6, 'An electron is in 3P^2 state, then its principal quantum number n=......', '0', '1', '2', '3', '3', 25),
(7, 'A spaceship of rest length 100m is moving with a velocity  of 0.6c  w.r.t. earth. Its length wrt earth observer is', '100 m', '80 m', '125 m', '0', '80 m', 30),
(8, 'The effective number of lattice points in Face centred cubic (FCC) is', '1', '2', '4', '8', '4', 35),
(9, 'As the mass number A increases, which of the following quantities related to a nucleus do not change?', 'Density', 'Binding energy', 'Mass', 'Volume', 'Density', 40),
(10, 'An electron is moving along +ve X direction, a uniform magnetic field is applied along +ve Z axis. The force exerted on the electron is', '+ve X', '+ve Y', '–ve Y', '–ve Y', '–ve Y', 45),
(11, 'Which of these statements is not true about diffraction?', 'Sine of angle of diffraction is proportional to wavelength', 'There is a limit to number of diffraction orders', 'Diffraction orders have to be a whole number', 'Only electromagnetic waves can be diffracted', 'Only electromagnetic waves can be diffracted', 50);

-- --------------------------------------------------------

--
-- Table structure for table `e`
--

CREATE TABLE `e` (
  `ID` int(11) DEFAULT NULL,
  `Question` varchar(250) DEFAULT NULL,
  `A` varchar(250) DEFAULT NULL,
  `B` varchar(250) DEFAULT NULL,
  `C` varchar(250) DEFAULT NULL,
  `D` varchar(250) DEFAULT NULL,
  `Correct` varchar(250) DEFAULT NULL,
  `Score` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `e`
--

INSERT INTO `e` (`ID`, `Question`, `A`, `B`, `C`, `D`, `Correct`, `Score`) VALUES
(2, 'The discoverer of proton is', 'Thomson', 'Rutherford', 'Bohr', 'Chadwick', 'Rutherford', 5),
(3, 'The rest  mass of the photon is', 'Zero', 'Infinity', 'Depends on its wavelength', '1.6x10^(-24) kg', 'Zero', 10),
(4, 'Radiocarbon is produced in the atmosphere as a result of', 'collision between fast neutrons and nitrogen nuclei', 'Action of ultraviolet light from the sun on oxygen', 'Action of cosmic rays on carbon dioxide', 'Lightning discharge in atmosphere', 'collision between fast neutrons and nitrogen nuclei', 15),
(5, 'The viscosity of a fluid depends on its', 'Velocity of flow', 'Temperature', 'Density', 'Volume', 'Temperature', 20),
(6, 'Every elementary particle entity exhibits the properties of not only particles, but also waves is known as', 'The wave particle sigularity', 'The wave particle duality', 'The wave particle triality', 'The wave particle infinality', 'The wave particle duality', 25),
(7, 'Neel sleeps for 2 hours in  the train according to his friend Bill in the train which is moving with a speed 0.9c wrt platform. His other friend Sumit is on the platform  and according to him Neel slept for', '2 hours', '0.63 hours', '4.55 hours', '0.88 hours', '4.55 hours', 30),
(8, 'A Cooper Pair in superconductor is system of two electrons formed by electron -    ________ interaction', 'Photon', 'Phonon', 'Proton', 'Neutron', 'Phonon', 35),
(9, 'In which of the following nuclear process, does the element not change?', 'Alpha – decay', 'Beta decay', 'Gamma decay', 'Positron emmission', 'Gamma decay', 40),
(10, 'A footballer kicks a football from the penalty spot. A graph of force on the ball against time is drawn. The area under the force-time graph represents', 'Acceleration', 'Change in momentum', 'Change in Kinetic energy', 'Displacement', 'Change in momentum', 45),
(11, 'Which of the following changes would increase the resolution of telescope?', 'Using light of greater wavelength, Increase in aperturen', 'Using light of greater wavelength, decrease in aperture', 'Using light of lesser wavelength, increase in aperture', 'Using light of lesser wavelength, decrease in aperture', 'Using light of lesser wavelength, increase in aperture', 50);

-- --------------------------------------------------------

--
-- Table structure for table `f`
--

CREATE TABLE `f` (
  `ID` int(11) DEFAULT NULL,
  `Question` varchar(250) DEFAULT NULL,
  `A` varchar(250) DEFAULT NULL,
  `B` varchar(250) DEFAULT NULL,
  `C` varchar(250) DEFAULT NULL,
  `D` varchar(250) DEFAULT NULL,
  `Correct` varchar(250) DEFAULT NULL,
  `Score` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `f`
--

INSERT INTO `f` (`ID`, `Question`, `A`, `B`, `C`, `D`, `Correct`, `Score`) VALUES
(2, 'Nobel Prize in Physics for this year has been declared for the work on', 'Blue LED', 'CCD', 'Higg’s boson', 'Neutrino', 'Neutrino', 5),
(3, 'According to Bohr\'s atomic model the angular momentum of electron in nth orbit is equal to an integral multiple of', '2h/pi', 'h/(2*pi)', 'h/pi', 'pi/h', 'h/(2*pi)', 10),
(4, 'Which one of among the following determines the atomic number of a nucleus?', 'Number of nucleons', 'Number of protons', 'Number of neutrons', 'Number of ions', 'Number of protons', 15),
(5, 'If two events separated in space, occur simultaneously in  frame A ,', 'They are simultaneous in all frames', 'They are simultaneous in all inertial frames', 'They are simultaneous in all frames which are at rest w.r.t.  A', 'They are simultaneous in any other frame.', 'They are simultaneous in all frames which are at rest w.r.t.  A', 20),
(6, 'If Wigner-seitz cell of reciprocal lattice has volume Vws and volume of second order Brillouin zone is VBZ2 then', 'Vws = VBZ2', 'Vws*2 = VBZ2', 'Vws/2  =  VBZ2', 'Vws/4 = VBZ2', 'Vws = VBZ2', 25),
(7, 'Tom and Jerry are sitting in a train moving with high velocity c/2 with respect to You. Tom is holding one hardboard outside the window of train. According to Jerry it is circle. You will see it as -----------------', 'Square', 'Ellipse', 'Circle', 'Pentagon', 'Ellipse', 30),
(8, 'Angle between [100] direction and (100) plane is', 'Parallel : 0 degrees', 'Perpendicular : 90  degrees', '45 degrees', 'Vary with crystal system', 'Vary with crystal system', 35),
(9, 'Spin of a photon is', '0', '1', 'Half', '3/4', '1', 40),
(10, 'A glass tube, closed at one end, has a loudspeaker placed at the other end. This is used to create a vibrating column of air. The wave in tube is best described as', 'Longitudinal and progressive', 'Longitudinal and standing', 'Transverse and standing', 'Transverse and progressive', 'Longitudinal and standing', 45),
(11, 'A beam of electron spreads out into several distinct beams after passing through a crystallographic material. This demonstrates that', 'Electron behave as particle', 'Electron behave as wave', 'Electron exists in different energy levels', 'Electron has negative charge', 'Electron behave as wave', 50);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `name` varchar(80) DEFAULT NULL,
  `class` varchar(30) DEFAULT NULL,
  `score` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
