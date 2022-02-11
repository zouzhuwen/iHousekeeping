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
        #判断两个参数不为空
        if loginName is None and password is None:
            login_data = { }
            return session.post(url=self.login_url, json=login_data)
        elif loginName is None:
            login_data = {
                "password": password
            }
            return session.post(url=self.login_url, json=login_data)
        elif password is None:
            login_data = {
                "loginName": loginName,
            }
            return session.post(url=self.login_url, json=login_data)
        else:
            login_data = {
                "loginName": loginName,
                "password": password
            }
            return session.post(url=self.login_url, json=login_data)




