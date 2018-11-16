from flask import Flask, jsonify, request
import datetime
import sendgrid
import os
from sendgrid.helpers.mail import *
app = Flask(__name__)


datastore = []


@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    """  Posts new patient data to the server in the form of a dictionary
    Args:
        None

    Returns:
        new_pat: a dictionary with the patient_id, attending_email,
        and user_age
    """
    new_pat = {
     "patient_id": "1",  # usually this would be the patient MRN
     "attending_email": "cen17@duke.edu",
     "user_age": 1,  # in years
    }
    global datastore
    datastore.append({
            'patient_id': new_pat['patient_id'],
            'age': new_pat['user_age'],
            'heart_rates': [],
            'heart_rate_times': [],
            'attending_email': new_pat['attending_email']
    })
    print(datastore)
    return jsonify(new_pat)


@app.route("/api/heart_rate", methods=["POST"])
def heart_rate():
    """ Posts heart rate info for a specific patient and
    the time that heart rate was recorded
    Args:
        None

    Returns:
         pat_hr: a dictionary with patient_id, heart_rate,
         and time_stamp of that heart rate
    """
    pat_hr = {
     "patient_id": "1",  # usually this would be the patient MRN
     "heart_rate": 160,
     "time_stamp": datetime.datetime.now()
    }
    global datastore
    for item in datastore:
        if item["patient_id"] == pat_hr["patient_id"]:
            item["heart_rates"].append(pat_hr["heart_rate"])
            item["heart_rate_times"].append(pat_hr["time_stamp"])
            print(datastore)
            return jsonify(pat_hr)


@app.route("/api/status/<patient_id>", methods=["GET"])
def tachycardia(patient_id):
    """ GET request of whether a specified patient is tachycardic
    or not based on their age and most recent heart rate
    Args:
        patient_id: string patient id value for a patient of interest

    Returns:
        answer: string telling whether the specific patient is tachycardic
        or not based on their last heart rate measure
    """
    global datastore
    answer = calculate_tach(datastore, patient_id)
    return answer


def calculate_tach(datastore, patient_id):
    """ Calculates whether or not a specific patient is tachycardic
    or not based on their age and most recent heart rate
    Args:
        datastore: list of dictionaries containing the patient_id, age,
        attending_email, heart_rates list, and heart_rate_times list
        patient_id: string of the id for the patient of interest

    Returns:
        state: string stating whether or not the specified patient is
        tachycardic
    """
    for item in datastore:
        if item["patient_id"] == patient_id:
            age = item["age"]
            hr = item["heart_rates"]
            email = item["attending_email"]
            if age >= 1 and age <= 2:
                if hr[-1] > 151:
                    state = 'tachycardia'
                    # sg = sendgrid.SendGridAPIClient(
                    # apikey=os.environ.get(''))
                    # from_email = Email("claireniederriter@ymail.com")
                    # to_email = Email("cen17@duke.edu")
                    # subject = "Tachycardia"
                    # content = Content("text/plain",
                    # "and easy to do anywhere, even with Python")
                    # mail = Mail(from_email, subject, to_email, content)
                    # response = sg.client.mail.send.post(
                    # request_body=mail.get())
                    # print(response.status_code)
                    # print(response.body)
                    # print(response.headers)
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
    """ GET request of all of the previous heart rate measurements
    for the patient with the corresponding patient id
    Args:
        patient_id: string patient id value for a patient of interest

    Returns:
        prev_hrs: list of all the previous heart rate measurements
        for a specific patient

    """
    global datastore
    answer = calc_prev_hr(datastore, patient_id)
    return jsonify(answer)


def calc_prev_hr(datastore, patient_id):
    """ Finds all of the previous heart rate measurements
    for the patient with the corresponding patient id
    Args:
        datastore: list of dictionaries containing the patient_id,
        age, attending_email, heart_rates list, and heart_rate_times list
        patient_id: string of the id for the patient of interest

    Returns:
        prev_hrs: list of all of the previous heart rate
        values for the specified patient
    """
    for item in datastore:
        if item["patient_id"] == patient_id:
            prev_hrs = item["heart_rates"]
            return prev_hrs


@app.route("/api/heart_rate/average/<patient_id>", methods=["GET"])
def average_hr(patient_id):
    """ GET request of the average heart rate of a specific
    patient for all their heart rate measurements
    Args:
        patient_id: string patient id value for a patient of interest

    Returns:
        answer: float of the average heart rate for all
        heart rate measurements for a specific patient

    """
    global datastore
    answer = calc_av_hr(datastore, patient_id)
    return jsonify(answer)


def calc_av_hr(datastore, patient_id):
    """ Finds the average heart rate of a specific
    patient for all their hert rate measurements
    Args:
        datastore: list of dictionaries containing the patient_id,
        age, attending_email, heart_rates list, and heart_rate_times list
        patient_id: string of the id for the patient of interest

    Returns:
        hr_av: float of the average heart rate for all
        heart rate measurements for a specific patient

    """
    for item in datastore:
        if item["patient_id"] == patient_id:
            hrs = item["heart_rates"]
            hr_av = sum(hrs)/len(hrs)
            return hr_av


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def int_av():
    """ Finds the average heart rate for a specific patient after a specified time
    Args:
        None

    Returns:
        hr_time_av: float of the average heart rate
        after a time specified in the input dictionary time_av
    """
    time_av = {
     "patient_id": "1",
     "heart_rate_average_since": "Thu, 8 Nov 2018 23:44:20 GMT"
    }
    global datastore
    for item in datastore:
        if item["patient_id"] == time_av["patient_id"]:
            strp_since_tm = datetime.datetime.strptime(
                time_av['heart_rate_average_since'], '%a, %b %d %H:%M:%S %Y')
            strp_hr_tm = datetime.datetime.strptime(
                item['heart_rate_times'], '%a, %b %d %H:%M:%S %Y')
            # indices = [i for i, v in enumerate(item["heart_rate_times"]
            # >= time_av["heart_rate_average_since"]) if v]
            indices = [n for n, i in enumerate(strp_hr_tm) if
                       i >= strp_since_tm]
            hr_since_time = item['heart_rates'][indices]
            hr_time_av = sum(hr_since_time)/len(hr_since_time)
            return jsonify(hr_time_av)


if __name__ == "__main__":
    app.run(host="127.0.0.1")
