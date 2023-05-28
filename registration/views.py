from django.shortcuts import render, redirect
from .forms import *
from .models import *

def multistep_form(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        address_form = AddressForm(request.POST)
        car_form = CarForm(request.POST)
        
        if customer_form.is_valid() and address_form.is_valid() and car_form.is_valid():
            address = address_form.save()
            customer = customer_form.save(commit=False)
            customer.address = address
            customer.save()
            car_form.save()
            return redirect('success')
            
        else:
            print("Form validation failed.")
            
    else:
        address_form = AddressForm()
        customer_form = CustomerForm()
        car_form = CarForm()
        
    context = {
        'address_form': address_form,
        'customer_form': customer_form,
        'car_form': car_form
    }
        
    return render(request, 'multistep_form.html', context=context)


def success_view(request):
    return render(request, 'success.html')