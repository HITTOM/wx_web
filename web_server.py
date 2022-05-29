# -*- coding: utf-8 -*-
# filename: web_server.py
# created by tom in 2022.5.29

from utils.mysql_wrapper import MysqlWrapper

import web

class WebServer(object):
    def GET(self):
        data = web.input()
        print('Get input: ', data)
        name = "北京"
        if 'name' in data:
            name = data['name']
        res_data = self.get_data(name)
        return res_data
    
    def get_data(self, name):
        print('name: ', name)
        data = name + '地区的热线:\n'
        sql_contents = MysqlWrapper().query_like(name)
        for sql_content in sql_contents:
            data += sql_content[0] + '\n'
        print('data: ', data)
        return {name: data}