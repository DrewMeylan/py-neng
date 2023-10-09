import os
import logging
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
backup_dir = '/home/drew/backups/network_devices/'

nr = InitNornir(config_file="../config.yaml")

def create_backups_dir():
    if not os.path.exists(backup_dir):
        os.mkdir(backup_dir)

def save_config(method, hostname, config):
    filename = f"{hostname}-{method}.cfg"
    with open(os.path.join(backup_dir, filename), "w") as f:
        f.write(config)

def get_netmiko_backups():
    backup_results = nr.run(
        task=netmiko_send_command,
        command_string="show run"
    )

    for hostname in backup_results:
        save_config(
            method="netmiko",
            hostname=hostname,
            config=backup_results[hostname][0].result,
        )

def get_napalm_backups():
    backup_results = nr.run(
        task=napalm_get,
        getters=["config"]
    )
    for hostname in backup_results:
        config = backup_results[hostname][0].result["config"]["startup"]
        save_config(method="napalm", hostname, config=config)


if __name__ == "__main__":
    create_backups_dir()
    get_netmiko_backups()
    get_napalm_backups()