# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:39:59 2019

@author: vic
"""

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'To-Do' in browser.title, f"Browser title was: {browser.title}"

browser.quit()