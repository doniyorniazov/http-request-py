import requests
import time
import os

host = os.getenv("HOST")
company = os.getenv("COMPANY")
sleep = os.getenv("SLEEP")

url = f"http://{host}/ERP/{company}/Status"

print(url)

while True:
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        data = response.json()

        can_shutdown = data.get("CanShutdown", False)

        if can_shutdown:
            print(f"Company {company} is ready to shut down.")
            break
        else:
            print(f"Company {company} is not ready to shut down. Retrying...")

    else:
        print(f"Request to {url} is failed!")

    time.sleep(sleep)
