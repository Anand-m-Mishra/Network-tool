import requests
from logger import log_action
def checkWeb(url):
    try:
        # Send a GET request
        response = requests.get(url , timeout=10)
        # If the GET request is successful, the status code will be 200
        if response.status_code ==200:
            result = f"{url} is working good"
            print(result)
        else:
            result = f"{url} is not working. status_code:{response.status_code}"
            print(result)
        log_action("Uptime Check", result,"info")
    except requests.exceptions.RequestException as e:
        result = f"An error occurred: {e}"
        print(result)
        log_action("Uptime Check", result,"error")


