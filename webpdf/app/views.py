from django.shortcuts import render
from .models import DuLieu
# Create your views here.
def home(request):
    dulieu_list = DuLieu.objects.all()   
    return render(request, 'app/home.html', {'dulieu_list': dulieu_list})
