from django.contrib import admin
from django.urls import path
from . import views

app_name='autho'

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.index, name="home"),
    path('reg/', views.reg, name="reg"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('success/', views.success, name="success"),
]