import requests
import time
import os
import sys

host = os.getenv("HOST")
port = os.getenv("PORT") #Defaul 8002
company = os.getenv("COMPANY")
sleep = os.getenv("SLEEP")

url = f"http://{host}:{port}/ERP/{company}/Status"

print(f"Request USR:: {url}")

while True:
    try:
        response = requests.get(url)
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")

        if response.status_code == 200:
            data = response.json()

            can_shutdown = data.get("CanShutdown", False)

            if can_shutdown:
                print(f"Company {company} is ready to shut down.")                                
                break
                sys.exit(0)
            else:
                print(f"Company {company} is not ready to shut down. Retrying...")

        else:
            print(f"Request to {url} is failed!")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

    time.sleep(5)
    
print("Status check completed!")
sys.exit(0)