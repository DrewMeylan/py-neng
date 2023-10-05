from netmiko import ConnectHandler

class IterRegistry(type):
    def __iter_(cls):
        return iter(cls._registry)


class managedDevice:
    def __init__(self, hostname, vendor, devtype, devmodel, management_IP):
        self.hostname = hostname
        self.vendor = vendor
        self.type = devtype
        self.model = devmodel
        self.management_IP = management_IP
    
    def device_info(self):
        return {
            'device_type': self.vendor,
            'hostname': self.hostname,
            'username': 
            'password': 
        }

    def _str__(self):
        return {
            'device_type': self.hostname

        }

class switch(managedDevice):
    def __init__(self, hostname):
    super().__init__    
    pass

class router(managedDevice):
    pass

class endpoint(managedDevice):
    pass