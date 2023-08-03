from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings
from my_apps.recipes_app.views import *

urlpatterns = [
    # path('', views.HomeView.as_view(), name='home'),

    path('', main_page, name='index'),
    path('<int:recipe_id>', single_recipe, name='single_recipe'),
    path('soup', soup_page, name='soup_page'),
    path('dish', dish_page, name='dish_page'),
    path('aperetize', aperetize_page, name='aperetize_page'),
    path('drink', drink_page, name='drink_page'),
    path('rewiew/<int:pk>', add_comments, name='add_comments'),
    path('search', search_page, name='search_page'),
]