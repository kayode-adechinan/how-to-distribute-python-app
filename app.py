import requests

import os

x = requests.get("https://w3schools.com/python/demopage.htm")

print(x.text)


print(os.system("ls"))
