from selenium import webdriver
from selenium.webdriver.support.select import Select
# driver = webdriver.Firefox()
# driver.get("http://www.w3school.com.cn/jquery/jquery_ref_selectors.asp")
# a = driver.find_element_by_css_selector(".dataintable tr")
#
# print(a)

import unittest
from nose_parameterized import parameterized
import random

class TestMathUnitTest(unittest.TestCase):
    params = [
        ("01",1,2,3),
        ("02",2,2,4),
    ]
    # def test_d(self):
    #     self.assertEqual(1,1)

    @parameterized.expand(input=params)
    def test(self, name, a, b, c):
        self.assertEqual(a + b, c)

if __name__ == '__main__':

    # unittest.main(verbosity=2)
    # suiteTest = unittest.TestSuite()
    # suiteTest.addTest(TestMathUnitTest(test))
    # runner = unittest.TextTestRunner()
    # runner.run(suiteTest)

    # suit = unittest.TestLoader().discover("./", pattern="demo.py", top_level_dir=None)
    # runner = unittest.TextTestRunner()
    # runner.run(suit)
    for i in range(5):
        print(random.randint(0,8))