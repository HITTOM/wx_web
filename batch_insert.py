from utils.mysql_wrapper import MysqlWrapper

MysqlWrapper().drop_table()
MysqlWrapper().create_table()

filename = '/root/data/ll_phones'
f = open(filename, 'r', encoding = 'UTF-8')
lines = f.readlines()
for line in lines:
  if 1 == len(line):
    continue
  MysqlWrapper().insert_row(line[0:-1].strip('"'))