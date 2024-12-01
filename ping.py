import os
from logger import log_action  

def ping(host):
  
    resource = os.system(f"ping -c 1 {host}")
    
    # Determine if the host is reachable
    if resource == 0:
        result = f"{host} is reachable."
        print(result)
        log_action("Ping successful", result, "info")
    else:
        result = f"{host} not reachable."
        print(result)
        log_action("Ping failed", result, "error")

