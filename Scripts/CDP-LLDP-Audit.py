from netmiko import ConnectHandler

with open('devices.txt') as devices:
    for IP in devices:
        device = {
            "device_type": "cisco_ios",
            "ip": IP,
            "username": "roger",
            "password": "cisco"
        }

        with ConnectHandler(**device) as target:
            hostname = target.send_command("show run | i host").split(" ")
            cdp_neighbors = target.send_command("show cdp neighbors")
            lldp_neighbors = target.send_command("show lldp neighbors")
            ## Parse strings to convert to dict object?
            filname = f"/home/drew/mapper/neighborships/{hostname}.txt"
            with open(filname, "a") as log_file:
                log_file.write(cdp_neighbors + "\n")
                log_file.write(lldp_neighbors + "\n")
        target.disconnect()

## Test!
## Retool inputs so username, passwrd are not statically coded?