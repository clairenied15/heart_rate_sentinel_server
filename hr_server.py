from flask import Flask, jsonify, request
import datetime
app = Flask(__name__)


datastore = []

@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    new_pat = {
     "patient_id": "1",  # usually this would be the patient MRN
     "attending_email": "cen17@duke.edu",
     "user_age": 50,  # in years
    }
    global datastore
    datastore.append({
            'patient_id': new_pat['patient_id'],
            'age': new_pat['user_age'],
            'heart_rates': [],
            'heart_rate_times': [],
            'attending email': new_pat['attending_email']
    })
    print(datastore)
    return jsonify(new_pat)


@app.route("/api/heart_rate", methods=["POST"])
def heart_rate():
    pat_hr = {
     "patient_id": "1",  # usually this would be the patient MRN
     "heart_rate": 100,
     "time_stamp": datetime.datetime.now()
    }
    global datastore
    for item in datastore:
        if item["patient_id"] == pat_hr["patient_id"]:
            item["heart_rates"].append(pat_hr["heart_rate"])
            item["heart_rate_times"].append(pat_hr["time_stamp"])
    # datastore[pat_hr["patient_id"]]["heart_rates"].append(pat_hr["heart_rate"])
    # datastore[pat_hr["patient_id"]]["heart_rate_times"].append(pat_hr["time_stamp"])
    # hr_lst = [l['heart_rate'] for l in pat_hr_list]
    # time_list = [m['time_stamp'] for m in pat_hr_list]
            return jsonify(pat_hr)


@app.route("/api/status/<patient_id>", methods=["GET"])
def tachycardia(patient_id):
    global datastore
    for item in datastore:
        if item["patient_id"] == patient_id:
            age = item["age"]
            hr = item["heart_rates"]
            if age >= 1 and age <= 2:
                if hr[-1] > 151:
                    state = 'tachycardia'
                else:
                    state = 'no tachycardia'
                return state

            if age >= 3 and age <= 4:
                if hr[-1] > 137:
                    state = 'tachycardia'
                else:
                    state = 'no tachycardia'
                return state

            if age >= 5 and age <= 7:
                if hr[-1] > 133:
                    state = 'tachycardia'
                else:
                    state = 'no tachycardia'
                return state

            if age >= 8 and age <= 11:
                if hr[-1] > 130:
                    state = 'tachycardia'
                else:
                    state = 'no tachycardia'
                return state

            if age >= 12 and age <= 15:
                if hr[-1] > 119:
                    state = 'tachycardia'
                else:
                    state = 'no tachycardia'
                return state

            if age > 15:
                if hr[-1] > 100:
                    state = 'tachycardia'
                else:
                    state = 'no tachycardia'
                return state


@app.route("/api/heart_rate/<patient_id>", methods={"GET"})
def prev_hr(patient_id):
    global datastore
    for item in datastore:
        if item["patient_id"] == patient_id:
            prev_hrs = item["heart_rates"]
            return jsonify(prev_hrs)


@app.route("/api/heart_rate/average/<patient_id>", methods=["GET"])
def average_hr(patient_id):
    global datastore
    for item in datastore:
        if item["patient_id"] == patient_id:
            hrs = item["heart_rates"]
            hr_av = mean(hrs)
            return jsonify(hr_av)


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def int_av():
    time_av = {
     "patient_id": "1",
     "heart_rate_average_since": "Thu, 8 Nov 2018 18:05:50 GMT"
    }
    global datastore
    for item in datastore:
        if item["patient_id"] == time_av["patient_id"]:
            strp_since_tm = datetime.datetime.strptime(time_av['heart_rate_average_since'], '%a, %b %d %H:%M:%S %Y')
            indices = [i for i, v in enumerate(item["heart_rate_times"] >= strp_since_tm) if v]
            hr_since_time = item['heart_rates'][indices]
            hr_time_av = mean(hr_since_time)
            return jsonify(time_av, hr_since_time, hr_time_av)


if __name__ == "__main__":
    app.run(host="127.0.0.1")
