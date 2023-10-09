import time
import requests
while(True):
    requests.get("http://0.0.0.0/api/syncweek")
    time.sleep(604800)
