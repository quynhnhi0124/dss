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
    object = Giangvien.objects.filter(ma_nganh="MAT130").values('ten', 'nam_sinh', 'dia_chi', 'gioi_tinh', 'ma_truong', 'tn_dh', 'tn_ch', 'hoc_vi', 'hoc_ham', 'nam_tn_dh', 'nam_tn_ch', 'nam_tn_ts', 'tn_ts')
    # res = json.dumps(list(object), ensure_ascii=False).encode('utf8')
    # print({'list' : list(object)})
    return render(request, "pages/base.html", {'giaovien' : list(object)})
