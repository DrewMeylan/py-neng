import os
from pathlib import Path
from dotenv import load_dotenv
from nornir import InitNornir

# Load and population the env variables
load_dotenv()

#Set Path
NORNIR_CONFIG_FILE = f'{Path(__file__).parent.parent} /config.yaml'
  #>> Path not defined?

#Nornir Init Func
def nrinit():
    # Initialization
    nr = InitNornir(config_file=NORNIR_CONFIG_FILE)
    #Set username and password
    nr.inventory.defaults.username = os.getenv("DEVICE_USERNAME")
    nr.inventory.defaults.password = os.getenv("DEVICE_PASSWORD")
    
    return nr