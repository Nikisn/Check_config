# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 18:08:15 2020

@author: stipl
"""
#/usr/bin/env python
from datetime import datetime
from netmiko import ConnectHandler
import yaml
      
       


with open ("hosts.yaml") as f:
       devices_port = yaml.load(f)
       print(devices_port)


print (f'''Возможные взаимодействия с сетевым узлом:
        1-->отправка конфигурационного файла
        2-->отправка команды
        ''')

while True:
       action = (input('Введите цифру из списка действий\n'))
       
       if  action.isdigit() and (1 <= int(action) <= 2 ):
              print(f'ОДОБРЕНО')
              break
       else:
              print(f'ОТКЛОНЕНО введите число от 1 до 3')
    
                           
       
if action == '2':
       command = input('введите команду-->Например: show ip ro\n')

elif action == '3':
       list_command = input('введите список команд-->Например: show int\n') 
         
    
while True:
       user = input ('Введите имя пользователя\n')
       password = input ('Введите пароль\n')
       ip = input ('Введите IP-адрес\n')
       if user and password and ip:
              print('Данные введены!')
              break
       else:
              print('Введите запрашиваемую информацию!')            
           
       
       
for name, port  in devices_port.items():
       print(f'Подключаюсь к устройству {name}')
       if action == '1':
              path = input('введите путь до конфигурационного файла-->Например: r1.txt\n')
           
       device_params = {
                            'device_type': 'cisco_ios',
                            'ip': ip,
                            'port': port,
                            'username': user,
                            'password': password,
                            'session_log': "output.txt"
                            } 
       output = ' '
       start_time = datetime.now()
       with ConnectHandler(**device_params, ) as ssh:
              if action == '1':
                     ssh.send_config_from_file(path, cmd_verify=False)
                     output = ssh.send_command('show running-config')
                     print(output)
                     print (f'конфирурация была загружена {name}')
                     print ('*' * 40)
              
              elif action == '2':
                     output = ssh.send_command(command)
                     print (output)
                         
                  
                      
       
       
       
       
       
           


        
        
        