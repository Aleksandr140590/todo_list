import datetime
from pprint import pprint

from django.shortcuts import render, get_object_or_404
from rest_framework import status, mixins
from rest_framework.decorators import api_view
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from todo.models import Todo
from .serializers import CreateTodoSerializer, TodoSerializer


# Create your views here.



class CreateTodoViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Todo.objects.all()
    serializer_class = CreateTodoSerializer


class GetTodoViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = TodoSerializer
    lookup_field = ('uuid', )

    def get_queryset(self):
        if 'uuid' in self.request.query_params:
            return Todo.objects.filter(uuid=self.request.query_params.get('uuid'))



class GetAllTodoViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

@api_view(["DELETE"])
def delete_todo(request):
    uuid = request.GET['uuid']
    if Todo.objects.filter(uuid=uuid).exists():
        Todo.objects.get(uuid=uuid).delete()
        return Response('Deleted', status=status.HTTP_204_NO_CONTENT)
    return Response("Object not founded", status=status.HTTP_404_NOT_FOUND)


class ListTodoViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = TodoSerializer
    lookup_field = ('start', 'end')

    def get_queryset(self):
        if 'start' in self.request.query_params and 'end' in self.request.query_params:
            start_date_obj = datetime.datetime.strptime(self.request.query_params.get('start'), '%d.%m.%y')
            end_date_obj = datetime.datetime.strptime(
                self.request.query_params.get('end'), '%d.%m.%y')

            return Todo.objects.filter(created__range=(start_date_obj, end_date_obj))