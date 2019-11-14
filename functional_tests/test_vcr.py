# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:47:53 2019

@author: vic
"""

import vcr
import requests
 
myvcr = vcr.VCR(
        record_mode='new_episodes'
        )
@myvcr.use_cassette()
def test_api():
    id = 162
    response = requests.get(f"https://xkcd.com/{id}/info.0.json")
    assert "test" in response.json()['safe_title']

test_api()