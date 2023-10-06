from netmiko import ConnectHandler
import json
import psycopg2
from cryptography.fernet import Fernet

'''
Meta-class definitions
'''
class IterRegistry(type):
    def __iter_(cls):
        return iter(cls._registry)



'''
Parent Class Definition
'''
class managedDevice:
    @staticmethod
    def credGen():
        password = Fernet.generate_key()
        public_key
        
        export_credentials(password, key)
        
        return password.decode('utf-8'), key_pair.decode('utf-8')

    def __init__(self, hostname, vendor, management_IP, username, password):
        self.hostname = hostname
        self.deviceVendor = vendor
        self.managementIP = management_IP
        self.username = username
        self.password = password

        ## credGen module to generate new credentials
        self.username = 



    def device_info(self):
        return {
            'device_type': self.vendor,
            'hostname': self.hostname,
            'username': 
            'password': 
        }

    def __str__(self):
        return {
            'device_type': self.hostname

        }

''' 
Sub-class Definitions
'''

class switch(managedDevice):
    def __init__(self, hostname):
    super().__init__    
    pass

class router(managedDevice):
    pass

class firewall(managedDevice):
    pass

class endpoint(managedDevice):
    pass