from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Register)
admin.site.register(models.MemeCaption)
admin.site.register(models.LoginHistory)