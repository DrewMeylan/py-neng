from netmiko import ConnectHandler

cisco1 = {
        "device_type": "invalid",
        "host": "cisco1.lasthop.io",
        "username": "test",
        "password": "test"
        }

#net_connect = ConnectHandler(**cisco1)
#net_connect.disconnect()

with open('netmiko-device_types.txt', "a") as file:
    file.write(ConnectHandler(**cisco1))

net_connect.disconnect()
