# -*- coding: UTF-8 -*-

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains


class LoginOrderTestCase(unittest.TestCase):
    def setUp(self):
        print("测试开始")
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "https://xdclass.net"
        self.driver.get(self.base_url)


    def tearDown(self):
        print("单个测试用例结束")

    def test_login_and_order(self):
        u"登录测试用例"
        driver = self.driver
        driver.find_element_by_css_selector('.login > span:nth-child(1)').click()
        sleep(1)

        # 清空输入框
        driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div/div[1]/input').clear()
        driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div/div[1]/input') \
            .send_keys('13692183615')
        sleep(1)

        driver.find_element_by_css_selector('.psw > input:nth-child(1)').clear()
        driver.find_element_by_css_selector('.psw > input:nth-child(1)').send_keys('aaa111')
        sleep(1)

        # 点击登录按钮
        driver.find_element_by_css_selector('.btn').click()
        sleep(1)
        driver.maximize_window()

        # 定位到账号元素，并hover鼠标
        name = driver.find_element_by_css_selector('.avatar_img')
        ActionChains(driver).move_to_element(name).perform()
        sleep(3)

        # 校验用户名是否正确
        username = driver.find_element_by_css_selector('.username').text
        if username == "独照灯塔":
            print("login ok")
        else:
            print("login error")

        u"下单测试用例"
        driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/a[1]/div/img').click()
        sleep(2)

        all_handles = driver.window_handles
        curr_win = driver.current_window_handle

        for i in all_handles:
            if i != curr_win:
                driver.switch_to.window(i)
        print(driver.title)

        driver.find_element_by_css_selector('.buy_tolearn > a').click()
        print("进入下单页面")


if __name__ == '__main__':
    unittest.main()


