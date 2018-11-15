import requests

def call_hr_id():
    # my_dict = {"patient_id": '1', "heart_rate": [80, 95, 99, 87], "time_stamp": ['Thu, 8 Nov 2018 18:05:50 GMT', 'Thu, 8 Nov 2018 18:19:50 GMT', 'Thu, 15 Nov 2018 13:19:50 GMT', 'Thu, 15 Nov 2018 18:19:50 GMT']}
    r = requests.get("http://127.0.0.1:5000/api/heart_rate/1")
    answer = r.json()
    print(answer)


if __name__ == "__main__":
    call_hr_id()