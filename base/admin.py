from django.contrib import admin
from .models import Task, BaseAppInfo
# Register your models here.


admin.site.register(Task)
admin.site.register(BaseAppInfo)
