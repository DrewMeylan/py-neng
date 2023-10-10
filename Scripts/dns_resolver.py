from nornir import InitNornir
import socket
import re

'''
Query DNS func
!! Maybe recode to take in different types of input?
'''
def query_dns(hostpath) -> dict:
    ''' Takes in hosts file and outputs a dict with each hostname and corresponding IP'''
    dns_results = {} 
    with open(hostpath) as hosts:
        for host in hosts:
            try:
                response = socket.gethostbyname_ex(host)
                ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', str(response))
                dns_results[host] = ip
            except:
                dns_results[host] = "Null"
    return dns_results

'''
Compare DNS func
'''

#@query_dns
#def compare_dns() -> dict:
#    ''' Takes dict of hostname:IP and compares against NetBox'''

if __name__ == "__main__":
    query_dns()