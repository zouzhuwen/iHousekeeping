"""
定义接口测试用例
使用unittest
1、导包
2、创建测试类
    2.1、前置处理
    2.3、创建测试方法
    2.3 后置处理
"""


# 1、导包
import json

import requests
import unittest
from api.login import LoginAPI
from parameterized.parameterized import parameterized

#构造测试数据
def  build_data():
    file = "../data/login.json"
    test_data = []
    with open(file,encoding='utf-8') as f :
        json_data = json.load(f)
        for  case_data in json_data :
            loginName = case_data.get("loginName")
            password = case_data.get("password")
            status_code = case_data.get("status_code")
            returnCode = case_data.get("returnCode")
            returnMsg = case_data.get("returnMsg")

            test_data.append((loginName, password, status_code, returnCode, returnMsg))
    return test_data

# 2、创建测试类
class TestLogin(unittest.TestCase):
#     2.1、前置处理
    def setUp(self):
        self.login_api = LoginAPI()     #实例化接口类
        self.session = requests.Session() #创建session对象
#     2.3、后置处理
    def tearDown(self):
        if self.session:
            self.session.close()

#     2.3 创建测试方法
    @parameterized.expand(build_data())
    def test01_login_success(self,loginName,password,status_code,returnCode,returnMsg):
        #调用登录接口获取登录信息，并进行断言
        response = self.login_api.login(self.session,loginName,password)
        print(response.json())

        self.assertEqual(status_code,response.status_code)
        self.assertEqual(returnCode,response.json().get("returnCode"))
        self.assertIn(returnMsg,response.json().get("returnMsg"))
