#导包
import unittest
import time
from app import BASE_DIR
# from scripts.test01_login import TestLogin
# from scripts.test02_login_params import TestLogin2
from  scripts.test import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner

#封装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
# suite.addTest(unittest.makeSuite(TestLogin2))
#指定测报告路径
report = BASE_DIR+"/report/report{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
#以文件流形式打开文件
with open(report,"wb") as f :
    #创建HTMLTestRunner的运行器
    runner = HTMLTestRunner(f,title="iHousekeeping接口测试报告")
    #执行测试套件
    runner.run(suite)