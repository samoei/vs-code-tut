import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = f"Hello {who_to_greet}"
    return greeting


print(greet("Phil"))
print(greet("Samoei"))
r = requests.get("http://www.samphiltech.com/")
print(r.status_code)
