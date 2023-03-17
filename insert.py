#/usr/bin/python3

import psycopg2

try:
   connection = psycopg2.connect(user="replica",
                                  password="password",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="test")
   cursor = connection.cursor()

   postgres_insert_query = """ insert into usuarios(id,nombre, apellido) VALUES (%s,%s,%s)"""
    
  
   for i in range(10,30):
    record_to_insert = (i, 'Jhon', 'Doe')
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    count = cursor.rowcount
    print (i, "Record inserted successfully into users table")

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into users table", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
