from netmiko import ConnectHandler
from getpass import getpass

username = input('Username: ')
password = getpass() ##?

CSR = {
        "device_type": 'cisco_ios',
        "ip": "192.168.1.220",
        "password": password,
        "username": username
        }

net_connect = ConnectHandler(**CSR)

print('-'*79)
print('Saving Config...')
print('-'*79)

# This doesn't actually save the config; it just dumps it
# Re-write to open file at a given path and write the config information to the file
output = net_connect.save_config()
print(output)


print('-'*79)
print("Saved Config!")
print('-'*79)


