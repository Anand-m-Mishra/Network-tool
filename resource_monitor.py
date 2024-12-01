import psutil
from logger import log_action 
#import ping from ping
#import Uptime_check 

def networkCheck():
    # Get the current network I/O statistics
    net_io = psutil.net_io_counters(); #returns a object with attributes like byte_send and recv

    result = f"Number of bytes sent:{net_io.bytes_sent} and Number of bytes recievced:{net_io.bytes_recv}"
    print(result)

    log_action("networkCheck",result)


