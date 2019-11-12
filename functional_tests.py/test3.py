# -*- coding: utf-8 -*-''
"""
Created on Tue Nov 12 09:58:10 2019

@author: vic
"""

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        #checkout the homepage title
        self.browser.get('http://localhost:8000')
        #page title
        self.assertIn("To-Do", self.browser.title)
        self.fail('Test finalizado')
        
        """functionalities pending"""

if __name__=='__main__':
    unittest.main(warnings='ignore')