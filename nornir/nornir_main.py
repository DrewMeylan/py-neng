from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get

nr = InitNornir(
        runner={
            "plugin": "threaded",
            "options": {
                "num_workers": 20,
                },
            },
        inventory={
            "plugin": "SimpleInventory",
            "options": {
                "host_file": "/home/kidscripto/Git/py-neng/nornir/inventory/hosts.yaml"
                },
            },
        )

results = nr.run(task=napalm_get, getters=["facts"])
print_result(results)

