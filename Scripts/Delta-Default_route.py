# Script to check if the default route has changed on Gateway Routers
import os
from datetime import datetime
from netmiko import ConnectHandler

# Define input parameters
input_file_path = "router_ips.txt"  # Replace with the path to your .txt file containing IP addresses

# Exception handling: gracefully fail if the input file does not exist
if not os.path.exists(input_file_path):
    print(f"Error: Input file '{input_file_path}' not found.")
    exit(1)

# Define the common device settings
device_settings = {
    "device_type": "cisco_ios",
    "username": "your_username",  # Replace with your Cisco device username
    "password": "your_password",  # Replace with your Cisco device password
}

# Loop through each router IP address and check the default route
with open(input_file_path, "r") as input_file:
    router_ips = input_file.read().splitlines()

for ip_address in router_ips:
    try:
        # Create a device connection object
        device = {**device_settings, "ip": ip_address}
        net_connect = ConnectHandler(**device)

        # Send the "show ip route | include ^S" command to check the default route
        output = net_connect.send_command("show ip route | include ^S")

        # Parse the output to find the default route change date
        lines = output.strip().splitlines()
        if len(lines) > 0:
            last_change_line = lines[0]
            last_change_parts = last_change_line.split()
            last_change_date = " ".join(last_change_parts[1:4])
            print(f"Router {ip_address}: Last default route change: {last_change_date}")
        else:
            print(f"Router {ip_address}: Default route not found.")

        net_connect.disconnect()

    except Exception as e:
        print(f"Error connecting to {ip_address}: {str(e)}")

print("Script completed.")

# FROM CHATGPT; TEST AND REFACTOR