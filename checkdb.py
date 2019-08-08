import cdb
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
try:

     connection = mysql.connector.connect(host='localhost',
                                 database='python_db',
                                 user='vitaly',
                                 password='')



     cursor = connection.cursor()
           # val = (val())
     # Val= cdb.val()
    # # rc = cursor.execute("SELECT * FROM school")
     r = "SELECT count(*) FROM school where Roll_Number = '5'"
     # num = (Val,)
     cursor.execute(r)
     # count = cursor.fetchall
     rc =cursor.rowcount;
     print 'rows=',rc
     if (rc == 0 or rc == 1):
       # Val = cdb.val()
       sql_insert_query = "INSERT INTO school(Roll_number) VALUES (5)"
       result  = cursor.execute(sql_insert_query)
       connection.commit()
       print ("Record inserted successfully into python_users table")
       # else:
     #  break

except mysql.connector.Error as error :
        connection.rollback() #rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))

finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")