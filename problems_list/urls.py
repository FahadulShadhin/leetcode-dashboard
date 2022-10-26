from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from . import views

app_name = 'problems_list'
urlpatterns = [
    path( 
        '', 
        views.problems_list, 
        name='home'
    ),
    path( 
        'search/', 
        views.search, 
        name='search'
    ),
    path( 
        '<int:pk>/', 
        views.note, 
        name = 'note'
    ),
    path( 
        'about/', 
        views.about, 
        name = 'about'
    ),
    # path(
    #     'add/',
    #     views.add,
    #     name = 'add'
    # ),
    path(
        'favicon.ico',
        RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')),
        name = 'favicon'
    ),
]