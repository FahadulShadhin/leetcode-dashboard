from django.urls import path
from . import views

app_name = 'problems_list'
urlpatterns = [
    path(
        '', 
        views.problems_list, 
        name='home'
    ),
    path(
        '<int:pk>/', 
        views.note, 
        name='note'
    ),
    path(
        'about/', 
        views.about, 
        name='about'
    ),
]