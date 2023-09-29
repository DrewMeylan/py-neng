from netmiko import ConnectHandler

# Device Object
CSR = {
  'device_type': 'cisco_ios',
  'ip': '127.0.0.1',
  'username': 'roger',
  'password': 'cisco'
}

# Establish connection
net_connect = ConnectHandler(**CSR)

# Sending Commands
output = net_connect.send_command('sh ip int brief')
print(output)

# Closing Connection
net_connect.disconnect()

