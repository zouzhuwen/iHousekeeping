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
import requests
import unittest
from api.login import LoginAPI

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
    def test01_login_success(self):
        #调用登录接口获取登录信息，并进行断言
        response = self.login_api.login(self.session,"13500000000","e52f073160e5604f72b24a7d6df0d526b5c0b0e2fa7ecac31ca45223ebe9a0d1")
        print(response.json())

        self.assertEqual(200,response.status_code)
        self.assertEqual("0000",response.json().get("returnCode"))
        self.assertIn("Success",response.json().get("returnMsg"))

    def test02_login_user_isnot_exist(self):
        # 调用登录接口获取登录信息，并进行断言
        response = self.login_api.login(self.session, "13500009999",
                                        "e52f073160e5604f72b24a7d6df0d526b5c0b0e2fa7ecac31ca45223ebe9a0d1")
        print(response.json())

        self.assertEqual(200, response.status_code)
        self.assertEqual("IHK14", response.json().get("returnCode"))
        self.assertIn("用户不存在", response.json().get("returnMsg"))

    def test03_login_password_error(self):
        # 调用登录接口获取登录信息，并进行断言
        response = self.login_api.login(self.session, "13500000000",
                                        "1e52f073160e5604f72b24a7d6df0d526b5c0b0e2fa7ecac31ca45223ebe9a0d1")
        print(response.json())

        self.assertEqual(200, response.status_code)
        self.assertEqual("IHKER04", response.json().get("returnCode"))
        self.assertIn("账号或密码有误，请重新输入。提示：账号或密码输入错误超过5次，系统将锁定30分钟", response.json().get("returnMsg"))