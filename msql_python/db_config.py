import  mysql.connector

def create_connection():
    try:
        connection=mysql.connector.connect(
            user='root',
            password='root',
            host='localhost',
            database='mysql_python'
        )
        print('connection created')
        return connection
    except Exception:
        print("some problem occured")
        return None

        