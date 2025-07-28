from django.shortcuts import render

from users.models import User, Company, Customer
from services.models import Service, ServiceRequest


def home(request):
    return render(request, 'users/home.html', {'user': request.user})


def customer_profile(request, name):
    user = User.objects.get(username=name)
    customer = Customer.objects.get(user=user)
    service_requests = ServiceRequest.objects.filter(customer=customer).order_by('-date_requested')
    
    # Calculate age
    from datetime import date
    today = date.today()
    age = today.year - customer.date_of_birth.year - ((today.month, today.day) < (customer.date_of_birth.month, customer.date_of_birth.day))
    
    return render(request, 'users/profile.html', {
        'user': user, 
        'user_age': age,
        'sh': service_requests
    })


def company_profile(request, name):
    # fetches the company user and all of the services available by it
    user = User.objects.get(username=name)
    services = Service.objects.filter(
        company=Company.objects.get(user=user)).order_by("-date")

    return render(request, 'users/profile.html', {
        'user': user, 
        'services': services
    })
