from django.contrib import admin
from .models import Category, PartnerOffer

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')

@admin.register(PartnerOffer)
class PartnerOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'count')
    list_filter = ('category',)