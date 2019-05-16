# -*- coding:UTF-8 -*-

from selenium import  webdriver
import  unittest
from time import  sleep
from selenium.webdriver.common.action_chains import  ActionChains


class moveToMenu(unittest.TestCase):
    def setUp(self):
        print("测试开始")
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.shiyanlou.com"
        self.driver.get(self.base_url)

    def tearDown(self):
        print("测试用例执行结束")
        self.driver.quit()


    def test_menu(self):
        u"多级菜单测试用例"
        driver = self.driver
        target_element = driver.find_element_by_xpath('//div[@class="course-nav"]/ul/li[1]/div/a[1]')
        # 鼠标移动到目标菜单上
        ActionChains(driver).move_to_element(target_element).perform()
        sleep(2)
        driver.find_element_by_xpath('//div[@class="course-nav"]/ul/li[1]/div[2]/div/div[1]/a[5]').click()

if __name__ == '__main__':
    unittest.main()


