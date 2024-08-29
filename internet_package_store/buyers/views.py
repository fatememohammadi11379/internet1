from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Buyer

def register_buyer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        Buyer.objects.create(name=name, phone_number=phone_number)
        return redirect('buyer_list')
    return render(request)

def buyer_list_json(request):
    buyers = list(Buyer.objects.values())
    return JsonResponse(buyers, safe=False)