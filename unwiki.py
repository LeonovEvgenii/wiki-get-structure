#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:05:25 2019

@author: dan
"""

import re 
c = 'лингви́стика'[6]

def unwiki(keywords):
    for word in keywords:
        yield re.sub(c, '', word)
        
if __name__ == '__main__':
    print(list(unwiki(['лингви́стика', 'языкозна́ние', 'языкове́дение'])))
    