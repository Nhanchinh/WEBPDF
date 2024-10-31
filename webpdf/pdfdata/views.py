import os
from django.conf import settings
from django.shortcuts import render
import requests
from django.http import HttpResponse
from .models import PDFFile
# Create your views here.
def pdfdata(request):
    return render(request, 'pdfdata/pdfdata.html')


def download_pdf(request):
    if request.method == 'POST':
        pdf_url = request.POST.get('pdf_url')  # Lấy URL từ form
        response = requests.get(pdf_url)

        if response.status_code == 200:
            # Lưu file vào server
            name = pdf_url.split('/')[-1]  # Lấy tên file từ URL
            file_path = os.path.join(settings.MEDIA_ROOT, name)  # Đường dẫn lưu file vào MEDIA_ROOT
            with open(file_path, 'wb') as f:
                f.write(response.content)

            # Lưu thông tin vào cơ sở dữ liệu
            PDFFile.objects.create(name=name, pdf_url=pdf_url, file_path=file_path)

            return HttpResponse("success")
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error")
