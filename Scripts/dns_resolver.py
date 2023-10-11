#from nornir import InitNornir
from re import re.compile, re.findall
from socket import gethostbyname_ex as gethost
import sys

'''
Pattern def and sifter standalone func
'''
ip_pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')

def sifter(pattern):  ## Takes in a string and generates a function to serve as a regex filter to match the passed string
    ''' Sifter function takes in a regex pattern and returns filter_text function  '''
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
def sysargs(func): ### Take in sysargs and pass them directly to the decorated query function as a list
    def sysarg_query(*args) -> list:
        '''Sysarg_query takes in system arguments as a list and passes this list to the decorated query function'''
        func(*args) ## sys.argv is of type list; can be passed straight through to decorated query function
    return sysarg_query # Returns function, not a list?

def filepath(func, sift_string:str=None):  ## Take in the query function and a sifter, which can be used to filter the 
    def file_query(filepath:str) -> list:
        hostlist = []
        with open(filepath) as hosts:
            for host in hosts:
                hostlist.append(str(host).rstrip())
            
            if sift_string:
                inner_filter = sifter(sift_string)
                filtered_hosts = inner_filter(" ".join(hostlist))
                func(filtered_hosts)
            else:
                func(hostlist)
    return file_query


'''
Query Function --> Construct dictionary from hostname list to compare against netbox
'''
def query(host:list) -> dict:
    ''' Takes in a list of hostnames outputs a dict with each hostname and corresponding IP'''
    dns_results = {} 
    with open(*args) as hosts:  ### Export file context management to decorator
        for host in hosts:
            host = host.rstrip()  ## rstrip should become redundant with decorators
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

def main():
    if len(sys.argv >= 1):
        args = sys.argv
        sysarg_query(sys.argv)
        pass
    if 

if __name__ == "__main__":
    main()
    exit(1)
