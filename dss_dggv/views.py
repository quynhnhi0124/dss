from django.shortcuts import render
# Create your views here.
from django.db.models import Sum
from django.http import JsonResponse
from django.http import HttpResponse
from  .models import Giangvien
from django.db.models import Count
import json
from django.db.models import Q

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
        if name != None: object = object.filter(Q(ten__icontains=name) | Q(gioi_tinh__icontains=name) | Q(hoc_vi__icontains=name) | Q(hoc_ham__icontains=name) | Q(dia_chi__icontains=name))
    return index(request, object)

def index(request, object = None):
    if object == None:
        object = Giangvien.objects.filter(ma_nganh="MAT130").values('ten', 'nam_sinh', 'dia_chi', 'gioi_tinh', 'ma_truong', 'tn_dh', 'tn_ch', 'hoc_vi', 'hoc_ham', 'nam_tn_dh', 'nam_tn_ch', 'nam_tn_ts', 'tn_ts')
    # res = json.dumps(list(object), ensure_ascii=False).encode('utf8')
    # print({'list' : list(object)})
    print(len(object))
    return render(request, "pages/base.html", {'giaovien' : list(object), 'soluong' : len(object)})
def plot_res(request):
    filed = "hoc_vi"
    if request.method == "POST":
        filed = request.POST.get('plot_field', None)
    labels = []
    data = []
    
    queryset = Giangvien.objects.filter(ma_nganh="MAT130").order_by(filed).values(filed).annotate(hoc_vi_count=Count(filed))
    if filed == 'gioi_tinh':
        labels.append("Nam")
        labels.append("Nữ")
        if queryset[0][filed]:
            data.append(queryset[0]['hoc_vi_count'])
            data.append(queryset[1]['hoc_vi_count'])
        else:
            data.append(queryset[1]['hoc_vi_count'])
            data.append(queryset[0]['hoc_vi_count'])
    else:    
        for i in queryset:
            if(i[filed] is not None):
                labels.append(i[filed])
                data.append(i['hoc_vi_count'])

    return render(request, 'pages/plot.html',{
        'labels': labels,
        'data': data,
    })

