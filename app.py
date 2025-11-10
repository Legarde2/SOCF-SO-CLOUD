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
    cpu = psutil.cpu_percent(percpu=True)
    memoria = psutil.virtual_memory().used // 1024 ** 2
    pid_processo = os.getpid()
    so = platform.platform()

    return json.dumps([
        {'metricas': {
            "CPU": cpu,
            "Memoria": f"{memoria} MB",
            "PID Processo": pid_processo,
            "SO": so
            }
        }
    ])