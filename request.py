import requests
import time
import os
import sys

host = os.getenv("HOST")
port = os.getenv("PORT")

company = os.getenv("COMPANY")
sleep = os.getenv("SLEEP")

url = f"http://{host}:{port}/ERP/{company}/Status"

print(url)

while True:
    try:
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            data = response.json()

            can_shutdown = data.get("CanShutdown", False)

            if can_shutdown:
                print(f"Company {company} is ready to shut down.")                
                sys.exit()
            else:
                print(f"Company {company} is not ready to shut down. Retrying...")

        else:
            print(f"Request to {url} is failed!")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    time.sleep(5)
    
print("Closing the app!")
