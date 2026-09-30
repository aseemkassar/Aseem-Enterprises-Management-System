import pymysql

def create_database():

    con=pymysql.connect(
        host="localhost",
        user="root",
        password=""
    )

    cur=con.cursor()

    cur.execute("CREATE DATABASE IF NOT EXISTS kryptoradb")

    cur.execute("USE kryptoradb")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS std_info(
    id INT AUTO_INCREMENT PRIMARY KEY,
    f_name VARCHAR(50),
    l_name VARCHAR(50),
    contact VARCHAR(20),
    email VARCHAR(50),
    password VARCHAR(50)
    )
    """)

    con.commit()
    con.close()

create_database()
