
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from film2serial.views import homepage,login_user,logout_user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage,name="home"),
    path('login/',login_user,name="login"),
    path('logout/',logout_user,name="logout")
]
