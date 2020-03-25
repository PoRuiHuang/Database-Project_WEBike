Use Project;


-- -----------------------------------------User-------------------------------------------------
-- User register
INSERT INTO _User (StudentID, StudentName)
VALUES ('ID', 'Name');

-- change User location with ID
UPDATE _User
SET Location = 'Location'
WHERE StudentID = 'S_ID';

-- add EMPLOYEE with ID
UPDATE _User
SET EmployeeSSN = 'ESSN'
WHERE StudentID = 'S_ID';

-- add Violation
INSERT INTO Violation_Record (StudentID, V_Date, V_Time, Fine)
VALUES ('ID', 'Date', 'Time', 'Fine');

-- add Transaction
INSERT INTO Transaction_Record (StudentID, T_Date, T_Time, Balance, Amount)
VALUES ('ID', 'Date', 'Time', 'Fine', 'balance', 'Amount');

-- add Lend
INSERT INTO Lend_Record (StudentID, BikeID, L_Date, Start_Time, Given_rate)
VALUES ('S_ID', 'B_ID', 'Date', 'S_Time', 'Rate');

-- add Reservation
INSERT INTO Reservation_Record (StudentID, BikeID, R_Date, R_Time)
VALUES ('S_ID', 'B_ID', 'R_Date', 'R_Time');
-- ----------------------------------------------------------------------------------------------


-- -----------------------------------------Employee---------------------------------------------

-- Employee register
INSERT INTO Employee (EmployeeSSN, EmployeeName)
VALUES ('ID', 'Name');

-- ----------------------------------------------------------------------------------------------




-- -----------------------------------------Bike-------------------------------------------------

-- Bike register
INSERT INTO Bike (BikeID, LockID, Renting, OwnerID)
VALUES ('B_ID', (ABS(CAST(NEWID() AS binary(6)) %10000000000)), 0, 'S_ID');

-- Bike rented
UPDATE Bike
SET Renting = 1
WHERE BikeID = 'B_ID';

-- Bike rented
UPDATE Bike
SET Renting = 0
WHERE BikeID = 'B_ID';

-- Bike rate
UPDATE Bike
SET Earning_Rate = 'Rate'
WHERE BikeID = 'B_ID';

-- Bike rate
UPDATE Bike
SET Cost = 'Cost'
WHERE BikeID = 'B_ID';

-- Bike rating
UPDATE Bike
SET Rating = '1 to 5'
WHERE BikeID = 'B_ID';

-- Bike location
UPDATE Bike
SET Location = 'Location'
WHERE BikeID = 'B_ID';

-- add Fix
INSERT INTO Fixed_Record (BikeID, F_Date, Content)
VALUES ('ID', 'Date', 'F_content');

-- ----------------------------------------------------------------------------------------------
