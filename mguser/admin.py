from django.contrib import admin
from .models import Mguser
# Register your models here.

class MguserAdmin(admin.ModelAdmin): # django admin을 커스텀할때 쓰는 클래스
    list_display = ('username', 'password') # list_display 필드에 출력하고 싶은 것을 출력

admin.site.register(Mguser, MguserAdmin)
