from hr_server import calculate_tach


def test_tach():
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
    r = calculate_tach(datastore, patient_id)
    assert r == "no tachycardia"
