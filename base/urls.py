"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings



from recipes_app.views import main_page
from recipes_app.views import single_recipe
from recipes_app.views import soup_page
from recipes_app.views import dish_page
from recipes_app.views import aperetize_page
from recipes_app.views import drink_page
from recipes_app.views import add_comments


urlpatterns = [
    path('admin/', admin.site.urls),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('', main_page, name='index'),
    path('<int:recipe_id>', single_recipe, name='single_recipe'),
    path('soup', soup_page, name='soup_page'),
    path('dish', dish_page, name='dish_page'),
    path('aperetize', aperetize_page, name='aperetize_page'),
    path('drink', drink_page, name='drink_page'),
    path('rewiew/<int:pk>', add_comments, name='add_comments'),


    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members_app.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# image
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)