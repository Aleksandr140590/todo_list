from django.conf.urls import url
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter

from .views import GetTodoViewSet, GetAllTodoViewSet, delete_todo, ListTodoViewSet, \
    CreateTodoViewSet

v1_router = SimpleRouter()

v1_router.register('record/create', CreateTodoViewSet, basename='create')
v1_router.register('record/get', GetTodoViewSet, basename='get_todo')
v1_router.register('records/all', GetAllTodoViewSet, basename='get_all_todo')
v1_router.register(r'records/list', ListTodoViewSet, basename='list_todo')



urlpatterns = [
    path('', include(v1_router.urls)),
    path('record/delete', delete_todo, name='delete_todo'),
]
