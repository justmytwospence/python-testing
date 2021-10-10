import os
from dotenv import load_dotenv

import mysql.connector


load_dotenv()

connection = mysql.connector.connect(
    host='localhost',
    user='root',

    passwd=os.environ['MYSQL_PW'],
    database='sm_app')

cursor = connection.cursor()
# cursor.execute("CREATE DATABASE sm_app")

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT,
  name TEXT NOT NULL,
  age INT,
  gender TEXT,
  nationality TEXT,
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""

cursor.execute(create_users_table)
