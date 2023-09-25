## SSH to multiple devices from devices file
from netmiko import ConnectHandler

with open('devices.txt') as routers:
    for IP in routers:
        router = {
                'device_type': 'cisco_ios'
                'ip': IP,
                'username': 'test'
                'password': 'test'
                }

        net_connect = ConnectHandler(**router)

        print('Connecting to ' + IP)
        print('-'*79)
        output = net_connect.send_command('sh ip int brief')
        print(output)
        print()
        print('-'*79)

net_connect.disconnect()

