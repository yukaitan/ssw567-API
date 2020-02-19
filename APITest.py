#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on Tue Feb 18 15:53:16 2020

@author: yukai
"""

import unittest

from API import main

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestAPI(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testAPI1(self): 
        self.assertEqual(main('richkempinski'),['Repo: hellogitworld Number of commits:30', 'Repo: helloworld Number of commits:6', 'Repo: Mocks Number of commits:10', 'Repo: Project1 Number of commits:2', 'Repo: threads-of-life Number of commits:1'])
        

    
    def testAPI2(self): 
        self.assertEqual(main('yukaitan'),['Repo: ssw567 Number of commits:1', 'Repo: ssw810 Number of commits:1', 'Repo: TriangleTest-ssw567 Number of commits:10', 'Repo: ssw567-API Number of commits:10'])
        
    
        
    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()