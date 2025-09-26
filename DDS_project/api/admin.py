from django.contrib import admin
from .models import Status, Type, Category, Subcategory, Transaction


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Transaction)
