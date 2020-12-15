# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Chuyennganh(models.Model):
    manganh = models.CharField(db_column='MaNganh', primary_key=True, max_length=10)  # Field name made lowercase.
    nhomnganh = models.ForeignKey('Nhomnganh', models.DO_NOTHING, db_column='NhomNganh')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChuyenNganh'


class Coquan(models.Model):
    macoquan = models.AutoField(db_column='MaCoQuan', primary_key=True)  # Field name made lowercase.
    tencoquan = models.CharField(db_column='TenCoQuan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    diachi = models.CharField(db_column='DiaChi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    makhuvuc = models.ForeignKey('Khuvuc', models.DO_NOTHING, db_column='MaKhuVuc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CoQuan'


class Khuvuc(models.Model):
    makhuvuc = models.AutoField(db_column='MaKhuVuc', primary_key=True)  # Field name made lowercase.
    tenkhuvuc = models.CharField(db_column='TenKhuVuc', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KhuVuc'


class Lamviec(models.Model):
    maviec = models.AutoField(db_column='MaViec', primary_key=True)  # Field name made lowercase.
    masinhvien = models.CharField(db_column='MaSinhVien', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manganh = models.IntegerField(db_column='MaNganh', blank=True, null=True)  # Field name made lowercase.
    macoquan = models.ForeignKey(Coquan, models.DO_NOTHING, db_column='MaCoQuan', blank=True, null=True)  # Field name made lowercase.
    batdau = models.DateTimeField(db_column='BatDau', blank=True, null=True)  # Field name made lowercase.
    ketthuc = models.DateTimeField(db_column='KetThuc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LamViec'


class Nhomnganh(models.Model):
    nhomnganh = models.AutoField(db_column='NhomNganh', primary_key=True)  # Field name made lowercase.
    tenchuyennganh = models.CharField(db_column='TenChuyenNganh', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NhomNganh'


class Sinhvien(models.Model):
    makey = models.AutoField(db_column='MaKey', primary_key=True)  # Field name made lowercase.
    masinhvien = models.CharField(db_column='MaSinhVien', unique=True, max_length=50)  # Field name made lowercase.
    tensinhvien = models.CharField(db_column='TenSinhVien', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gioitinh = models.CharField(db_column='GioiTinh', max_length=5)  # Field name made lowercase.
    noisinh = models.CharField(db_column='NoiSinh', max_length=100, blank=True, null=True)  # Field name made lowercase.
    namtotnghiep = models.IntegerField(db_column='NamTotNghiep', blank=True, null=True)  # Field name made lowercase.
    loaitotnghiep = models.CharField(db_column='LoaiTotNghiep', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SinhVien'


class Truong(models.Model):
    matruong = models.CharField(db_column='MaTruong', primary_key=True, max_length=5)  # Field name made lowercase.
    tentruong = models.CharField(db_column='TenTruong', max_length=70)  # Field name made lowercase.
    diachi = models.CharField(db_column='DiaChi', max_length=120, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=75, blank=True, null=True)  # Field name made lowercase.
    tinhthanh = models.CharField(db_column='TinhThanh', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dvchuquan = models.CharField(db_column='DVChuquan', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Truong'


class Truongnganh(models.Model):
    matruong = models.ForeignKey(Truong, models.DO_NOTHING, db_column='MaTruong', primary_key=True)  # Field name made lowercase.
    manganh = models.ForeignKey(Chuyennganh, models.DO_NOTHING, db_column='MaNganh')  # Field name made lowercase.
    namdt = models.IntegerField(db_column='NamDT')  # Field name made lowercase.
    socb = models.IntegerField(db_column='SoCB')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TruongNganh'
        unique_together = (('matruong', 'manganh'),)


class Tuyensinh(models.Model):
    matruong = models.ForeignKey(Truong, models.DO_NOTHING, db_column='MaTruong', primary_key=True)  # Field name made lowercase.
    manganh = models.ForeignKey(Chuyennganh, models.DO_NOTHING, db_column='MaNganh')  # Field name made lowercase.
    diemchuan = models.FloatField(db_column='DiemChuan')  # Field name made lowercase.
    chitieu = models.IntegerField(db_column='ChiTieu', blank=True, null=True)  # Field name made lowercase.
    sldatuyen = models.IntegerField(db_column='SLDaTuyen', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TuyenSinh'
        unique_together = (('matruong', 'manganh'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Co_Quan(models.Model):
    ten_co_quan = models.CharField(primary_key=True, max_length=50)
    dia_chi = models.CharField(max_length=100, blank=True, null=True)
    tinh = models.CharField(max_length=20, blank=True, null=True)
    co_quan_quan_li = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'co_quan'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Giangvien(models.Model):
    ten = models.CharField(primary_key=True, max_length=30)
    nam_sinh = models.CharField(max_length=5, blank=True, null=True)
    dia_chi = models.CharField(max_length=30, blank=True, null=True)
    anh = models.BinaryField(blank=True, null=True)
    gioi_tinh = models.BooleanField(blank=True, null=True)
    ma_truong = models.ForeignKey('TruongThong', models.DO_NOTHING, db_column='ma_truong')
    tn_dh = models.CharField(max_length=80, blank=True, null=True)
    tn_ch = models.CharField(max_length=80, blank=True, null=True)
    ma_nganh = models.ForeignKey('Nganh', models.DO_NOTHING, db_column='ma_nganh', blank=True, null=True)
    hoc_vi = models.CharField(max_length=20, blank=True, null=True)
    hoc_ham = models.CharField(max_length=20, blank=True, null=True)
    nam_tn_dh = models.CharField(max_length=10, blank=True, null=True)
    nam_tn_ch = models.CharField(max_length=10, blank=True, null=True)
    nam_tn_ts = models.CharField(max_length=10, blank=True, null=True)
    tn_ts = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'giangvien'
        unique_together = (('ten', 'ma_truong'),)


class KhoaHoc(models.Model):
    ma_khoa_hoc = models.CharField(primary_key=True, max_length=10)
    nam_vao = models.IntegerField(blank=True, null=True)
    nam_ra = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'khoa_hoc'


class Nganh(models.Model):
    ma_nganh = models.CharField(primary_key=True, max_length=15)
    ten_nganh = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nganh'


class NganhDaoTao(models.Model):
    ma_nganh_dao_tao = models.CharField(primary_key=True, max_length=10)
    ten_nganh = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nganh_dao_tao'


class NganhNghe(models.Model):
    ma_nganh_nghe = models.CharField(primary_key=True, max_length=10)
    ten_nganh = models.CharField(max_length=30, blank=True, null=True)
    luong_khoi_diem = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nganh_nghe'


class Sinh_Vien(models.Model):
    ma_sinh_vien = models.CharField(primary_key=True, max_length=10)
    ho_ten = models.CharField(max_length=30, blank=True, null=True)
    ngay_sinh = models.CharField(max_length=10, blank=True, null=True)
    gioi_tinh = models.CharField(max_length=5, blank=True, null=True)
    dan_toc = models.CharField(max_length=10, blank=True, null=True)
    que_quan = models.CharField(max_length=15, blank=True, null=True)
    ma_khoa_hoc = models.ForeignKey(KhoaHoc, models.DO_NOTHING, db_column='ma_khoa_hoc', blank=True, null=True)
    hoc_luc = models.CharField(max_length=10, blank=True, null=True)
    ma_nganh_dao_tao = models.ForeignKey(NganhDaoTao, models.DO_NOTHING, db_column='ma_nganh_dao_tao', blank=True, null=True)
    ma_nganh_nghe = models.ForeignKey(NganhNghe, models.DO_NOTHING, db_column='ma_nganh_nghe', blank=True, null=True)
    ten_co_quan = models.ForeignKey(Co_Quan, models.DO_NOTHING, db_column='ten_co_quan', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sinh_vien'


class TruongThong(models.Model):
    ma_truong = models.CharField(primary_key=True, max_length=10)
    ten_truong = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'truong_Thong'
