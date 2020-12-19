from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest
from .forms import AuthenticationForm, DetailsForm
from django.core.files.storage import FileSystemStorage

def login(request):
    # authenticate username and password, returns login view
    if request.method == 'POST':
        auth_form = AuthenticationForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['user_name']
            password = auth_form.cleaned_data['password']
            
            return HttpResponseRedirect('details')
    else:
        auth_form = AuthenticationForm()
        context = {
            'form': auth_form
        }
        return render(request, 'apply/login.html', context)

def details(request):
    # submit the details to the server, returns the application form
    if request.method == 'POST':
        details_form = DetailsForm(request.POST, request.FILES)
        if details_form.is_valid():
            print('data valid')
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
            fs = FileSystemStorage()
            filename = fs.save(cv_file.name, cv_file)
            print(cv_file)
            print(cv_file.name)
            print(name)
            print(email)
            print(phone)
            print(full_address)
            print(name_of_university)
            print(graduation_year)
            print(cgpa)
            print(experience_in_months)
            print(current_work_place_name)
            print(applying_in)
            print(expected_salary)
            print(field_buzz_reference)
            print(github_project_url)
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
    