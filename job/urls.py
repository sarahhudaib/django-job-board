from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'job'

urlpatterns = [
    path('', views.job_list), # path('path_name/', include('app_name.urls'))
    path('<int:id>', views.job_detail, name='job_detail'),
]
