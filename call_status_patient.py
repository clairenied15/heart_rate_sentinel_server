import requests


def call_status():
    r = requests.get("http://127.0.0.1:5000/api/status/1")
    answer = r.text
    print(answer)


if __name__ == "__main__":
    call_status()
