# -*- coding: utf-8 -*-
# filename: handle.py

from lxml import etree
from utils.mysql_wrapper import MysqlWrapper

import hashlib
import web


class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is tommi framework"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "tom" #请按照公众平台官网\基本配置中信息填写

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            return echostr
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Argument:
            return Argument

    def POST(self):
        data = web.data()
        print('post data: ', data)
        xml = etree.fromstring(data)
        print('xml: ', xml)
        client_user = xml.find('FromUserName').text
        server_user = xml.find('ToUserName').text
        client_content = xml.find('Content').text
        print('client_user: {}, server_user: {}, content: {}', client_user, server_user, client_content)
        server_content = self.get_server_content(client_content)
        res = self.make_response(client_user, server_user, server_content)
        return res
    
    def get_server_content(self, client_content):
        print('client_content: ', client_content)
        server_content = client_content + '地区的热线:\n'
        sql_contents = MysqlWrapper().query_like(client_content)
        for sql_content in sql_contents:
            server_content += sql_content[0] + '\n'
        print('server_content: ', server_content)
        return server_content

    def make_response(self, client_user, server_user, server_content):
        res = "<xml><ToUserName><![CDATA[{}]]></ToUserName><FromUserName><![CDATA[{}]]></FromUserName><CreateTime>1348831860</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[{}]]></Content><MsgId>1234567890123456</MsgId></xml>".format(client_user, server_user, server_content)
        print(res)
        return res