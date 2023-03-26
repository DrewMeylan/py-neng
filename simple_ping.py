import subprocess

def ping_ip(ipAddr):
    reply = subprocess.run(['ping', '-c', '3', '-n', ipAddr],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
    
    if reply.returncode == 0:
        print(True)
    else:
        print(False)


## TEST
#ping_ip('8.8.8.8')  