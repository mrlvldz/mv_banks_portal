create database mv_banks_portal;

create table accounts (
accountID int not null unique auto_increment primary key,
ownerName varchar (45) Not Null,
owner_ssn int not null,
balance decimal (10,2) default 0.00,
account_status varchar (45)
);

create table Transactions (
transactionID int not null unique auto_increment primary key,
accountID int not null,
transactionType varchar (45) not null,
transactionAmount decimal (10,2) not null,
foreign key (accountID) 
references accounts(accountID)
);

insert into accounts (ownerName, owner_ssn, balance, account_status) values 
('Maria Jozef', 123456789, 10000.00, 'active'),
('Linda Jones', 987654321, 2600.00, 'inactive'),
('John McGrail', 222222222, 100.50, 'active'),
('Patty Luna', 111111111, 509.75, 'inactive');

insert into Transactions (accountID, transactionType, transactionAmount) values 
(1, 'deposit', 650.98), 
(3, 'withdraw', 899.87),
(3, 'deposit', 350.00);

create procedure accountTransactions(IN accountID int) 
select * from Transactions 
where accountID = accountID;

call accountTransactions(1);

DELIMITER //
create procedure deposit(IN accountID int, IN amount decimal(10,2))
begin
  start transaction;
  insert into Transactions (accountID, transactionType, transactionAmount) values (accountID, 'deposit', amount);
  update accounts
  set balance = balance + amount
  where accountID = accountID;
end //
DELIMITER ;

call deposit (1, 650.98);

DELIMITER //
create procedure withdraw(IN accountID int, IN amount decimal(10,2))
begin
  start transaction;
  insert into Transactions (accountID, transactionType, transactionAmount) values (accountID, 'withdraw', amount);
  update accounts
  set balance = balance - amount
  where accountID = accountID;
end //
DELIMITER ;

call withdraw (3, 899.87);

DELIMITER //
create procedure deposit(IN accountID int, IN amount decimal(10,2))
begin
  start transaction;
  insert into Transactions (accountID, transactionType, transactionAmount) values (accountID, 'deposit', amount);
  update accounts
  set balance = balance + amount
  where accountID = accountID;
end //
DELIMITER ;

call deposit (3, 350.00);
