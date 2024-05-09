
from django.contrib import admin
from django.urls import path
from . import settings
from django.conf.urls.static import static
from film2serial.views import homepage,login_user,logout_user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage,name="home"),
    path('login/',login_user,name="login"),
    path('logout/',logout_user,name="logout")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
