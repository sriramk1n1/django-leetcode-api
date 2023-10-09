import time
import requests
while(True):
    requests.get("http://0.0.0.0/api/sync")
    time.sleep(86400)
