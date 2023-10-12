#from nornir import InitNornir
from re import re.compile, re.findall
from socket import gethostbyname_ex as gethost
import sys

'''
Pattern def and standalone functions
'''
ip_pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')

def read_hosts_file(file_path):
    with open(file_path, 'r') as file:
        hostnames = [line.strip() for line in file]
    return hostnames

def sifter(pattern):  ## Takes in a string and generates a function to serve as a regex filter to match the passed stringclear
    ''' Sifter function takes in a regex pattern and returns filter_text function. '''
    try:
        regex = re.compile(pattern)
        def filter_text(text):
            return regex.findall(text)
        return filter_text
    except Exception as error:
        print(f'Error parsing string: {error}')
        return None

'''
Decorators for extensibility: handle different inputs types to construct list for Query function
'''
def sysargs(func):  ## Should be good to go
  ''' This is a decorator function that is meant to read in system arguments and pass them off to an arbitrary function.
    The point of this to be able to modify the means by which the decorated function receives input. 
  '''
    def sysarg_query(*args, **kwargs):
        # Get command line arguments (excluding the script name)
        cmd_args = sys.argv[1:]
        # Pass the command line arguments to the wrapped function
        return func(cmd_args)
    return sysarg_query

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

'''
Query Function --> Construct dictionary from hostname list to compare against netbox
'''

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


'''
Compare Function --> Checks dictionary values against netbox and returns an array: [Hostname], [DNS VAL], [Netbox VAL], [Bool ( 1 = Diff ) ]
'''
#@query_dns
#def compare_dns() -> dict:
#    ''' Takes dict of hostname:IP and compares against NetBox'''

'''

'''
