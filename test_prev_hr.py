from hr_server import calc_prev_hr


def test_pre_hr():
    time1 = "Thu, 8 Nov 2018 23:44:20 GMT"
    time2 = "Thu, 15 Nov 2018 23:44:20 GMT"
    time3 = "Thu, 15 Nov 2018 23:55:20 GMT"
    datastore = [{'patient_id': "2",
                  'attending_email': "test@test.com",
                  'age': 52,
                  'heart_rates': [80, 76, 77],
                  'heart_rate_times': [time1, time2, time3]},
                 {'patient_id': "3", 'attending_email': "test@test.com",
                  'age': 42,
                  'heart_rates': [80, 76, 77],
                  'heart_rate_times': [time1, time2, time3]}]
    patient_id = "2"
    r = calc_prev_hr(datastore, patient_id)
    assert r == [80, 76, 77]
