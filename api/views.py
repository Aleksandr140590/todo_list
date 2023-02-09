import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from todo.models import Todo
from .generator_uuid import GeneratorUuid
from .serializers import CreateTodoSerializer, TodoSerializer
from .validators import validate_date

generator = GeneratorUuid()


@api_view(["POST"])
def create_todo(request):
    serializer = CreateTodoSerializer(data=request.data)
    serializer.is_valid()
    serializer.save(uuid=generator.created())
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_todo(request):
    uuid = request.GET['uuid']
    if Todo.objects.filter(uuid=uuid).exists():
        serializer = TodoSerializer(Todo.objects.get(uuid=uuid))
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response('Неверный "uuid"', status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def get_all_todo(request):
    queryset = Todo.objects.all()
    serializer = TodoSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_todo(request):
    uuid = request.GET['uuid']
    if Todo.objects.filter(uuid=uuid).exists():
        Todo.objects.get(uuid=uuid).delete()
        return Response('Deleted', status=status.HTTP_204_NO_CONTENT)
    return Response("Object not founded", status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def list_todo(request):
    if 'start' in request.GET and 'end' in request.GET:
        if not validate_date(
                request.GET['start']
        ) or not validate_date(
            request.GET['end']
        ):
            return Response('Неверный формат даты. Атрибуты "start" и '
                            '"end" должны быть в формате ДД.ММ.ГГ',
                            status=status.HTTP_400_BAD_REQUEST)
        start_date_obj = datetime.datetime.strptime(
            request.GET['start'], '%d.%m.%y')
        end_date_obj = datetime.datetime.strptime(
            request.GET['end'], '%d.%m.%y')
        queryset = Todo.objects.filter(created__range=(start_date_obj,
                                                       end_date_obj))
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response('Неверный запрос. Атрибуты "start" и "end" должны быть '
                    'в формате ДД.ММ.ГГ', status=status.HTTP_404_NOT_FOUND)
