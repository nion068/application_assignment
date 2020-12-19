from django.conf import settings
import requests, uuid, time
from django.core.files.storage import FileSystemStorage

def authenticate(username, password):
    # Authenticate username and password using specified API
    url = settings.AUTH_API
    header = {
        'Content-Type': 'application/json'
    }
    
    payload = {
        "username": username,
        "password": password
    }

    try:
        response = requests.post(url=url, json=payload, headers=header)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None
    # print(response.json())

def submit_details(auth_token, name, email, phone, full_address, name_of_university, graduation_year, cgpa, experience_in_months, current_work_place_name, applying_in, expected_salary, field_buzz_reference, github_project_url):
    # Submit the details given by the applicant to the specified api
    token = "Token {token}".format(token=auth_token)
    #generate uuid for details and cv_file
    uuid_details = str(uuid.uuid4())
    uuid_cv_file = str(uuid.uuid4())
    creation_time = str(int(time.time() * 1000))
    url = settings.INFO_SUBMIT_API_TEST
    # url = settings.INFO_SUBMIT_API_FINAL
    header = {
        "Content-Type": "application/json",
        "Authorization": token
    }

    payload = {
        "tsync_id": uuid_details,
        "name": name,
        "email": email,
        "phone": phone,
        "full_address": full_address,
        "name_of_university": name_of_university,
        "graduation_year": graduation_year,
        "cgpa": cgpa,
        "experience_in_months": experience_in_months,
        "current_work_place_name": current_work_place_name,
        "applying_in": applying_in,
        "expected_salary": expected_salary,
        "field_buzz_reference": field_buzz_reference,
        "github_project_url": github_project_url,
        "cv_file": {
            "tsync_id": uuid_cv_file
        },
        "on_spot_creation_time": creation_time
    }

    try:
        response = requests.post(url=url, json=payload, headers=header)
        # print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None

def file_upload_handler(auth_token, file_upload_token, cv_file):
    # save the uploaded form file to our local server first
    # fs = FileSystemStorage()
    # filename = fs.save(cv_file.name, cv_file)
    # uploaded_file_loc = 'media/{filename}'.format(filename=filename)
    # upload the cv_file using specified api
    token = "Token {token}".format(token=auth_token)
    url = settings.FILE_UPLOAD_API.format(FILE_TOKEN_ID=file_upload_token)
    # with open(uploaded_file_loc, 'rb') as cv:
    cv = cv_file.read()
    # with open(uploaded_file_loc, 'rb') as cv:
    header = {
        "Authorization": token
    }

    payload = {
        "file": (cv_file.name, cv, 'application/pdf')
    }

    try:
        response = requests.put(url=url, files=payload, headers=header)
        print(response.json())
        cv_file.close()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None    
