import mysql.connector
from config import MYSQL_CONFIG
from sqlalchemy import create_engine

#Conection to Database Mysql, send dataframe to select table
def connection_mysql_to_tbl (dataframe, table_name):
    try:
        connection = mysql.connector.connect(
            host=MYSQL_CONFIG['host'],
            user=MYSQL_CONFIG['user'],
            password=MYSQL_CONFIG['password'],
            database=MYSQL_CONFIG['database'],
            port = MYSQL_CONFIG['port']
        )
        #Create engine sqlalchemy
        engine = create_engine(f"mysql+mysqlconnector://{MYSQL_CONFIG['user']}:{MYSQL_CONFIG['password']}@{MYSQL_CONFIG['host']}:{MYSQL_CONFIG['port']}/{MYSQL_CONFIG['database']}")
        #Send dataframe to tbl
        dataframe.to_sql(table_name, con=engine, if_exists='replace', index=False)
        #Close connection
        connection.close()

    # Error Mysql
    except mysql.connector.Error as error:
        print(f"Error de MySQL: {error}")
    #Error others error
    except Exception as error:
        print(f"Ocurrió un error: {error}")
    #Close any connections
    finally:
        # Close conection
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Close connections")