import requests


def call_hr_id():
    r = requests.get("http://127.0.0.1:5000/api/heart_rate/1")
    answer = r.json()
    print(answer)


if __name__ == "__main__":
    call_hr_id()
