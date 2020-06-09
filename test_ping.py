rom netmiko import ConnectHandler


cfg_file='r1.txt'
command = ['hostname R1','interface enp0s8','ip address 22.1.3.1/24', 'ip ospf message-digest-key 1 md5 123']
user = 'sysadmin'
password = '123'
enable_pass = '123'
ip = '127.0.0.1'

devices_port = {'r1':2222,'r2':2200,'r3':2201,'r4':2202,'r5':2203,'r6':2204,
                'r7':2205,
                }


print('connection to device')
device_params = {
    'device_type': 'linux',
    'ip': ip,
    'port': 2201,
     'username': user,
     'password': password}

"подключение и снятие команды"
   
with ConnectHandler(**device_params) as ssh:
       ping = ssh.send_command('ping 2.2.2.2 -c 4')
       
       with open ('test.txt', 'w') as dest:
              for line in ping:
                 t = dest.write(line)
                 print(type(t))

"работа с файлом пинга"

a = ''
with open ('test.txt', 'r') as src:
       for line in src:
              if line.startswith('4'):
                     
                     send, rec, loss, _ = line.split(',')
  
                  
print(f'''
      Отправлено: {send}
      Доставлено: {rec}
      Потери: {loss}''')
         


"""
ssh.enable() f"{name}.txt
'session_log': "output.txt"
                      
"""        