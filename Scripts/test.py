import re
import socket


file_path = "hosts.txt"
ip_pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')

def read_hosts_file(file_path):
    with open(file_path, 'r') as file:
        hostnames = [line.strip() for line in file]
    return hostnames

def hostname_filter_decorator(hosts_file, filter_pattern=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Read hostnames from the file
            hostnames = read_hosts_file(hosts_file)

            # Apply filtering if a filter pattern is provided
            if filter_pattern:
                filtered_hostnames = [host for host in hostnames if re.search(filter_pattern, host)]
            else:
                filtered_hostnames = hostnames

            # Pass the filtered hostnames to the decorated function
            return func(*args, filtered_hostnames, **kwargs)

        return wrapper
    return decorator

# Example usage:
@hostname_filter_decorator('hosts.txt', filter_pattern=) # Find way to pass command line arguement or argparse arguement to filter_pattern 
def query(args): ## Works with sysargs decorator
    dns_results = {}
    for host in args:
        try:
            response = str(socket.gethostbyname_ex(host))
            ip = re.findall(ip_pattern, response)
            dns_results[host] = ip
        except:
            dns_results[host] = "Null"
    return dns_results

if __name__ == "__main__":
    print(query())
