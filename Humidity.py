import math
from time import gmtime, strftime
import time
import requests
import random
import json
while True:
    data = random.randint(0, 10)
    showtime = strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    x = {"data": data, "date": showtime}
    requests.post('http://localhost:3000/api/Humidity',x)
    time.sleep(1)
