from django.urls import path
from . import views  # here . means current folder
from django.contrib import admin
# mapping urls to views
# every app has its url configuration
urlpatterns = [
    path('home/', views.home, name='home'),
    path('admin/', admin.site.urls),
    # path('new-search/', views.new_search, name = 'new_search')
]