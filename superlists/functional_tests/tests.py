# -*- coding: utf-8 -*-''
"""
Created on Tue Nov 12 09:58:10 2019

@author: vic
"""
from django.test import LiveServerTestCase
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = self.browser.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        #checkout the homepage title
        #self.browser.get('http://localhost:8000')
        self.browser.get(self.live_server_url)
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
        self.browser.implicitly_wait(1)

        #print(edith_list_url)
        self.check_for_row_in_list_table('1: Buy stuff')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use it to fly')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy stuff')
        self.browser.implicitly_wait(1)
        self.check_for_row_in_list_table('2: Use it to fly')
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/*')
        
        self.browser.quit()
        self.browser = webdriver.Firefox()

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.asserNotIn('Buy stuff', page_text)
        self.asserNotIn('Use it to fly', page_text)

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.asserIn('Buy stuff', page_text)
        self.assertIn('Buy milk', page_text)

        """functionalities pending"""

#if __name__=='__main__':
#    unittest.main(warnings='ignore')
