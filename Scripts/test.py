import sys
import socket
import re

args = sys.argv
ip_pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')
'''
def sysargs(func):
    def sysarg_query(*args) -> list:
        'This is a sysarg_query docstring'
        func(*args)
    return sysarg_query 
'''
def query(some_fucking_list):
    dns_results = {}
    for host in some_fucking_list:
        try:
            response = str(socket.gethostbyname_ex(host))
            ip = re.findall(ip_pattern, response)
            dns_results[host] = ip
        except:
            dns_results[host] = "Null"
    return dns_results


if __name__ == '__main__':
    print(query([args]))