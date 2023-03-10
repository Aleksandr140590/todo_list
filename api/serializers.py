from rest_framework import serializers

from todo.models import ToDo


class CreateToDoSerializer(serializers.ModelSerializer):
    """Сериализатор при создании объекта."""
    class Meta:
        fields = ('text', 'uuid')
        read_only_fields = ('uuid', 'created', 'active')
        model = ToDo


class ToDoSerializer(serializers.ModelSerializer):
    """Сериализатор GET запросов."""
    class Meta:
        model = ToDo
        fields = '__all__'
