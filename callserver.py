import requests


def call_server():
    r = requests.post("http://127.0.0.1:5000/api/new_patient")
    answer = r.json()
    print(answer)


if __name__ == "__main__":
    call_server()
