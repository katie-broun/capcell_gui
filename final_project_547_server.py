from datetime import datetime
from flask import Flask, request, jsonify
from pymodm import connect, MongoModel, fields
from pymodm import errors as pymodm_errors
from server_database import Patient
import requests

app = Flask(__name__)


@app.route("/room_numbers", methods=['GET'])
def get_room_numbers():
    message, status_code = room_numbers_driver()
    return message, status_code


def room_numbers_driver():
    room_numbers = []
    for value in Patient.objects.raw({}):
        room_numbers.append(value.room_no)
    return room_numbers, 200

# need to create methods to test this and if there
# are errors, then we can go from there

# get patient info route?? confused as to what this will do
# compared to that of latest_patient_info 


@app.route("/latest_patient_info/<room_number>", methods=['GET'])
def get_new_info(room_number):
    message, status_code = latest_info_driver(room_number)
    return message, status_code


def latest_info_driver(room_no):
    patients = Patient.objects.all()
    patient_room_key = None # initilize value
    primary_keys = [patient.pk for patient in patients]
    for value in primary_keys:
        if value == int(room_no): 
            patient_room_key = value
            break
    print(patient_room_key)
    setup = patient_room_key
    message = 'This function is running ' + str(setup)
    status_code = 200
    # search where room no is equal to the primary key to find
    # the exact patient?
    # get all data in form of json
    # extract data
    # return message and status code
    return message, status_code


@app.route("/latest_cpap_info/<room_number>", methods=['GET'])
def get_latest_cpap_data(room_no):
    message, status_code = latest_cpap_driver(room_no)
    return message, status_code


def latest_cpap_driver(room_no):
    # search for primary keys to find room_no of interest
    # get cpap data in form of json
    # extract data and place onto gui 
    # return message and status code 
    return 


@app.route("/latest_cpap_timestamps/<room_number>", methods=['GET'])
def get_latest_cpap_timestamp(room_no):
    message, status_code = latest_cpap_time(room_no)
    return message, status_code


def latest_cpap_time(room_no):
    # search for primary keys to find room_no of interest
    # get all cpap timestamps for this room as list 
    # return as list to display on gui 
    # return message and status code sent with thi
    return


@app.route("/cpap_image/<room_number>/<time_stamp>", methods=['GET'])
def get_cpap_image(room_no, time_stamp):
    message, status_code = cpap_image_driver(room_no, time_stamp)
    return message, status_code


def cpap_image_driver(room_no, time_stamp):
    # retrieve room no from set of primary keys 
    # match time stamp to time stamp within time stamps list
    # return and display image 
    # return message and status code 
    return


def init_server():
    connect("mongodb+srv://kgb40:BMEoptics2028@cluster0.ibr62cw.mongodb.net/"
            "patient_data?retryWrites=true&w=majority&appName=Cluster0")

    # x = Patient(room_no = 10)
    # x.save()


if __name__ == "__main__":
    init_server()
    app.run()