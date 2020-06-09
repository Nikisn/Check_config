# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:45:38 2020

@author: stipl
"""

import textfsm
from tabulate import tabulate 

with open('show_ip_route_ALL.template') as f, open('test.txt') as text:
      re_table = textfsm.TextFSM(f)
     # print(re_table)
      header = re_table.header
      result = re_table.ParseText(text.read())
      print(result)
      print(tabulate(result, headers=header))
      
