from django.shortcuts import render, redirect
from .models import Package

def add_package(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        Package.objects.create(name=name, price=price)
        return redirect('package_list')
    return render(request, 'packages/add.html')

def package_list(request):
    packages = Package.objects.filter(is_available=True)
    return render(request, 'packages/list.html', {'packages': packages})

def buy_package(request, package_id):
    package = Package.objects.get(id=package_id)
    if package.is_available:
        
        pass
    return redirect('package_list')