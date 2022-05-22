import mysql.connector
from mysql.connector.cursor import MySQLCursor

class MysqlWrapper():
  def __init__(self):
    self._connect = mysql.connector.connect(
      host = '127.0.0.1',
      port = 3306,
      user = 'root',
      password = 'yjl3104@H',
      database = 'll',
    )

  def drop_table(self):
    sql = "drop table rough_phones;"
    cursor = self._connect.cursor()
    cursor.execute(sql)
    self._connect.commit()
    
  def create_table(self):
    sql = "CREATE TABLE IF NOT EXISTS `rough_phones`( \
      `id` INT UNSIGNED AUTO_INCREMENT, \
      `content` VARCHAR(5000), \
      PRIMARY KEY ( `id` ) \
    );"
    cursor = self._connect.cursor()
    cursor.execute(sql)
    self._connect.commit()

  def insert_row(self, row):
    sql = 'insert into `rough_phones` (content) values ("{}");'.format(row)
    print(sql)
    cursor = self._connect.cursor()
    cursor.execute(sql)
    self._connect.commit()

  def query_like(self, query):
    sql = "select content from `rough_phones` where content like '%{}%';".format(query)
    print(sql)
    cursor = self._connect.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    return res