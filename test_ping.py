from netmiko import ConnectHandler
from textfsm import clitable
import yaml

with open ("hosts.yaml") as f:
       ping_src = yaml.load(f)
       
              

ping_dst = {
            'r1':'ping 1.1.1.1 -c 4',
            'r2':'ping 2.2.2.2 -c 4',
            'r3':'ping 3.3.3.3 -c 4',
            'r4':'ping 4.4.4.4 -c 4',
            'r5':'ping 5.5.5.5 -c 4',
            'r6':'ping 6.6.6.6 -c 4',
            'r7':'ping 7.7.7.7 -c 4'
            }



from_ping = input('Введите ОТ какого хоста слать ICMP-пакеты (r1,r2...)\n')
to_ping = input('Введите ДО какого хоста слать ICMP-пакеты (r1,r2...)\n')






cli_table = clitable.CliTable('index', 'TextFSM_templates')



attributes = {'Command':ping_dst[to_ping], 'Vendor': 'Cisco'}


device_params = {
    'device_type': 'linux',
    'ip': '127.0.0.1',
    'port': ping_src[from_ping],
    'username': 'sysadmin',
    'password': '123'}

with ConnectHandler(**device_params) as ssh:
       ping = ssh.send_command(ping_dst[to_ping])


cli_table.ParseCmd(ping,attributes)

data_rows = [list(row) for row in cli_table]


if data_rows[0][0] == '4' and  data_rows[0][1] == '0':
       print(f'PING ОТ {from_ping} ДО {to_ping} УСПЕШНО!')
       print('РЕЗУЛЬТАТ:\n', cli_table.FormattedTable())
else:
       print(f'ОТ {from_ping} ДО {to_ping} ОТСУТСТВИЕ ОТВЕТА!')
       print('РЕЗУЛЬТАТ:\n', cli_table.FormattedTable())

































#cfg_file='r1.txt'
#command = ['hostname R1','interface enp0s8','ip address 22.1.3.1/24', 'ip ospf message-digest-key 1 md5 123']
#user = 'sysadmin'
#password = '123'
#enable_pass = '123'
#ip = '127.0.0.1'
#
#devices_port = {'r1':2222,'r2':2200,'r3':2201,'r4':2202,'r5':2203,'r6':2204,
#                'r7':2205,
#                }
#
#
#print('connection to device')
#device_params = {
#    'device_type': 'linux',
#    'ip': ip,
#    'port': 2201,
#     'username': user,
#     'password': password}
#
#"подключение и снятие команды"
#   
#with ConnectHandler(**device_params) as ssh:
#       ping = ssh.send_command('ping 2.2.2.2 -c 4')
#       
#       with open ('test.txt', 'w') as dest:
#              for line in ping:
#                 t = dest.write(line)
#                 print(type(t))
#
#"работа с файлом пинга"
#
#a = ''
#with open ('test.txt', 'r') as src:
#       for line in src:
#              if line.startswith('4'):
#                     
#                     send, rec, loss, _ = line.split(',')
#  
#                  
#print(f'''
#      Отправлено: {send}
#      Доставлено: {rec}
#      Потери: {loss}''')
#         
#
#
#"""
#ssh.enable() f"{name}.txt
#'session_log': "output.txt"
#                      
#"""        