from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomForm, FormField

class FormFieldInline(admin.TabularInline):
    model = FormField
    extra = 1

@admin.register(CustomForm)
class CustomFormAdmin(admin.ModelAdmin):
    inlines = [FormFieldInline]
