import time
import requests
while(True):
    requests.get("http://0.0.0.0/api/evaluate")
    time.sleep(14400)


