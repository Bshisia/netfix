#!/usr/bin/env python3
import os
import sys
import django
from datetime import date

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netfix.settings')
django.setup()

from users.models import User, Customer, Company
from services.models import Service, ServiceRequest

def create_sample_data():
    print("Creating sample data...")
    
    # Create sample customers
    if not User.objects.filter(username='john_customer').exists():
        customer_user = User.objects.create_user(
            username='john_customer',
            email='john@example.com',
            password='password123',
            is_customer=True
        )
        Customer.objects.create(
            user=customer_user,
            date_of_birth=date(1990, 5, 15)
        )
        print("Created customer: john_customer")
    
    # Create sample companies
    if not User.objects.filter(username='plumbing_pro').exists():
        company_user = User.objects.create_user(
            username='plumbing_pro',
            email='contact@plumbingpro.com',
            password='password123',
            is_company=True
        )
        Company.objects.create(
            user=company_user,
            field='Plumbing'
        )
        print("Created company: plumbing_pro")
    
    if not User.objects.filter(username='all_services').exists():
        all_company_user = User.objects.create_user(
            username='all_services',
            email='info@allservices.com',
            password='password123',
            is_company=True
        )
        Company.objects.create(
            user=all_company_user,
            field='All in One'
        )
        print("Created company: all_services")
    
    # Create sample services
    plumbing_company = Company.objects.get(user__username='plumbing_pro')
    all_company = Company.objects.get(user__username='all_services')
    
    if not Service.objects.filter(name='Emergency Plumbing').exists():
        Service.objects.create(
            company=plumbing_company,
            name='Emergency Plumbing',
            description='24/7 emergency plumbing services for urgent repairs',
            price_hour=75.00,
            field='Plumbing'
        )
        print("Created service: Emergency Plumbing")
    
    if not Service.objects.filter(name='House Cleaning').exists():
        Service.objects.create(
            company=all_company,
            name='House Cleaning',
            description='Complete house cleaning service including all rooms',
            price_hour=25.00,
            field='House Keeping'
        )
        print("Created service: House Cleaning")
    
    if not Service.objects.filter(name='Garden Maintenance').exists():
        Service.objects.create(
            company=all_company,
            name='Garden Maintenance',
            description='Professional garden care and maintenance',
            price_hour=30.00,
            field='Gardening'
        )
        print("Created service: Garden Maintenance")
    
    print("Sample data creation completed!")

if __name__ == '__main__':
    create_sample_data()