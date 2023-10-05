import netmiko 

class managedDevice:
    def __init__(self, hostname, vendor, devtype, devmodel, management_IP):
        self.hostname = hostname
        self.vendor = vendor
        self.type = devtype
        self.model = devmodel
        self.management_IP = management_IP


'''
    def show(self):
        print('Name:', self.name, "\nManagement IP:", self.management_IP)
'''     
