# MySQL Menu-driven Program

import mysql.connector
import getpass

def cnameprod():
    cur.execute('SELECT CLIENT.CLIENTNAME, PRODUCT.PRODUCTNAME FROM CLIENT\
        INNER JOIN PRODUCT ON CLIENT.P_ID = PRODUCT.P_ID\
        ORDER BY CLIENT.CLIENTNAME DESC;')
    print('')
    for i in cur.fetchall():
        print(i)

def priceinc():
    cur.execute('UPDATE PRODUCT SET PRICE = PRICE + (PRICE*0.05);')
    cur.execute('SELECT * FROM PRODUCT;')
    print('')
    for i in cur.fetchall():
        print(i)

def removebangalore():
    cur.execute("DELETE FROM CLIENT WHERE City = 'Bangalore'")
    cur.execute('SELECT * FROM CLIENT;')
    print('')
    for i in cur.fetchall():
        print(i)

def clientno():
    cur.execute("SELECT COUNT(*) AS 'Number of Clients', City FROM CLIENT GROUP BY City;")
    print('')
    for i in cur.fetchall():
        print(i)

def incwidth():
    cur.execute("ALTER TABLE CLIENT MODIFY COLUMN City varchar(50);")

while True:
    rootpwd = getpass.getpass('Please enter the root password: ')
    try:
        db = mysql.connector.connect(host='localhost', user='root', password=rootpwd, autocommit=True)
        break
    except:
        print('\nTry again.')

cur = db.cursor(buffered=True)

cur.execute('CREATE DATABASE STORE;')
cur.execute('USE STORE;')

cur.execute('CREATE TABLE PRODUCT(\
    P_ID varchar(255) NOT NULL,\
    PRODUCTNAME varchar(255),\
    MANUFACTURER varchar(255),\
    PRICE int,\
    PRIMARY KEY (P_ID)\
    );')
cur.execute('CREATE TABLE CLIENT(\
    C_ID int NOT NULL,\
    CLIENTNAME varchar(255),\
    City varchar(255),\
    P_ID varchar(255),\
    PRIMARY KEY (C_ID)\
    );')

cur.execute("INSERT INTO PRODUCT (P_ID, PRODUCTNAME, MANUFACTURER, PRICE)\
    VALUES \
        ('TP01','TALCOM POWDER','LAK',40),\
        ('FW05','FACE WASH','ABC',45),\
        ('BS01','BATH SOAP','ABC',55),\
        ('SH06','SHAMPOO','XYZ',120),\
        ('FW12','FACE WASH','XYZ',95);")

cur.execute("INSERT INTO CLIENT (C_ID, CLIENTNAME, CITY, P_ID)\
    VALUES \
        (01,'COSMETIC SHOP','Delhi','FW05'),\
        (06,'TOTAL HEALTH','Mumbai','BS01'),\
        (12,'LIVE LIFE','Delhi','SH06'),\
        (15,'PRETTY WOMAN','Delhi','FW12'),\
        (16,'DREAMS','Bangalore','TP01');")

while True:
    print('\n[1] Display Client Name and Product Purchased\
        \n[2] Increase price by 5%\
        \n[3] Remove clients from Bangalore\
        \n[4] Display number of clients from each city\
        \n[5] Change width of City column to 50\
        \n[6] Quit')
    try:
        useropt = int(input("\nSelect [1], [2], [3], [4], [5], or [6]: "))
    except:
        print('\nPlease enter a number.')
        continue
    if useropt == 1:
        cnameprod()
    elif useropt == 2:
        priceinc()
    elif useropt == 3:
        removebangalore()
    elif useropt == 4:
        clientno()
    elif useropt == 5:
        incwidth()
    elif useropt == 6:
        break
    else:
        print('\nPlease enter a value between 1 and 6')