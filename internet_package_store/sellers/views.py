from django.shortcuts import render, redirect
from .models import Seller

def register_seller(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Seller.objects.create(name=name)
        return redirect('seller_list')
    return render(request, 'sellers/register.html')

def seller_list(request):
    sellers = Seller.objects.all()
    return render(request, 'sellers/list.html', {'sellers': sellers})
