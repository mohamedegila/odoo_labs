import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from medical.forms import MedicineForm
from medical.models import Medicine
from medical.utils import fetch_data_from_odoo, sync_data_to_odoo


@require_http_methods(['GET'])
def index_orders(request):
    return render(request, 'medical/medicines/index.html', {'medicines': Medicine.objects.all()})


@require_http_methods(['GET', 'POST'])
def create(request):
    medicine_form = MedicineForm(request.POST or None)
    if medicine_form.is_valid():
        medicine_form.save()
        return redirect("medicine_index")

    return render(request, "medical/medicines/create.html", {"form": medicine_form})


@require_http_methods(['GET'])
def index(request):
    return render(request, 'medical/index.html')


@require_http_methods(['POST'])
def sync_from_odoo(request):
    data = fetch_data_from_odoo([])
    medicines = Medicine.objects.values_list('name', flat=True)
    new_medicines = [medicine for medicine in data if medicine.get('name') not in medicines]
    bulk_new_medicines = []
    for new_medicine in new_medicines:
        bulk_new_medicines.append(
            Medicine(name=new_medicine.get('name'),
                     description=new_medicine.get('description'),
                     manufacturer=new_medicine.get('manufacturer'),
                     price=new_medicine.get('price')
                     )
        )

    Medicine.objects.bulk_create(bulk_new_medicines)
    return HttpResponse('fetched successfully')


@require_http_methods(['POST'])
def sync_to_odoo(request):
    income_medicines = fetch_data_from_odoo([])
    income_medicines_name = [income_medicine.get('name') for income_medicine in income_medicines]
    different_medicines = Medicine.objects.exclude(name__in=income_medicines_name)
    for different_medicine in different_medicines:
        sync_data_to_odoo({
            "name": different_medicine.name,
            "description": different_medicine.description,
            "manufacturer": different_medicine.manufacturer,
            "price": different_medicine.price,
        })
    return HttpResponse('updated successfully')
