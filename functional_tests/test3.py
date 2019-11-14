# -*- coding: utf-8 -*-''
"""
Created on Tue Nov 12 09:58:10 2019

@author: vic
"""

from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        #checkout the homepage title
        self.browser.get('http://localhost:8000')
        #page title
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #enter a todo item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )
        inputbox.send_keys('Buy stuff')
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
                any(row.text == '1: Buy stuff' for row in rows)
            )
        self.fail('Test finalizado')
        
        """functionalities pending"""

if __name__=='__main__':
    unittest.main(warnings='ignore')