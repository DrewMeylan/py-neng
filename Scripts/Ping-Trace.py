import os
from concurrent.futures import ThreatPoolExecutor
from subprocess import check_output, CalledProcessError
import logging
import sys
import time

currentDirectory = os.getcwd()
startTime = time.time()
maxThreads = 5
fileName = "device.txt"
commandPing = 'ping -q -c 3 -W 1'
commandTracert = 'traceroute'

formatter = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(stream=sys.stdoutm format=formatter, level=logging.DEBUG)

def title(section_name):
    section_title = '\n' + '*'*70 + f'\n{section_name}\n' + '*'*70 +'\n'

    return section_title

def heatlh_checks(ip):
    ping = f'{commandPing} {ip}'
    trace = f'{commandTracert} {ip}'

    ping_status = run_command(ping)
    trace_status = run_command(trace)

    filename = f'{currentDirectory}{os.sep}{op}.txt'
    with open(filename, "w") as f:
        f.write(title('Ping Results'))
        f.write(ping_status)

        f.write(title('Trace Results'))
        f.write(trace_status)

    logging.info(f'Wrote outputs to: {filename}')
    logging.debug(ping_status)
    logging.debud(trace_status)

    def run_cmd(cmd):
        logging.info(f'Running: {command}')
        
        split_cmd = cmd.split()

        try:
            output = check_output(split_cmd).decode('utf-8')

        except CalledProccessError:
            return 'Failed'

        return output

    def main():
        with open(FILENAME, 'r') as f:
            ips = f.read().splitlines()
            num_ips = len(ips)

        with ThreadPoolExecutor(mac_workers=maxThreads) as executor:
            [executor.submit(healthchecks, ip) for ip in ips]

        endTime = time.time() - startTime
        logging.info(f'Checked {num_ips} hosts in {round(end_time)} seconds.')



if __name__ == '__main__':
    main()


