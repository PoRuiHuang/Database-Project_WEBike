create database Project;
-- show databases;
Use Project;


create table _User(
	StudentID varchar(9) NOT NULL,
    StudentName varchar(255) NOT NULL,
    EmployeeSSN varchar(10),
    PRIMARY KEY(StudentID),
    Location varchar(255)
);

-- show user;
-- DROP TABLE USER; 

create table Employee(
    EmployeeName varchar(255) NOT NULL,
    EmployeeSSN varchar(10)  NOT NULL,
    PRIMARY KEY(EmployeeSSN)
);

-- DROP TABLE EMPLOYEE;

create table Bike(
	BikeID varchar(20) NOT NULL,
    Lock_Password varchar(32) NOT NULL,
    Cost int,
    Renting bool NOT NULL,
    Rating float,
    OwnerID varchar(9) NOT NULL,
    PRIMARY KEY(BikeID)
);

-- DROP TABLE Bike;

create table Transaction_Record(
    StudentID varchar(9) NOT NULL PRIMARY KEY,
    Balance int NOT NULL,
    T_Date varchar(20) NOT NULL,
    T_Time varchar(20) NOT NULL,
    Amount int  NOT NULL,
    FOREIGN KEY (StudentID) references _User (StudentID) 
);

create table Reservation_Record(
    StudentID varchar(9) NOT NULL ,
    BikeID varchar(20) NOT NULL ,
    R_Date varchar(20) NOT NULL,
    R_Time varchar(20) NOT NULL,
    primary key(StudentID, BikeID),
    FOREIGN KEY (StudentID) references _User (StudentID),
    FOREIGN KEY (BikeID) references Bike (BikeID)  
);

-- DROP TABLE Reservation_Record;

create table Lend_Record(
    StudentID varchar(9) NOT NULL ,
    BikeID varchar(20) NOT NULL ,
    L_Date varchar(20) NOT NULL,
    Start_Time varchar(20) NOT NULL,
    End_Time varchar(20),
    Given_rate float,
    primary key(StudentID, BikeID),
    FOREIGN KEY (StudentID) references _User (StudentID),
    FOREIGN KEY (BikeID) references Bike (BikeID)  
);

create table Fixed_Record(
    BikeID varchar(20) NOT NULL,
    F_Date varchar(20) NOT NULL,
    Content varchar(1024),
    primary key(BikeID),
    FOREIGN KEY (BikeID) references Bike (BikeID)  
);

create table Violation_Record(
    StudentID varchar(9) NOT NULL ,
    V_Date varchar(20) NOT NULL,
    V_Time varchar(20) NOT NULL,
    Fine int NOT NULL,
    primary key(StudentID),
    FOREIGN KEY (StudentID) references _User (StudentID)
);

-- select* from Bike;

-- show tables;