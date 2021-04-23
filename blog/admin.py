from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin
from . import models


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Tag)

class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "category", "create_at", "id"]
    inlines = [RecipeInline, ]

@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "prep_time", "cook_time", "post"]


admin.site.register(Comment)