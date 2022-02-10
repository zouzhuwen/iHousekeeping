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
from tools.dbutil import DBUtil
from api.login import LoginAPI
from parameterized.parameterized import parameterized

#构造测试数据
def  build_data():
    sql = "select * from t_login;"
    db_data =DBUtil.exe_sql(sql)
    print(db_data)
    test_data = []
    for  case_data in db_data :
        loginName = case_data[2]
        password = case_data[3]
        status_code = case_data[4]
        returnCode = case_data.get[5]
        returnMsg = case_data[6]

        test_data.append((loginName, password, status_code, returnCode, returnMsg))
    return test_data

# 2、创建测试类
class TestLogin2(unittest.TestCase):
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
