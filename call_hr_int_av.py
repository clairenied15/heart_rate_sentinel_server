import requests


def call_hr_intav():
    my_dict = {"patient_id": "1", "heart_rate_average_since": "Thu, 15 Nov 2018 23:44:20 GMT"}
    r = requests.get("http://127.0.0.1:5000/api/heart_rate/interval_average", json=my_dict)
    answer = r.json()
    print(answer)


if __name__ == "__main__":
    call_hr_intav()
