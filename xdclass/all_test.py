import unittest
import HTMLTestRunner
import login_order, category
import time
from mail_demo import MailUtils



# 创建一个容器
def create_suite():
    print("测试开始")
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(login_order.LoginOrderTestCase))
    suite.addTest(unittest.makeSuite(category.moveToMenu))
    return suite


if __name__ == "__main__":
    suite = create_suite()

    #file_prefix = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    fp = open("./report.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner\
        (stream=fp, title=u"xdclass测试报告", description="测试用例执行情况")
    runner.run(suite)
    fp.close()
    # 发送邮件
    MailUtils.send_test_report()