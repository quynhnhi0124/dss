from django.shortcuts import render
# Create your views here.
from django.db.models import Sum
from django.http import JsonResponse
from django.http import HttpResponse
from  .models import Giangvien
from django.db.models import Count
import json


def homepage(request):
    return render(request, "pages/base.html")

def gv_detail_view(request):

    return HttpResponse();

def gv_filter(request):
    gioi_tinh = []
    hoc_vi = []
    hoc_ham = []
    dia_chi = []
    name = ""
    object = None
    if request.method == "POST":
        name = request.POST.get('name', None)
        if request.POST.get('nam', None): gioi_tinh.append(1)
        if request.POST.get('nu', None): gioi_tinh.append(0)
        if request.POST.get('tiensi', None): hoc_vi.append("Tiến sĩ")
        if request.POST.get('thacsi', None): hoc_vi.append("Thạc sĩ")
        if request.POST.get('cunhan', None): hoc_vi.append("Cử nhân")
        if request.POST.get('giaosu', None):
            hoc_ham.append("Giáo sư")
            hoc_ham.append("GS")
        if request.POST.get('phogiaosu', None):
            hoc_ham.append("Phó giáo sư")
            hoc_ham.append("PSG")
            hoc_ham.append("PGS")
        object = Giangvien.objects.filter(ma_nganh="MAT130")
        if len(gioi_tinh) != 0: object = object.filter(gioi_tinh__in=gioi_tinh)
        if len(hoc_vi) != 0: object = object.filter(hoc_vi__in=hoc_vi)
        if len(hoc_ham) != 0: object = object.filter(hoc_ham__in=hoc_ham)
        if len(name) != 0: object = object.filter(ten__icontains=name)
    return index(request, object)

def index(request, object = None):
    if object == None:
        object = Giangvien.objects.filter(ma_nganh="MAT130").values('ten', 'nam_sinh', 'dia_chi', 'gioi_tinh', 'ma_truong', 'tn_dh', 'tn_ch', 'hoc_vi', 'hoc_ham', 'nam_tn_dh', 'nam_tn_ch', 'nam_tn_ts', 'tn_ts')
    # res = json.dumps(list(object), ensure_ascii=False).encode('utf8')
    # print({'list' : list(object)})
    return render(request, "pages/base.html", {'giaovien' : list(object)})

def plot_res(request):
    
    queryset = Giangvien.objects.order_by('hoc_vi').values('hoc_vi').annotate(hoc_vi_count=Count('hoc_vi'))

    data = list(queryset.values_list('hoc_vi_count', flat=True))
    labels = list(queryset.values_list('hoc_vi', flat=True))

    return render(request, "pages/plot.html", {
    'labels': labels,
    'data': data,
    })

