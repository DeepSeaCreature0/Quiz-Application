from django.contrib import admin
from .models import Response

@admin.register(Response)
class ResponseList(admin.ModelAdmin):
    list_display = ('user_id','user_name','favorite_game','submission_date')
