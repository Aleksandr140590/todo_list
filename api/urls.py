from django.urls import path

from .views import get_todo, get_all_todo, delete_todo, list_todo, create_todo


urlpatterns = [
    path('record/create', create_todo, name='create'),
    path('record/get', get_todo, name='get_todo'),
    path('records/all', get_all_todo, name='get_all_todo'),
    path('records/list', list_todo, name='list_todo'),
    path('record/delete', delete_todo, name='delete_todo'),
]
