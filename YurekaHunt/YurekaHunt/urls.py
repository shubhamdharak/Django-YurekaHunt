
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),
    path("api/", include("api.urls"), name="api"),
  
    path("account/", include('account.urls'),name="account"),
] 

admin.site.site_header = 'YurekaHunt Administration'
# admin.site.site_title = 'Yureka'