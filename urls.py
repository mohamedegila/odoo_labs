from django.contrib import admin
from django.urls import path

from medical.views import *

urlpatterns = [
    path('', index, name='medical_index'),
    path('medicines/', index_orders, name='medicine_index'),
    path('medicines/create', create, name='medicine_create'),
    path('medicines/sync_from_odoo', sync_from_odoo, name='medicine_sync_from_odoo'),
    path('medicines/sync_to_odoo', sync_to_odoo, name='medicine_sync_to_odoo'),
]
