from netmiko import ConnectHandler
import getpass

username = input("Enter username: ")
passwd = getpass.getpass("\nEnter password: ")

def backup_devices(hostfile, filter=None):
    username = input("Enter username: ")
    passwd = getpass.getpass("\nEnter Password: ")

    with open(hostfile, "r") as routers:
        for IP in routers:
            router = {
                    'device_type': 'cisco_ios',
                    'ip': IP,
                    'username': username,
                    'password': passwd
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
        
