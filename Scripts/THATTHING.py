import pynetbox
import socket
from dns.resolver import query
from dns.exception import DNSException
import logging

# Initialize the logging configuration
log_file = 'cross_check.log'
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the Python-NetBox API client
api_url = "http://netbox-url/api/"
api_token = "your-api-token"
nb = pynetbox.api(url=api_url, token=api_token)

# Define the DNS server to query
dns_server = "your-dns-server"

# Query NetBox to retrieve a list of devices (modify filters as needed)
devices = nb.dcim.devices.filter()

# Function to perform DNS query and cross-check
def cross_check_dns(device):
    hostname = device.name
    try:
        # Query DNS to retrieve the IP address associated with the hostname
        answer = query(hostname, dns_server)
        for rdata in answer:
            ip_address = rdata.address
            # Compare the DNS IP address with the primary IP address from NetBox
            if device.primary_ip4 and device.primary_ip4.address == ip_address:
                log_message = f"Match: {hostname} - NetBox IP: {ip_address}"
                logging.info(log_message)
            else:
                log_message = f"Mismatch: {hostname} - NetBox IP: {device.primary_ip4.address}, DNS IP: {ip_address}"
                logging.warning(log_message)
    except DNSException as e:
        log_message = f"DNS Error: {hostname} - {str(e)}"
        logging.error(log_message)
    except socket.gaierror as e:
        log_message = f"Socket Error: {hostname} - {str(e)}"
        logging.error(log_message)

# Iterate through devices and cross-check with DNS
for device in devices:
    cross_check_dns(device)
