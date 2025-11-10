from flask import Flask

import platform
import os
import psutil
import json

# Uso de CPU por núcleo
print(psutil.cpu_percent(percpu=True))

# Memória
print(psutil.virtual_memory().used // 1024 ** 2, "MB")

# PID do processo
print(os.getpid())

# SO
print(platform.platform())

APP = Flask(__name__)

@APP.get("/info")
def info():
    return json.dumps([
        {'integrantes': [
                'Gustavo Lisboa',
                'Vinicius'
            ]
        }
    ])

@APP.get("/metrica")
def metrica():
    cpu_usage_per_core = psutil.cpu_percent(percpu=True)
    memory_used_mb = psutil.virtual_memory().used // 1024 ** 2
    process_id = os.getpid()
    operating_system = platform.platform()

    return json.dumps([
        {'metricas': {
            "cpu_usage_per_core": cpu_usage_per_core,
            "memory_used": f"{memory_used_mb} MB",
            "process_id": process_id,
            "operating_system": operating_system
            }
        }
    ])