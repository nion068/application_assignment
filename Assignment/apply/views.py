from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect, HttpRequest
from .forms import AuthenticationForm, DetailsForm
from .api import authenticate, submit_details, file_upload_handler

def login(request):
    # authenticate username and password, returns login view
    if request.method == 'POST':
        auth_form = AuthenticationForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['user_name']
            password = auth_form.cleaned_data['password']
            auth_response = authenticate(username, password)
            # check the response for different cases
            if auth_response is None:
                context = {
                    'form': auth_form,
                    'message': 'Something Error Occured'
                }
                return render(request, 'apply/login.html', context)
            elif auth_response['success'] is True:
                # set token expiration time
                request.session.set_expiry(settings.SESSION_TIMEOUT)
                # store token in session
                request.session['token'] = auth_response['token']
                print("Authentication successfull")
                return HttpResponseRedirect('details')
            else:
                context = {
                    'form': auth_form,
                    'message': auth_response['message']
                }    
                return render(request, 'apply/login.html', context)
    else:
        auth_form = AuthenticationForm()
        context = {
            'form': auth_form
        }
        return render(request, 'apply/login.html', context)

def details(request):
    # submit the details to the server, returns the application form
    print(request.session.get('token'))
    if request.method == 'POST':
        details_form = DetailsForm(request.POST, request.FILES)
        if details_form.is_valid():
            print('Data Valid')
            auth_token = request.session.get('token')
            name = details_form.cleaned_data['name']
            email = details_form.cleaned_data['email']
            phone = details_form.cleaned_data['phone']
            full_address = details_form.cleaned_data['full_address']
            name_of_university = details_form.cleaned_data['name_of_university']
            graduation_year = details_form.cleaned_data['graduation_year']
            cgpa = details_form.cleaned_data['cgpa']
            experience_in_months = details_form.cleaned_data['experience_in_months']
            current_work_place_name = details_form.cleaned_data['current_work_place_name']
            applying_in = details_form.cleaned_data['applying_in']
            expected_salary = details_form.cleaned_data['expected_salary']
            field_buzz_reference = details_form.cleaned_data['field_buzz_reference']
            github_project_url = details_form.cleaned_data['github_project_url']
            cv_file = request.FILES['cv_file']

            details_response = submit_details(auth_token, name, email, phone, full_address, name_of_university, graduation_year, cgpa, experience_in_months, current_work_place_name, applying_in, expected_salary, field_buzz_reference, github_project_url)
            # check responses for different cases
            if details_response is None:
                print("Something error occured in details submission")
                return render(request, 'apply/details.html', {'form': details_form})
            elif details_response['success'] is False:
                print("Submission failed")
                return render(request, 'apply/details.html', {'form': details_form})
            else:
                print("Details Submission successful")
                file_token_id = details_response['cv_file']['id']
                print("file_token_id =  " + str(file_token_id))
                file_upload_response = file_upload_handler(auth_token, file_token_id, cv_file)
                #check responses
                if file_upload_response is None:
                    print("Something error occured in file upload")
                    return render(request, 'apply/details.html', {'form': details_form})
                elif file_upload_response['success'] is False:
                    print("File upload failed")
                    return render(request, 'apply/details.html', {'form': details_form})
                else:
                    print("File upload successfull. Let's cross fingers.")
                    return render(request, 'apply/details.html', {'form': details_form})
            
        else:
            print('Data Invalid')
            print(details_form.errors)
        return render(request, 'apply/details.html', {'form': details_form})
    else:
        details_form = DetailsForm()
        context = {
            'form': details_form
        }
        return render(request, 'apply/details.html', context)
    