from flask import Flask, jsonify, request
import datetime
app = Flask(__name__)


@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    new_pat_list = [{
     "patient_id": "1",  # usually this would be the patient MRN
     "attending_email": "cen17@duke.edu",
     "user_age": 50,  # in years
    }]
    return jsonify(new_pat_list)


@app.route("/api/heart_rate", methods=["POST"])
def heart_rate():
    pat_hr_list = [{
     "patient_id": "1",  # usually this would be the patient MRN
     "heart_rate": 100,
     "time_stamp": datetime.datetime.now()
    }]
    pat_hr_list.append({
     "patient_id": "1",  # usually this would be the patient MRN
     "heart_rate": 80,
     "time_stamp": datetime.datetime.now()
    })
    return jsonify(pat_hr_list)


@app.route("/api/status/patient", methods=["GET"])
def tachycardia():
    r = request.get_json()
    age = r["user_age"]
    hr = r["heart_rate"]
    if age >= 1 & age <= 2:
        if hr > 151:
            state = 'tachycardia'
        else:
            state = 'no tachycardia'
        return state

    if age >= 3 & age <= 4:
        if hr > 137:
            state = 'tachycardia'
        else:
            state = 'no tachycardia'
        return state

    if age >= 5 & age <= 7:
        if hr > 133:
            state = 'tachycardia'
        else:
            state = 'no tachycardia'
        return state

    if age >= 8 & age <= 11:
        if hr > 130:
            state = 'tachycardia'
        else:
            state = 'no tachycardia'
        return state

    if age >= 12 & age <= 15:
        if hr > 119:
            state = 'tachycardia'
        else:
            state = 'no tachycardia'
        return state

    if age > 15:
        if hr > 100:
            state = 'tachycardia'
        else:
            state = 'no tachycardia'
        return state


@app.route("/api/heart_rate/<patient_id>", methods={"GET"})
def prev_hr(patient_id):
    s = request.get_json()
    d = s["patient_id"]
    if d == patient_id:
        pre_hr = s["heart_rate"]
        return pre_hr


@app.route("/api/heart_rate/average/<patient_id>", methods=["GET"])
def average_hr(patient_id, pre_hr):
    p = request.get_json()
    d = p["patient_id"]
    if d == patient_id:
        av_hr = mean(pre_hr)
        return av_hr


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def int_av(t_stamp):
    time_av = {
     "patient_id": "1",
     "heart_rate_average_since": t_stamp[-1]
    }
    return jsonify(time_av)


if __name__ == "__main__":
    app.run(host="127.0.0.1")
