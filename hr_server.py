from flask import Flask, jsonify, request
import datetime
app = Flask(__name__)


pat_list = []
pat_hr_list = []
c = {}
g = {}
b = []
p = []

@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    new_pat = {
     "patient_id": "1",  # usually this would be the patient MRN
     "attending_email": "cen17@duke.edu",
     "user_age": 50,  # in years
    }
    global pat_list
    pat_list.append(new_pat)
    return jsonify(new_pat)


@app.route("/api/heart_rate", methods=["POST"])
def heart_rate():
    pat_hr = {
     "patient_id": "1",  # usually this would be the patient MRN
     "heart_rate": 100,
     "time_stamp": datetime.datetime.now()
    }
    global pat_hr_list
    global c
    global g
    pat_hr_list.append(pat_hr)
    for d in pat_hr_list:
        c.setdefault(d['patient_id'], []).append(d['heart_rate'])
    global b
    b = [{'patient_id': k, 'heart_rate': v} for k, v in c.items()]
    for n in pat_hr_list:
        g.setdefault(n['patient_id'], []).append(n['time_stamp'])
    global p
    p = [{'patient_id': k, 'time_stamp': v} for k, v in g.items()]
    # hr_lst = [l['heart_rate'] for l in pat_hr_list]
    # time_list = [m['time_stamp'] for m in pat_hr_list]
    return jsonify(pat_hr)


@app.route("/api/status/<patient_id>", methods=["GET"])
def tachycardia(patient_id):
    #  for most recent/last hr!!!
    # every time have post request, see if person is tachycardic
    # r = request.get_json()
    # age = r["user_age"]
    # hr = r["heart_rate"]
    hrlist = b
    hrinfo_by_id = build_dict(hrlist, key="patient_id")
    hr_info = hrinfo_by_id.get(patient_id)
    patlist = pat_list
    patinfo_by_id = build_dict(patlist, key="patient_id")
    pt_info = patinfo_by_id.get(patient_id)
    age = pt_info['user_age']
    hr = hr_info['heart_rate']
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
    # s = requests.get("http://127.0.0.1:5000/api/heart_rate")
    # for d in s:  # does this work if its json???
      #  if d['patient_id'] == patient_id:
       #     pre_hr = d['heart_rate']
        #    return jsonify(pre_hr)
    # r = request.get_json()
        # patinfo = item[0]
    hrlist = b
    timelist = p
    hrinfo_by_id = build_dict(hrlist, key="patient_id")
    hr_info = hrinfo_by_id.get(patient_id)
    tminfo_by_id = build_dict(timelist, key="patient_id")
    tm_info = tminfo_by_id.get(patient_id)
    prev_hrs = hr_info['heart_rate']
    return jsonify(prev_hrs)


@app.route("/api/heart_rate/average/<patient_id>", methods=["GET"])
def average_hr(patient_id):
    # p = request.get_json()
    # p = requests.get("http://127.0.0.1:5000/api/heart_rate")
    # for d in p:
    #  if d['patient_id'] == patient_id:
    #     hrs = d['heart_rate']
    #    av_hr = mean(hrs)
    #   return jsonify(av_hr)
    # r = request.get_json()
    # for item in r:
        # patinfo = item[0]
    hrlist = b
    timelist = p
    hrinfo_by_id = build_dict(hrlist, key="patient_id")
    hr_info = hrinfo_by_id.get(patient_id)
    tminfo_by_id = build_dict(timelist, key="patient_id")
    tm_info = tminfo_by_id.get(patient_id)
    hrs = hr_info['heart_rate']
    hr_av = mean(hrs)
    return jsonify(hrs, hr_av)


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def int_av():
    time_av = {
     "patient_id": "1",
     "heart_rate_average_since": "Thu, 8 Nov 2018 18:05:50 GMT"
    }
    # r = request.get_json()
    # for item in r:
        # patinfo = item[0]
    hrlist = b
    timelist = p
    hrinfo_by_id = build_dict(hrlist, key="patient_id")
    hr_info = hrinfo_by_id.get(time_av["patient_id"])
    tminfo_by_id = build_dict(timelist, key="patient_id")
    tm_info = tminfo_by_id.get(time_av["patient_id"])
    # r = requests.get("http://127.0.0.1:5000/api/heart_rate")  # can do get request in POST???
    strp_tm_info = datetime.datetime.strptime(tm_info['time_stamp'], '%a, %d %b %Y %H:%M:%S %Z')
    strp_since_tm = datetime.datetime.strptime(time_av['heart_rate_average_since'], '%a, %b %d %H:%M:%S %Y')
    indices = [i for i, v in enumerate(strp_tm_info >= strp_since_tm) if v]
    hr_since_time = hr_info['heart_rate'][indices]
    hr_time_av = mean(hr_since_time)
        # if dict['patient_id'] == time_av['patient_id']:
        #  j = [i for i in d['time_stamp'] if i >= time_av['heart_rate_average_since']]
        # indices = [i for i, v in enumerate(d['time_stamp'] >= time_av['heart_rate_average_since']) if v]
        #  num = len(j)
        # hr_since_time = d['heart_rate'][indices]
    return jsonify(time_av, hr_since_time, hr_time_av)


def build_dict(seq, key):
    return dict((d[key], dict(d, index=index)) for (index, d) in enumerate(seq))


if __name__ == "__main__":
    app.run(host="127.0.0.1")
