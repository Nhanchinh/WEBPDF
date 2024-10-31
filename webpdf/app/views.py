from django.shortcuts import render
from .models import DuLieu
from .forms import DuLieuForm
# Create your views here.

def home(request):
    dulieu_list = DuLieu.objects.all()   
    dulieu = DuLieu.objects.first()
    form = DuLieuForm(instance = dulieu)
    return render(request, 'app/home.html', {'dulieu_list': dulieu_list, 'form':form})
