#Create a table into dbpython database  
import mysql.connector  

def CreateConnectionAndDB():
   mysqldb=mysql.connector.connect(host="localhost",user="root",password="spiderman06")#established connection   
   mycursor=mysqldb.cursor()#cursor() method create a cursor object  
   mycursor.execute("create database dbpython")#Execute SQL Query to create a database    
   mysqldb.close()#Connection Close  

def CreateTable():
   mysqldb=mysql.connector.connect(host="localhost",user="root",password="spiderman06",database="dbpython")#established connection between your database   
   mycursor=mysqldb.cursor()#cursor() method create a cursor object  
   mycursor.execute("create table student(roll INT,name VARCHAR(255), marks INT)")#Execute SQL Query to create a table into your database  
   mysqldb.close()#Connection Close  

def InsertValues():
   mysqldb=mysql.connector.connect(host="localhost",user="root",password="spiderman06",database="dbpython")#established connection between your database  
   mycursor=mysqldb.cursor()#cursor() method create a cursor object    
   try:  
      #Execute SQL Query to insert record  
      mycursor.execute("insert into student values(1,'Sarfaraj',80),(2,'Kumar',89),(3,'Sohan',90)")  
      mysqldb.commit() # Commit is used for your changes in the database  
      print('Record inserted successfully...')   
   except:  
      # rollback used for if any error   
      mysqldb.rollback()  
   mysqldb.close()#Connection Close  

def Display():
   mysqldb=mysql.connector.connect(host="localhost",user="root",password="spiderman06",database="dbpython")#established connection between your database  
   mycursor=mysqldb.cursor()#cursor() method create a cursor object  
   try:  
      mycursor.execute("select * from student")#Execute SQL Query to select all record   
      result=mycursor.fetchall() #fetches all the rows in a result set   
      for i in result:    
         roll=i[0]  
         name=i[1]  
         marks=i[2]  
         print(roll,name,marks)  
   except:   
      print('Error:Unable to fetch data.')  
   mysqldb.close()#Connection Close  

def Update():
   mysqldb=mysql.connector.connect(host="localhost",user="root",password="spiderman06",database="dbpython")#established connection between your database  
   mycursor=mysqldb.cursor()#cursor() method create a cursor object  
   try:  
      mycursor.execute("UPDATE student SET name='Vijay', marks=100 WHERE roll=1")#Execute SQL Query to update record
      mysqldb.commit() # Commit is used for your changes in the database  
      print('Record updated successfully...')   
   except:   
      # rollback used for if any error  
      mysqldb.rollback()  
   mysqldb.close()#Connection Close

def DeleteRecorrd():
   mysqldb=mysql.connector.connect(host="localhost",user="root",password="spiderman06",database="dbpython")#established connection between your database  
   mycursor=mysqldb.cursor()#cursor() method create a cursor object   
   try:   
      mycursor.execute("DELETE FROM student WHERE roll=3")#Execute SQL Query to detete a record   
      mysqldb.commit() # Commit is used for your changes in the database  
      print('Record deteted successfully...')  
   except:  
      # rollback used for if any error  
      mysqldb.rollback()  
   mysqldb.close()#Connection Close  

#CreateConnectionAndDB()
#CreateTable()
#InsertValues()
Display()
#Update()
#DeleteRecorrd()