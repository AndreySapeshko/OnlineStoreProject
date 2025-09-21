from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def catalog(request):
    return render(request, 'catalog/catalog.html')


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        print(f'Сообщение от {name} {phone}: {message}')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'catalog/contacts.html')
