from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add_record', views.add_record, name="add_record"),
    path('save', views.save_record, name="save_record"),
    path('reports', views.reports, name="reports"),
    path('reports/download', views.download_pdf, name="download_pdf"),
]
