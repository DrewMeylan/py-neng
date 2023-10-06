#! /usr/bin/env python3
import argparse
from netmiko import ConnectHandler

## Argument Definitions w/ Argparse
parser = argparse.ArgumentParser(description="Get Hostname")
parser.add_argument('-n', '--hostname', required=True, type=str)
parser.add_argument('-i', '--ip', required=False, type=str) #False if DNS resolution is possible
parser.add_argument('-t', '--template', required=True, type=str)
parser.add_argument('-v', '--vlan(s)', required=True, type=str)
parser.add_argument('-t', '--type', required=True, default='cisco_ios', type=str)  
args = parser.parse_args()

## Define Used vs Unusued Templates
used_template = [
    'swtichport mode access',
    f'switchport access vlan {arg2}',
    'switchport nonegotiate',
    'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

unused_template = [
    'switchport mode access',  #Manually define access mode
    f'switchport access vlan {SOMETHING}', #Move to unusued vlan
    'switchport nonegotiate', #Disable DTP
    'shut' #Shutdown interface
]

def applyTemplate(ip, interface, template, vlans):
    device_info = {
        'device_type': f'{type}',
        'host': f'{hostname}.{domain}',
        'username': f'{username}',
        'password': f'{password}',
            }
    net_connect = ConnectHandler(**device_info)

    #Connect to interface and apply template
    net_connect.send_command(f"interface {interface}")
    for cmd in template:
        net_connect.send_command(cmd)
        
## Push template config def to target(s)
print('\n'.join(access_template).format(5))






'''
IF NAME == MAIN
'''

if __name__ == '__main__':.
# Define device information from provided paramters
device_info {
    "device_type": f"{type}",
    "ip": f"{ip}",
    "username": f"{username}",
    "password": f"{password}"
}
# Define create device object; this part seems redundant
device = {**device_info}

# Create connectHandler object
net_connect = ConnectHandler(**device)

# Using net_connect object, send commands to device




