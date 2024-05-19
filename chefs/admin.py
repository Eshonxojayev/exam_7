from django.contrib import admin
from .models import Chef, Cooker, Assistantcook
from django.contrib.admin.sites import AlreadyRegistered


admin.site.register(Chef)
admin.site.register(Cooker)
admin.site.register(Assistantcook)