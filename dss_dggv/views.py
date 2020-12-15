from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from  .models import Giangvien

def gv_detail_view(request):

    return HttpResponse();

def index(request):
    object = Giangvien.objects.filter(ma_nganh="MAT130");
    print(object[0].ma_nganh);
    return HttpResponse("Hello, world. You're at the polls index.")