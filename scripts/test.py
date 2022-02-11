import json
import unittest
import requests
from parameterized import parameterized
from app import BASE_DIR
from api.login import LoginAPI

#构造测试数据
def build_data():
    file = BASE_DIR+"/data/login2.json"
    test_data = []
    with open(file,encoding="utf-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            loginName = case_data.get("loginName")
            password = case_data.get("password")
            status_code = case_data.get("status_code")
            returnCode = case_data.get("returnCode")
            returnMsg = case_data.get("returnMsg")

            test_data.append((loginName,password,status_code,returnCode,returnMsg))
    return test_data

#创建测试类
class TestLogin(unittest.TestCase):
    #前置处理
    def setUp(self):
       self.login =  LoginAPI() #实例化登录接口类
       self.session =requests.Session() #创建Session对象

    #后置处理
    def tearDown(self):
        if self.session:
            self.session.close()

    @parameterized.expand(build_data())
    def test01_login(self,loginName,password,status_code,returnCode,returnMsg):
        response = self.login.login(self.session,loginName,password)
        print(loginName)
        print(password)
        print(response.json())


        self.assertEqual(status_code,response.status_code)
        self.assertEqual(returnCode,response.json().get("returnCode"))
        self.assertEqual(returnMsg,response.json().get("returnMsg"))

