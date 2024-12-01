import logging

logging.basicConfig(filename='network_monitor.log',
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s')

def log_action(action,result):
    logging.info(f"{action}-{result}")