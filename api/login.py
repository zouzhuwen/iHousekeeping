"""
被测系统的接口封装
登录：http://192.168.0.99:9080/api/uaa/web-backend-os-login
"""

#导包



#定义类
class LoginAPI():
    #初始化
    def __init__(self):
        self.login_url="http://192.168.0.99:9080/api/uaa/web-backend-os-login"

    #登录
    def login(self,session,loginName,password):
        login_data={
            "loginName":loginName,
            "password":password
        }
        return session.post(url=self.login_url,json=login_data)
