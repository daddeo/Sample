import sys
import requests

print(sys.version)
print(sys.executable)

r = requests.get("http://www.google.com")
print("status ", r.status_code)
print("ok     ", r.ok)
