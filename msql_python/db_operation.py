from db_config import create_connection

def create_table():
    connection=create_connection()
    cursor=connection.cursor()
    create_table_query="""
    CREATE TABLE IF NOT EXISTS citizen(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(55),
        email VARCHAR(255)
    );
    """
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()

def create_user(name,email):
    connection=create_connection()
    cursor=connection.cursor()
    insert_query='INSERT INTO citizen(name,email)VALUES(%s,%s)'
    cursor.execute(insert_query,(name,email))
    connection.commit()
    print("user created successfully!")
    cursor.close()
    connection.close()

def get_user():
    connection=create_connection()
    cursor=connection.cursor()
    select_query="SELECT * from citizen"
    cursor.execute(select_query)
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()

def update_user(user_id,new_name,new_email):
    connection=create_connection()
    cursor=connection.cursor()
    update_user="UPDATE     citizen SET name=%s,email=%s WHERE id=%s"
    cursor.execute(update_user,(new_name,new_email,user_id))
    connection.commit()
    print('user updated successfully:')
    cursor.close()
    connection.close()

def delete_user(user_id):
    connection=create_connection()
    cursor=connection.cursor()
    delete_query='DELETE FROM citizen WHERE id=%s'
    cursor.execute(delete_query,(user_id,))
    connection.commit()
    print('user deleted successfully!')
    cursor.close()
    connection.close()