from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from  .models import Giangvien

import json

from django.shortcuts import render


def homepage(request):
    return render(request, "pages/base.html")

def gv_detail_view(request):

    return HttpResponse();

def index(request):
    object = Giangvien.objects.filter(ma_nganh="MAT130").values('ten', 'ma_nganh');
    res = json.dumps(list(object), ensure_ascii=False).encode('utf8')
    print(res.decode())
    return render(request, "pages/base.html", {})