from django.contrib import admin
from  .models import Realtor

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone','hire_date','is_mvp')
    list_filter = ('name','email','phone','hire_date')
    list_display_links = ('id','name')
    list_editable = ('is_mvp',)
