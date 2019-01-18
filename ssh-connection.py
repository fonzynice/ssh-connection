from netmiko import *

cisco = {'device_type': 'cisco_ios',
          'ip': '172.16.43.145',
          'username': 'admin',
          'password': 'admin',
          'secret': 'admin'

         }


connect = ConnectHandler(**cisco)
connect.enable()
output = connect.send_command('show ip int brief')
print(output)
# config = connect.send_config_set(config_commands='int fa0/0\n'
#                                                 'no ip add dhcp\n'
#                                                 'ip add 192.168.10.3 255.255.255.0\n'
#                                                 'no sh\n'
#                                                 'do wr\n'
#                                                 )
#
# new_output = connect.send_command('sh ip int brief')
# print(config, '\n',
#      new_output)

#    OR

# config = ['int fa0/0\n',
#           'ip add 10.10.10.6 255.255.255.0\n',
#           'no sh\n',
#           'do wr\n']
# console = connect.send_config_set(config)
#
# new_output = connect.send_command('sh ip int brief')
# print(console, '\n',
#       new_output)


