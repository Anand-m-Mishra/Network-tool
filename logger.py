import logging
import os

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/network_monitor.log",  # Log file path
    level=logging.INFO,                  
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log message format
    filemode="a"                        
)

# Create a console handler to show logs in the terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# Add console handler to the root logger
logging.getLogger().addHandler(console_handler)

def log_action(action, result, level="info"):
  
    message = f"{action} - {result}"
    
    if level.lower() == "info":
        logging.info(message)
    elif level.lower() == "error":
        logging.error(message)
    elif level.lower() == "debug":
        logging.debug(message)
    elif level.lower() == "warning":
        logging.warning(message)
    elif level.lower() == "critical":
        logging.critical(message)
    else:
        logging.info(message)  
