from netmiko import connectHandler

def pushTemplate(devicefile, template):
    with open(devicefile) as devices:
        for IP in devices:
            device = {
                "device_type": "cisco_ios",
                "ip": IP,
                "username": "roger",
                "password": "cisco"
            }
            target = ConnectHandler(**device)
            hostname = target.send_command("show run | i host").split(" ")
            hostname.split(" ")
            hostname, device = hostname.split(" ")
            with open(template) as temp:
                for line in temp.split("\n"):
                    target.send_command(line)
