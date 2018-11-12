from flask import Flask, jsonify, request
import datetime
app = Flask(__name__)

@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    pat_info = {
    "patient_id": "1", # usually this would be the patient MRN
    "attending_email": "suyash.kumar@duke.edu",
    "user_age": 50, # in years
    }
    return jsonify(pat_info)

@app.route("/api/heart_rate", methods=["POST"])
def heart_rate():
    pat_hr = {
    "patient_id": "1", # usually this would be the patient MRN
    "heart_rate": 100
    }
    t_stamp = datetime.datetime.now()
    return jsonify(pat_hr)

@app.route("/api/status/patient", methods=["GET"])
def tachycardia(t_stamp):
    r = request.get_json()
    age = r["user_age"]
    hr = r["heart_rate"]
    if age >= 1 & age <=2:
        if hr > 151:
            state = 'tachycardia'
        else:
            state = 'no tachycardia'

    if age >= 3 & age <=4:
        if hr > 137:
            state = 'tachycardia'
        else:
            state = 'no tachycardia'

    if age >=5 & age <=7:
        if hr > 133:
            state = 'tachycardia'
        else:
            state = 'no tachycardia'

    if age >= 8 & age <=11:
        if hr > 130:
            state = 'tachycardia'
        else:
            state = 'no tachycardia'

    if age >= 12 & age <=15:
        if hr > 119:
            state = 'tachycardia'
        else:
            state = 'no tachycardia'

    if age > 15:
        if hr > 100:
            state = 'tachycardia'
        else:
            state = 'no tachycardia'


    return(state)
    return(t_stamp)

@app.route("/api/heart_rate/<patient_id>", methods={"GET"})
def prev_hr():
    s = request.get_json()
    pre_hr = s["heart_rate"]
    return(pre_hr)

@app.route("/api/heart_rate/average/<patient_id>", methods=["GET"])
def average_hr(pre_hr):
    av_hr = mean(pre_hr)
    return(av_hr)

@app.route("/api/heart_rate/interval_average", methods=["POST"])
def int_av():
    time_av = {
    "patient_id": "1",
    "heart_rate_average_since": "2018-03-09 11:00:36.372339"
    }
    return jsonify(time_av)

if __name__ == "__main__":
     app.run(host = "127.0.0.1")