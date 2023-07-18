from django.contrib import admin
from my_apps.recipes_app.models import Recipes, Comments

# Register your models here.
admin.site.register(Recipes)
admin.site.register(Comments)

