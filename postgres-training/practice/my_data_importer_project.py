import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="cafebazaar_papp",
                                  password="hello",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="cafebazaar_db")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    sql2 = '''COPY developer(id, title, email) FROM './data/developers.csv' DELIMITER ',' CSV HEADER;'''
    result2 = cursor.execute(sql2)
    sql3 = '''COPY application(package_name, developer_id, creation_date, publish_state, price) FROM './data/applications.csv' DELIMITER ',' CSV HEADER'''
    result3 = cursor.execute(sql3)
    connection.commit()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

  
