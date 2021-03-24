from flask import Flask, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

'''
from datetime import time
import firebase_admin
import requests
from firebase_admin import credentials
from firebase_admin import firestore
import flask
from flask import request, jsonify, Flask, render_template
# initialize firebase application
#firebase_admin.initialize_app()
cred = credentials.Certificate('testing-bf5a4-firebase-adminsdk-k3wvf-9481825d20.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://testing-bf5a4.firebaseio.com/'
})
db = firestore.client()
'''

cred = credentials.Certificate('testing-bf5a4-firebase-adminsdk-k3wvf-9481825d20.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://testing-bf5a4.firebaseio.com/'
})
db = firestore.client()

app = Flask(__name__)


# GET requests will be blocked
# GET requests will be blocked
@app.route('/')
def hello():
    return 'Hello There'


@app.route('/profile-example', methods=['POST'])
def profile_example():
    request_data = request.get_json()

    city = None
    email = None
    name = None
    user_name = None
    addressal_name = None
    mobile = None
    gender = None
    dob = None
    nationality = None
    dob_month = None
    dob_year = None

    if request_data:
        if 'city' in request_data:
            city = request_data['city']

        if 'email' in request_data:
            email = request_data['email']

        if 'dob' in request_data:
            dob = request_data['dob']
            dob_year = dob[0:4]
            dob_month = dob[5:7]

        if 'mobile' in request_data:
            mobile = request_data['mobile']

        if 'gender' in request_data:
            gender = request_data['gender']

        if 'nationality' in request_data:
            nationality = request_data['nationality']

        if 'name' in request_data:
            name = request_data['name']
    
    
    value = { 'Name':name, 'User_name':user_name, 'Addressal_name' : addressal_name, 'City' : city, 'Email' : email, 'Mobile' : mobile, 'Date_of_birth' : dob,
             'Birth_month' : dob_month,'Birth_year' : dob_year,'Gender' : gender}
    
    doc_ref = db.collection(u'Profile').document()
    ldoc_id = docref.set(value)
    
    data = '''
            Name: {}
            User_name: {}
            Addressal_name: {}
            City: {}
            Email: {}
            Mobile: {}
            Date_of_birth: {}
            Birth_month: {}
            Birth_year: {}
            Gender: {}
            Document_id: {}'''.format(name, user_name, addressal_name, city, email, mobile, dob, dob_month, dob_year, gender, ldoc_id)

    return str(data)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.0', port=8080, debug=True)
