import requests

def call_status():
    my_dict = {"user_age": 50, "heart_rate": 120}
    r = requests.get("http://127.0.0.1:5000/api/status/patient", json=my_dict)
    answer = r.text
    print(answer)


if __name__ == "__main__":
    call_status()
