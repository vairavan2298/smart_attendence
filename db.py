
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode



def dbval(val):

    try:
        connection = mysql.connector.connect(host='localhost',
                                     database='python_db',
                                     user='vitaly',
                                     password='')



        cursor = connection.cursor()

        sql = "SELECT * FROM school where Roll_number = %s "
        cursor.execute(sql, (val,))
        # count = cursor.execute(sql)
        cursor.fetchall()
        
        rc = cursor.rowcount;

        # print 'rows=',rc
        if (rc == 0 ):
            sql_insert_query = "INSERT INTO school(Roll_Number) VALUES (%s)"
            result  = cursor.execute(sql_insert_query, (val,))
            connection.commit()
            print ("Record inserted successfully into python_users table")
        # else:
        #     sys.exit()

    except mysql.connector.Error as error :
     connection.rollback() #rollback if any exception occured
     print("Failed inserting record into python_users table {}".format(error))

    finally:
    #     #closing database connection.
     if(connection.is_connected()):
      cursor.close()
      connection.close()
      # print("MySQL connection is closed")