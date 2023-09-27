import netmiko 

class managedDevice:
    def __init__(self,hostname,management_IP):
        self.name = hostname
        self.management_IP = management_IP
        self.macAddress
        self.firmwareVersion
        self.iosVersion
        self.vlanDatabase
        self.interfaceStatus
        self.neighbors
        self.type
        self.logBuffer
        self.lastBackup

    def show(self):
        print('Name:', self.name, "\nManagement IP:", self.management_IP)
        
