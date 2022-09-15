from django.contrib import admin
from .models import Vacancy, Application, Rejected ,Accepted
# Register your models here.
admin.site.register(Vacancy)
admin.site.register(Application)
admin.site.register(Rejected)
admin.site.register(Accepted)
