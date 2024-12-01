import os

def ping(host):
    #use a variable to store the result of ping command
    resource = os.system(f"ping -c 1 {host}");
    #if the result is 0, it means the host is up
    if resource ==0;
    print(f"{host} reachable");
    else
    print(f"{host} not reachable");
    log_action("ping",result)
