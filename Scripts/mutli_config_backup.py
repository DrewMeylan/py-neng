import os
from netmiko import ConnectHandler

# Define input parameters
input_file_path = "device_ips.txt"  # Replace with the path to your .txt file containing IP addresses

# Exception handling: gracefully fail if the input file does not exist
if not os.path.exists(input_file_path):
    print(f"Error: Input file '{input_file_path}' not found.")
    exit(1)

# Read the list of IP addresses from the input file
with open(input_file_path, "r") as input_file:
    ip_addresses = input_file.read().splitlines()

# Define the common device settings
device_settings = {
    "device_type": "cisco_ios",
    "username": "your_username",  # Replace with your Cisco device username
    "password": "your_password",  # Replace with your Cisco device password
    "secret": "your_enable_secret",  # Replace with your enable secret/password
}

# Loop through each device and back up its configuration
for ip_address in ip_addresses:
    try:
        # Create a device connection object
        device = {**device_settings, "ip": ip_address}
        net_connect = ConnectHandler(**device)

        # Get the device hostname
        hostname = net_connect.send_command("show running-config | include hostname")
        hostname = hostname.strip().split(" ")[-1]

        # Backup the configuration
        output = net_connect.send_command("show running-config")
        backup_filename = f"{hostname}.txt"

        # Save the configuration to a local .txt file
        with open(backup_filename, "w") as backup_file:
            backup_file.write(output)

        print(f"Configuration backup for {hostname} ({ip_address}) saved as {backup_filename}")
        net_connect.disconnect()

    except Exception as e:
        print(f"Error backing up configuration for {ip_address}: {str(e)}")

print("Backup process completed.")

#FROM GPT; TEST AND REFACTOR