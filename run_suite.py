#导包
import unittest
import time
from scripts.test01_login import TestLogin
from scripts.test02_login_params import TestLogin2
from tools.HTMLTestRunner import HTMLTestRunner

#封装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestLogin2))
#指定测报告路径
report = "./report/report{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
#以文件流形式打开文件
with open(report,"wb") as f :
    #创建HTMLTestRunner的运行器
    runner = HTMLTestRunner(f,title="iHousekeeping接口测试报告")
    #执行测试套件
    runner.run(suite)