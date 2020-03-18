import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who):
    greeting = "Hello, {}".format(who)
    return greeting


print(greet("World"))
print(greet("Jason"))

r = requests.get("http://www.google.com")
print("status ", r.status_code)
