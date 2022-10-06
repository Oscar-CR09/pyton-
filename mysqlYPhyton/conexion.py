# instalar driver comando = pip install mysql-connector-python

#from psycopg2 import pool
#from logger import logger
#import mysql as bd

#import mysql.connector

#connection = mysql.connector.connect(user='root', password='1989cero',
#                                     host='localhost',
 #                                    database='escuela',
  #                                   port='3306')

#from typing_extensions import Self
import mysql.connector


class DataBase:
    def __init__ (self):
        self.connection=mysql.connector.connect(
            user="root", password="1989cero",
            host="localhost", 
            database="escuela",
            port="3306"
         )
        self.cursor=self.connection.cursor() 

#print(conexion)

