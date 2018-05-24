CREATE USER 'm2m'@'localhost' IDENTIFIED BY 'm2m';
GRANT ALL PRIVILEGES ON *.* TO 'm2m'@'localhost';
CREATE DATABASE 5GRobot;
USE 5GRobot;


CREATE TABLE RobotStatus (robotId VARCHAR(20), ipAddress VARCHAR(15), command INT, speed VARCHAR(15), angle VARCHAR(15),trackStatus VARCHAR(15), detectStatus VARCHAR(15),time VARCHAR(15),);

INSERT INTO RobotStatus (RobotId,RobotIp,speed,command) VALUES ("robot1", "172.24.1.5",2,"STOP");

