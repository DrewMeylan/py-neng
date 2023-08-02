from netmiko import ConnectHandler

with open('devices.txt') as routers:
    for IP in routers:
        for IP in routers:
            Router = {
                    'device_type': 'cisco_ios',
                    'ip': IP,
                    'username': 'roger',
                    'password': 'cisco',
                    }
            net_connect = ConnectHandler(**Router)

            print('Connecting to ' + IP)
            print('-'*79)
            output = net_connect.send_command('show ip interface brief')
            print(output)
            print()
            print('-'*79)
            
            net_connect.disconnect()

            
