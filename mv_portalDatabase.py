import mysql.connector
from mysql.connector import Error


class Database():
    def __init__(self,
                 host="localhost",
                 port="3306",
                 database="mv_banks_portal",
                 user='root',
                 password='Labtechs85'):

        self.host       = host
        self.port       = port
        self.database   = database
        self.user       = user
        self.password   = password
        self.connection = None
        self.cursor     = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host         = self.host,
                port         = self.port,
                database     = self.database,
                user         = self.user,
                password     = self.password)
            
            if self.connection.is_connected():
                return
        except Error as e:
            print("Error while connecting to MySQL", e)


    def getAllAccounts(self):
        if self.connection.is_connected():
            self.cursor= self.connection.cursor();
            query = "select * from accounts"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records

    def getAllTransactions(self):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * from transactions"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records
        pass
       
    def deposit(self, accountID, amount):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "CALL deposit_procedure(%s, %s)"
            p = (accountID, amount)
            self.cursor.execute(query, p)
            self.connection.commit()
            results = self.cursor.fetchall()
            return results
            
        ''' Complete the method that calls store procedure
                    and return the results'''
        pass
   

    def withdraw(self, accountID, amount):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "CALL withdraw_procedure(%s, %s)"
            para = (accountID, amount)
            self.cursor.execute(query, para)
            self.connection.commit()
            results = self.cursor.fetchall()
            return results
        
        ''' Complete the method that calls store procedure
                    and return the results'''
        pass
        
    def addAccount(self, ownerName, owner_ssn, balance, status):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "INSERT INTO accounts (ownerName, owner_ssn, balance, account_status) VALUES (%s, %s, %s, %s)"
            values = (ownerName, owner_ssn, balance, status)
            self.cursor.execute(query, values)
            self.connection.commit()
    
        ''' Complete the method to insert an
                    account to the accounts table'''
        pass
  
    def accountTransactions(self, accountID):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "CALL accountTransaction(%s)"
            pa = (accountID)
            self.cursor.execute(query, pa)
            results = self.cursor.fetchall()
            return results
        
        ''' Complete the method to call
                    procedure accountTransaction return results'''
        pass
  
    def deleteAccount(self, AccountID):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "DELETE FROM transactions WHERE account_id = %s"
            params = (accountID)
            self.cursor.execute(query, params)
            self.connection.commit()
        ''' Complete the method to delete account
                and all transactions related to account'''
        pass
