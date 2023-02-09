from rest_framework import serializers

from todo.models import Todo


class CreateTodoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('text', 'uuid')
        read_only_fields = ('uuid', 'created', 'active')
        model = Todo


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'
