# coding:utf-8

from HTMLTestRunner import HTMLTestRunner
from modules import sendEmail
from modules import dir_path
import unittest

if __name__ == '__main__':
    test_dir = dir_path.dir_path() + '/testCases'
    report_dir = dir_path.dir_path() + '/report'

    filename = report_dir + '/report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='auto report', description='runned results')
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    runner.run(discover)
    fp.close()
    sendEmail.send_mail(filename)
    mail = sendEmail.send_mail(filename)
    if mail:
        print(u'email send success!')
    else:
        print(u'email send failed!')
