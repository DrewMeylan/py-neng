from netmiko import ConnectHandler

with open('device.txt') as routers:
    for IP in routers:
        router = {
                'device_type': 'cisco_ios',
                'ip': IP,
                'username': 'UNAME',
                'password': 'PASSWORD'
        }

        net_connect = ConnectHandler(**router)

        hostname = net_connect.send_command('show run | i host')
        hostname.split(" ")
        hostname, device = hostname.split(" ")
        print("Backing up " + device + "...")

        filename = '$HOME/backups/network_devices/' + device + '.txt'
        
        showrun = net_connect.send_command('show run')
        showvlan = net_connect.send_command('show vlan')
        showver = net_connect.send_command('show ver')
        log_file = open(filename, "a")
        log_file.write(showrun + "\n")
        log_file.write(showvlan + "\n")
        log_file.write(showver + "\n")

net_connect.disconnect()
        
