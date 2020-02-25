#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:20:33 2020

@author: yukai
"""

import requests
import json

def get_jason_name(name):
    r = requests.get('https://api.github.com/users/' + name + '/repos')
    s = json.dumps(r.json())
    s1 = json.loads(s)

    return s1


def get_repo_name(jason_name):
    
    
    #print (s['name'])
    s1 = jason_name
    name_list = []
    
    for i in s1:
        name_list.append(i["name"])
    
    #print(s1[0]["name"])
    return (name_list)

def get_jason_times(name, repo_name):

    r = requests.get('https://api.github.com/repos/' + name + '/' + repo_name + '/commits')
    #print('https://api.github.com/repos/' + name + '/' + repo_name + '/commits')
    s = json.dumps(r.json())
    s1 = json.loads(s)

    return s1

def get_number(name, i): 
    
    s1 = get_jason_times(name, i)
    
    return len(s1)




def main(name):
  
    jason1 = get_jason_name(name)
    repo_list = get_repo_name(jason1)
     
    repo_number = []
    for i in repo_list:
        repo_number.append(get_number(name, i))

    result = []
    tem = ""
    
    for i in range(len(repo_list)):
        tem = "Repo: " + str(repo_list[i]) +  " Number of commits:"  + str(repo_number[i])
        result.append(tem)
    
    print(result) 
    
    

if __name__ == "__main__":
    
    name = input("Please enter an name to check")
    main(name)
        
    




