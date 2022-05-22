from utils.mysql_wrapper import MysqlWrapper

import pytest

def test_drop_and_create():
  MysqlWrapper().drop_table()
  MysqlWrapper().create_table()
  
def test_insert_row():
  MysqlWrapper().insert_row('金金')

def test_query_like():
  res = MysqlWrapper().query_like('金')
  print(res)