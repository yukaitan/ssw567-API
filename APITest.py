#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:53:16 2020

@author: yukai
"""
from unittest.mock import Mock, patch
import unittest
from unittest import mock
from API import main
from API import get_jason_name
from API import get_repo_name
import json




# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


# Standard library imports...

# Third-party imports...
from nose.tools import  assert_list_equal

# Local imports...



class TestAPI(unittest.TestCase):

    @patch('requests.get')
    def test_get_repo_name(self, mock_get):

        with open('json_name.json') as f:

            json_name = json.load(f)

        # with open('jason_times.txt') as g:

        #     json_times = g
            
        # Configure the mock to return a response with an OK status code.
        #mock_get.return_value.ok = True

        mock_get.return_value.json.return_value = json_name
        # Call the service, which will send a request to the server.
        
        
        response = get_repo_name(json_name)
        # If the request is sent successfully, then I expect a response to be returned.
        
        assert_list_equal(response, ['hellogitworld', 'helloworld', 'Mocks', 'Project1', 'threads-of-life'])

    
    @patch('requests.get')
    def test_get_repo_times(self, mock_get):

        with open('json_times.json') as f:

            json_times = json.load(f)

        # with open('jason_times.txt') as g:

        #     json_times = g
            
        # Configure the mock to return a response with an OK status code.
        #mock_get.return_value.ok = True

        mock_get.return_value.json.return_value = json_times
        # Call the service, which will send a request to the server.
        
        

        response = len(json_times)
        # If the request is sent successfully, then I expect a response to be returned.
        
        assert_list_equal([response], [1])

    
    

if __name__ == '__main__':
    unittest.main()        
    
        
    

# if __name__ == '__main__':
#     print('Running unit tests')
#     unittest.main()