# coding=utf-8
# -*- coding:utf-8 -*-
import json
import unittest

import logging
import swaggerpy
from swaggerpy.client import SwaggerClient
from swaggerpy.http_client import SynchronousHttpClient

from test_case.public import define_regex
from test_case.public import define_request
from test_case.public.define_log import LogDefine


class TestSongUrl(unittest.TestCase):
    def setUp(self,method="get", url="http://121.40.68.137:12008/api/v1/media/songurl"):
        LogDefine()
        self.parameters = {
            "userId": "1",
            "sourceId":"1"
        }
        self.verification = []
        self.res = define_request.make_request(method="get", url=url, parameters=self.parameters)

    def test_songurl(self):
        """获取失效歌曲链接"""
        res = self.res
        response_code = res.status_code
        if response_code == 200:
            logging.info("get code == 200 ,request success!")
            print "返回200，响应成功",res.url
            print res.text
            s=define_regex.find_code(text=res.text)
            if s>=0 :
                logging.info("correct response code: %s ",s)
                print u"返回正确 code: %s" %s
            else:
                logging.error("incorrect response code: %s",s)
                print u"接口请求失败 code: %s " %s
        else:
            logging.error("not return code 200 ,maybe hava some problem")
            print u"响应出错 code %s" %response_code

    def tearDown(self):
        self.assertEqual([],self.verification)

if __name__=="__main__":
    unittest.main()