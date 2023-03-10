"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from skms.admin import skms_admin_site
from django.conf import settings
from django.conf.urls.static import static
from skms import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('skmsadmin/login/', views.index),
    path('skmsadmin/', skms_admin_site.urls),
    path('skms/', include('skms.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

admin.site.index_title = "Security Knowledge Management System"
admin.site.site_header = "S.K.M.S. Admin"
admin.site.site_title = "Admin"