# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:49:49 2019

@author: vic
"""

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title