from rest_framework import serializers

from todo.models import ToDo


class CreateToDoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('text', 'uuid')
        read_only_fields = ('uuid', 'created', 'active')
        model = ToDo


class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDo
        fields = '__all__'
