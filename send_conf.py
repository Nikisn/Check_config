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

       

  
while True:
       action = (input('Введите цифру из списка действий\n'))
       
       if  action.isdigit() and (1 <= int(action) <= len(action_list)):
              print(f'ОДОБРЕНО {action_list[action]}')
              break
       else:
              print(f'ОТКЛОНЕНО введите число от 1 до {len(action_list)}')


if action == '1':
       path = input('введите путь до конфигурационного файла-->Например: r1.txt\n')                        
       
elif action == '2':
       command = input('введите команду-->Например: show ip ro\n')

elif action == '3':
       list_command = input('введите список команд-->Например: show int\n')


send_dict = {
             '1':'send_config_from_file',
             '2':'send_command',
             '3':'send_config_set' 
             }
            
            


while True:
       user = input ('Введите имя пользователя\n')
       password = input ('Введите пароль\n')
       ip = input ('Введите IP-адрес\n')
       if user and password and ip:
              print('Данные введены!')
              break
       else:
              print('Введите запрашиваемую информацию!')

#start_time = datetime.now()


for name, port  in devices_port.items():
       print(f'Подключаюсь к устройству {name}')
       device_params = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'port': port,
        'username': user,
        'password': password,
        'session_log': "output.txt"
        }      
       
       with ConnectHandler(**device_params, ) as ssh:
                        
           if action == '1':
                  output = ssh.send_config_from_file(path, cmd_verify=False)
                  print (output)
           
           elif action == '2':
                  output = ssh.send_command(command)
                  print (output)
                
           elif action == '3':
                  output = ssh.send_config_set(list_command)
                  print (output)
		   


		   
		   
       


        
        
        
