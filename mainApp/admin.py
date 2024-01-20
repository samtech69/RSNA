from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=["id","name","description","pic"]

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display=["id","name","pic"]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=["id","name","phone","email","message"]

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display=["id","email"]

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display=["id","pic"]


