# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:45:39 2020

@author: stipl
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 18:08:15 2020

@author: stipl
"""
from netmiko import ConnectHandler
#from datetime import datetime для расчета времени прохождения




devices_port = {'r1':2222,'r2':2200}

       


              
action_list = {
              '1':'отправка конфигурационного файла', 
              '2':'отправка команды',
              '3':'отправка списка команд'
              }
          

print (f'''Возможные действия при конфигурации сетевого узла:
        1-->{action_list['1']}
        2-->{action_list['2']}
        3-->{action_list['3']}
        ''')

       


        
        
        
