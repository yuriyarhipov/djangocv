from django.contrib import admin
from django.urls import path
from cv import views as cv_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cv_views.main)
]
