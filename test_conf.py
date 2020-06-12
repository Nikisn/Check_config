# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:45:38 2020

@author: stipl
"""
#/usr/bin/env python


from textfsm import clitable
from netmiko import ConnectHandler
import yaml


with open ("hosts.yaml") as f:
       src = yaml.load(f)






cli_table = clitable.CliTable('index', 'TextFSM_templates') 




print ('''
       варианты тестирования:
       - проверка соседей OSPF  - show ip ospf neighbor
       - проверка работы RIP    - show ip rip status 
       - проверка соседей IS-IS - show isis neighbor
       - проверка маршрутов IS-IS     - show isis topology
       - запрос различных таблиц маршрутизации - show ip route
       ''')
       
command = input ('введите команду для тестирования\n')

       
attributes = {'Command': command, 'Vendor': 'Cisco'}

while True:
      user = input ('Введите имя пользователя\n')
      password = input ('Введите пароль\n')
      port = input ('Введите устройство тестирования (r1,r2,r3...)\n')
      if user and password and port:
             print('Данные введены!')
             break
      else:
             print('Введите запрашиваемую информацию!')  
       

       
device_params = {
                 'device_type': 'cisco_ios',
                 'ip': '127.0.0.1',
                 'port': src[port],
                 'username': user,
                 'password': password,
                 'session_log': "output.txt"
                            }      
def send_command (device_params, command):
       with ConnectHandler(**device_params, ) as ssh:
              out = ssh.send_command(command)
       return out


outg = send_command(device_params, command)        
                  
if command == 'show ip ospf neighbor':
       cli_table.ParseCmd(outg, attributes)
       print('CLI Table output:\n', cli_table)
       print('*' * 70)
       data_rows = [str(row[0]) for row in cli_table]
       if not data_rows:
            print ('OSPF-cоседей не обнаружено! ')    
       elif data_rows == ['1.1.1.1', '2.2.2.2']:
              print ('Если проверяется R3, то настройки корректны')
       elif data_rows == ['2.2.2.2', '3.3.3.3']:
              print ('Если проверяется R1, то настройки корректны')
       elif data_rows == ['1.1.1.1', '3.3.3.3']:
              print ('Если проверяется R3, то настройки корректны')     
       else: 
              print (f'Обнаружен следующий список соседей {data_rows}') 


elif command == 'show ip rip status':
      cli_table.ParseCmd(outg, attributes)
      print('Formatted Table:\n', cli_table.FormattedTable())
      print('*' * 70) 


elif command == 'show isis neighbor':
      cli_table.ParseCmd(outg, attributes)
      print('Formatted Table:\n', cli_table.FormattedTable())
      print('*' * 70) 
       

elif command == 'show isis topology':
      cli_table.ParseCmd(outg, attributes)
      data_rows = [str(row[0]) for row in cli_table]
      if not data_rows:
             print('IS-IS соединений не обнаружено')
      elif '4.4.4.4' in data_rows and port == '2222':
             print('Для R1 установлено IS-IS соседство с R4')
             print(cli_table.FormattedTable())
      elif '1.1.1.1' in data_rows and port == '2202':
             print('Для R4 установлено IS-IS соседство с R1')
             print(cli_table.FormattedTable())
      else:
            print('Заданы некорректные настрйойки смотри таблицу')
            print('Formatted Table:\n', cli_table.FormattedTable())
            print('*' * 70) 



elif command == 'show ip route':
      cli_table.ParseCmd(outg, attributes)
      print('Formatted Table:\n', cli_table.FormattedTable())
      print('*' * 70)
      
elif command == 'show ip route ospf':
      cli_table.ParseCmd(outg, attributes)
      print('Formatted Table:\n', cli_table.FormattedTable())
      print('*' * 70)

elif command == 'show ip route rip':
      cli_table.ParseCmd(outg, attributes)
      print('Formatted Table:\n', cli_table.FormattedTable())
      print('*' * 70)


elif command == 'show ip route bgp':
      cli_table.ParseCmd(outg, attributes)
      print('Formatted Table:\n', cli_table.FormattedTable())
      print('*' * 70)

elif command == 'show ip route connected':
      cli_table.ParseCmd(outg, attributes)
      print('Formatted Table:\n', cli_table.FormattedTable())
      print('*' * 70)
      
           

else:
       print(f'''КОМАНДА НЕ ВХОДИТ В ТЕСТИРОВАНИЕ, ВЫВОД:
             
             {outg}''')
                         
                  



