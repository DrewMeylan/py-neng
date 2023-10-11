#from nornir import InitNornir
from re import re.compile, re.findall
from socket import gethostbyname_ex as gethost
import sys

'''
Pattern def and sifters
'''
ip_pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')

'''
Decorators for extensibility: handle different inputs types to construct list for Query function
'''
def sysargs(func):
    def sysarg_query(*args, *kwargs, sys.argv):
        func(sys.argv) ## sys.argv is of type list; can be passed straight through to decorated query function
    return sysarg_query

def filepath(func, sifter=None):  ## Take in the query function and a sifter, which can be used to filter the 
    def file_query(*args, **kwargs, filepath):
        hostlist = []
        with open(filepath) as hosts:
            for host in hosts:
                hostlist.append(str(host).rstrip())
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
        sysarg_query(sys.argv)
        pass
    if 

if __name__ == "__main__":
    main()
    exit(1)
