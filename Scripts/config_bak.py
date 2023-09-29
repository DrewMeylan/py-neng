from netmiko import ConnectHandler

# Device Object
CSR = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.220',
    'username': 'roger',
    'password': 'cisco'
    }

net_connect = ConnectHandler(**CSR)

hostname = net_connect.send_command('show run | include host')
hostname.split(" ")
hostname, device = hostname.split()
print("Backing up " + device)

filename = "$HOME/Git/py-neng/backups/" + device + ".txt"

showrun = net_connect.send_command("show run")
showvlan = net_connect.send_command("show vlan")
showver = net_connect.send_command("show ver")
log_file = open(filename, "a") # append mode
log_file.write(showrun)
logfile.write("\n")
logfile.write(showvlan)
logfile.write("\n")
logfile.write(showver)
logifle.write("\n")

net_connect.disconnect()