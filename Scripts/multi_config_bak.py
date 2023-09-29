from netmiko import ConnectHandler

with open('devices.txt') as routers:
    for IP in routers:
        Router = {
                'device_type': 'cisco_ios',
                'ip': IP,
                'username': 'roger',
                'password': 'cisco'
                }

        net_connect = ConnectHandler(**Router)
        hostname = net_connect.send_command('show run | include host')
        hostname.split(" ")
        hostname,device = hostname.split(" ")
        print("Backing up " + deivce)

        filename = "$HOME/Git/py-neng/backups/" + device + ".txt"

        showrun = net_connect.send_command("show run")
        showlvan = net_connect.send_command("show vlan")
        showver = net_connect.send_command("show ver")
        logfile = open(filename, "a")
        logfile.write(showrun)
        logfile.write("\n")
        logfile.write(showvlan)
        logfile.write("\n")
        logfile.write(showver)
        logfile.write("\n")

        net_connect.disconnect()
