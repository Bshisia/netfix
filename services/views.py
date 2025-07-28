from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from users.models import Company, Customer, User

from .models import Service, ServiceRequest
from .forms import CreateNewService, RequestServiceForm


def service_list(request):
    services = Service.objects.all().order_by("-date")
    return render(request, 'services/list.html', {'services': services})


def index(request, id):
    service = Service.objects.get(id=id)
    return render(request, 'services/single_service.html', {'service': service})


@login_required
def create(request):
    if not request.user.is_company:
        return redirect('services_list')
    
    company = Company.objects.get(user=request.user)
    
    # Set available choices based on company field
    if company.field == 'All in One':
        choices = [
            ('Air Conditioner', 'Air Conditioner'),
            ('Carpentry', 'Carpentry'),
            ('Electricity', 'Electricity'),
            ('Gardening', 'Gardening'),
            ('Home Machines', 'Home Machines'),
            ('House Keeping', 'House Keeping'),
            ('Interior Design', 'Interior Design'),
            ('Locks', 'Locks'),
            ('Painting', 'Painting'),
            ('Plumbing', 'Plumbing'),
            ('Water Heaters', 'Water Heaters'),
        ]
    else:
        choices = [(company.field, company.field)]
    
    if request.method == 'POST':
        form = CreateNewService(request.POST, choices=choices)
        if form.is_valid():
            Service.objects.create(
                company=company,
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price_hour=form.cleaned_data['price_hour'],
                field=form.cleaned_data['field']
            )
            return redirect('services_list')
    else:
        form = CreateNewService(choices=choices)
    
    return render(request, 'services/create.html', {'form': form})


def service_field(request, field):
    # search for the service present in the url
    field = field.replace('-', ' ').title()
    services = Service.objects.filter(
        field=field)
    return render(request, 'services/field.html', {'services': services, 'field': field})


@login_required
def request_service(request, id):
    service = Service.objects.get(id=id)
    
    if request.method == 'POST':
        form = RequestServiceForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.get(user=request.user)
            ServiceRequest.objects.create(
                customer=customer,
                service=service,
                address=form.cleaned_data['address'],
                service_time=form.cleaned_data['service_time']
            )
            return redirect('services_list')
    else:
        form = RequestServiceForm()
    
    return render(request, 'services/request_service.html', {
        'form': form, 
        'service': service
    })


@login_required
def edit_service(request, id):
    service = Service.objects.get(id=id)
    
    # Only allow the company that owns the service to edit it
    if not request.user.is_company or service.company.user != request.user:
        return redirect('services_list')
    
    company = Company.objects.get(user=request.user)
    
    # Set available choices based on company field
    if company.field == 'All in One':
        choices = [
            ('Air Conditioner', 'Air Conditioner'),
            ('Carpentry', 'Carpentry'),
            ('Electricity', 'Electricity'),
            ('Gardening', 'Gardening'),
            ('Home Machines', 'Home Machines'),
            ('House Keeping', 'House Keeping'),
            ('Interior Design', 'Interior Design'),
            ('Locks', 'Locks'),
            ('Painting', 'Painting'),
            ('Plumbing', 'Plumbing'),
            ('Water Heaters', 'Water Heaters'),
        ]
    else:
        choices = [(company.field, company.field)]
    
    if request.method == 'POST':
        form = CreateNewService(request.POST, choices=choices)
        if form.is_valid():
            service.name = form.cleaned_data['name']
            service.description = form.cleaned_data['description']
            service.price_hour = form.cleaned_data['price_hour']
            service.field = form.cleaned_data['field']
            service.save()
            return redirect('index', id=service.id)
    else:
        form = CreateNewService(choices=choices, initial={
            'name': service.name,
            'description': service.description,
            'price_hour': service.price_hour,
            'field': service.field
        })
    
    return render(request, 'services/edit.html', {'form': form, 'service': service})
