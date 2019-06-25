from django.contrib import admin

from .models import Home,Worker,Category
# Register your models here.
admin.site.register(Home)
admin.site.register(Category)
admin.site.register(Worker)