from django.contrib import admin
from book.models import Bookinfo,Peopleinfo

# Register your models here.

admin.site.register(Bookinfo)
admin.site.register(Peopleinfo)