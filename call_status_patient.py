import requests

def call_status():
    r = requests.get("http://127.0.0.1:5000/api/status/patient")
    answer = r.json()
    print(r)


if __name__ == "__main__":
    call_status()
