import psutil
from logger import log_action 
#import ping from ping
#import Uptime_check 

def networkCheck():
    net_io = psutil.net_io_counters(); 

    result = f"Number of bytes sent:{net_io.bytes_sent} and Number of bytes recievced:{net_io.bytes_recv}"
    print(result)

    log_action("network check completed",result,"info")


