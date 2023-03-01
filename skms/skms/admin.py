from django.contrib import admin
from .models import UserAccount
from . import models

class SKMSAdminData(admin.AdminSite):
    index_title = 'S.K.M.S. User Information'
    site_header = "Security Knowledge Management System"
    site_title = "S.K.M.S."


skms_admin_site = SKMSAdminData(name='SKMSAdmin')

skms_admin_site.register(models.UserAccount)
skms_admin_site.register(models.Comment)
skms_admin_site.register(models.Post)
skms_admin_site.register(models.Report)
skms_admin_site.register(models.Voice)


skms_admin_site.site_url = "/skms/index/"
