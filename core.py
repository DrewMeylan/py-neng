### Importations
from netmiko import ConnectHandler
### 
CSR = {
    "device_type": "cisco_ios", 
    "ip": "sandbox-nso-1.cisco.com",
    "username":"developer",
    "password":"Services4Ever"
}
# Functions definition
def main():
    net_connect = ConnectHandler(**CSR)
    output = net_connect.send_command('show ip interface brief')
    print(output)
    net_connect.disconnect()

# Classes definition

#def main()
 #   print("Hello world")



if __name__ == "__main__":
    main()
