import requests

server = "http://127.0.0.1:5000"

# this is in_json
patient_1 = {"room_no": 10,
             "name": "Penelope North",
             "patient_mrn": 101,
             }
r = requests.post(server + "/upload_info", json=patient_1)
print(r.status_code)
print(r.text)

r2 = requests.get(server + "/room_numbers")
print(r2.status_code)
print(r2.text)

r3 = requests.get(server+"/latest_patient_info/1")
print(r3.status_code)
print(r3.text) 