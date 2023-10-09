from helper import nrinit
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
form norinr_utils.plugins.tasks.files import write_file

nr = nrinit()

BACKUP_PATH = "./data/configs"

def backup_config(task, path):
    device_confg = task.run(task=napalm_get, getters=["config"])

    task.run(
        task=write_file,
        content=device_confg.result["config"]["running"],
        filename=f"{path}/{task.host}.txt",
    )

result = nr.run(
    name="Backup device configurations", path=BACKUP_PATH, task=backup_config
)

print_result(result, vars=["stdout"])