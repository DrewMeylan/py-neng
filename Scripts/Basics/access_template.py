#! /usr/bin/env python3
## sys args 
from sys import argv
import argparse
from netmiko import ConnectHandler

ip = argv[1]
interface = argv[2]
template = argv[3]
vlans = argv[4]

## Argument Definitions using ArgParse?
parser = argparse.ArgumentParser(description="Get Hostname")
parser.add_argument('-n', '--hostname', required=True, type=str)
parser.add_argument('-i', '--ip', required=False, type=str) #False if DNS resolution is possible
parser.add_argument('-t', '--template', required=True, type=str)
parser.add_argument('-v', '--vlan(s)', required=True, type=str)
parser.add_argument('-t', '--type', required=True, default='cisco_ios', type=str)  
args = parser.parse_args()

'''
device_settings {
    "device_type": "cisco_ios",
    "ip"
}
device = {**deivce}
'''

## Access Template template definition
###Class permutations? IDK
use = [
    'swtichport mode access',
    f'switchport access vlan {arg2}',
    'switchport nonegotiate',
    'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

unuse = [
    'switchport mode access',  #Manually define access mode
    f'switchport access vlan {SOMETHING}', #Move to unusued vlan
    'switchport nonegotiate', #Disable DTP
    'shut' #Shutdown interface
]

net_connect = ConnectHandler(**ip)

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


#if __name__ == '__main__':

