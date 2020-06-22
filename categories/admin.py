from django.contrib import admin
from .models import Category
from .models import CategoryType

admin.site.register(Category)
admin.site.register(CategoryType)