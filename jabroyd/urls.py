from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('', include('landingpage.urls')),
    path('accounts/', include('accounts.urls')),
    #path('signin/', include('landingpage.urls')),
    #path('signout/', include('landingpage.urls')),

]
