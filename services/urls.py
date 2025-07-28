from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.service_list, name='services_list'),
    path('most-requested/', v.most_requested, name='most_requested'),
    path('search/', v.search, name='search'),
    path('create/', v.create, name='services_create'),
    path('<int:id>', v.index, name='index'),
    path('<int:id>/edit/', v.edit_service, name='edit_service'),
    path('<int:id>/request_service/', v.request_service, name='request_service'),
    path('<slug:field>/', v.service_field, name='services_field'),
]
