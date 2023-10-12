from netmiko import ConnectHandler

with open('devices.txt') as routers:
    for IP in routers:
        router = {
                'device_type': 'cisco_ios',
                'ip': IP,
                'username': 'roger',
                'password': 'cisco'
        }

        net_connect = ConnectHandler(**router)
        hostname = net_connect.send_command('sh run | i host')
        hostname.split(" ")
        hostname, device = hostname.split(" ")
        print("Backing up " + device + "...")

        filename = '/home/drew/backups/network_devices/' + device + '.txt'
        
        showrun = net_connect.send_command('show run')
        showvlan = net_connect.send_command('show vlan')
        showver = net_connect.send_command('show ver')
        with open(filename, "a") as log_file:
            log_file.write(showrun + "\n")
            log_file.write(showvlan + "\n")
            log_file.write(showver + "\n")

net_connect.disconnect()
        
