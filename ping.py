import os
from logger import log_action 

def ping(host):
    #use a variable to store the result of ping command
    resource = os.system(f"ping -c 1 {host}")
    #if the result is 0, it means the host is up
    if resource == 0:
        result = f"{host} is reachable."
        print(result)
    else:
        result = f"{host} not reachable"
        print(result)
    log_action("ping",result)
