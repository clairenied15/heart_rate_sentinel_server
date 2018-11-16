import requests


def call_server_hr():
    r = requests.post("http://127.0.0.1:5000/api/heart_rate")
    answer = r.json()
    print(answer)


if __name__ == "__main__":
    call_server_hr()
