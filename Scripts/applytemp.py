import paramiko
import time

def apply_config(hostname, username, password, template_file):
    # Read the template configuration
    with open(template_file, 'r') as f:
        config_lines = f.readlines()

    # Initialize SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the device
        ssh.connect(hostname, username=username, password=password, timeout=10)
        print("Connected to", hostname)

        # Start an interactive shell
        shell = ssh.invoke_shell()

        # Wait for the prompt
        while not shell.recv_ready():
            time.sleep(1)

        # Send configuration commands line by line
        for line in config_lines:
            shell.send(line.strip() + '\n')
            time.sleep(0.5)  # Adjust delay as needed

        # Wait for commands to be executed
        time.sleep(2)

        # Capture output (optional)
        output = shell.recv(65535).decode('utf-8')
        print(output)

        print("Configuration applied successfully.")

    except paramiko.AuthenticationException:
        print("Authentication failed.")
    except paramiko.SSHException as ssh_exc:
        print("SSH error:", ssh_exc)
    except Exception as exc:
        print("Error:", exc)
    finally:
        # Close SSH connection
        ssh.close()

if __name__ == "__main__":
    hostname = input("Enter the hostname or IP address of the Cisco IOS device: ")
    username = input("Enter your SSH username: ")
    password = input("Enter your SSH password: ")
    template_file = input("Enter the path to the template configuration file: ")

    apply_config(hostname, username, password, template_file)

