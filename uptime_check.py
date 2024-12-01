import requests
def checkWeb(url):
    try:
        # Send a GET request
        response = requests.get(url , timeout=10);
        # If the GET request is successful, the status code will be 200
        if response.status_code ==200:
            print(f"{url} is working good");
        else:
            print(f"{url} is not working. status_code:{response.status_code}");
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}");


