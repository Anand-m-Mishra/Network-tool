import psutil

def networkCheck():
    # Get the current network I/O statistics
    net_io = psutil.net_io_counter(); #returns a object with attributes like byte_send and recv

    print(f"Number of bytes sent:{net_io.bytes_sent} and Number of bytes recievced:{net_io.bytes_recv}");


