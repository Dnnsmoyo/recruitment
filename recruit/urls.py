"""recruit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('panel',views.admin_panel),
    path('new/vacancy',views.VacancyCreateView.as_view()),
    path('new/application',views.ApplicationCreateView.as_view()),
    path('api/vacancies',views.VacancyList.as_view()),
    path('api/applications',views.ApplicationList.as_view()),
    path('api/rejections',views.RejectedList.as_view()),
    path('api/accepted',views.AcceptedList.as_view()),
    path('vacancy/<pk>/', views.VacancyDetailView.as_view(),name="group_detail"),   
    path('application/<pk>/', views.ApplicationDetailView.as_view(),name="group_detail"),   
    path("register/", views.UserCreate.as_view(), name="register"),  # <-- added
    path('admin/', admin.site.urls),
]
